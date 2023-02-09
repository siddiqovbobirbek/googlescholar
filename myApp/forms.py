from django import forms
from myApp.models import FileHandler

class FileHandlerForm(forms.ModelForm):

    file_upload = forms.FileField

    class Meta():
        model = FileHandler
        fields = ('file_upload',)

# class SignUpForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["username"].widget.attrs.update({
#             'required':'',
#             'name':'username',
#             'id':'username',
#             'type':'text',
#             'class':'form-control form-control-lg',
#             'placeholder':'username',
#         })
#         self.fields["email"].widget.attrs.update({
#             'required':'',
#             'name':'email',
#             'id':'id="emailAddress',
#             'type':'text',
#             'class':'form-control form-control-lg',
#             'placeholder':'email',
#         })
#         self.fields["password1"].widget.attrs.update({
#             'required':'',
#             'name':'password1',
#             'id':'password1',
#             'type':'password',
#             'class':'form-control form-control-lg',
#             'placeholder':'password',
#             'minleght':'8'
#         })
#         self.fields["password2"].widget.attrs.update({
#             'required':'',
#             'name':'password2',
#             'id':'password2',
#             'type':'password',
#             'class':'form-control form-control-lg',
#             'placeholder':'password',
#             'minleght':'8'
#         })

#     class Meta:
#         model = User
#         fields = [
#             'username', 
#             'email', 
#             'password1', 
#             'password2',
#         ]
