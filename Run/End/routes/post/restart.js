const express = require('express');
const router = express.Router();
const { spawn } = require('child_process');

router.use(express.json()); // Middleware to parse JSON request bodies

router.post('/', (req, res) => {
    const { run } = req.body;

    if (run === 'true') {
        // Execute doneManipulated.py
        const pythonProcess1 = spawn('python', [
            'C:\\Users\\Sumit\\Desktop\\Online\\Visuals Production\\run\\pylib\\doneManipulated.py'
        ]);

        pythonProcess1.stdout.on('data', (data) => {
            console.log(`stdout: ${data}`);
        });

        pythonProcess1.stderr.on('data', (data) => {
            console.error(`stderr: ${data}`);
        });

        pythonProcess1.on('close', (code1) => {
            console.log(`doneManipulated.py exited with code ${code1}`);
            // Execute removeChar.py after doneManipulated.py
            const pythonProcess2 = spawn('python', [
                'C:\\Users\\Sumit\\Desktop\\Online\\Visuals Production\\run\\pylib\\removeChar.py'
            ]);

            pythonProcess2.stdout.on('data', (data) => {
                console.log(`stdout: ${data}`);
            });

            pythonProcess2.stderr.on('data', (data) => {
                console.error(`stderr: ${data}`);
            });

            pythonProcess2.on('close', (code2) => {
                console.log(`removeChar.py exited with code ${code2}`);
                res.status(200).json({ message: 'Python scripts executed successfully' });
            });
        });
    } else {
        res.status(400).json({ message: 'Invalid request body' });
    }
});

module.exports = router;
