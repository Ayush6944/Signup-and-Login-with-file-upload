from django import forms
from .models import EBooksModel
#  we are using form to get a file input from user here
# we are creating class of form
class UploadBookForm(forms.ModelForm):
    class Meta:
        model = EBooksModel
        fields = ('title', 'pdf',)


        # writen by ayush