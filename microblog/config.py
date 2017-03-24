CSRF_ENABLED = True
SECRET_KEY = 'r00tme'
OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id', 'image': 'static/logos/google.gif' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com', 'image': 'static/logos/yahoo.gif' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>', 'image': 'static/logos/aol.gif' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>', 'image': 'static/logos/Flickr.gif' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com', 'image': 'static/logos/OpenID.gif' }]
