# Config
from flask import Flask

app = Flask(__name__)
app.run(debug=True)

# Terminal export FLASK_DEBUG=1


#index route
@app.route('/')
def index():
    return '<style> h1 { text-align: center} h1:hover { color: red} div {height:100vh} </style> <h1>Hello, this is PetFax</h1>'

# pets index route
@app.route('/pets')
def pets():
    return 'These are our pets available for adoption'