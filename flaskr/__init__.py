import os
 
from flask import Flask
#from flask_login import login_manager

from flask import ( Blueprint, flash, g, redirect, render_template, request, session, url_for)

import sqlite3


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

 #   login_manager = LoginManager()
  #  login_manager.init_app(app)
    @app.route('/')
    def home():
        return render_template('home.html')
    
    @app.route('/rankresume')
    def rankresume():
        return render_template('rankresume.html')
  
    #here reads resume and goes to result.html
    @app.route('/results')
    def res():
            return render_template('result.html')    
    
    #result is searched and result.html is returned
    @app.route('/resultsearch' ,methods = ['POST', 'GET'])
    def resultsearch():
        if request.method == 'POST':
            search_st = request.form.get('Name')
            print(search_st)
            result = search.res(search_st)
            return render_template('result.html', results = result)
        
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app