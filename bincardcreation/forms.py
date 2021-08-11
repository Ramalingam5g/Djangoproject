from django import forms  
from bincardcreation.models import *
class MaterialForm(forms.ModelForm):  
    class Meta:  
        model = Material  
        fields = "__all__"  