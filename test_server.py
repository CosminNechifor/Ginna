from flask import Flask


app = Flask(__name__)


@app.route('/test')
def endpoint():
    response = app.response_class(
        response={},
        status=200,
        mimetype='application/json'
    )
    return response


app.run()
