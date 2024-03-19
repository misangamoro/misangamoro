const express = require('express');
const fs = require('fs');
const readline = require('readline');
const router = express.Router();

router.use(express.json()); // Middleware to parse JSON request bodies

// Object to store the previous modification for each index
const previousModifications = {};

router.post('/', async (req, res) => {
  try {
    // Assuming the data sent from the frontend is in the request body
    const postData = req.body;
    
    // Log the received data
    console.log('Received data from frontend:', postData);

    // Read the input file
    const inputFilePath = 'C:\\Users\\Sumit\\Desktop\\Online\\Visuals Production\\Program2\\inputsoundmodify.txt';
    const rl = readline.createInterface({
      input: fs.createReadStream(inputFilePath),
      crlfDelay: Infinity
    });

    const modifiedLines = [];
    let lineNumber = 0;

    rl.on('line', (line) => {
      lineNumber++;
      if (lineNumber === postData.index + 1) {
        // Modify the line according to the received data
        const parts = line.split(':');
        let modifiedLine;
        if (!previousModifications[postData.index] || previousModifications[postData.index] === 'prefix') {
          // First call or need to modify prefix
          modifiedLine = `${postData.music}:${parts[1]}`;
          previousModifications[postData.index] = 'suffix'; // Update the modification state for this index
        } else {
          // Second or more call, modify suffix
          modifiedLine = `${parts[0]}:${postData.music}`;
          previousModifications[postData.index] = 'prefix'; // Update the modification state for this index
        }
        modifiedLines.push(modifiedLine);
      } else {
        // Add the original line
        modifiedLines.push(line);
      }
    });

    rl.on('close', () => {
      // Write the modified lines back to the file
      fs.writeFile(inputFilePath, modifiedLines.join('\n'), (err) => {
        if (err) {
          console.error('Error writing to file:', err);
          res.status(500).send('Internal server error.');
        } else {
          console.log('File modified successfully.');
          res.status(200).send('Data received and file modified successfully.');
        }
      });
    });
  } catch (error) {
    // Handle errors
    console.error('Error processing request:', error);
    res.status(500).send('Internal server error.');
  }
});

module.exports = router;
