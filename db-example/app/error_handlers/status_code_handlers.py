from flask import jsonify

from .. import app


@app.app_errorhandler(400)
def handle_bad_request_by_reqparse(err):
    res_data = {
        'message': 'Bad Request',
        'errors': err.data['message']
    }
    return jsonify(res_data), 400
