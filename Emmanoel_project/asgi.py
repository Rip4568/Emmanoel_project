import os
import sys
from pathlib import Path

from django.core.asgi import get_asgi_application

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(ROOT_DIR / "Emmanoel_project"))

# If DJANGO_SETTINGS_MODULE is unset, default to the local settings

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
#acho que não sera necessario

# Import websocket application here, so apps from django_application are loaded first
from . import routing  # noqa isort:skip

from channels.routing import ProtocolTypeRouter, URLRouter  # noqa isort:skip

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(routing.websocket_urlpatterns),
    }
)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Emmanoel_project.settings')

import django
django.setup()
#application = get_asgi_application()
