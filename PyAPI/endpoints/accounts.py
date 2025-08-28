from flask import Blueprint, request, jsonify, send_file
import json, os

accounts = Blueprint("accounts", __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ACCOUNTS_FILE = os.path.join(BASE_DIR, '..\data', 'accounts.json')

""" Return a list of accounts """
@accounts.route("/api/accounts")
def getAccounts():
    try:
        return send_file(
            ACCOUNTS_FILE, 
            mimetype='application/json',
            download_name="accounts.json",
            as_attachment=False
        ), 200

    except:
        return '<h1>500</h1>', 500

""" Add an account to the accounts list """
@accounts.route("/api/create-account", methods=["POST"])
def createAccount():
    data = request.get_json()
    
    if checkAccountValidity(data):
        
        with open(ACCOUNTS_FILE, "r") as f:
            try:
                accounts_json = json.load(f)
                
            except:
                accounts_json = []
                
        accounts_json.append(data)
            
        print(accounts_json)
        
        with open("accounts.json", "w") as f:
            json.dump(accounts_json, f, indent=4)
            
        return jsonify(data), 201
    
    else:
        return '<h1>400</h1>', 400

""" Get an account by its ID """
@accounts.route("/api/account")
def getAccount():
    acc_id = request.args.get('id')
    
    with open(ACCOUNTS_FILE, "r") as f:
        data = json.load(f)
        
        for entry in data:
            if "id" in entry:
                if entry["id"] == acc_id:
                    return entry, 200

    return '<h1>404</h1>', 404

def checkAccountValidity(data):
    valid = 0
    
    if "id" in data:
        if isinstance(data["id"], str):
            # Do UUID checks, i.e. check if unique, check pattern e.g. (3ac94ff3-ee6a-473a-ad35-c36164229144)
            valid += 1

    if "name" in data:
        if isinstance(data["name"], str):
            valid += 1
            
    if "startingBalance" in data:
        if isinstance(data["startingBalance"], float):
            valid += 1

    if "roundUpEnabled" in data:
        if isinstance(data["roundUpEnabled"], bool):
            valid += 1

    if valid == 4:
        return True
    
    else:
        return False