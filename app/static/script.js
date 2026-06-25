// Dynamic content loading
document.addEventListener('DOMContentLoaded', function() {
    // Load Data button handler
    const loadDataBtn = document.getElementById('load-data-btn');
    if (loadDataBtn) {
        loadDataBtn.addEventListener('click', async function() {
            try {
                const response = await fetch('/api/items');
                const data = await response.json();

                const itemsList = document.getElementById('items-list');
                const dataContainer = document.getElementById('data-container');

                itemsList.innerHTML = '';

                if (data.items && data.items.length > 0) {
                    data.items.forEach(item => {
                        const li = document.createElement('li');
                        li.textContent = `${item.name} - ${item.description}`;
                        li.setAttribute('data-item-id', item.id);
                        itemsList.appendChild(li);
                    });
                } else {
                    itemsList.innerHTML = '<li>No items found</li>';
                }

                dataContainer.style.display = 'block';
                loadDataBtn.textContent = 'Refresh Data';
            } catch (error) {
                console.error('Error loading data:', error);
                alert('Failed to load data from API');
            }
        });
    }

    // Toggle Content button handler
    const toggleBtn = document.getElementById('toggle-content-btn');
    if (toggleBtn) {
        toggleBtn.addEventListener('click', function() {
            const toggleContent = document.getElementById('toggle-content');
            if (toggleContent.style.display === 'none') {
                toggleContent.style.display = 'block';
                toggleBtn.textContent = 'Hide Content';
            } else {
                toggleContent.style.display = 'none';
                toggleBtn.textContent = 'Toggle Content';
            }
        });
    }

    // Contact Form Validation and Submission
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();

            // Clear previous error messages
            document.getElementById('name-error').textContent = '';
            document.getElementById('email-error').textContent = '';
            document.getElementById('message-error').textContent = '';
            document.getElementById('form-success').style.display = 'none';
            document.getElementById('form-error').style.display = 'none';

            // Get form values
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();

            let isValid = true;

            // Validate name
            if (name === '') {
                document.getElementById('name-error').textContent = 'Name is required';
                isValid = false;
            } else if (name.length < 2) {
                document.getElementById('name-error').textContent = 'Name must be at least 2 characters';
                isValid = false;
            }

            // Validate email
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (email === '') {
                document.getElementById('email-error').textContent = 'Email is required';
                isValid = false;
            } else if (!emailRegex.test(email)) {
                document.getElementById('email-error').textContent = 'Please enter a valid email address';
                isValid = false;
            }

            // Validate message
            if (message === '') {
                document.getElementById('message-error').textContent = 'Message is required';
                isValid = false;
            } else if (message.length < 10) {
                document.getElementById('message-error').textContent = 'Message must be at least 10 characters';
                isValid = false;
            }

            // If validation passes, show success message
            if (isValid) {
                document.getElementById('form-success').style.display = 'block';
                contactForm.reset();

                // Hide success message after 5 seconds
                setTimeout(() => {
                    document.getElementById('form-success').style.display = 'none';
                }, 5000);
            } else {
                document.getElementById('form-error').style.display = 'block';
            }
        });

        // Reset button handler
        const resetBtn = document.getElementById('reset-btn');
        if (resetBtn) {
            resetBtn.addEventListener('click', function() {
                // Clear error messages
                document.getElementById('name-error').textContent = '';
                document.getElementById('email-error').textContent = '';
                document.getElementById('message-error').textContent = '';
                document.getElementById('form-success').style.display = 'none';
                document.getElementById('form-error').style.display = 'none';
            });
        }
    }
});
