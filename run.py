from flask import Flask, jsonify, request, render_template,send_file,send_from_directory
from app.controllers import faid_registration_controller, faid_recommendation_controller
import json
import sys
from app.json_encoder import myJSONEncoder

_app = Flask(__name__)
_app.json_encoder = myJSONEncoder

@_app.route('/')
def index():
    return render_template("index.html")

@_app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@_app.route('/faid_registration', methods=['POST'])
def registration():
    """" This will take up the data from registration page to DB

    :return if success, db insertion is successful else fail
    """
    try:
        _data=request.json
        print("JSON DATA -->")
        print(_data)
        _status = faid_registration_controller.insert_to_db(_data)
        return jsonify({
            "success": _status
            })
    except Exception as e:
        return jsonify({"success": False, "status":500 ,"err":e.args,})


@_app.route('/faid_recommendation', methods=['POST'])
def recommendation():
    """ This will return recommendations based on user input

    :return: recommendations
    """
    try:
        _data=request.json
        print("JSON DATA")
        print(_data)
        _df = faid_recommendation_controller.predict(_data)
        return _df.to_json()
    except Exception as e:
        return jsonify({"success": False, "status":500 ,"err":e.args,})

if __name__ == '__main__':
    _app.run(host="0.0.0.0", port=8089)
