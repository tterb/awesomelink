import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';
// Styles
import { lineAnimation } from 'styles/animations'


const Button = styled.button`
    transform: scale(1);
    transition: all 300ms ease-in-out;
    &:hover {
        box-shadow: 0 0 5px #FD427A, 0 0 20px #FD427A, 0 0 40px #FD427A;
        transition-delay: 450ms;
        .line-top {
            ${lineAnimation('top', '250ms')}
        }
        .line-left {
            ${lineAnimation('left', '0ms')}
        }
        .line-right {
            ${lineAnimation('right', '250ms')}
        }
        .line-bottom {
            ${lineAnimation('bottom', '0ms')}
        }
    }
    &:active {
        transform: scale(0.95);
        box-shadow: 0 0 2px #FD427A, 0 0 10px #FD427A, 0 0 20px #FD427A;
    }
`

const NeonButton = ({ className, content, onClick, children }) => {
    const buttonText = content ? content : children;
    return (
        <Button
            className={`relative bg-white bg-opacity-10 font-rage text-xl text-accent w-auto rounded-md py-2 px-6 overflow-hidden focus:outline-none hover:bg-magenta-500 hover:text-white active:bg-magenta-500 active:text-white${className ? ` ${className}` : ''}`}
            onClick={onClick}
        >
            <span className='line-left absolute bg-gradient-to-l from-transparent to-magenta-400 w-full h-px -left-full bottom-0' />
            <span className='line-bottom absolute bg-gradient-to-b from-transparent to-magenta-400 w-px h-full -bottom-full right-0' />
            <span className='line-right absolute bg-gradient-to-r from-transparent to-magenta-400 w-full h-px -right-full top-0' />
            <span className='line-top absolute bg-gradient-to-t from-transparent to-magenta-400 w-px h-full -top-full left-0' />
            {buttonText}
        </Button>
    );
}
NeonButton.propTypes = {
    className: PropTypes.string,
    content: PropTypes.string,
    onClick: PropTypes.func,
    children: PropTypes.node,
};

export default NeonButton;