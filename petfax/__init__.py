from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return '<style> h1 { text-align: center} h1:hover { color: skyblue} div {height:100vh} </style> <h1>Hello, this is PetFax</h1>'     

        # pets index route
    @app.route('/pets')
    def pets():
        return 'These are our pets available for adoption'
    return app