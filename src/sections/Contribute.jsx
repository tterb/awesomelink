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
        <Section id={id} title={'Contribute'} className='relative flex flex-col items-center justify-start text-center'>
            <p className='text-lg md:text-xl text-white text-opacity-85'>
                Do you have an awesome link that you want to share?
            </p>
            <div className='flex flex-col md:flex-row w-19/20 md:w-full h-auto max-h-16 mx-auto my-6 sm:my-10'>
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
                    className='w-2/3 md:w-auto md:min-w-48 min-h-14 md:min-h-12 mt-10 md:mt-0 xs:mx-auto md:ml-auto md:mr-0 xs:px-12 md:px-6 border-1 sm:border-0 border-solid  border-magenta-500'
                    content={submitted ? 'Submitted!' : 'Submit it!'}
                    onClick={() => handleSubmit()}
                />
            </div>
        </Section>
    );
}
Contribute.propTypes = {
    id: PropTypes.string.isRequired,
};

export default Contribute;
