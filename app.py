from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from api.api_core import Inventory, get_price, get_profile

app = Flask(__name__)
CORS(app)


@app.route('/api', methods=["POST"])
def api():
    if request.method == 'POST':
        try:
            res = json.loads(request.data)
            data = Inventory(res['id'], res['app'])
            inv = data.get_inventory()
            return jsonify(inv)
        except:
            return jsonify({'error': 'Bad request'})


@app.route('/price_item', methods=["GET"])
def market():
    item_name = request.args.get('name', default='None', type=str)
    app_id = request.args.get('app', default=730, type=int)
    currency = request.args.get('currency', default=5, type=int)
    data = get_price(item_name, app_id, currency)
    return jsonify(data)

@app.route('/profile', methods=["GET"])
def profile():
    steamid = request.args.get('steamid')
    data = get_profile(steamid)
    return jsonify(data)


if __name__ == '__main__':
    app.run()