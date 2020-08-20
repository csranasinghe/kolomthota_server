from .base import get_config

if get_config('SERVER_TYPE') == 'local':
    from .local import *
elif get_config('SERVER_TYPE') == 'production':
    from .production import *
else:
    from .base import *