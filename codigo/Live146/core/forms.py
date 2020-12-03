from django import forms


from core.models import Todo


class FormTodo(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description"]
