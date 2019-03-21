#__author__ == "Chance Murphy (cmurphy)"

import os
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this

# Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./sample_movies.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy

collections = db.Table('collections',db.Column('movie_id', db.Integer, db.ForeignKey('movies.id')), db.Column('director_id',db.Integer,db.ForeignKey('directors.id')))

class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    # director = db.relationship('Director',secondary = collections,backref=db.backref('movie',lazy='dynamic'),lazy='dynamic')
    director = db.Column(db.Integer, db.ForeignKey("directors.name"))

    def __repr__(self):
        return "{} (ID: {})".format(self.name,self.id)

class Director(db.Model):
    __tablename__ = "directors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    movies = db.relationship('Movie',secondary = collections,backref=db.backref('director1',lazy='dynamic'),lazy='dynamic')


# class Song(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(64),unique=True) # Only unique title songs can exist in this data model
#     album_id = db.Column(db.Integer, db.ForeignKey("albums.id")) #ok to be null for now
#     artist_id = db.Column(db.Integer, db.ForeignKey("artists.id")) # ok to be null for now
#     genre = db.Column(db.String(64)) # ok to be null
#     # keeping genre as atomic element here even though in a more complex database it could be its own table and be referenced here
#
#     def __repr__(self):
#         return "{} by {} | {}".format(self.title,self.artist_id, self.genre)


##### Helper functions #####

### For database additions
### Relying on global session variable above existing

def get_or_create_director(d_name):
    director = Director.query.filter_by(name=d_name).first()
    if director:
        return director
    else:
        director = Director(name=d_name)
        session.add(director)
        session.commit()
        return director


##### Set up Controllers (route functions) #####

## Main route
@app.route('/')
def index():
    movies = Movie.query.all()
    num_movies = len(movies)
    return "There are " + str(num_movies) + " movies in the database"

@app.route('/movie/new/<name>/<director>/')
def new_movie(name, director):
    if Movie.query.filter_by(name=name).first(): # if there is a movie by that title
        return "That movie already exists! Go back to the main app!"
    else:
        new_director = get_or_create_director(director)
        movie = Movie(name=name, director=new_director.name)
        session.add(movie)
        session.commit()
        return "New movie: {} by {}. Check out the URL for ALL movies to see the whole list.".format(movie.name, new_director.name)

@app.route('/all_movies')
def see_all():
    all_movies = "" # Will be be tuple list of title, genre
    movies = Movie.query.all()
    for m in movies:
        director = Director.query.filter_by(name=m.director).first() # get just one artist instance
        all_movies = all_movies + m.name + " directed by " + director.name + "<br>"#.append((m.name,director.name)) # get list of songs with info to easily access [not the only way to do this]
    return str(all_movies) #render_template('all_songs.html',all_movies=all_movies) # check out template to see what it's doing with what we're sending!

@app.route('/all_directors')
def see_all_directors():
    all_directors = ""
    directors = Director.query.all()
    for d in directors:
        #num_movies = len(Director.query.filter_by(director_id=d.id).all())
        all_directors = all_directors + d.name + " has movies in the database." + "<br>"
        #newtup = (d.name,num_movies)
        #all_directors.append(d.name) # names will be a list of tuples
    return all_directors #render_template('all_artists.html',director_names=all_directors)


if __name__ == '__main__':
    db.create_all() # This will create database in current directory, as set up, if it doesn't exist, but won't overwrite if you restart - so no worries about that
    app.run() # run with this: python main_app.py runserver
