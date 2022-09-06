from django.shortcuts import render,redirect
from .forms import SignupForm,LoginForm
from django.contrib.auth import authenticate,login
# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    msg=None
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            msg='User Created successfully'
            return redirect('login')
        else:
            msg='Form is not Valid'
    else:
        form=SignupForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form=LoginForm(request.POST or None)
    msg=None
    if request.method == 'POST':
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None and user.is_patient:
                login(request, user)
                return redirect('patient')
            if user is not None and user.is_doctor:
                login(request, user)
                return redirect('doctor')
            else:
                msg='Invalid credentials'
        else:
            msg='Error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})
    
def patient(request):
    return render(request,'patient.html')

def doctor(request):
    return render(request,'doctor.html')