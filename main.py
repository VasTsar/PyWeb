from flask import Flask, render_template, redirect, url_for, request, session
from data import db_session
from forms.register_login import RegisterForm, LoginForm
from data.objects import Objects
from data.users import User
from flask_login import LoginManager, login_user, login_required, logout_user
from data.get_info import get_info
from map_builder import load_map_image

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
number_of_images = 0

login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init("db/architecture.db")
    app.run()


@login_manager.user_loader
def load_user(user_id):
    """ Загрузка ползователя """
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Функция, отвечающая за логин"""
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/", methods=['GET', 'POST'])
def index():
    """ Основная функция, отвечающая за происходящее на главной станице"""
    db_sess = db_session.create_session()
    objects = db_sess.query(Objects)
    if request.method == 'GET':
        session['info'] = get_info()
    kwargs = {'id1': session['info'].get('id1'),
              'id2': session['info'].get('id2'),
              'img1': url_for('static', filename=f"img/{session['info'].get('img1')}"),
              'img2': url_for('static', filename=f"img/{session['info'].get('img2')}"),
              'inf1': session['info'].get('inf1'),
              'inf2': session['info'].get('inf2'),
              'choose_image': False,
              'similar': []
              }
    if request.method == 'GET':
        return render_template("index.html", objects=objects, **kwargs)
    elif request.method == 'POST':
        if request.form:
            kwargs['choose_image'] = True
            chosen_object = db_sess.query(Objects).get(request.form['group1'])
            similar_objects = chosen_object.similar.split(', ')
            address = chosen_object.address
            kwargs['similar'] = similar_objects
            session['address'] = address
            return render_template("index.html", objects=objects, **kwargs)
        else:
            return redirect(url_for(f'map/{request.form["group1"]}'))


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    """ Регистрация """
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/show_map', methods=['GET', 'POST'])
def show_map():
    """ Показывает объект на карте"""
    global number_of_images
    if request.method == 'GET':
        if 'address' in session:
            style = 'map'
            load_map_image(session['address'], f'map_{number_of_images}.png', style)
            session['image_name'] = f'map_{number_of_images}.png'
            number_of_images += 1
    elif request.method == 'POST':
        if request.form:
            chosen_style = request.form['group2']
            load_map_image(session['address'], f'map_{number_of_images}.png', chosen_style)
            session['image_name'] = f'map_{number_of_images}.png'
            number_of_images += 1

    return render_template('show_map.html', image_name=url_for('static',
                                                               filename=f"img/{session.get('image_name')}"))


@app.route('/load', methods=['GET', 'POST'])
def load():
    """ Позволяет пользователю загрузить свой объект"""
    if request.method == 'GET':
        return render_template("load_object.html")
    elif request.method == 'POST':
        req = request.files.get('file', None)
        if req:
            with open(f'static/img/tmp.png', 'wb') as file:
                file.write(req.read())
            filename = 'tmp.png'
        return render_template("load_object.html")


if __name__ == '__main__':
    main()
