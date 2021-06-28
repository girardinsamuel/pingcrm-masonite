from masonite.foundation import HttpKernel

from .middleware.HandleInertiaRequests import HandleInertiaRequests


class AppHttpKernel(HttpKernel):
    http_middleware = [HandleInertiaRequests]
