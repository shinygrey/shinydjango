from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import home.views
import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", home.views.index, name="index"),
    path("", home.views.xkcd, name="one"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
