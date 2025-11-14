from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL
from config import Config
import os

# Create Flask app
app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

# Initialize MySQL globally
mysql = MySQL(app)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Import and register blueprints *after* MySQL init
from routes.auth_routes import auth_bp
from routes.report_routes import report_bp
from routes.claim_routes import claim_bp

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(report_bp, url_prefix='/api/report')
app.register_blueprint(claim_bp, url_prefix='/api/claim')

@app.route('/')
def home():
    return {"message": "Lost & Found Flask API running ✅"}

if __name__ == "__main__":
    app.run(debug=True)
