from flask import Flask, request, jsonify, make_response, render_template, redirect
from flask_cors import CORS, cross_origin
from io import BytesIO
import base64
from PIL import Image, ImageDraw, ImageFont
import requests
import shutil
import textwrap
import os

app = Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


#yha pe jo apna krna hai wo is function mai daal ke image return kr dena
def imagemaker(argument1, argument2):

    # # return imagedata




@app.route('/', methods=['OPTIONS', 'GET'])
def create_task():
    if request.method == "OPTIONS":
        return _build_cors_prelight_response()
    elif request.method == "GET":
        args = request.args
        print(args)  # For debugging
        argument2 = args.get('imagetype')
        argument1 = args.get('title')
        
        if argument2 ==None and argument1==None:
            return "her you can show any error"
        else:
            # ye pe function run krega
            g = imagemaker(argument1, argument2)
            argument1 = argument1.upper()
            file_name = f"images/{argument1}.png"
            return render_template("index.html", user_image=file_name, alt_name=argument1)
    else:
        abort(400)


def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


app.run()
