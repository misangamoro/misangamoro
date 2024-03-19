import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const FolderComponent = () => {
  const [folders, setFolders] = useState([]);
  const navigate = useNavigate(); // Initialize useNavigate

  useEffect(() => {
    fetch('http://localhost:3005/folders')
      .then(response => response.json())
      .then(data => {
        setFolders(data);
      })
      .catch(error => {
        console.error('Error fetching folders:', error);
      });
  }, []);

  const handleClick = (folderName) => {
    // Send POST request to mark folder as done
    fetch('http://localhost:3005/markDone', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ folderName: folderName })
    })
    .then(response => {
      if (response.ok) {
        console.log("Folder marked as done:", folderName);
        navigate('/2')
        // Update the UI or perform any other necessary actions

      } else {
        console.error('Failed to mark folder as done:', response.status);
      }
    })
    .catch(error => {
      console.error('Error marking folder as done:', error);
    });
  };
  

  return (
    <div>
      {folders.map(folder => (
        <div className="folder-container" key={folder.name}>
          <img src={`/folderIco.png`} alt="Folder Icon" />
          <div className="folder-name">{folder.name}</div>
          {folder.status === "Not done" && (
            <button onClick={() => handleClick(folder.name)}>Click to Mark Done</button>
          )}
        </div>
      ))}
    </div>
  );
};

export default FolderComponent;
