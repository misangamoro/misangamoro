const express = require('express');
const app = express();
const port = 3005;

const foldersRouter = require('./routes/get/folders');
const markDoneRouter = require('./routes/post/markDone');
const readforsound = require('./routes/get/readforsound');
const audioRouter = require('./routes/get/soundeff');
const Lmusic = require('./routes/get/music');
const sounddata = require('./routes/post/sounddata');
const imagedata = require('./routes/get/image');
const musicimagedata = require('./routes/post/imgmusic')
const restart = require('./routes/post/restart')

app.use(express.json());

// Middleware to enable CORS
app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', 'http://localhost:3000');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    res.setHeader('Access-Control-Allow-Credentials', true);
    next();
});

app.use('/folders', foldersRouter);
app.use('/markDone', markDoneRouter);
app.use('/readforsound', readforsound);
app.use('/audio', audioRouter);
app.use('/sounddata', sounddata)
app.use('/img', imagedata)
app.use('/images', express.static('C:\\Users\\Sumit\\Desktop\\Online\\Visuals Production\\Assest\\Image\\Charectes'));
app.use('/music', Lmusic)
app.use('/postimagemusic', musicimagedata)
app.use('/restart', restart)
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

