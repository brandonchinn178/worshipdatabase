"""
WSGI config for worshipdatabase project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import os
import sys


if os.environ.has_key('OPENSHIFT_REPO_DIR'):
     sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'site'))
     os.environ['DJANGO_SETTINGS_MODULE'] = 'site_settings.settings'
     virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
     os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.7/site-packages')
     virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
     try:
         execfile(virtualenv, dict(__file__=virtualenv))
     except IOError:
         pass

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
