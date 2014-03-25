try:
   from local_uwsgi import *
except ImportError, e:
   pass

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())