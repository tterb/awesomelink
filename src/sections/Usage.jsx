import React from 'react';
import PropTypes from 'prop-types';
// Components
import Section from 'components/Section'


const Usage = ({ id }) => (
    <Section
        id={id}
        title={'Usage'}
        className='relative flex flex-col items-center justify-start text-center'
    >
        <p className='text-lg md:text-xl text-white text-opacity-85'>
            The perfect amount of spontaniety and chaotic wonder to make your links <span className='font-rage text-accent pl-1'>awesome</span>.
        </p>
    </Section>
);
Usage.propTypes = {
    id: PropTypes.string.isRequired,
};

export default Usage;
