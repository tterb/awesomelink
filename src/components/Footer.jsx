import React from 'react';
import PropTypes from 'prop-types';
// Icons
import { FacebookOutline, LinkedinOutline, PaperPlaneOutline, TwitterOutline } from '@styled-icons/evaicons-outline';
import { LogoReddit } from '@styled-icons/ionicons-solid';

const Footer = () => {
    return (
        <div className='flex bg-indigo-100 align-middle items-center w-screen h-auto min-h-48 py-10 px-0'>
            <div className='flex flex-col items-start justify-center w-9/10 mx-auto'>
                <span className='text-lg text-accent font-semibold'>Share on:</span>
                <span className='flex flex-row text-xl text-accent my-3'>
                    <FacebookOutline className='w-8 mr-2 cursor-pointer' />
                    <TwitterOutline className='w-8 mr-2 cursor-pointer' />
                    <LogoReddit className='w-8 mr-2 cursor-pointer' />
                    <LinkedinOutline className='w-8 mr-2 cursor-pointer' />
                    <PaperPlaneOutline className='w-8 mr-0 cursor-pointer' />
                </span>
            </div>
        </div>
    );
};
Footer.propTypes = {};

export default Footer;