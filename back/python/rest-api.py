from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_restful import Resource

app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route('/', methods=["GET"])
def index():
    return "Welcome to API."


class Test(Resource):
    @staticmethod
    def get():
        return {"msg": "sucess"}
    

api.add_resource(Test, '/test')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888)
