from flask import ( Blueprint, render_template )
import json

pets = json.load(open('pets.json'))

bp = Blueprint('pet',__name__, url_prefix="/pets")

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)

@bp.route('/<int:pet_id>')
def show(pet_id):
    return render_template('show_pet.html', pet=pets[pet_id - 1])

@bp.route('/facts')
def facts():
    return render_template('facts.html')