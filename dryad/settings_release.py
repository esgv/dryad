from dryad.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DATABASES['default'] = DATABASES['remote']