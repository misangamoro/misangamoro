import React, { useState, useEffect } from 'react';
import axios from 'axios';


const Pull = () => {
  const [imageList, setImageList] = useState([]);

  useEffect(() => {
    const fetchImageFileNames = async () => {
      try {
        const response = await axios.get(
          'https://api.github.com/repos/misangamoro/misangamoroImg/git/trees/images?recursive=1'
        );
        console.log(response)

        const files = response.data.tree.filter(
          (file) => file.type === 'blob' && file.path.endsWith('.png')
        );

        const fileNames = files.map((file) => file.path);
        setImageList(fileNames);
        console.log(fileNames)
      } catch (error) {
        console.error('Error fetching image file names:', error);
      }
    };

    

    fetchImageFileNames();
  }, []);


  return (
      <div className="container">
        <div className="image-container">
          {imageList.map((fileName, index) => (
            <div key={index} className="image-item">
              <img
                src={`https://raw.githubusercontent.com/misangamoro/misangamoroImg/images/${encodeURIComponent(fileName)}?raw=true`}
                alt={fileName}
              />
            </div>
           ))}
        </div>
      </div>
  );
};

export default Pull;
