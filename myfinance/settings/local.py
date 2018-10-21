DEBUG = True

ALLOWED_HOSTS = ['192.168.33.10']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
        	'read_default_file': '/etc/mysql/my.cnf'
        },
    }
}