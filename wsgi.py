import sys
import os

# Add your project directory to Python path
path = os.path.expanduser('~/ticketing-app')
if path not in sys.path:
    sys.path.append(path)

# Import your Flask app
from app import app as application

# Optional: Set environment variables
os.environ['FLASK_ENV'] = 'production'