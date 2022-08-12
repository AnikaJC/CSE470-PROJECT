from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import AddMovie
from .import db
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/admin',methods = ['GET','POST'])
def admin():
    all_data = AddMovie.query.all()
    if request.method == 'POST':
        movies_name = request.form.get('movies_name')
        movies_director = request.form.get('movies_director')
        genre = request.form.get('genre')
        
        movie_data = AddMovie(movies_name = movies_name , movies_director = movies_director , genre = genre)
        db.session.add(movie_data)
        db.session.commit()
        flash("Movie added Successfully!")

        return redirect(url_for('views.admin'))
    return render_template("admin.html",movies = all_data)

@views.route('/update',methods =['POST'])
def update():
    
    if request.method == 'POST':
        movie_data = AddMovie.query.get(request.form.get('id'))
        movie_data.movies_name = request.form.get('movies_name')
        movie_data.movies_director = request.form.get('movies_director')
        movie_data.genre = request.form.get('genre')

        db.session.commit()
        flash("Movie Successfully Updated!")
        return redirect(url_for('views.admin'))
    return render_template("admin.html")

@views.route('/delete/<id>',methods = ['GET','POST'])
def delete(id):
    movie_data = AddMovie.query.get(id)
    db.session.delete(movie_data)
    db.session.commit()
    flash("Movie Successfully Deleted!")
    return redirect(url_for('views.admin'))





    



