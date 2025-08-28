import uuid, names, random, requests, json, csv
from datetime import datetime, timedelta

# Account information

""" Generate account data for a json file """
def genAccountData():
    headers = {'Content-Type': 'application/json'} # POST request header
    
    # Account JSON object template
    account_template = {
        "id": "",
        "name": "",
        "startingBalance": 0.0,
        "roundUpEnabled": False
    }
    
    # Generate X number of accounts
    for i in range(0, 1000):
        entry = createNewAccount(account_template) # Make new account entry
        
        # Make POST request to create-account endpoint using correct headers & bypassing SSL verification
        response = requests.post("http://127.0.0.1:5000/api/create-account", json=entry, verify=False, headers=headers)    

        # If the entry was added successfully (201 = Created)
        if response.status_code == 201:
            print("Successfully created new entry")
            
        # There was an issue when POSTing, break out of loop and end
        else:
            print("Error when trying to POST")
            break

""" Generate a new account entry with a unique UUID4 uuid, name, starting balance and round up """
def createNewAccount(template) -> dict:
    new_entry = template
    
    new_entry["id"] = uuid.uuid4().__str__()
    new_entry["name"] = names.get_full_name()
    new_entry["startingBalance"] = round(random.uniform(0.0, 10000.0), 2)
    new_entry["roundUpEnabled"] = random.choice([True, False])

    return new_entry

# Transaction information

""" Generate x number of transaction page json files containing a variety of transaction types """
def genTransactionData(pages:int=1):
    for i in range(0, pages):
        template = { 
            "pageResult": {
                "results": [],
                
                "hasNext": True if i+1 != pages else False
            }
        }
        
        results = []
        
        for j in range(0, 1000):
            results.append(genSingleTransaction())
            
        template["pageResult"]["results"] = results
    
        with open('data/transactions/transaction_'+ str(i+1) +'.json', 'x') as f:
            json.dump(template, f, indent=4)
            
        print("Successfully created transaction_" + str(i+1) +'.json')
    
    print("Successfully generated " + str(pages) + " transaction pages")
    
""" Generate a single new transaction entry with a unique UUID4 uuid,   """
def genSingleTransaction() -> dict:
    entry = {
        "id": "",
        "timestamp": "",
        "type": "",
        "to": "",
        "from": "",
        "amount": 0.0
    }
    
    start_time = datetime.strptime('1/1/2018 12:00 AM', '%d/%m/%Y %I:%M %p')
    end_time = datetime.strptime('1/12/2024 12:00 AM', '%d/%m/%Y %I:%M %p')
    
    entry["id"] = str(uuid.uuid4())
    entry["timestamp"] = str(genRandomTimestamp(start_time, end_time))
    
    # This is where we choose the transaction type, each type has slightly differing json formats
    entry["type"] = random.choice(["PAYMENT", "WITHDRAWAL", "DEPOSIT", "TRANSFER"])
    
    match entry["type"]:
        case "PAYMENT":
            entry = genPaymentTransaction(entry)
        
        case "WITHDRAWAL":
            entry = genWithdrawalTransaction(entry)
            
        case "DEPOSIT":
            entry = genDepositTransaction(entry)
        
        case "TRANSFER":
            entry = genTransferTransaction(entry)
            
        # Default case
        case _:
            pass    
    
    return entry

""" Generate a payment transaction structure given a base dictionary """
def genPaymentTransaction(base:dict) -> dict:
    new_payment = {
        "id": base["id"],
        "timestamp": base["timestamp"],
        "type": base["type"],
        "amount": round(random.uniform(0.0, 10000.0), 2),
        "to": genRandomBusinessID(),
        "from": genRandomAccountUUID()
    }
    
    return new_payment

""" Generate a withdrawal transaction structure given a base dictionary """
def genWithdrawalTransaction(base:dict) -> dict:
    new_withdrawal = {
        "id": base["id"],
        "timestamp": base["timestamp"],
        "type": base["type"],
        "amount": round(random.uniform(0.0, 10000.0), 2),
        "from": genRandomAccountUUID()
    }
    
    return new_withdrawal

""" Generate a deposit transaction structure given a base dictionary """
def genDepositTransaction(base:dict) -> dict:
    new_deposit = {
        "id": base["id"],
        "timestamp": base["timestamp"],
        "type": base["type"],
        "amount": round(random.uniform(0.0, 10000.0), 2),
        "to": genRandomAccountUUID()
    }
    
    return new_deposit

""" Generate a transfer transaction structure given a base dictionary """
def genTransferTransaction(base:dict) -> dict:
    acc_ids = genRandomAccountUUID(2)
    
    new_transfer = {
        "id": base["id"],
        "timestamp": base["timestamp"],
        "type": base["type"],
        "amount": round(random.uniform(0.0, 10000.0), 2),
        "to": acc_ids[0],
        "from": acc_ids[1]
    }
    
    return new_transfer

""" Generate a random timestamp between 2 boundaries """
def genRandomTimestamp(start:datetime, end:datetime) -> datetime:
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    
    random_second = random.randrange(int_delta)
    
    return start + timedelta(seconds=random_second)

""" Find random account uuid(s) from accounts.json and return it """
def genRandomAccountUUID(amount:int=1) -> str | list[str]:
    ids = []
    
    with open('data/accounts.json', 'r') as f:
        data = json.load(f)
        
        for entry in data:
            ids.append(entry["id"])
            
    if amount > 1:
        id_list = []
            
        acc_id = random.choice(ids)
        
        for i in range(0, amount):
            while acc_id in id_list:
                acc_id = random.choice(ids)
                
            id_list.append(acc_id)
    
        return id_list
    
    else:    
        return random.choice(ids)

""" Find random business id from businesses.csv and return it """
def genRandomBusinessID() -> str:
    
    ids = []
    
    with open('data/businesses.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        pass_column = False
        
        for row in reader:
            if pass_column:
                ids.append(row[0])
    
            else:
                pass_column = True
    
    return random.choice(ids)

# TO RUN
# Account Data
# # If you want to generate new account data, clear the accounts.json file inside of /data, then leave empty square braces ([])
# # Run `genAccountData()` to generate 1000 new accounts. NOTE: If you do this, you will need to regenerate the transaction data.

# Transaction Data
# # To generate new transaction data, delete all files inside of /data/transactions. Then run `genTransactionData()` By default,
# # it will make 1 page. If you want more than 1 page of data, add the number of pages you want inside the function.

# Example (After having cleared/deleted the correct files):

# genAccountData()
# genTransactionData(5)