import React from 'react';
import { Link } from 'react-scroll';
// Icons
import { FacebookOutline, LinkedinOutline, PaperPlaneOutline, TwitterOutline } from '@styled-icons/evaicons-outline';
import { LogoReddit } from '@styled-icons/ionicons-solid';
// Images
import awesomeLink from 'images/awesomelink.png';


const Footer = () => {
    return (
        <div className='flex flex-col md:flex-row bg-indigo-100 align-middle items-center w-screen h-auto min-h-48 py-10 px-8 pr-10 lg:px-12 lg:pr-14'>
            <Link 
                className='w-7/10 md:w-2/5 max-w-72 mx-auto md:ml-0 md:mr-auto mb-2 md:mb-0 cursor-pointer' 
                smooth={true}
                spy={true}
                offset={50}
                duration={500}
                delay={0} 
                to='hero'
            >
                <img
                    className='w-full h-auto'
                    src={awesomeLink}
                    alt='Awesome Link' 
                />
            </Link>
            <div className='flex flex-col items-start justify-center w-auto mx-auto md:ml-auto md:mr-0'>
                <span className='text-lg text-accent font-semibold w-auto mx-auto md:ml-0'>Share on:</span>
                <span className='flex flex-row text-xl text-accent my-3'>
                    <a className='text-magenta-500 hover:text-magenta-400' href='#'>
                        <FacebookOutline className='footer-icon w-8 mr-2 transition-all duration-250 cursor-pointer' />
                    </a>
                    <a className='text-magenta-500 hover:text-magenta-400' href='#'>
                        <TwitterOutline className='footer-icon w-8 mr-2 transition-all duration-250 cursor-pointer' />
                    </a>
                    <a className='text-magenta-500 hover:text-magenta-400' href='#'>
                        <LogoReddit className='footer-icon w-8 mr-2 transition-all duration-250 cursor-pointer' />
                    </a>
                    <a className='text-magenta-500 hover:text-magenta-400' href='#'>
                        <LinkedinOutline className='footer-icon w-8 mr-2 transition-all duration-250 cursor-pointer' />
                    </a>
                    <a className='text-magenta-500 hover:text-magenta-400' href='#'>
                        <PaperPlaneOutline className='footer-icon w-8 mr-0 transition-all duration-250 cursor-pointer' />
                    </a>
                </span>
            </div>
        </div>
    );
};
Footer.propTypes = {};

export default Footer;