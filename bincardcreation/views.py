""" this is a minshare application"""
from django.shortcuts import render, redirect
from bincardcreation.models import Material, MaterialsInventory
from bincardcreation.forms import MaterialForm
from .serializers import Materialserializers



def display(request):
    """ this function used for display the material list """
    materials = Material.objects.all()
    context = {"materials": materials}
    return render(request, "display.html", context)


def create_method(request):
    """ this function used for create a new data """
    doc_unique = Material.objects.values_list("Document_Number", flat=True)
    doc_unique = list(doc_unique)
    material_name = MaterialsInventory.objects.all()
    mydict = {}

    for data in material_name:
        mydict[data.Material_Name] = data.Quantity

    if request.method == "POST":
        get_selected_material_id = (
            MaterialsInventory.objects.filter(
                Material_Name=request.POST.get("Material_Names")
            )
            .values_list("id", flat=True)
            .first()
        )

        saverecord = Material()
        saverecord.Transaction_Type = request.POST.get("Transaction_Type")

        if request.POST.get("Received_From") == "":
            saverecord.Received_From = None
        else:
            saverecord.Received_From = request.POST.get("Received_From")
        if request.POST.get("Number_Of_Received") == "":
            saverecord.Number_Of_Received = None
        else:
            saverecord.Number_Of_Received = request.POST.get("Number_Of_Received")
        if request.POST.get("Issue_To") == "":
            saverecord.Issue_To = None
        else:
            saverecord.Issue_To = request.POST.get("Issue_To")

        if request.POST.get("Number_Of_Issued") == "":
            saverecord.Number_Of_Issued = None
        else:
            no_of_issued = request.POST.get("Number_Of_Issued")
            saverecord.Number_Of_Issued = int(no_of_issued)
        saverecord.Balance = request.POST.get("Balances")
        print("Balances", saverecord.Balance)

        saverecord.Material_Name_id = get_selected_material_id
        print("Material_Names", saverecord.Material_Name_id)
        saverecord.Date = request.POST.get("Date")
        print("Date", saverecord.Date)
        saverecord.Document_Number = request.POST.get("Document_Number")
        print("Document_Number", saverecord.Document_Number)
        saverecord.Verification_Date = request.POST.get("Verification_Date")
        saverecord.Verified_By = request.POST.get("Verified_By")
        saverecord.save()
        return redirect("/display")

    return render(
        request,
        "home.html",
        {
            "mat_name": material_name,
            "MaterialsInventory": mydict,
            "doc_id": doc_unique,
        },
    )


def update_method(request, id):# pylint: disable=C0103
    """ this function used for update the data """
    material = Material.objects.get(id=id)
    form = MaterialForm(instance=material)
    material_id = Material.objects.filter(id=id)[0].Material_Name_id
    selected_material_id = MaterialsInventory.objects.filter(id=material_id)[
        0
    ].Material_Name
    if request.method == "POST":
        if request.POST["Transaction_Type"] == "Received From":
            received_from = request.POST.getlist("Received_From")[0]
            number_of_received = request.POST.getlist("Number_Of_Received")[0]
            issue_to = None
            number_of_issued = None

        else:
            issue_to = request.POST.getlist("Issue_To")[0]
            number_of_issued = request.POST.getlist("Number_Of_Issued")[0]
            received_from = None
            number_of_received = None

        form = MaterialForm(request.POST, instance=material)

        material_id = MaterialsInventory.objects.filter(
            Material_Name=selected_material_id
        )[0].id

        Material.objects.filter(Document_Number = request.POST["Document_Number"]).update(
            Transaction_Type = request.POST["Transaction_Type"],
            Received_From = received_from,
            Number_Of_Received = number_of_received,
            Issue_To = issue_to,
            Number_Of_Issued = number_of_issued,
            Balance = request.POST["Balance"],
            Material_Name_id = material_id,
            Date = request.POST["Date"],
            Verification_Date = request.POST["Verification_Date"],
            Verified_By = request.POST["Verified_By"],
        )

        return redirect("/display")

    mat = Materialserializers(material).data
    context = {
        "form": form,
        "id": material_id,
        "mat": mat,
        "selected_material_id": selected_material_id
    }
    return render(request, "home.html", context)
