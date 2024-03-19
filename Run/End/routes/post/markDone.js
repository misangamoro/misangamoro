const express = require('express');
const router = express.Router();
const fs = require('fs').promises;
const path = require('path');
const { spawn } = require('child_process');

router.post('/', async (req, res) => {
    const folderName = req.body.folderName;
    console.log("Received folder name:", folderName);

    const sourcePath = `C:\\Users\\Sumit\\Desktop\\Online\\Storys\\lib\\${folderName}\\content.txt`;
    const nowChar = `C:\\Users\\Sumit\\Desktop\\Online\\Storys\\lib\\${folderName}\\name.txt`
    const destinationPath = 'C:\\Users\\Sumit\\Desktop\\Online\\Visuals Production\\Program2';
    const destinationPathtwo = 'C:\\Users\\Sumit\\Desktop\\Online\\Visuals Production\\run\\nowChar';

    try {
        const content = await fs.readFile(sourcePath, 'utf-8');
        await fs.writeFile(path.join(destinationPath, 'input.txt'), content, 'utf-8');
        
        console.log('File copied successfully');

        // Read and copy the second file after the first one is successfully copied
        const contentTwo = await fs.readFile(nowChar, 'utf-8');
        await fs.writeFile(path.join(destinationPathtwo, 'name.txt'), contentTwo, 'utf-8');

        console.log('Second file copied successfully');

        // Run Python scripts
        const pythonProcess1 = spawn('python', ['C:\\Users\\Sumit\\Desktop\\Online\\Visuals Production\\Program2\\Delete_for_new.py']);
        const pythonProcess2 = spawn('python', ['C:\\Users\\Sumit\\Desktop\\Online\\Visuals Production\\Program2\\Generate_new_click.py']);

        // Close the response immediately to prevent blocking the client
        res.status(200).send('Files copied successfully');

        // Detach the child processes to prevent them from being attached to the current terminal
        pythonProcess1.unref();
        pythonProcess2.unref();
    } catch (error) {
        console.error('Error copying or running files:', error);
        res.status(500).send('Error copying or running files');
    }
});

module.exports = router;
