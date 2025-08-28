from flask import Flask

from endpoints.accounts import accounts
from endpoints.businesses import businesses
from endpoints.transactions import transactions

app = Flask(__name__)

# Register blueprint endpoints
app.register_blueprint(accounts)
app.register_blueprint(businesses)
app.register_blueprint(transactions)

# Run server under debug. NOTE: This is NOT a production server, this is simply to run the server for the app to
# work, this should NEVER be used for any production software
if __name__ == "__main__":
    app.run(debug=True)