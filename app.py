import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
from models import setup_db,Movie, Actor
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)

    @app.after_request
    def after_request(response):
        header = response.headers
        header['Access-Control-Allow-Origin'] = '*'
        header['Access-Control-Allow-Headers'] = 'Authorization, Content-Type, true'
        header['Access-Control-Allow-Methods'] = 'POST,GET,PUT,DELETE,PATCH,OPTIONS'
        return response


#----------------------------------------------------------------------------#
#  Movies.
#----------------------------------------------------------------------------#

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(token):
        data = []

        movies = Movie.query.all()

        if not movies:
            abort(404)

        for movie in movies:
            data.append({
                "title": movie.title,
                "release date": movie.release_date
            })

        return json.dumps(data)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(token, movie_id):
        try:
            movie = Movie.query.filter_by(id=movie_id).one_or_none()
        except:
            abort(500)
        if movie is None:
            abort(404)

        movie.delete()
        return jsonify({
            'success': "True",
            'deleted': movie_id
        })

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_movie(token):
        data = request.get_json()

        if not ('title' in data and 'release_date' in data):
            abort(422)

        title = data.get('title', None)
        release_date = data.get('release_date', None)
        
        movie = Movie(title=title, release_date=release_date)

        try:
            Movie.insert(movie)
        except:
            abort(500)

        return jsonify({
            'success': "true",
            'created': movie.id
        })

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patch_movie(token, movie_id):
        data = request.get_json()

        if not ('title' in data or 'release_date'):
            abort(422)

        title = data.get('title', None)
        release_date = data.get('release_date', None)

        movie = Movie.query.filter_by(id=movie_id).one_or_none()

        if movie is None:
            abort(404)

        if title is not None:
            movie.title = title

        if release_date is not None:
            movie.release_date = release_date

        movie.update()

        return jsonify({
            'success': "true",
            'updated': movie.id
        })
      
    #----------------------------------------------------------------------------#
    #  Actors.
    #----------------------------------------------------------------------------#

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(token):
        data = []
        
        actors = Actor.query.all()

        if not actors:
            abort(404)

        for actor in actors:
            data.append({
                "name": actor.name,
                "age": actor.age,
                "gender": actor.gender
            })

        return json.dumps(data)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(token, actor_id):
        try:
            actor = Actor.query.filter_by(id=actor_id).one_or_none()
        except:
            abort(500)
        if actor is None:
            abort(404)

        actor.delete()
        return jsonify({
            'success': "True",
            'deleted': actor_id
        })

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_actor(token):
        data = request.get_json()

        if not ('name' in data and 'age' in data and 'gender' in data):
            abort(422)

        name = data.get('name', None)
        age = data.get('age', None)
        gender = data.get('gender', None)
        
        actor = Actor(name=name, age=age, gender=gender)

        try:
            Actor.insert(actor)
        except:
            abort(500)

        return jsonify({
            'success': "true",
            'created': actor.id
        })
      
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def patch_actor(token, actor_id):
        data = request.get_json()

        if not ('name' in data or 'age' in data or 'gender' in data):
            abort(422)

        name = data.get('name', None)
        age = data.get('age', None)
        gender = data.get('gender', None)


        actor = Actor.query.filter_by(id=actor_id).one_or_none()

        if actor is None:
            abort(404)

        if name is not None:
            actor.name = name
                  
        if age is not None:
            actor.age = age

        if gender is not None:
            actor.gender = gender

        actor.update()

        return jsonify({
            'success': "true",
            'updated': actor.id
        })

    #----------------------------------------------------------------------------#
    # Errors.
    #----------------------------------------------------------------------------#

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'Unauthorized'
        }, 401)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False, 
            "error": 404,
            "message": "Not found"
            }), 404

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
                "success": False, 
                "error": 422,
                "message": "Unprocessable Entity"
            }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
                "success": False, 
                "error": 500,
                "message": "Internal Server Error"
            }), 500

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
