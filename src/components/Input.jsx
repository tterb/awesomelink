import React from 'react';
import PropTypes from 'prop-types';


const Input = ({ className, type, name, value, onChange, placeholder, subtext, isValid, autocomplete }) => {
    const validationClass = !isValid && subtext.length ? 'border-red-400' : 'border-transparent';
    return (
        <div className='flex flex-col w-full mr-6'>
            <input
                className={`font-sans bg-black bg-opacity-40 text-lg text-accent w-full min-h-12 rounded shadow-inner border-1 border-solid py-1 px-4 md:px-6 focus:outline-none ${validationClass}${className ? ` ${className}` : ''}`}
                type={type}
                name={name}
                value={value}
                onChange={onChange}
                placeholder={placeholder}
                autoComplete={autocomplete.toString()}
            />
            {!isValid && subtext.length ?
                <span className='text-sm text-red-400 text-center md:text-left w-full mx-auto pt-1 pl-0 md:pl-1'>{subtext}</span>
            : null}
        </div>
    );
}
Input.defaultProps = {
    type: 'text',
    autocomplete: false,
};
Input.propTypes = {
    className: PropTypes.string, 
    type: PropTypes.string,
    subtext: PropTypes.string,
    name: PropTypes.string.isRequired,
    value: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
    placeholder: PropTypes.string.isRequired,
    onChange: PropTypes.func.isRequired,
    isValid: PropTypes.bool.isRequired,
    autocomplete: PropTypes.bool,
};

export default Input;
