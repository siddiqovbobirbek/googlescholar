from django.urls import path
from myApp.views import IndexView
from .views import home, show_files, editor

app_name = "myApp"

urlpatterns = [
    path("", home, name="home"),
    path("upload/", IndexView.as_view(), name="upload"),
    path("files/", show_files, name="show_files"),
    path("editor/", editor, name="editor"),
    # path('register/', SignUpView.as_view(), name="register"),
    # path("register/", register, name="register"),
    
]