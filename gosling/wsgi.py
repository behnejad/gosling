import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"] = "gosling.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gosling.settings")
sys.path.append(os.path.dirname(__file__) + "/../")
application = get_wsgi_application()

