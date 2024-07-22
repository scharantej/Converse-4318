
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, flash

# Initialize the Flask application
app = Flask(__name__)

# Set up secret key for session management
app.secret_key = 'mysecretkey'

# Home page route
@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')

# Contact page route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Handle the contact page."""
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Validate the form data
        if not name or not email or not message:
            flash('All fields are required.')
            return redirect(url_for('contact'))

        # Send the email to the speaker
        # ... (Code to send the email goes here) ...

        # Redirect to the home page with a success message
        flash('Your message has been sent.')
        return redirect(url_for('index'))

    return render_template('contact.html')

# Custom error handler for 404 errors
@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors."""
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
