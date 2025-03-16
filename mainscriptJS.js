document.addEventListener('DOMContentLoaded', () => {
    const textDisplay = document.getElementById('text-display');
    const textInput = document.getElementById('text-input');
    const text = "This is a sample text for typing practice.";
    
    // Split the text into individual characters
    const textArray = text.split('');
    
    // Display the text with each character wrapped in a span
    textDisplay.innerHTML = textArray.map(char => `<span>${char}</span>`).join('');
    
    const spans = textDisplay.querySelectorAll('span');
    let currentIndex = 0;
    
    textInput.addEventListener('input', () => {
        const inputValue = textInput.value;
        const inputArray = inputValue.split('');
        
        inputArray.forEach((char, index) => {
            if (char === textArray[index]) {
                spans[index].classList.add('correct');
                spans[index].classList.remove('incorrect');
            } else {
                spans[index].classList.add('incorrect');
                spans[index].classList.remove('correct');
            }
        });
        
        currentIndex = inputValue.length;
        
        // Remove highlighting for the rest of the text
        for (let i = currentIndex; i < textArray.length; i++) {
            spans[i].classList.remove('correct', 'incorrect');
        }
    });
});
