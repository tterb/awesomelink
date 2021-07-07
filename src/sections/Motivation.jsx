import React from 'react';
import PropTypes from 'prop-types';
// Components
import Section from 'components/Section'


const Motivation = ({ id }) => (
    <Section id={id} className='relative flex flex-col items-center justify-start text-center'>
        <div className='w-9/10 md:w-5/6 lg:4/5 max-w-250 mx-auto mt-10 mb-32'>
            <h1 className='relative text-6xl md:text-8xl text-chrome font-black mt-0 mb-2 md:mb-6'>Motivation</h1>
            <p className='text-lg md:text-xl text-white text-opacity-85'>
                The internet was once the new great frontier. It was exciting, unpredictable, disorganized, and fostered exploration.<br />
                Though as the internet has <span className='strikethrough'>d</span>evolved, digital exploration has deteriorated to scrolling sterilized feeds from major social-media networks.<br />
                As a result, the unique discoveries and experiences that could be expected from the early internet have seemingly fallen by the wayside.
                <a href='http://awesomel.ink/' className='font-rage text-accent pl-2' target='_blank' rel='noopener noreferrer'>AwesomeLink</a> is an attempt to bring back some of that unpredictability and exploration.
            </p>
        </div>
    </Section>
);
Motivation.propTypes = {
    id: PropTypes.string.isRequired,
};

export default Motivation;
