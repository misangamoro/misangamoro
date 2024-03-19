import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom'; // Import useNavigate

const Compare = () => {
  const [messages, setMessages] = useState([]);
  const [hoveredImage, setHoveredImage] = useState(null);
  const [selectedMusic, setSelectedMusic] = useState('');
  const navigate = useNavigate(); // Initialize useNavigate
  const musicList = ['Peachy', 'Gemini','Domini Beats', 'Chiapas Marimba','Look Both Ways','Sailing','Sharp Edges','Tinker Time','Whodoyouthink'];

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:3005/img');
        setMessages(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const handleHover = (musicName) => {
    const audioElement = document.getElementById(musicName);
    if (audioElement.paused) {
      audioElement.play()
        .then(() => {
          console.log(`Playing ${musicName}`);
        })
        .catch((error) => {
          console.error(`Error playing ${musicName}:`, error);
        });
    }
  };

  const handleStop = (musicName) => {
    const audioElement = document.getElementById(musicName);
    audioElement.pause();
    audioElement.currentTime = 0;
  };

  const handleSelectMusic = async (musicName, imageName) => {
    setSelectedMusic(musicName);
    try {
      await axios.post('http://localhost:3005/postimagemusic', {
        imageName: imageName,
        music: musicName
      });
    } catch (error) {
      console.error('Error posting data:', error);
    }
  };

  const handleRestart = async () => {
    try {
      await axios.post('http://localhost:3005/restart', { run: 'true' });
      navigate('/')

    } catch (error) {
      console.error('Error restarting server:', error);
    }
  };

  return (
    <div className="flex flex-col absolute left-0 top-0">
      <button onClick={handleRestart} className="fixed top-0 right-0 mt-4 mr-4 bg-blue-500 text-white p-2 rounded">Restart</button>
      {messages.map((message, index) => (
        <div
          key={index}
          className="relative"
          onMouseEnter={() => setHoveredImage(message.name.trim())}
          onMouseLeave={() => setHoveredImage(null)}
        >
          <img
            src={`http://localhost:3005/images/${message.name.trim()}.png`}
            alt={message.name.trim()}
            className="max-w-xs"
          />
          {hoveredImage === message.name.trim() && (
            <div className="absolute top-0 left-0 bg-gray-600 p-2 rounded shadow-md z-10">
              <ul>
                {musicList.map((musicName, i) => (
                  <li key={i} className="flex items-center">
                    <div className="w-4 h-4 mr-2 bg-blue-600 rounded-full"></div>
                    <span className="mr-2">{musicName}</span>
                    <button onClick={() => handleSelectMusic(musicName, message.name.trim())}>Select</button>
                    <audio
                      id={musicName}
                      controls
                      className="flex-1"
                      onMouseEnter={() => handleHover(musicName)}
                      onMouseLeave={() => handleStop(musicName)}
                    >
                      <source src={`http://localhost:3005/music/lmusic/${musicName}.mp3`} type="audio/mpeg" />
                      Your browser does not support the audio element.
                    </audio>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      ))}
    </div>
  );
};

export default Compare;
