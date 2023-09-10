// Contact.js
import { faFacebook, faTwitter, faInstagram } from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { Box, Paper } from '@mui/material';
import React from 'react';

function Contact() {
  return (
    
    <Box>
         <center><h1>Contact Me</h1></center>
        <Paper elevation={3}>
    <section className="contact">
      <p>If you would like to get in touch, you can reach me at:</p>
      <ul>
      <li>Name: Thejaswini TR</li>
        <li>Email: thejaswinitr@gmail.com</li>
        <li>Phone: 8748976574</li>
        
        <li>GitHub: <a href="https://github.com/theju1997">Your GitHub Profile</a></li>
      </ul>
    </section>
    <Box>
<div className="social-media-links" style={{ marginLeft: '300px'}}>
        <a href="https://www.facebook.com/your-page-url" target="_blank" rel="noopener noreferrer" >
          <FontAwesomeIcon icon={faFacebook} style={{height:'50px'}}/>
        </a>
        <div>
        <a href="https://www.twitter.com/your-page-url" target="_blank" rel="noopener noreferrer">
          <FontAwesomeIcon icon={faTwitter} style={{height:'50px'}} />
        </a>
        </div>
        <div>
        <a href="https://www.instagram.com/your-page-url" target="_blank" rel="noopener noreferrer">
          <FontAwesomeIcon icon={faInstagram} style={{height:'50px'}}/>
        </a>
        </div>
      </div>
      
</Box>
    </Paper>
    </Box>
  );
}

export default Contact;
