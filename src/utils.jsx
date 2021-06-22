import { ReturnDownBack } from '@styled-icons/ionicons-sharp';
import React from 'react';


const validateUrl = (value) => {
    return /((?:(?:http?|ftp)[s]*:\/\/)?[a-z0-9-%\/\&=?\.]+\.[a-z]{2,4}\/?([^\s<>\#%"\,\{\}\\|\\\^\[\]`]+)?)/gi.test(value)
};

export {
    validateUrl,
};