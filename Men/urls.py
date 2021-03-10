from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


from . import views
from Men.views import indexview

app_name = 'Men'

urlpatterns=[
    path('',indexview.as_view(),name="index")
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

