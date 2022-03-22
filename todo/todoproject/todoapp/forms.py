from django import forms
from .models import Todo

class Todo_forms(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['reminder','priority','date']