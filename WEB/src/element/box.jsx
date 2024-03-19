import React, { useState, useRef } from 'react';

const Box = ({ folderName, images, closeModal }) => {
  const [selectedImage, setSelectedImage] = useState(null);
  const imageRef = useRef(null);

  const openImage = (imageUrl) => {
    setSelectedImage(imageUrl);
  };

  const closeImage = () => {
    setSelectedImage(null);
  };

  const closeOutsideImage = (event) => {
    // Check if selectedImage is not null and the click target is outside the selected image container
    if (selectedImage && imageRef.current && !imageRef.current.contains(event.target)) {
      closeModal(null);
    }
  };

  return (
    <div className="fixed inset-0 flex items-center justify-center z-50" onClick={closeOutsideImage}>
      <div className="absolute inset-0 bg-black opacity-75"></div>
      <div className="z-50" ref={imageRef}>
        {selectedImage && (
          <div className="fixed inset-0 z-50 flex items-center justify-center" onClick={closeImage}>
            <img src={selectedImage} alt="Selected Image" className="max-w-full max-h-full" />
          </div>
        )}
        <div className="fixed top-5 left-5 right-5 bottom-5 bg-opacity-50 backdrop-filter backdrop-blur-lg rounded-lg p-8 flex flex-col">
          <h2 className="text-white text-2xl mb-4">Images in {folderName}</h2>
          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 flex-grow overflow-auto">
            {images.map((imageUrl, index) => (
              <img
                key={index}
                src={imageUrl}
                alt={`Image ${index + 1}`}
                className="rounded-lg w-full cursor-pointer"
                onClick={() => openImage(imageUrl)}
              />
            ))}
          </div>
          <button className="bg-blue-500 text-white px-4 py-2 rounded-lg mt-4 self-end" onClick={(e) => { e.stopPropagation(); closeModal(null); }}>Close</button>
        </div>
      </div>
    </div>
  );
};

export default Box;
