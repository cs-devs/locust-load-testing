from flask import Flask
from flask_restful import Resource, Api, request

app = Flask(__name__)
api = Api(app)

class Login(Resource):
    def post(self):
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "admin":
            return {"message" : "ok"}, 200
        else: 
            return {"message" : "error"}, 400

class DumpLogin(Resource):
    def get(self):
         username = "admin" 
         password = "admin"
         return {"message" : username }

class DoNothing(Resource):
    def get(self):
        #print(request.headers)
        return {"message" : "ok"}

api.add_resource(Login, '/login')
api.add_resource(DumpLogin, '/dump')
api.add_resource(DoNothing, "/do_nothing")

if __name__ == '__main__':
    app.run(debug=True)
