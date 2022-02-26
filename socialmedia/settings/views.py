from django.shortcuts import render, HttpResponseRedirect
from .forms import UserForm
from .models import User
# Create your views here.

#this fnc add & show the user form
def add_show(request):
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['username']
            pw = fm.cleaned_data['password']
            em = fm.cleaned_data['email']
            ds = fm.cleaned_data['description']
            fn = fm.cleaned_data['first_name']
            ln = fm.cleaned_data['last_name']
            is_active = fm.cleaned_data['is_active']
            reg = User(username=nm, password=pw, email=em, description=ds, first_name=fn, last_name=ln, is_active=is_active)
            reg.save()
    else:
        fm = UserForm()
    usr = User.objects.all()
    return render(request, 'settings/addandshow.html', {'form': fm, 'usr': usr})

#fucn update the user
def update_data(request, id):
    if request.method == 'POST':
        upusr = User.objects.get(pk=id)
        fm = UserForm(request.POST, instance=upusr)
        if fm.is_valid():
            #can clean data here too
            fm.save()

    else:
        upusr = User.objects.get(pk=id)
        fm = UserForm(instance=upusr)
    return render(request, 'settings/updatesetting.html', {'form': fm})


# fucn will del the user
def delete_data(request, id):
    if request.method == 'POST':
        delusr = User.objects.get(pk=id)
        delusr.delete()
        return HttpResponseRedirect('/')