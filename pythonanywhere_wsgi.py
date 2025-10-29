# Production WSGI configuration for PythonAnywhere
# Save this file to: /var/www/snith_pythonanywhere_com_wsgi.py

import sys
import os

# Add your project directory to the sys.path
project_home = '/home/snith/pdf_tool'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set working directory
os.chdir(project_home)

# Import flask app
from web_app import app as application
