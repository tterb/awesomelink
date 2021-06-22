import React from 'react';
import PropTypes from 'prop-types';
// Components
import Section from 'components/Section'


const Usage = ({ id }) => (
    <Section id={id} className='relative flex flex-col items-center justify-start text-center'>
        <div className='w-9/10 md:w-5/6 lg:4/5 max-w-250 mx-auto mt-8 mb-32'>
            <h1 className='relative text-6xl md:text-8xl text-chrome font-black mt-0 mb-2 md:mb-6'>Usage</h1>
            <p className='text-lg md:text-xl text-white text-opacity-85'>
                The perfect amount of spontaniety and chaotic wonder to make your links <span className='font-rage text-accent pl-1'>awesome</span>.
            </p>
        </div>
    </Section>
);
Usage.propTypes = {
    id: PropTypes.string.isRequired,
};

export default Usage;
