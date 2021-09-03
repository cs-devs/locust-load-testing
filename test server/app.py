from flask import Flask, request, jsonify
from flask_restful import Resource, Api, request

app = Flask(__name__)
api = Api(app)

class Login(Resource):
    def post(self):
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "admin":
            return jsonify({"token" : "asdsad1213"})
        if username == "admin2" and password == "admin2":
                return jsonify({"token" : "admin2"})
       

class DumpLogin(Resource):
    def get(self):
         print(request.headers)
         return {"message" : "ok" }

class DoNothing(Resource):
    def get(self):
        #print(request.headers)
        return {"message" : "ok"}

class uploadText(Resource):
    def put(self):
        print(request.headers)
        return {"message" : "ok" }


api.add_resource(Login, '/login')
api.add_resource(DumpLogin, '/dump')
api.add_resource(DoNothing, "/do_nothing")

if __name__ == '__main__':
    app.run(debug=True)
