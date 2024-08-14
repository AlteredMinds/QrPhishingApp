# QR Code Phishing Campaign Experiment

A web application designed to track user interactions with QR codes for educational and research purposes.

## Overview

This project is an experiment in creating a phishing campaign using QR codes as the entry point. The web application is built with Flask and Python 3.8 and is designed to record user interactions by logging details such as IP addresses, date and time of visits, user agent strings, and the specific QR code scanned.

## Features

The application provides the following key features:

- **User Tracking**: Records details of each visit, including IP address, date, time, user agent, and QR code value.
- **QR Code Validation**: Validates scanned QR codes against a list of pre-approved codes stored in `valid_qr.txt`.
- **Admin Portal**: A protected route that allows authorized users to view all recorded visits and the total number of visits.
- **Database Management**: Provides maintenance routes for clearing the database and managing user sessions.

### Routes

1. **`/` (Root Route)**  
   Handles GET requests to record user visits when a valid QR code is scanned. If the QR code is invalid, a 406 Not Acceptable error is returned.

2. **`/adminportal`**  
   A protected route requiring a specific username and password to access the admin portal. Once logged in, users can view a summary of all recorded visits.

3. **`/clear_database`**  
   Allows an administrator, identified by a secret key, to delete all records from the database.

4. **`/logout`**  
   Logs out the currently logged-in admin user, ending the session.

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/AlteredMinds/QrPhishingApp.git
   cd QrPhishingApp
2. **Install Dependencies**
   Ensure you have Python 3.8 installed, then install the required packages:
   ```bash
   pip install Flask Flask-SQLAlchemy markupsafe
4. **Run the Application**  
   Start the application by navigating to the directory containing app.py and running:
   ```bash
   python3 app.py 

## Help

Page Not Loading?

If you're having trouble loading the page, ensure the application is running in debug mode. Verify that line 99 in app.py is set as follows:

    app.run(debug=True, host='0.0.0.0')

Deploying the Application?

For deployment, make sure the application is behind a WSGI server and reverse proxy. In this case, line 99 in app.py should be updated to:

    app.run()
