import logging
import os

import coloredlogs
import sentry_sdk
from aidbox_python_sdk.main import init as init_aidbox_app
from aidbox_python_sdk.main import setup_routes as setup_aidbox_app_routes
from aiohttp import web
from fhirpy.lib import AsyncFHIRClient
from sentry_sdk.integrations.aiohttp import AioHttpIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

from app.aidbox import sdk
from app.fhir_server import routes as fhir_routes, default_handler
from app.settings import fhir_app_settings

coloredlogs.install(level="DEBUG", fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)
logging.getLogger("aidbox_sdk").setLevel(logging.INFO)
logging.getLogger("urllib3").setLevel(logging.INFO)
logging.getLogger("faker").setLevel(logging.WARNING)

sentry_logging = LoggingIntegration(
    level=logging.DEBUG,  # Capture info and above as breadcrumbs
    event_level=logging.WARNING,  # Send warnings as events
)
sentry_sdk.init(integrations=[AioHttpIntegration(), sentry_logging])


async def create_gunicorn_app():
    if os.getenv("USE_AIDBOX", "True").lower() == "true":
        return create_aidbox_app()
    else:
        return create_fhir_app()


def create_aidbox_app():
    app = web.Application()
    app.cleanup_ctx.append(init_aidbox_app)
    app.update(
        settings=sdk.settings,
        sdk=sdk,
    )
    setup_aidbox_app_routes(app)
    return app


async def fhir_app_on_startup(app: web.Application):
    app["settings"] = fhir_app_settings
    app["client"] = AsyncFHIRClient(fhir_app_settings.BASE_URL)


def create_fhir_app():
    app = web.Application()
    app.add_routes(fhir_routes)
    app.add_routes([web.route("*", r'/{name:.*}', default_handler)])
    app.on_startup.append(fhir_app_on_startup)

    return app
