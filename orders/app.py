from flask import Flask
from flask import request, jsonify
import urllib.request, json

app = Flask(__name__)

# TODO: Change API endpoint to call data from REDIS database in docker instead
@app.route('/summary', methods=['POST'])
def total_orders():
    data = request.get_json()
    if not data:
        return jsonify(error="request body cannot be empty"), 400
    print(data)

    #orders = json.loads(data)
    total = 0
    for order in data:
        print(order['id'])    
        country = order['country']
        amount = int(order['amount'])
        tax = get_tax_from_api(country)
        print(amount, tax)
        total += amount * tax
    return jsonify(total_due=total), 200

def get_tax_from_api(country):
    url = "http://127.0.0.1:5000/tax?country={}".format(country)

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return int(dict["Tax"])

if __name__ == "__main__":
    app.run(debug=True, port=3000)


# TODO: Handle errors properly.