from django.conf.urls import include, url
from django.contrib import admin


urlpatterns=patterns('',
     # ...
     ( r'^app/helloworld/$', 'app.views.hello_world' ),
)
