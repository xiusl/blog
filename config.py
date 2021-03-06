# coding=utf-8
# config.py 存储配置

# import
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# config类，最基本的类，通用配置
class Config:
    # 成员变量
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'nadjk4#h389%1ajk^sadb32ead$3w@$'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BLOG_MAIL_SUBJECT_PREFIX = '[Blog]'
    BLOG_MAIL_SENDER = 'Blog Admin <help@xiusl.com>'
    BLOG_ADMIN = os.environ.get('BLOG_ADMIN')
    MAIL_SERVER = 'smtp.exmail.qq.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'help@xiusl.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    BLOG_POSTS_PER_PAGE = 20
    BLOG_FOLLOWERS_PER_PAGE = 10
    BLOG_COMMENTS_PER_PAGE = 10

    TEMPLATES_AUTO_RELOAD = True
    BOOTSTRAP_SERVE_LOCAL = True

    print(MAIL_PASSWORD)

    @staticmethod
    def init_app(app):
        pass


# DevelopmentConfig子类，开发用的配置
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1:3306/blogdb'

# TestingConfig子类，测试用的配置
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data_test.sqlite')

# ProductConfig子类，产品的配置
class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

# 可以在这添加新的配置
# ......


# config
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductConfig,

    'default': DevelopmentConfig
}
