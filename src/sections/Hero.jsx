import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';
// Components
import Section from 'components/Section'
// Images
import retroWave from 'images/retro-wave.jpg';
import awesomeLink from 'images/awesomelink.png';


const StyledSection = styled(Section)`
    &::after {
        content: '';
        position: absolute;
        background: linear-gradient(to top, #1D0B40, transparent);
        width: 100vw;
        height: 16rem;
        bottom: 0;
    }
`

const Hero = ({ id }) => {

    const bgStyle = {
        backgroundImage: `url(${retroWave})`,
    };

    return (
        <StyledSection id={id} className='relative flex flex-col items-center justify-center bg-cover bg-center bg-no-repeat min-h-160 md:min-h-180 xl:min-h-220' style={bgStyle}>
            <img
                className='relative -top-12 md:-top-16 lg:-top-20 w-full sm:w-9/10 md:w-4/5 xl:w-3/4 mx-auto pointer-events-none'
                src={awesomeLink}
                alt='logo' 
            />
        </StyledSection>
    );
}
Hero.propTypes = {
    id: PropTypes.string.isRequired,
};

export default Hero;
