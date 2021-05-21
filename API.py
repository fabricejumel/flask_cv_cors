import threading

from flask import Flask, jsonify
from flask_cors import CORS

# create a variable to store the data
data = None
# create the Flask application
app = Flask(__name__)
# make cross-origin AJAX possible
CORS(app)

# create a method to send the data to the API when requested
@app.route("/")
def send_data():
    # convert into JSON format first
    return jsonify(data)

def start(host, port):
    # get the host and the port as keywords attributes for app.run()
    app_kwargs = {'host':host, 'port':port}
    # run the app on a thread
    threading.Thread(target=app.run, kwargs=app_kwargs).start()
