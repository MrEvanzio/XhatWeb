from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="titulo tarea", max_length=200)
    description = forms.CharField(label="descripcion tarea",widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Name Project", max_length=200)