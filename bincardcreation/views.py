from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from bincardcreation.models import Material,MaterialsInventory
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from bincardcreation.forms import MaterialForm
from .serializers import *
import uuid

from datetime import datetime
from django.http import JsonResponse
def display(request):  
    materials = Material.objects.all()
    context = {'materials':materials} 
    return render(request,"display.html", context ) 


def Create_Method(request):
    # import pdb; pdb.set_trace()
    doc_unique=Material.objects.values_list('Document_Number', flat=True)
    doc_unique=list(doc_unique)
    material_name=MaterialsInventory.objects.all()
    # results=MaterialsInventory.objects.all()
    mydict={}
    
    for data in material_name:
        mydict[data.Material_Name] = data.Quantity;
   
   
    if request.method == 'POST':
        import pdb;pdb.set_trace()
        form = MaterialForm(request.POST)
        # material_id= Material.objects.filter(id=id)[0].Material_Name_id
        # print(material_id)
        
        # selected_material_name = MaterialsInventory.objects.filter(Material_Name = request.POST.get("Material_Names"))
        
        get_selected_material_id = MaterialsInventory.objects.filter(Material_Name = request.POST.get("Material_Names")).values_list('id', flat=True).first()
        print(get_selected_material_id)
        selected_material_id = MaterialsInventory.objects.filter(id = get_selected_material_id )[0].Material_Name    
        print(selected_material_id)
     
        # get_id = MaterialsInventory.objects.values_list('id', 'Material_Name')
        # print(get_id)
 
        # selected_material_name.save()
        # selected_material_name.id
        
        
        saverecord=Material()
        saverecord.Transaction_Type=request.POST.get('Transaction_Type')
        print("Transaction_Type",saverecord.Transaction_Type)
        
        if request.POST.get('Received_From') == '':
            saverecord.Received_From = None
        else:
            saverecord.Received_From=request.POST.get('Received_From')
        if request.POST.get("Number_Of_Received") =='':
            saverecord.Number_Of_Received = None
        else:
            saverecord.Number_Of_Received=request.POST.get("Number_Of_Received")
    
        if request.POST.get('Issue_To') == '':
            saverecord.Issue_To = None
        else:
            
            saverecord.Issue_To=request.POST.get('Issue_To')

        if request.POST.get("Number_Of_Issued") =='':
            saverecord.Number_Of_Issued = None
        else:
            no_of_issued = request.POST.get("Number_Of_Issued")
            saverecord.Number_Of_Issued= int(no_of_issued)
        saverecord.Balance=request.POST.get('Balances')    
        print("Balances",saverecord.Balance)

        saverecord.Material_Name_id = get_selected_material_id
        print("Material_Names",saverecord.Material_Name_id)
        saverecord.Date=request.POST.get('Date')
        print("Date",saverecord.Date)
        saverecord.Document_Number=request.POST.get('Document_Number')
        print("Document_Number",saverecord.Document_Number)
        saverecord.Verification_Date=request.POST.get('Verification_Date')
        saverecord.Verified_By=request.POST.get('Verified_By')
        saverecord.save()
        # print(saverecord)
        return redirect('/display')
        
    else:
        # form = MaterialForm.objects.all(),{"mat":form}
        # print(material_name)

        return render(request, 'home.html',{'mat_name':material_name,'MaterialsInventory':mydict,'doc_id':doc_unique})
        


def update(request, id):
    
    import pdb;pdb.set_trace()
    material = Material.objects.get(id=id)
    form = MaterialForm(instance=material)
    material_id= Material.objects.filter(id=id)[0].Material_Name_id
    print(material_id)
    selected_material_id = MaterialsInventory.objects.filter(id = material_id )[0].Material_Name    
    
    print(selected_material_id)
    if request.method == 'POST':
        if request.POST.get('Received_From') == '':
            Received_From = None
        else:
            Received_From=request.POST.get(' request.POST.getlist("Received_From")[0]')
        if request.POST.get("Number_Of_Received") =='':
            Number_Of_Received = None
        else:
            Number_Of_Received=request.POST.get('request.POST.getlist("Number_Of_Received")[0]')
    
        if request.POST.get('Issue_To') == '':
            Issue_To = None
        else:
            
            Issue_To=request.POST.get('request.POST.getlist("Issue_To")[0]')

        if request.POST.get("Number_Of_Issued") =='':
            Number_Of_Issued = None
        else:
            no_of_issued = request.POST.get("request.POST.getlist('no_of_issued')[0]")
            Number_Of_Issued= int(no_of_issued)
        

        form = MaterialForm(request.POST, instance=material)        
        
        mat_id = MaterialsInventory.objects.filter( Material_Name = selected_material_id )[0].id
        print(mat_id)
        Material.objects.filter(Document_Number = request.POST["Document_Number"]).update(
            Transaction_Type =request.POST["Transaction_Type"],
            Received_From = Received_From,
            Number_Of_Received = Number_Of_Received ,
            Issue_To = Issue_To, 
            Number_Of_Issued = Number_Of_Issued,
            Balance =request.POST["Balance"],
            Material_Name_id = mat_id,
            Date = request.POST["Date"],
            Verification_Date = request.POST["Verification_Date"],
            Verified_By = request.POST["Verified_By"]
            ) 
        
        # if form.is_valid():
        
        return redirect('/display')
    else:

        mat =  Materialserializers(material).data
        context = {'form':form,'id':material.id,'mat':mat,'selected_material_id':selected_material_id}
        print("------",material)    
        return render(request, 'home.html', context)


def add_materail_view(request,id):
    category = MaterialsInventory.objects.filter(pk=id)
    print(category)
    # for report in category:
    #     print('ID:{} Material_Name :{}'.format(report.Material_Name_id.uuid , report.Material_Name_id.Material_Name))
    # form = MaterialForm(request.POST or None, initial={'category':category.Material_Name,})
    # if form.is_valid():
    #     instance = form.save(commit=False)
    #     instance.save()
    # return render(request,'material.html',{'form': form ,'for_debug':category})
    return render(request, 'home.html')








#  Received_From=request.POST.get(' request.POST.getlist("Received_From")[0]')

# doc_unique=Material.objects.values_list('Document_Number', flat=True)
#     doc_unique=list(doc_unique)
#     material_name=MaterialsInventory.objects.all()
#     # results=MaterialsInventory.objects.all()
#     mydict={}
#     materliallist = []
#     material_name_list = MaterialsInventory.objects.all()
#     for matname in material_name_list:
#         materliallist.append(matname.Material_Name)
#         print(materliallist)