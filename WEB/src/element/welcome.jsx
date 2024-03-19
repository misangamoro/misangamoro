// Welcome.jsx
import React from 'react';
import Protobox from './protobox';

const Welcome = () => {
  return (
    <div className="flex flex-col justify-center items-center h-screen">
      <div className="text-center">
        <h1 className="title text-8xl font-trocchi mb-4">
          Misan Gamoro
        </h1>
        <Protobox/>
      </div>
    </div>
  );
};

export default Welcome;
