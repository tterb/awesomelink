import { keyframes, css } from 'styled-components'


const topLine = keyframes`
    0% { top: -100%; }
    100% { top: 100%; }
`
const leftLine = keyframes`
    0% { left: -100%; }
    100% { left: 100%; }
`
const rightLine = keyframes`
    0% { right: -100%; }
    100% { right: 100%; }
`
const bottomLine = keyframes`
    0% { bottom: -100%; }
    100% { bottom: 100%; }
`
export const lineAnimation = (direction, delay) => {
    let animation;
    if (direction === 'top') {
        animation = topLine;
    } else if (direction === 'left') {
        animation = leftLine;
    } else if (direction === 'right') {
        animation = rightLine;
    } else if (direction === 'bottom') {
        animation = bottomLine;
    }
    return (
        css`animation: ${animation} 300ms linear ${delay};`
    );
}