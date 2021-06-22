import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-scroll';
import styled from 'styled-components';
// Images
import logo from 'images/logo.png';


const MenuLink = styled(Link)`
    color: transparent !important;
    &::before {
        content: '';
        display: block;
        position: absolute;
        background: #FD427A;
        height: 3px;
        top: 50%;
        left: -10%;
        right: -10%;
        border-radius: 2px;
        margin-top: 0px;
        transform: scale(0);
        transition: transform 900ms cubic-bezier(.16,1.08,.38,.98);
        z-index: 99999;
    }

    &:hover, &:active {
        &::before {
            transform: scale(1);
        }
        .menu-item-mask {
            color: #FFF;
            transform: skewX(-12deg) translateX(4px);
        }
        .menu-item-mask + .menu-item-mask {
            transform: skewX(-12deg) translateX(-4px);
        }
    }

    .menu-item-mask {
        transition: all 900ms cubic-bezier(0.16, 1.08, 0.38, 0.98);
    }

    .menu-item-mask + .menu-item-mask {
        height: 59.9%;
        top: 49.9%;
        span {
            transform: translateY(-50%);
        }
    }
`

const InlineMenu = ({ sectionLinks }) => (
    <div className='block right-0 sm:right-10 ml-auto'>
        <ul className='menu flex flex-row relative bg-transparent w-full font-title font-medium text-right list-reset m-0 z-9999'>
            {sectionLinks.map(({ id, label }) => (
                <MenuLink
                    key={id}
                    className='inline-block relative text-gray-1000 text-opacity-90 text-base md:text-lg lg:text-xl text-center font-semibold w-auto mr-5 last:mr-0 p-0 cursor-pointer z-9999'
                    smooth={true}
                    spy={true}
                    offset={50}
                    duration={500}
                    delay={0}
                    to={id}
                >
                    {label}
                    <span className='menu-item-mask absolute block text-white text-opacity-80 font-semibold h-1/2 top-0 overflow-hidden'>
                        <span className='block'>{label}</span>
                    </span>
                    <span className='menu-item-mask absolute block text-white text-opacity-80 font-semibold h-1/2 top-0 overflow-hidden'>
                        <span className='block'>{label}</span>
                    </span>
                </MenuLink>
            ))}
        </ul>
    </div>
);
InlineMenu.propTypes = {
    sectionLinks: PropTypes.arrayOf(PropTypes.shape({
        id: PropTypes.string.isRequired,
        label: PropTypes.string.isRequired,
    })),
};

const Navbar = ({ sectionLinks }) => (
    <div className='nav-wrapper relative block font-title h-0 top-0 left-0 right-0 z-999'>
        <div className='flex relative w-9/10 md:w-4/5 h-22 flex-wrap items-center align-middle mx-auto pt-6 pb-4 px-0 box-border'>
            <div className='w-6 sm:w-8 md:w-12 h-auto ml-0 mr-auto'>
                <Link
                    className='w-6 sm:w-8 md:w-12 h-auto'
                    smooth={true}
                    spy={true}
                    offset={50}
                    duration={500}
                    delay={0}
                    to={'hero'}
                >
                    <img src={logo} alt='AwesomeLink' />
                </Link>
            </div>
            <InlineMenu sectionLinks={sectionLinks} />
        </div>
    </div>
);
Navbar.propTypes = {
    sectionLinks: PropTypes.arrayOf(PropTypes.shape({
        id: PropTypes.string.isRequired,
        label: PropTypes.string.isRequired,
    })),
};

export default Navbar;
