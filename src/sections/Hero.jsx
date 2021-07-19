import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';
import { Element } from 'react-scroll';
// Images
import retroWave from 'images/retro-wave.jpg';
import awesomeLink from 'images/awesomelink.png';


const Wrapper = styled.div`
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
        <Element id={id} name={id}>
            <Wrapper className='relative flex flex-col items-center justify-center bg-indigo-200 w-full h-full bg-cover bg-center bg-no-repeat min-h-160 md:min-h-220 xl:min-h-220' style={bgStyle}>
                <img
                    className='relative -top-12 md:-top-3/5 lg:-top-1/2 xl:-top-1/3 w-9/10 md:w-4/5 xl:w-3/4 mx-auto pointer-events-none'
                    src={awesomeLink}
                    alt='logo'
                />
            </Wrapper>
        </Element>
    );
}
Hero.propTypes = {
    id: PropTypes.string.isRequired,
};

export default Hero;
