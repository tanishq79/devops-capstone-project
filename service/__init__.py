"""
Package: service
Package for the application models and service routes
This module initializes the Flask app and security features
"""
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

# Security headers using Talisman
talisman = Talisman(app)

# Cross-Origin Resource Sharing (CORS) policies
CORS(app)

from service import routes, models
