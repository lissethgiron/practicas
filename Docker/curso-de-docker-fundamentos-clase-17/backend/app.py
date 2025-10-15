from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Lis",
        "lastname": "Gir",
        "socialMedia":
        {
            "facebookUser": "lisgir",
            "instagramUser": "Sereia",
            "xUser": "Sereia",
            "linkedin": "lis-gir",
            "githubUser": "Sereia"
        },
        "blog": "https://Sereia.com",
        "author": "Sereia G"
    }

    return jsonify(value)

if __name__ == '__main__':
    app.run(port=5000)