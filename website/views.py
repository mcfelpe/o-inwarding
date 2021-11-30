from django.core.files.base import endswith_lf
from django.shortcuts import redirect, render
from .models import Inwarding
from .forms import InwardingForm, InwardingFormHOD, InwardingFormFIN, InwardingFormEdit
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
import os
#import boto3


# Function for logging out user
def logout_user(request):
    logout(request)
    messages.success(request, ('User Logged Out Successfully!'))
    return redirect('auth_login')

# Function for loggin in user
def auth_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('User Logged In Successfully!'))
            return redirect('inw_data_table')
        else:         
            messages.success(request, ('Invalid Username and Password'))
            return redirect('auth_login')
    else:
        return render(request, 'auth_login.html', {})

# Function for inserting an inward
def inw_insert(request):
    if request.method == "POST":
        form = InwardingForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
        messages.success(request, ('Inward saved succcessfully!'))
        return redirect('inw_data_table')
    else:
        urlObject = request.path
        return render(request, 'inw_insert.html', {'showURL':urlObject})

# Function for showing inwards from the Inwarding model/table based on user login
def inw_data_table(request):
    current_user = request.user.get_username()
    current_department = request.user.filtering.user_department
    current_filter = request.user.filtering.user_filter_group

    if current_filter == "HOD":    
        all_inwards = Inwarding.objects.filter(inw_sourcing_department=current_department)
        urlObject = request.path
        return render(request, 'inw_data_table.html', {'all_inwards':all_inwards, 'showURL':urlObject, 'current_department':current_department, 'current_filter':current_filter})
    elif current_filter == "FINANCE" or current_filter == "ADMIN": 
        all_inwards = Inwarding.objects.all()
        urlObject = request.path
        return render(request, 'inw_data_table.html', {'all_inwards':all_inwards, 'showURL':urlObject, 'current_department':current_department, 'current_filter':current_filter})
    else:
        all_inwards = Inwarding.objects.filter(inw_owner=current_user)
        urlObject = request.path
        return render(request, 'inw_data_table.html', {'all_inwards':all_inwards, 'showURL':urlObject, 'current_department':current_department, 'current_filter':current_filter})

# Function for showing inwards from Inwarding model/table regardless of whos logged in (Table form)
def inw_all_table(request):   
    all_inwards = Inwarding.objects.all()   
    urlObject = request.path
    return render(request, 'inw_all_table.html', {'all_inwards':all_inwards, 'showURL':urlObject})  

# Function for showing inwards from Inwarding model/table regardless of whos logged in (Individual form)
def inw_ind_table(request):
    p = Paginator(Inwarding.objects.all(), 1)
    page = request.GET.get('page')
    ind_inwards = p.get_page(page)
    
    urlObject = request.path
    return render(request, 'inw_ind_table.html', {'ind_inwards':ind_inwards, 'showURL':urlObject})
    
# Function for deleting an inward based on the item number being passed
def inw_delete(request, delete_item_id):
    delete_item = Inwarding.objects.get(pk=delete_item_id)
    # The code indicates that if there is an existing image based on the database value, then delete that image specified in the image path
    # if delete_item.inw_img != "": 
        # os.remove(delete_item.inw_img.path)
    # The code indicates that if there is an existing image based on the database value, then delete that image in the s3 bucket
    # if delete_item.inw_img != "":
        # s3_resource=boto3.client("s3")
        # s3_resource.delete_object(Bucket='mcfelpe-inw-bucket', Key=delete_item.inw_img.url)
    delete_item.delete()
    messages.success(request, ('Inward deleted succcessfully!'))
    return redirect('inw_data_table')

# Function for viewing an inward based on the item number being passed
def inw_view(request, view_item_id):
    view_item = Inwarding.objects.get(pk=view_item_id)
    return render(request, 'inw_view.html', {'view_item':view_item})

# Function for viewing an inward based on the item number being passed before deleting permanently
def inw_view_delete(request, view_delete_item_id):
    view_delete_item = Inwarding.objects.get(pk=view_delete_item_id)
    return render(request, 'inw_view_delete.html', {'view_delete_item':view_delete_item})

# Function for editing an inward based on the item number being passed
def inw_edit(request, edit_item_id):
    edit_item = Inwarding.objects.get(pk=edit_item_id)
    if request.method == "POST": 
        form = InwardingFormEdit(request.POST or None, request.FILES or None, instance=edit_item)
        # The code indicates that if there is an existing image based on the database value, then delete that image specified in the image path
        # if len(request.FILES) != 0:
            # if edit_item.inw_img != "":
                # os.remove(edit_item.inw_img.path)
        if form.is_valid():
            form.save()
        messages.success(request, ('Inward updated succcessfully!'))
        return redirect('inw_data_table')
    else:
        
        if edit_item.inw_location == "Dahra Main Office":
            loc1 = "selected"
        else:
            loc1 = ""
        
        if edit_item.inw_location == "KNO":
            loc2 = "selected"
        else: 
            loc2 = ""
        
        if edit_item.inw_location == "ISC":
            loc3 = "selected"
        else:
            loc3 = ""
        if edit_item.inw_location == "Messaid":
            loc4 = "selected"
        else: 
            loc4 = ""
        
        if edit_item.inw_category == "Permanent - Computer & Peripheral":
            cat1= "selected"
        else:
            cat1 =""
        if edit_item.inw_category == "Permanent - Furniture & Fixtures":
            cat2= "selected"
        else:
            cat2 =""
        if edit_item.inw_category == "Permanent - Office Equipment":
            cat3= "selected"
        else:
            cat3 =""
        if edit_item.inw_category == "Permanent - Office Renovation":
            cat4= "selected"
        else:
            cat4 =""
        if edit_item.inw_category == "Permanent - Motor Vehicle":
            cat5= "selected"
        else:
            cat5 =""
        if edit_item.inw_category == "Consumables - IT Consumables":
            cat6= "selected"
        else:
            cat6 =""
        if edit_item.inw_category == "Consumables - Hygiene":
            cat7= "selected"
        else:
            cat7 =""
        if edit_item.inw_category == "Consumables - Pantry":
            cat8= "selected"
        else:
            cat8 =""
        if edit_item.inw_category == "Consumables - Stationery":
            cat9= "selected"
        else:
            cat9 =""
            
        if edit_item.inw_type == "Inventory":
            item1 = "selected"
        else:
            item1 =""
        if edit_item.inw_type == "Services":
            item2 = "selected"
        else:
            item2 =""
            
        return render(request, 'inw_edit.html', {'edit_item':edit_item, 'loc1':loc1, 'loc2':loc2, 'loc3':loc3, 'loc4':loc4, 'cat1':cat1, 'cat2':cat2, 'cat3':cat3, 'cat4':cat4, 'cat5':cat5, 'cat6':cat6, 'cat7':cat7, 'cat8':cat8, 'cat9':cat9, 'item1':item1, 'item2':item2})
        
# Function for HOD approval of an inward based on the item number being passed
def inw_hod_app(request, hod_item_id):
    hod_item = Inwarding.objects.get(pk=hod_item_id)
    if request.method == "POST":
        form = InwardingFormHOD(request.POST or None, instance=hod_item)
        if form.is_valid():
            form.save()
        messages.success(request, ('HOD changes saved successfully!'))
        return redirect('inw_data_table')
    else:          
        return render(request, 'inw_hod_approve.html', {'hod_item':hod_item})

# Function for Finance approval of an inward based on the item number being passed
def inw_fin_app(request, fin_item_id):
    fin_item = Inwarding.objects.get(pk=fin_item_id)
    if request.method == "POST":
        form = InwardingFormFIN(request.POST or None, instance=fin_item)
        if form.is_valid():
            form.save()
        messages.success(request, ('FINANCE changes saved successfully!'))
        return redirect('inw_data_table')
    else:          
        return render(request, 'inw_fin_approve.html', {'fin_item':fin_item})