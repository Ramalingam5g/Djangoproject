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
   
    # import pdb;pdb.set_trace()
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        
        
        
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
        saverecord.Material_Name_id=request.POST.get("MaterialsInventory_id")
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
    
	# import pdb;pdb.set_trace()
	material = Material.objects.get(id=id)
	form = MaterialForm(instance=material)

	if request.method == 'POST':
		form = MaterialForm(request.POST, instance=material)
		if form.is_valid():
			form.save()
			return redirect('/display')
	mat =  Materialserializers(material).data
	context = {'form':form,'id':material.id,'mat':mat}
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