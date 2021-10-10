from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from enroll.models import User
from .forms import UserForm

# Create your views here.

# This function add new data and display it

def add_show(request):
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['Name']
            em = fm.cleaned_data['Email']
            pw = fm.cleaned_data['Password']
            reg = User(Name=nm,Email=em,Password=pw)
            reg.save()
            messages.success(request,'User has been added Successfully !!!')
        fm = UserForm()
    else:
        fm = UserForm()

    stud = User.objects.all()

    return render(request,'enroll/addandshow.html',{'form':fm ,'stu':stud})
    

# This function delete data

def  delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


# Update data
    
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = UserForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'User has been Updated Successfully !!!')
    else:
        pi = User.objects.get(pk=id)
        fm = UserForm(instance=pi)
    return render(request,'enroll/update.html', {'form':fm} )
    