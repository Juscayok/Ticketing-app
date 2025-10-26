# Red Token Tickets

A Flask-based ticketing system with support for ticket creation, work logs, and status tracking.

## Features

- Create and manage support tickets
- Track ticket status (Open/Closed/Canceled)
- Add work logs to tickets
- Export tickets to JSON
- Dark theme UI
- Admin authentication
- Search and filter tickets

## Local Development Setup

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Juscayok/Ticketing-app.git
cd Ticketing-app
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

### Default Login Credentials

- Username: `admin`
- Password: `pass123`

## Deployment to PythonAnywhere

1. Sign up for a free account at [PythonAnywhere](https://www.pythonanywhere.com)

2. Upload your code:
   - Go to the Files tab
   - Create a new directory (e.g., `ticketing-app`)
   - Upload all project files or use Git:
     ```bash
     git clone https://github.com/Juscayok/Ticketing-app.git
     ```

3. Set up a virtual environment:
```bash
mkvirtualenv --python=/usr/bin/python3.9 ticketing-env
pip install -r requirements.txt
```

4. Configure the web app:
   - Go to the Web tab
   - Add a new web app
   - Choose Manual Configuration
   - Select Python 3.9
   - Set up the WSGI configuration file:

```python
import sys
path = '/home/YOUR_USERNAME/ticketing-app'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

5. Update static files configuration:
   - In Web tab, add static files mapping:
     - URL: /static/
     - Directory: /home/YOUR_USERNAME/ticketing-app/static

6. Reload the web app

## Project Structure

```
Ticketing-app/
├── app.py               # Flask application
├── requirements.txt     # Python dependencies
├── tickets.json        # Data storage
├── static/             # Static assets
│   ├── images/         # Images including logo
│   │   └── logo.png
│   └── style.css       # Main stylesheet
└── templates/          # Flask HTML templates
    ├── index.html      # Dashboard
    ├── login.html      # Login page
    ├── submit.html     # Ticket submission
    └── ticket.html     # Ticket details
```

## Security Notes

For production deployment:
1. Change the secret key in `app.py`
2. Update the default admin credentials
3. Consider using a proper database instead of JSON file
4. Set up HTTPS
5. Implement proper user authentication

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.