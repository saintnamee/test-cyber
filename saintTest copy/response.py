from flask import jsonify


def handle_response(code, message, result=""):
    return jsonify({
        "code": code,
        "message": message,
        "result": result
    }), code