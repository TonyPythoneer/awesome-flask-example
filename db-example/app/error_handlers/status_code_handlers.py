from flask import jsonify

from .. import app


__all__ = [
    "handle_noresultfound_exception",
    "handle_bad_request_by_webargs"
]


@app.errorhandler(404)
def handle_noresultfound_exception(err):
    """Execute query but it doesn't find the data

    return example:
        {
            "message": "Not Found"
        }
    """
    return jsonify({"message": "Not Found"}), 404


@app.errorhandler(422)
def handle_bad_request_by_webargs(err):
    msgs = {k: v.pop() for k, v in err.data['messages'].items()}
    return jsonify({
        'message': "Invalid request could not be understood "
                   "by the server due to malformed syntax.",
        'errors': msgs,
    }), 400
    return jsonify(res_data), 400
