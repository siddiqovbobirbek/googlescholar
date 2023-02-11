from django.urls import path
from myApp.views import IndexView
from .views import home, show_files, editor, book, dissertation, maqola, dgu

app_name = "myApp"

urlpatterns = [
    path("", home, name="home"),
    path("upload/", IndexView.as_view(), name="upload"),
    path("files/", show_files, name="show_files"),
    path("editor/", editor, name="editor"),
    path("dgu/", dgu, name="dgu"),
    path("maqola/", maqola, name="maqola"),
    path("book/", book, name="book"),
    path("dissertation/", dissertation, name="dissertation"),
    # path('register/', SignUpView.as_view(), name="register"),
    # path("register/", register, name="register"),
    
]