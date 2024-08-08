from django import forms
from todoList.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task', 'done']
        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'done': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
