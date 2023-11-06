from django.urls import path
from . import views # .(DOT) is used to specify the destination file or class present iside the current module


urlpatterns = [
    path('', views.display),
]
