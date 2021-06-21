import React from 'react';
import PropTypes from 'prop-types';
// Components
import Section from 'components/Section'


const Input = () => {

}

const Submit = () => (
    <span className='w-auto h-full border-2 border-solid border-magenta-400 rounded-sm p-2'>
        <span className='relative w-full h-full border-2 border-solid border-magenta-400 rounded-sm p-1'>
            <input type='submit' value='Submit it' className='submit-button font-rage bg-magenta-400 text-xl text-white rounded-sm py-2 px-6 cursor-pointer' />
        </span>
    </span>
)


const Contribute = ({ id }) => (
    <Section id={id} className='relative flex flex-col items-center justify-start text-center'>
        <div className='w-9/10 md:w-4/5 max-w-250 mx-auto mt-10 mb-32'>
            <h1 className='relative text-8xl text-chrome font-black mt-0 mb-6'>Contribute</h1>
            <p className='text-xl text-white text-opacity-85'>
                Do you have an awesome link that you would like to share?
            </p>
            <form className='flex flex-row w-full my-10'>
                <input
                    type='text'
                    value=''
                    placeholder='https://your-awesome-link.com/'
                    className='font-sans bg-black bg-opacity-40 text-xl text-accent w-full rounded-full shadow-inner mr-6 py-1 px-6 focus:outline-none'
                />
                <Submit />
                {/* <input type='submit' value='Submit it' className='submit-button font-rage bg-gradient-to-b from-magenta-400 via-magenta-500 to-magenta-400 text-xl text-white rounded-full py-2 px-6 cursor-pointer' /> */}
            </form>
        </div>
    </Section>
);
Contribute.propTypes = {
    id: PropTypes.string.isRequired,
};

export default Contribute;
