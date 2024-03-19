import React, { useState } from 'react';

const Textarea = ({ setFilterString }) => {
  const [searchString, setSearchString] = useState('');

  const handleChange = (event) => {
    const { value } = event.target;
    setSearchString(value);
    setFilterString(value); // Pass the search string to the parent component
  };

  return (
    <div className="fixed top-4 right-4"> {/* Set position to fixed */}
      <textarea
        className="textbox mt-4 w-10/12 h-12"
        placeholder="Search..."
        value={searchString}
        onChange={handleChange}
      ></textarea>
    </div>
  );
};

export default Textarea;
