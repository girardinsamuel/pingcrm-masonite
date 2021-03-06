"""Providers Configuration File."""

from masonite.providers import (
    AppProvider,
    AuthenticationProvider,
    BroadcastProvider,
    CacheProvider,
    CsrfProvider,
    HelpersProvider,
    MailProvider,
    QueueProvider,
    RouteProvider,
    SessionProvider,
    StatusCodeProvider,
    UploadProvider,
    ViewProvider,
    WhitenoiseProvider,
)
from masonite.validation.providers.ValidationProvider import ValidationProvider
from masoniteorm.providers.ORMProvider import ORMProvider

from masonite.logging.providers import LoggingProvider
from masonite.validation.providers import ValidationProvider
from masonite.inertia import InertiaProvider
from masonite.js_routes import JSRoutesProvider

from app.providers.MyAppProvider import MyAppProvider

"""Providers List
Providers are a simple way to remove or add functionality for Masonite
The providers in this list are either ran on server start or when a
request is made depending on the provider. Take some time to can
learn more more about Service Providers in our documentation
"""

PROVIDERS = [
    # Framework Providers
    AppProvider,
    AuthenticationProvider,
    SessionProvider,
    RouteProvider,
    StatusCodeProvider,
    WhitenoiseProvider,
    ViewProvider,
    ORMProvider,
    # Optional Framework Providers
    MailProvider,
    UploadProvider,
    QueueProvider,
    CacheProvider,
    BroadcastProvider,
    CsrfProvider,
    HelpersProvider,
    ValidationProvider,
    # Third Party Providers
    LoggingProvider,
    ValidationProvider,
    JSRoutesProvider,
    InertiaProvider,
    # Application Providers
    MyAppProvider,
]
