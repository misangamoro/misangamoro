import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Box from '../element/box'; // Import the Box component

const Pull = ({ filterString }) => { // Receive filterString as prop
  const [folderList, setFolderList] = useState([]);
  const [selectedFolder, setSelectedFolder] = useState(null); // State to track selected folder
  const [selectedFolderImages, setSelectedFolderImages] = useState([]); // State to track selected folder images

  useEffect(() => {
    fetchData();
  }, []);

  // Function to fetch folder list and first image for each folder
  const fetchData = async () => {
    try {
      const response = await axios.get(
        'https://api.github.com/repos/misangamoro/misangamoroImg/contents/images'
      );
      const folders = response.data.filter((item) => item.type === 'dir');
      const folderDataPromises = folders.map(async (folder) => {
        const imagesResponse = await axios.get(
          `https://api.github.com/repos/misangamoro/misangamoroImg/contents/images/${folder.name}`
        );
        const images = imagesResponse.data.filter(
          (item) => item.type === 'file' && item.name.endsWith('.png')
        );
        const previewImageUrl = images.length > 0 ? images[0].download_url : null;
        return { ...folder, previewImageUrl };
      });
      const folderData = await Promise.all(folderDataPromises);
      setFolderList(folderData);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  // Event handler for folder click
  const handleFolderClick = async (folderName) => {
    try {
      const response = await axios.get(
        `https://api.github.com/repos/misangamoro/misangamoroImg/contents/images/${folderName}`
      );
      const images = response.data.filter(
        (item) => item.type === 'file' && item.name.endsWith('.png')
      );
      setSelectedFolderImages(images.map(image => image.download_url));
      setSelectedFolder(folderName); // Set the selected folder
    } catch (error) {
      console.error('Error fetching images for folder:', error);
    }
  };

  // Filter the folder list based on the search string
  const filteredFolders = folderList.filter(folder => folder.name.toLowerCase().includes(filterString.toLowerCase()));

  // Render UI
  return (
    <div className="mx-auto px-4 pb-8">
      <div className={`grid grid-cols-1 md:grid-cols-5 gap-2 justify-center`}>
        {filteredFolders.map((folder, index) => (
          <div
            key={index}
            className={`rounded-lg shadow-md bg-gray-800 p-4 cursor-pointer w-full md:w-auto flex flex-col items-center`}
            onClick={() => handleFolderClick(folder.name)}
          >
            <img
              src={folder.previewImageUrl}
              alt={folder.name}
              className="rounded-lg w-full h-auto"
            />
            <p className="text-white text-center mt-2">{folder.name}</p>
            {selectedFolder === folder.name && (
              <Box folderName={selectedFolder} images={selectedFolderImages} closeModal={setSelectedFolder} />
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Pull;
