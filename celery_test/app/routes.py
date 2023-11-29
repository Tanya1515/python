from flask import Flask, request, render_template, redirect, url_for
import time
from app import flask_app
from app import celery_app
import sys

@flask_app.route('/time', methods=['GET'])
def sleep():
    print(f'_______', file=sys.stdout)
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    print(f'{a}', file=sys.stdout)
    my_sleep.apply_async(args=[a, b])
    return "OK", 200


@celery_app.task
def my_sleep(a, b):
    time.sleep(a*b*5)
