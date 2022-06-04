from flask import ( Flask, redirect )

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return redirect("/pets")
    from . import pet
    app.register_blueprint(pet.bp)   
    from . import fact
    app.register_blueprint(fact.bp)
     
    return app