from django import forms

from .models import todo


class todo_forms(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['task', 'priority', 'date']