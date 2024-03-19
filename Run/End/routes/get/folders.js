const express = require('express');
const router = express.Router();
const fs = require('fs').promises;
const path = require('path');

router.get('/', async (req, res) => {
  const folderPath = 'C:/Users/Sumit/Desktop/Online/Storys/lib';

  try {
    const folderNames = await fs.readdir(folderPath);
    const folderStatuses = [];

    for (const folderName of folderNames) {
      const folderInfo = {
        name: folderName,
        status: 'Not done'
      };

      const doneFilePath = path.join(folderPath, folderName, 'done.txt');

      try {
        await fs.access(doneFilePath);
        const text = await fs.readFile(doneFilePath, 'utf-8');

        folderInfo.status = text.trim().toLowerCase() === 'yes' ? 'Already done' : 'Not done';
      } catch (error) {}

      folderStatuses.push(folderInfo);
    }

    res.json(folderStatuses);
  } catch (error) {
    console.error('Error occurred:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

module.exports = router;
