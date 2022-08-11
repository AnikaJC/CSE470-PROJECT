from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class AddMovie(db.Model):
    __tablename__ = "addmovie"
    id = db.Column(db.Integer,primary_key=True)
    movies_name = db.Column(db.String(150))
    movies_director = db.Column(db.String(150))
    genre = db.Column(db.String(150))
    showtime = db.relationship("ShowTime", back_populates="addmovie", uselist=False)
    

class ShowTime(db.Model):
    __tablename__ = "showtime"
    id = db.Column(db.Integer,primary_key=True)
    show_time = db.Column(db.DateTime(timezone=True), default=func.now())
    addmovie = db.relationship("AddMovie", back_populates="showtime")
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))

class Ticket(db.Model):
    __tablename__ = "ticket"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(150))
    phone_no = db.Column(db.Integer)
    no_of_seats = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
      
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    #movies = db.relationship('AdminManage')

    
    