from django import forms
from .models import Diagnostico, Examen_Laboratorio

class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['Descripcion']
        widgets = {
            'Resultado':forms.Textarea(attrs={'rows':4}),
                   }
        
class Examen_Laboratorio_Form(forms.ModelForm):
    class Meta:
        model = Examen_Laboratorio
        fields = ['Medico', 'Tipo_Examen', 'Archivo', 'Resultado']
        widgets = {
            'Resultado':forms.Textarea(attrs={'rows':4}),
                   }

    def clean_Archivo(self):
        archivo = self.cleaned_data.get('Archivo')
        if archivo:
            if archivo.size >10*1024*1024:
                raise forms.ValidationError("EL archivo no puede superar los 10 MB")
            if not archivo.name.lower().endswith((".pdf", ".jpg", ".jpeg", ".png")):
                raise forms.ValidationError("no es un formato permitido")
        return archivo