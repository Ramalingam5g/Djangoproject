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
        print(saverecord.Transaction_Type)
        
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
        print(saverecord.Balance)
        saverecord.Material_Name=request.POST.get('Material_Name')
        saverecord.Date=request.POST.get('Date')
        saverecord.Document_Number=request.POST.get('Document_Number')
        saverecord.Verification_Date=request.POST.get('Verification_Date')
        saverecord.Verified_By=request.POST.get('Verified_By')
        saverecord.save()
        # print(saverecord)
        return redirect('/display')
        
    else:
        # form = MaterialForm.objects.all(),{"mat":form}
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

