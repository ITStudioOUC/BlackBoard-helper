"""BlackBoard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from utils.router_builder import RouterBuilder

from BlackBoard.settings import NOTICE_HOMEWORK_DEADLINE

if NOTICE_HOMEWORK_DEADLINE:
    from utils import scheduler

router = RouterBuilder(trailing_slash=False)
router_slashed = RouterBuilder(trailing_slash=True)
urlpatterns = [
    path("", include(router.urls)),
    path("", include(router.url_patterns)),
    path("", include(router_slashed.urls)),
    path("", include(router_slashed.url_patterns)),
]