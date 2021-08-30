from django import forms  
from bincardcreation.models import *



class MaterialForm(forms.ModelForm):
    # import pdb;pdb.set_trace()
    Material_Name= MaterialsInventory.objects.all()

    def __init__(self, *args, **kwargs):
        super(MaterialForm, self).__init__(*args, **kwargs)
        if self.initial:
            self.fields['Material_Name'].queryset = MaterialsInventory.objects.all()
            self.fields['Material_Name'].initial = self.initial['Material_Name']



    class Meta:  
        model = Material  
        fields = "__all__"  
