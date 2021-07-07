import React from 'react';
// Sections
import Hero from 'sections/Hero'
import Motivation from 'sections/Motivation'
import Usage from 'sections/Usage'
import Contribute from 'sections/Contribute'
// Components
import Navbar from 'components/Navbar'
import Footer from 'components/Footer'
// Styles
import 'styles/fonts.css';
import 'styles/main.css';


function App() {

  const sectionLinks = [
    { id: 'motivation', label: 'Motivation' },
    // { id: 'usage', label: 'Usage' },
    { id: 'contribute', label: 'Contribute' },
  ]

  return (
    <div className='app'>
      <Navbar sectionLinks={sectionLinks} />
      <Hero id='hero' />
      <Motivation id='motivation' />
      <Contribute id='contribute' />
      <Footer />
    </div>
  );
}

export default App;
