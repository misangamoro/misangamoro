import React, { useRef, useEffect, useState } from 'react';
import './App.css';
import Ground from './background';
import Pull from './Imgpull/pull';
import Header from './element/header';
import Welcome from './element/welcome';
import Textarea from './element/Textarea'; // Import the Textarea component

const App = () => {
  const [filterString, setFilterString] = useState(''); // State to track search string

  return (
    <div className="container">
      <Header />
      <Welcome />
      <Ground />
      <div className="absolute top-4 right-4">
        <Textarea setFilterString={setFilterString} />
      </div>
      <Pull filterString={filterString} /> 
    </div>
  );
};

export default App;
