from flask import Blueprint, request, send_file
import os

transactions = Blueprint("transactions", __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRANSACTIONS_FOLDER = os.path.join(BASE_DIR, '..\data', 'transactions')

@transactions.route("/api/transactions")
def getTransactions():
    try:
        page_num = request.args.get('page')
        quantity = request.args.get('size') # TODO: Implement size, might need restructure this file

        page_num = int(page_num) + 1

        transactions_file = os.path.join(TRANSACTIONS_FOLDER, "transaction_"+str(page_num)+".json")

        return send_file(
            transactions_file,
            mimetype='application/json',
            download_name="transaction_"+str(page_num)+".json",
            as_attachment=False
        ), 200
    
    except:
        return '<h1>500</h1>', 500