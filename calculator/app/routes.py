from app import utils
from flask import Flask, request, jsonify
from app import flask_app


@flask_app.route('/calculate', methods=['POST'])
def calculate_expression():
    data = request.json
    a = list(data['expression'])
    return jsonify({"res": utils.calculate_expression(
        utils.convert_to_polish(utils.make_list_ok(a)))}), 200


@flask_app.route('/')
def hello():
    return "Hello, world!"