from flask import Flask, jsonify, request

#App definition
app = Flask(__name__)

#Endpoint definition
stores = [
    {
        'name':'store_name',
        'items:':[
            {
                'name': 'My item',
                'price':'9.99'
            }
        ]
    }
]

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store(data):
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items':[]

    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if name == request_data['name']:
              return jsonify(store)

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})


# POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    if name in stores:
        request_data = request.get_json()
        new_item = {
            'name': request_data['name'],
            'price':float(request_data['name'])

        }
        stores[name]['items'].append(new_item)
        return jsonify(new_item)
    else:
        return jsonify({'message': 'store not found'})


# #Get /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    
    return jsonify({'message': 'store not found'})


app.run(port=8088)