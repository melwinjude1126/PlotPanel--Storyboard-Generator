document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('script-form');
    const loading = document.getElementById('loading');
    const storyboard = document.getElementById('storyboard');
    const imageGrid = document.getElementById('image-grid');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const script = document.getElementById('script').value;
        if (!script.trim()) {
            alert('Please enter a script.');
            return;
        }

        // Hide form and show loading
        form.classList.add('hidden');
        loading.classList.remove('hidden');
        storyboard.classList.add('hidden');
        imageGrid.innerHTML = '';

        try {
            const response = await fetch('/generate', {
                method: 'POST',
                body: new FormData(form),
            });

            if (!response.ok) {
                throw new Error('An error occurred while generating the storyboard.');
            }

            const data = await response.json();

            // Hide loading and show storyboard
            loading.classList.add('hidden');
            storyboard.classList.remove('hidden');

            if (data.images && data.images.length > 0) {
                data.images.forEach(imageUrl => {
                    const img = document.createElement('img');
                    img.src = imageUrl;
                    img.alt = 'Storyboard Image';
                    imageGrid.appendChild(img);
                });
            } else {
                imageGrid.innerHTML = '<p>No images were generated. Please try a different script.</p>';
            }
        } catch (error) {
            // Hide loading and show form again
            loading.classList.add('hidden');
            form.classList.remove('hidden');
            alert(error.message);
        }
    });
});
