from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from bincardcreation.models import Material,MaterialsInventory
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from bincardcreation.forms import MaterialForm


from datetime import datetime
from django.http import JsonResponse
def display(request):  
    materials = Material.objects.all()
    context = {'materials':materials} 
    return render(request,"display.html", context ) 

def post_method(request):
    import pdb; pdb.set_trace()
    # form = MaterialForm()
    if request.method == 'POST':
        if request.POST.get('Transaction_Types') and request.POST.get('Material_Name') and request.POST.get('Date') and request.POST.get('Document_Number') and request.POST.get('Received_From') and request.POST.get('Number_Of_Received') and request.POST.get('Issued_From') and request.POST.get('Number_Of_Issue')  and rerequest.POST.get('Balance')  and request.POST.get('Verification_Date') and request.POST.get('Verified_By'):
            saverecord=Material()
            saverecord.Transaction_Type=request.POST.get('Transaction_Types')
            saverecord.Material_Name=request.POST.get('Material_Name')
            saverecord.Date=request.POST.get('Date')
            saverecord.Document_Number=request.POST.get('Document_Number')
            saverecord.Received_From=request.POST.get('Received_From')
            saverecord.Number_Of_Received=request.POST.get("Number_Of_Received")
            saverecord.Issue_From=request.POST.get('Issued_From')
            saverecord.Number_Of_issued=request.POST.get('Number_Of_Issue')
            saverecord.Balance=request.POST.get('Balance')    
            saverecord.Verification_Date=request.POST.get('Verification_Date')
            saverecord.Verified_By=request.POST.get('Verified_By')
            saverecord.save()
            return render(request, 'home.html')
    else:
            return render(request, 'home.html')



        
    #     form = MaterialForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/display')
    # else:
    #     material_name=MaterialsInventory.objects.all()
        # print(material_name)

    # return render(request, 'home.html', {'form':form,'material_name':material_name})



# def edit(request,id):
#     serializer=Material.objects.get(id=id)
#     return render(request,'Edit.html',{'Material':serializer})

# def update(request, id):

# 	material = Material.objects.get(id=id)
# 	form = MaterialForm(instance=material)

# 	if request.method == 'POST':
# 		form = MaterialForm(request.POST, instance=material)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/display')

# 	context = {'form':form}
# 	return render(request, 'Edit.html', context)

# def delete(request, id):
# 	order = MaterialForm.objects.get(id=id)
# 	order.delete()
# 	return redirect('/display')

	


# def post_method(request):  
#     if request.method == "POST":  
#         datas = request.POST.copy()
#         datas['date'] = datetime.strptime(request.POST['date'], '%m-%d-%Y').strftime('%Y-%m-%d')
#         datas['verification_date'] = datetime.strptime(request.POST['verification_date'], '%m-%d-%Y').strftime('%Y-%m-%d')
#         form = MaterialForm(datas)  
#         if form.is_valid():
#             form.save()  
#             return redirect('/display') 
#         else:
#             return JsonResponse(form.errors, status=401)

#             # return Response(form.errors) 
#     else:  
#         form = MaterialForm() 
#     return render(request, 'materials.html', {'form':form})

# def display(request):  
#     materials = Material.objects.all()
#     context = {'materials':materials} 
#     return render(request,"display.html", context )  

# def edit(request, id): 
#     import pdb;pdb.set_trace()
#     serializer = Material.objects.filter(id=id).update(**request.PUT)
#     context = {'Material':serializer} 
#     # return render(request,'Edit.html', context )  
#     materials = Material.objects.all()
#     context = {'materials':materials} 
#     return render(request,"display.html", context )  

# def update(request, id):  
#     serializer = Material.objects.get(id=id)  
#     datas = request.POST.copy()
#     datas['date'] = datetime.strptime(request.POST['date'], '%b. %d, %Y').strftime('%Y-%m-%d')
#     datas['verification_date'] = datetime.strptime(request.POST['verification_date'], '%b. %d, %Y').strftime('%Y-%m-%d')
#     form = MaterialForm(datas, instance = serializer)  
#     if form.is_valid():  
#         form.save()
#         return redirect('/display')
#     materials = Material.objects.all()
#     context = {'materials':materials} 
#     return render(request,"display.html", context )    

# def delete(request, id):  
#     serializer = Material.objects.get(id=id)  
#     serializer.delete()  
#     return redirect("/display")


    














    # def post(self, request, format=None):
    #     material_list = material.objects.filter(receipt_no=request.POST['receipt_no'])
    #     serializer = materialserializers(material_list, many=True)
    #     return render(request, "material.html", {"serializer":serializer.data})
    
    
    # def put(self,request, receipt_no=None):
    #     #import pdb;pdb.set_trace()
    #     data=request.data
    #     obj=material.objects.filter(receipt_no=receipt_no)
    #     print(obj)
    #     putserializer=materialserializers(obj,data=data)
    #     if putserializer.is_valid():
    #         putserializer.save()
    #         return Response(putserializer.data, status=status.HTTP_201_CREATED)
    #     return Response(putserializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self,request,receipt_no=None):
    #     obj=self.get_object(receipt_no)
    #     obj.delete()
    #     return Response(status=status.HTTP_200_OK)



# def user_data(request):
    # context = {
    # "date":"2021-07-20",
    # "doc_no":"20202",
    # "received_from":"sri ram industries",
    # "receipt_no":"102",
    # "issue":"ram industries",
    # "balance":"100",
    # "verification_date":"2020-01-11",
    # "verified_by":"ramalingam"

    # }
#     template_name="material.html"
#     return render(request, template_name, context)    

    
    # def post(self, request, format=None):
    #     serializer = materialserializers(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    # def get(self,request):
    #     material_list=material.objects.all()
    #     serializer = materialserializers(material_list,many=True)
    #     return Response(serializer.data)
    
    # def get_object(self,receipt_no):
    #     try:
    #         return material.objects.get(receipt_no=receipt_no)
    #     except material.DoesNotExist:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)

    # # def get(self,request,receipt_no):
    # #     obj=self.get_object(receipt_no)
    # #     serializer = materialserializers(obj)
    # #     return Response(serializer.data)


    # def put(self,request,receipt_no=102):
    #     obj=self.get_object(receipt_no)
    #     putserializer=material(obj)
    #     if putserializer.is_valid():
    #         putserializer.save()
    #         return Response(putserializer.data, status=status.HTTP_201_CREATED)
    #     return Response(putserializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self,request,receipt_no=102):
    #     obj=self.get_object(receipt_no)
    #     obj.delete()
    #     return Response(status=status.HTTP_200_OK)
        

    
    # def get(self,request):
    #     material_list=material.objects.all()
    #     serializer=materialserializers(material_list,many=True)
    #     return Response(serializer.data)
    
    # def get_object

# class Put_delete_method(APIView):

#     def get_object(self,receipt_no):
#         try:
#             return material.objects.get(receipt_no=receipt_no)
#         except material.DoesNotExist:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#     def get(self,request,receipt_no):
#         obj=self.get_object(receipt_no)
#         serializer = materialserializers(obj)
#         return Response(serializer.data)

#     def put(self,request,receipt_no):
#         obj=self.get_object(receipt_no)
#         putserializer=material(obj,data=request.data)
#         if putserializer.is_valid():
#             putserializer.save()
#             return Response(putserializer.data, status=status.HTTP_201_CREATED)
#         return Response(putserializer.error,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,receipt_no):
#         obj=self.get_object(receipt_no)
#         obj.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)






        
    
    
    





# Create your views here.
