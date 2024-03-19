import React from 'react';
import BackLogo from './backLogo';

const Header = () => {
  const handleClick = () => {
    window.open('https://www.youtube.com/@Misangamoro/videos?sub_confirmation=1', '_blank');
  };
 
  return (
    <div>
      <BackLogo/>
      <img
        src={`${process.env.PUBLIC_URL}/logo.svg`}
        alt="Logo"
        className="w-20 h-20 absolute top-0 left-0 cursor-pointer"
        onClick={handleClick}
      />
    </div>
  );
};
  
export default Header;
