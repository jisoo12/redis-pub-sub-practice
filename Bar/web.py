from flask import Flask, request
from bar import Bar


app = Flask(__name__)

@app.route('/bar')
def bar():
    return Bar.bar_action("bar_reqeust", test="True")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)