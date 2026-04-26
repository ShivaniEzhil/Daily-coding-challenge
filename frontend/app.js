document.addEventListener('DOMContentLoaded', async () => {
    try {
        // Fetch the challenge from the data folder
        // Note: When deployed, this path needs to be correct relative to the HTML
        const response = await fetch('../data/challenge.json');
        const data = await response.json();

        // Update the UI
        document.getElementById('challenge-date').textContent = data.date;
        document.getElementById('challenge-title').textContent = data.title;
        document.getElementById('challenge-description').textContent = data.description;
        
        const difficultyEl = document.getElementById('challenge-difficulty');
        difficultyEl.textContent = data.difficulty;
        difficultyEl.classList.add(data.difficulty.toLowerCase());

        // Update link
        const solveBtn = document.getElementById('solve-btn');
        solveBtn.href = data.link || `https://www.google.com/search?q=how+to+solve+${encodeURIComponent(data.title)}+programming+challenge`;
        solveBtn.target = "_blank";

    } catch (error) {
        console.error('Error loading challenge:', error);
        document.getElementById('challenge-title').textContent = 'Oops! Failed to load.';
        document.getElementById('challenge-description').textContent = 'Check back soon for more challenges.';
    }
});
