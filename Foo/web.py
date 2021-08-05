from flask import Flask, request
from foo import Foo


app = Flask(__name__)

@app.route('/foo')
def foo():
    return Foo.foo_action("foo_request", test="True")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6001, debug=True)