
from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import AddMovie
from .import db
from flask_login import login_required,current_user

views = Blueprint('views', __name__)
is_admin=False

@views.route('/')
@login_required
def home():
    all_data = AddMovie.query.all()
    return render_template("home.html",user =current_user,movies = all_data)

@views.route('unsign',methods=['GET','POST'])
def unsign():
    global is_admin
    is_admin=True
    return redirect(url_for('views.sign'))
@views.route('/sign',methods=['GET','POST'])
def sign():
    global is_admin
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if password=='pass' and username=='root':
            flash('Logged in successfully!', category='success')
            print(3)
            is_admin=True
            return redirect(url_for('views.admin'))
        else:
            flash('Incorrect password, try again.', category='error')

    return (render_template("sign.html"))

@views.route('/admin',methods = ['GET','POST'])
def admin():
    all_data = AddMovie.query.all()
    if request.method == 'GET':
        #print(0)
        if is_admin:
            #print(1)
            return render_template("admin.html",movies = all_data,is_admin=is_admin)
        else:
            #print(2)
            return (redirect(url_for('views.sign')))
    if request.method == 'POST':
        movies_name = request.form.get('movies_name')
        movies_director = request.form.get('movies_director')
        genre = request.form.get('genre')
        
        movie_data = AddMovie(movies_name = movies_name , movies_director = movies_director , genre = genre)
        db.session.add(movie_data)
        db.session.commit()
        flash("Movie added Successfully!")

        return redirect(url_for('views.admin'))

    return render_template("admin.html",movies = all_data,user=current_user)


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





    



