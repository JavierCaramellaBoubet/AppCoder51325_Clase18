from django import forms

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=50, label = "Nombre del Profesor", help_text="INGRESE EL NOMBRE DEL PROFE")
    apellido = forms.CharField(max_length=50)
    #dni =  models.IntegerField()
    email = forms.EmailField()
    profesion = forms.CharField(max_length=50)



