const express = require('express');
const fs = require('fs');
const router = express.Router();

router.use(express.json()); // Middleware to parse JSON request bodies

router.post('/', async (req, res) => {
  try {
    // Assuming the data sent from the frontend is in the request body
    const { imageName, music } = req.body;
    
    // Log the received data
    console.log('Received data from frontend:', imageName, music);

    // Construct the text to append to the file
    const textToAppend = `\n${imageName} : "C:\\Users\\Sumit\\Desktop\\Online\\Visuals Production\\Assest\\Audio\\music\\${music}.mp3"`;

    // Append the text to the file
    const filePath = 'C:\\Users\\Sumit\\Desktop\\Online\\Visuals Production\\Program2\\inputmusic.txt';
    fs.appendFileSync(filePath, textToAppend);

    // Respond with success
    res.status(200).send('Data received successfully');
  } catch (err) {
    console.error('Error:', err);
    res.status(500).send('Internal Server Error');
  }
});

module.exports = router;
