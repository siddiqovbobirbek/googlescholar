from django.urls import path
from myApp.views import IndexView
from .views import home

app_name = "myApp"

urlpatterns = [
    path("", home, name="home"),
    path("upload/", IndexView.as_view(), name="upload"),
    # path('register/', SignUpView.as_view(), name="register"),
    # path("register/", register, name="register"),
    
]