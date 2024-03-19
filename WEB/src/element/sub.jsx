import React, { useState } from 'react';

const SubscriptionCheck = () => {
  const [subscribed, setSubscribed] = useState(false);

  // Function to check if the user is subscribed (manually verified)
  const checkSubscription = () => {
    // Manually verify if the user is subscribed
    // This can't be automated due to YouTube API restrictions
    // You can redirect the user to the channel's subscription page and let them confirm
    window.open('https://www.youtube.com/@thevibeguide');
  };

  return (
    <div>
      <h1>Check Subscription Status</h1>
      <button onClick={checkSubscription}>Check Subscription</button>
      {subscribed ? <p>Subscribed</p> : <p>Not Subscribed</p>}
    </div>
  );
};

export default SubscriptionCheck;
