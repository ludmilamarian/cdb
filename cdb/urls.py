"""cdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    url(r'cdbmeta/', include('cdbmeta.urls'), name="search"),

    url(r'accounts/', include('django.contrib.auth.urls')),

    url(r'cdbdata/', include('cdbdata.urls')),
    url(r'^contact/$',
        TemplateView.as_view(template_name='cdbmeta/contact.html'),
        name="contact"),
    url(r'^$', TemplateView.as_view(template_name='cdbmeta/index.html'),
        name="home"),
]


from django.conf import settings
from django.conf.urls import include
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

