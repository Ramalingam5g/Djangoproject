from django.db import models
import uuid

class MaterialsInventory(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    Material_Code = models.CharField(max_length=255,blank=False,null=False,unique=True)
    Material_Name= models.CharField(max_length=255)
    Material_Location=models.CharField(max_length=255,blank=True,null=True)
    Unit_of_Measurement=models.CharField(max_length=255,null=True, blank=True)  
    Maximum_Level=models.IntegerField(null=True, blank=True)
    Minimum_Level=models.IntegerField(null=True, blank=True)
    Re_order_Level=models.IntegerField(null=True, blank=True)
    Quantity=models.IntegerField(null=True,blank=True)

    class Meta:
        db_table="bincardcreation_materialsinventory"
    
    # def __str__(self):
    #     return self.Material_Name


Trans_type=(
    ('RF','Recieved from'),
    ("IT","Issued to"),
)

class Material(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Transaction_Type=models.CharField(max_length=20,choices=Trans_type,default='RF')
    Received_From=models.CharField(max_length=200,null=True,blank=True)
    Number_Of_Received=models.IntegerField(null=True)
    Issue_To=models.CharField(max_length=200,null=True,blank=True)
    Number_Of_issued=models.IntegerField(null=True)
    Balance=models.IntegerField()
    Material_Name=models.ForeignKey(MaterialsInventory,on_delete = models.CASCADE)
    Date=models.DateField()
    Document_Number=models.IntegerField(unique=True)
    Verification_Date=models.DateField()
    Verified_By=models.CharField(max_length=100)

    def __str__(self):
        return self.Material_Name
    

    

# Create your models here.
