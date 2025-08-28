from flask import Blueprint, send_file
import os 

businesses = Blueprint("businesses", __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BUSINESS_FILE = os.path.join(BASE_DIR, '..\data', 'businesses.csv')

@businesses.route("/api/businesses")
def getBusinesses():
    try:
        return send_file(
            BUSINESS_FILE, 
            mimetype='text/csv',
            download_name="businesses.csv",
            as_attachment=False
        ), 200

    except:
        return '<h1>500</h1>', 500