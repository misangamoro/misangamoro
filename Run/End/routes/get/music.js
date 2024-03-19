const express = require('express');
const router = express.Router();
const fs = require('fs');
const path = require('path');

const audioFolderPath = 'C:\\Users\\Sumit\\Desktop\\Online\\Visuals Production\\Assest\\Audio\\music';

router.get('/lmusic/:filename', (req, res) => {
  const { filename } = req.params;
  const filePath = path.join(audioFolderPath, filename);

  fs.readFile(filePath, (err, data) => {
    if (err) {
      console.error('Error reading audio file:', err);
      res.status(500).json({ error: 'Internal Server Error' });
      return;
    }

    res.setHeader('Content-Type', 'audio/mpeg');
    res.send(data);
  });
});

module.exports = router;
