import os

CSRF_ENABLED = True
SECRET_KEY = 'r00tme'
OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id', 'image': 'static/logos/google.gif' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com', 'image': 'static/logos/yahoo.gif' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>', 'image': 'static/logos/aol.gif' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>', 'image': 'static/logos/Flickr.gif' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com', 'image': 'static/logos/OpenID.gif' }]
#base dir for database, uri and dir for future-migrations
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
#If set to True, Flask-SQLAlchemy will track modifications of objects and emit signals.
# The default is None, which enables tracking but issues a warning that it will be disabled by default in the future.
# This requires extra memory and should be disabled if not needed.
SQLALCHEMY_TRACK_MODIFICATIONS = True
################################
