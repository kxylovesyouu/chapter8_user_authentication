from app import app, db
from app.models import User 
from flask_login import login_user, logout_user, login_required
from flask import render_template, flash, redirect, url_for
from flask import render_template
from app.forms import RegisterForm, AddProductForm, LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login URL"""
    form = LoginForm() 
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid User Name Or Password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash(f'Welcome {form.username.data} ')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register URL"""
    form= RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'You Have Been Successfuly Registered! ')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/')
@app.route('/home')
@login_required
def index():
    """Index URL"""
    return render_template('shop.html', title='Shop Page')

@app.route('/about-me')
@login_required
def about_me():
    """About Me URL"""
    return render_template('about_me.html', title='About Me')

    
@app.route('/add_product', methods=['GET','POST'])
def add_product():
    
    
    """Add Product URL"""
    form = AddProductForm()
    if form.validate_on_submit():
        flash(f'Product added ')
        return redirect(url_for('index'))
    return render_template('add_product.html', title='Add Product Page', form=form)


# 