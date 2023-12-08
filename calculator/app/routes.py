from app import utils
from flask import Flask, request
from app import flask_app

@flask_app.route('/calculate', methods=['GET'])
def calculate_expression():
    a = list(request.args.get('expression'))
    return a
    #return calculate_expression(utils.convert_to_polish(utils.make_list_ok(a)))

@flask_app.route('/')
def hello():
    return "Hello, world!"