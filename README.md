# QR Code Phishing Campaign Experiment

A web application designed to track user interactions with QR codes.

## Description

This project is an experiment in creating a phishing campaign using QR codes as the entry point. The web application, built using Flask and Python 3.8, tracks user visits by recording their IP address, date, time, user agent string, and the value of the scanned QR code.

The application features two routes:

    /: This route handles GET requests and records user visits to the site if the scanned QR code is valid. It checks against a list of known valid QR codes stored in 'valid_qr.txt'. If the QR code is invalid, it returns a 406 Not Acceptable error.

    '/adminportal': This route is protected by a login form that requires a specific username and password combination to access the admin portal. If the credentials are correct, the user can view all recorded visits and the total number of visits.

Additionally, there are two maintenance routes:

    '/clear_database': This route allows an administrator (identified by a secret key) to delete the entire contents of the database.

    '/logout': This route logs out the currently logged-in user.

## Getting Started

To run this program, you'll need to install Flask, Python 3.8, Flask-SQLAlchemy, and markupsafe. After installing these dependencies, navigate to the directory containing the app.py file in your command prompt or terminal and execute python3 app.py. Navigate to http://127.0.0.1:5000.

### Dependencies

* Flask
* Python 3.8
* Flask-SQLAlchemy
* markupsafe

## Help

If the page won't load, make sure the application is in debug mode. Check that line 99 in app.py looks like this: "app.run(debug=True, host='0.0.0.0')".
