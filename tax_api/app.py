from flask import Flask
from flask import request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'taxes',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)

@app.route('/tax')
def tax_by_country():
    country_arg = request.args.get('country')
    #print(country_arg)
    #for tax in Tax.objects:
    #    print(tax.country)
    #   print(tax.value)
    db_tax = Tax.objects(country=country_arg).first()
    if not db_tax:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(db_tax.to_json())

class Tax(db.Document):
    country = db.StringField()
    value = db.StringField()
    def to_json(self):
        return {"Country": self.country,
                "Tax": self.value}

if __name__ == "__main__":
    app.run(debug=True, port=5000)

# readme 
# pip install flask
# pip install flask-mongoengine
###
#Schema MongoDB:
#{
#  "_id": {
#    "$oid": "644093d44100e8d352e8ee06"
#  },
#  "country": "BR",
#  "value": 11
#}
###