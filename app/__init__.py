# coding=utf-8
# __init__.py 程序的工厂函数


# all import
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config


# 变量


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

# login
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


# 工厂函数
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    login_manager.init_app(app)

    # 附加路由和自定义的错误界面
    # 使用蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # 附加auth蓝本
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    return app
