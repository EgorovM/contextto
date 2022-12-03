from rest_framework.routers import SimpleRouter, Route, DynamicRoute


class SessionRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'post': 'create'},
            name='{basename}',
            detail=False,
            initkwargs={}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'delete': 'destroy'},
            name='{basename}-detail',
            detail=True,
            initkwargs={}
        ),
    ]