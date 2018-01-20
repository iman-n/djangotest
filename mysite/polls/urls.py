from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index")
]
# just want to add some comment
