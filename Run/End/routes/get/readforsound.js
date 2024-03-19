const express = require('express');
const router = express.Router();
const fs = require('fs');

router.get('/', async (req, res) => {
  const inputFilePath = 'C:\\Users\\Sumit\\Desktop\\Online\\Visuals Production\\Program2\\input.txt';

  try {
    const data = await new Promise((resolve, reject) => {
      fs.readFile(inputFilePath, 'utf8', (err, data) => {
        if (err) {
          reject(err);
          return;
        }
        resolve(data);
      });
    });

    const lines = data.trim().split('\n');
    const processedLines = [];

    for (let i = 0; i < lines.length; i += 3) {
      const concatenatedLine = lines[i] + ' ' + lines[i + 1];
      processedLines.push(concatenatedLine);
    }

    res.json(processedLines);
  } catch (err) {
    console.error('Error reading input file:', err);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

module.exports = router;
