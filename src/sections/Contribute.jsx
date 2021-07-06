import React, { useState } from 'react';
import PropTypes from 'prop-types';
// Components
import Section from 'components/Section'
import NeonButton from 'components/NeonButton'
import Input from 'components/Input'
// Utils
import { validateUrl } from '../utils';


const Contribute = ({ id }) => {

    const [inputValue, setInputValue] = useState('');
    const [inputValid, setInputValid] = useState(false);
    const [inputMessage, setInputMessage] = useState('');
    const [submitted, setSubmitted] = useState(false);


    const handleInputChange = (evt) => {
        setInputValue(evt.target.value);
        setSubmitted(false);
    }

    const handleSubmit = () => {
        const isValid = validateUrl(inputValue);
        setInputValid(isValid);
        if (isValid) {
            setSubmitted(true);
            setInputMessage('');
            setTimeout(() => {
                setInputValue('');
                setSubmitted(false);
            }, 5000)
            return;
        }
        setInputMessage('The input must be a valid URL');
    }

    return (
        <Section id={id} className='relative flex flex-col items-center justify-start text-center'>
            <div className='w-9/10 md:w-5/6 lg:4/5 max-w-250 mx-auto mt-10 mb-32'>
                <h1 className='relative text-6xl md:text-8xl text-chrome font-black mt-0 mb-2 md:mb-6'>Contribute</h1>
                <p className='text-lg md:text-xl text-white text-opacity-85'>
                    Do you have an awesome link that you want to share?
                </p>
                <div className='flex flex-col md:flex-row w-19/20 md:w-full h-auto max-h-16 mx-auto my-10'>
                    <Input
                        type='text'
                        name='link'
                        value={inputValue}
                        placeholder='https://your-awesome-link.com/'
                        subtext={inputMessage}
                        isValid={inputValid}
                        onChange={(evt) => handleInputChange(evt)}
                    />
                    <NeonButton
                        className='xs:w-1/2 md:w-auto md:min-w-48 min-h-12 mt-10 md:mt-0 xs:mx-auto md:ml-auto md:mr-0 xs:px-12 md:px-6 border-1 sm:border-0 border-solid  border-magenta-500'
                        content={submitted ? 'Submitted!' : 'Submit it!'}
                        onClick={() => handleSubmit()}
                    />
                </div>
            </div>
        </Section>
    );
}
Contribute.propTypes = {
    id: PropTypes.string.isRequired,
};

export default Contribute;
