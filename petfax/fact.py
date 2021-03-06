from flask import ( Blueprint, render_template, request, redirect ) 

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new')
def facts():
    return render_template('facts/facts.html')

@bp.route('/', methods=['GET','POST'])
def index():
    if request.method == "POSST":
        print(request.form)
        return redirect('/facts')

    return render_template('facts/index.html')