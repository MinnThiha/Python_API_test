import http

from flask import Flask, render_template, jsonify, make_response, request, Response

app = Flask(__name__)


@app.route('/world')
def get_hello_world():
    return "Hello World!"


@app.route('/mth')
def get_hello_mth():
    return "Hello Minn Thiha!"


@app.route('/html')
def get_html():
    return render_template('index.html')


@app.route('/orders')
def get_orders():
    resp = make_response(jsonify(order), 200)
    return resp


@app.route('/orders/<order_id>')
def getOrderByID(order_id):
    if order_id not in order:
        return "order not found!"
    else:
        resp = make_response(jsonify(order[order_id]), 200)
        return resp


@app.route("/postorder/<order_id>", methods=["POST"])
def postOrder(order_id):
    req = request.get_json()
    if order_id in order:
        resp = make_response(jsonify({"error: order_id already exist!"}), 400)
        return resp
    order.update({order_id: req})
    resp: Response = make_response(jsonify({"Message: New order Create"}), 201)
    return resp


order = {
    'order1': {
        "Size": "Medium",
        "Topping": "Cheese",
        "Crust": "Thin Crust"
    },
    'order2': {
        "Size": "Large",
        "Topping": "Tomato",
        "Crust": "Thick Crust"
    },
    'order3': {
        "Size": "Small",
        "Topping": "Cheese",
        "Crust": "Thin Crust"
    },

}

if __name__ == '__main__':
    app.run(debug=True)
