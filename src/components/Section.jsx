import React from 'react';
import PropTypes from 'prop-types';
import { Element } from 'react-scroll';


const Section = (props) => {
    const {id, className, children, ...rest} = props;
    return (
        <Element id={id} name={id}>
            <div
                className={`bg-indigo-200 w-full h-full${className ? ` ${className}` : ''}`}
                {...rest}
            >
                {children}
            </div>
        </Element>
    );
};
Section.propTypes = {
    id: PropTypes.string.isRequired,
    className: PropTypes.string,
    children: PropTypes.oneOfType([
        PropTypes.arrayOf(PropTypes.node),
        PropTypes.node,
    ]),
};

export default Section;