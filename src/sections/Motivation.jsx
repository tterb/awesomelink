import React from 'react';
import PropTypes from 'prop-types';
// Components
import Section from 'components/Section'


const Motivation = ({ id }) => (
    <Section
        id={id}
        title={'Motivation'}
        className='relative flex flex-col items-center justify-start text-center'
    >
        <p className='text-lg md:text-xl text-white text-opacity-85'>
            The internet was once the new great frontier. It was exciting, unpredictable, disorganized, and fostered exploration.<br />
            Though as the internet has <span className='strikethrough'>d</span>evolved, digital exploration has deteriorated to scrolling sterilized feeds from major social-media networks.<br />
            The unique discoveries and experiences that could be expected from the early internet have seemingly fallen by the wayside.
            <a href='http://awesomel.ink/' className='font-rage rage-link text-accent hover:text-magenta-500 pl-2' target='_blank' rel='noopener noreferrer'>AwesomeLink</a> is an attempt to bring back some of that unpredictability and exploration.
        </p>
    </Section>
);
Motivation.propTypes = {
    id: PropTypes.string.isRequired,
};

export default Motivation;
