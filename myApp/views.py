from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from myApp.models import FileHandler
from .forms import FileHandlerForm
from Users.models import CustomUser
# from django.views import generic
# from django.urls import reverse_lazy
# from django.contrib.auth import authenticate, login

def home(request):
    get_files = FileHandler.objects.prefetch_related('user').last()
    # first_file_user = get_files.first()
    # print("First", first_file_user.user)
    print("Files", get_files)
    context = {'get_files':get_files}
    return render(request, "home.html", context)

class IndexView(TemplateView): 
    template_name = "upload.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        get_files = FileHandler.objects.prefetch_related('user').all()
        print("Files", get_files)
        context = {'form':FileHandlerForm, 'get_files':get_files}
        return context

    def post(self, request, **kwargs): 
        context = {}
        if request.method == 'POST':
            form = FileHandlerForm(request.POST, request.FILES)
            
            if form.is_valid():
                FileHandler.objects.get_or_create(file_upload=form.cleaned_data.get('file_upload'))

                return redirect('myApp:upload')
            else:
                context['form'] = form
        else:
            context['form'] = form

        return redirect('myApp:home')
        
def show_files(request):
        get_files = FileHandler.objects.prefetch_related('user').last()
        first_file_user = get_files.first()
        print("First", first_file_user.user)
        print("Files", get_files)
        context = {'get_files':get_files}
        return render(request, "files.html", context)


def editor(request):
    context = {}
    return render(request, "editor.html", context)


def book(request):
    context = {}
    return render(request, "book.html", context)


def dgu(request):
    context = {}
    return render(request, "dgu.html", context)


def dissertation(request):
    context = {}
    return render(request, "dissertatsiya.html", context)


def maqola(request):
    context = {}
    return render(request, "maqola.html", context)

# def register(request):
#     # if not request.user.is_anonymous:
#     #     return redirect("/")

#     if request.method == "POST":
#         user_form = SignUpForm(request.POST)
#         if user_form.is_valid():
#             username = user_form.cleaned_data.get("username")
#             password = user_form.cleaned_data.get("password")
#             user_form.save()
#             new_user = authenticate(username=username, password=password)
#             if new_user is not None:
#                 login(request, new_user)
#                 return redirect("register")

#     user_form = SignUpForm()
    
#     context = {
#         "user_form":user_form
#     }
#     return render(request, "register.html", context)