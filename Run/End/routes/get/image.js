const express = require('express');
const router = express.Router();
const fs = require('fs').promises;
const path = require('path');

router.get('/', async (req, res) => {
    try {
        const filePath = 'C:\\Users\\Sumit\\Desktop\\Online\\Visuals Production\\run\\nowChar\\name.txt';
        const fileContent = await fs.readFile(filePath, 'utf-8');
        const lines = fileContent.split('\n');
        const filteredList = lines.filter(line => !line.includes('z'));

        // Create dynamic image links for each element in the filteredList
        const imageLinks = filteredList.map(element => {
            return { name: element};
        });

        // Render the images for the backend
        res.json(imageLinks);
    } catch (error) {
        console.error('Error reading file or generating image links:', error);
        res.status(500).send('Internal Server Error');
    }
});

module.exports = router;
