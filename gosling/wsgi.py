import os, sys

os.environ["DJANGO_SETTINGS_MODULE"] = "gosling.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gosling.settings")
sys.path.append(os.path.dirname(__file__) + "/../")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

