## Flask Application Design for a Conference Speaker Landing Page

### HTML Files

1. **index.html**:
   - Main landing page containing the speaker's personal brand, bio, and call-to-action to contact the speaker.

2. **contact.html**:
   - Contact page with a form for potential clients to reach out to the speaker.

### Routes

1. **@app.route('/')**:
   - Maps to the index.html file and displays the speaker's landing page.

2. **@app.route('/contact')**:
   - Maps to the contact.html file and handles the contact form submission.

3. **@app.route('/submit_contact', methods=['POST'])**:
   - Receives the contact form data, validates it, and sends an email to the speaker.

4. **@app.errorhandler(404)**:
   - Handles 404 errors (page not found) by displaying a custom error page.