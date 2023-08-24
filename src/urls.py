from django.urls import path, include
from .views import home,sucess

urlpatterns = [
    path('', home, name="home"),
    path('sucess/',sucess, name= "sucess")
]
