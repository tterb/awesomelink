import React from 'react';
import PropTypes from 'prop-types';
import { Element } from 'react-scroll';


const Section = (props) => {
    const {id, className, title, children, ...rest} = props;
    return (
        <Element id={id} name={id}>
            <div
                className={`bg-indigo-200 w-full h-full${className ? ` ${className}` : ''}`}
                {...rest}
            >
                <div className='w-9/10 md:w-5/6 lg:4/5 max-w-250 mx-auto mt-10 mb-32'>
                    <h1 className='relative text-5xl md:text-6xl lg:text-8xl font-rage font-black text-accent mt-0 mb-4 md:mb-6' style={{ 'transform': 'rotate(-3deg)' }}>
                        {title}
                    </h1>
                    {children}
                </div>
            </div>
        </Element>
    );
};
Section.propTypes = {
    id: PropTypes.string.isRequired,
    title: PropTypes.string.isRequired,
    className: PropTypes.string,
    children: PropTypes.oneOfType([
        PropTypes.arrayOf(PropTypes.node),
        PropTypes.node,
    ]),
};

export default Section;