from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, User, House, Payment

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email    = request.form['email']
        password = request.form['password']
        role     = request.form['role']  # 'admin', 'vecino', 'guardia'
        
        new_user = User(username = username, email = email, password = password, role = role)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.index'))
    
    return render_template('register.html')
