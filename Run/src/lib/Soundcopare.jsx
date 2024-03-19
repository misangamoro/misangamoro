import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom'; // Import useNavigate hook
import { Link } from 'react-router-dom'; // Import Link component from react-router-dom

const Compare = () => {
  const [messages, setMessages] = useState([]);
  const [hoveredMessage, setHoveredMessage] = useState(null);
  const [selectedMusic, setSelectedMusic] = useState(Array(messages.length).fill('')); // State to track selected music for each text box
  const musicList = ['happy','nani', 'ahhh', 'anger', 'byby', 'fear','happyaa','realization','sad','sadxx']; // Add more music names here
  const navigate = useNavigate(); // Initialize navigate

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:3005/readforsound');
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

  const handleSelectMusic = async (musicName, index) => {
    setSelectedMusic(prevState => {
      const updatedMusic = [...prevState];
      updatedMusic[index] = musicName;
      return updatedMusic;
    });
  
    try {
      // Post data to the backend immediately when music is selected
      await axios.post('http://localhost:3005/sounddata', {
        index: index,
        music: musicName
      });
    } catch (error) {
      console.error('Error posting data:', error);
    }
  };
  

  const handleClick = async (index) => {
    try {
      // Post data to the backend
      await axios.post('http://localhost:3005/sounddata', {
        index: index,
        music: selectedMusic[index]
      });
    } catch (error) {
      console.error('Error posting data:', error);
    }
  };

  return (
    <div className="flex justify-center">
      <div className="flex flex-col items-start">
        {messages.map((message, index) => (
          <div
            key={index}
            className="relative bg-blue-500 text-white p-4 m-2 rounded cursor-pointer hover:bg-blue-600 transition duration-300"
            onMouseEnter={() => setHoveredMessage(message)}
            onMouseLeave={() => setHoveredMessage(null)}
          >
            {message.split('\r').map((line, i) => (
              <p key={i}>{line}</p>
            ))}
            {/* Little box containing the music file */}
            {hoveredMessage === message && (
              <div className="absolute left-0 bg-gray-600 p-2 rounded shadow-md z-10">
                <ul>
                  {musicList.map((musicName, i) => (
                    <li key={i} className="flex items-center">
                      <div className="w-4 h-4 mr-2 bg-blue-600 rounded-full"></div>
                      <span className="mr-2">{musicName}</span>
                      <button onClick={() => handleSelectMusic(musicName, index)}>Select</button>
                      <audio
                        id={musicName}
                        controls
                        className="flex-1"
                        onMouseEnter={() => handleHover(musicName)}
                        onMouseLeave={() => handleStop(musicName)}
                      >
                        <source src={`http://localhost:3005/audio/music/${musicName}.mp3`} type="audio/mpeg" />
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
      {/* Next button */}
      <div className="absolute top-0 right-0 m-4">
        <Link to="/3" className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded">
          Next
        </Link>
      </div>
    </div>
  );
};

export default Compare;
