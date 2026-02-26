from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def loginVerification(request):

    if request.method == "POST":

        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        if uname and pwd:
            user = authenticate(request, username=uname, password=pwd)

            if user is not None:

                login(request, user)
                request.session.set_expiry(600) 
                return redirect('home')
            else:
              
                return render(request, 'ki/login_error.html')
        else:
           
            return render(request, 'ki/login_error.html')

    else:
       
        return render(request, "ki/login.html")


def home(request):
    if request.user.is_authenticated:
        return render(request, 'ki/home.html')
    else:
        return redirect('login')


def colleges(request):
    if request.user.is_authenticated:
        colleges_list = ['SVEW', 'VIT', 'BVRIT']
        return render(request, 'ki/colleges.html', {'colleges': colleges_list})
    else:
        return redirect('login')


def students(request):
    if request.user.is_authenticated:
        students_list = [
            {'sno': 1, 'name': 'meena', 'branch': 'IT', 'age': 20},
            {'sno': 2, 'name': 'neha', 'branch': 'ECE', 'age': 17},
            {'sno': 3, 'name': 'Ram', 'branch': 'AIDS', 'age': 90},
            {'sno': 4, 'name': 'sai', 'branch': 'MECH', 'age': 18},
        ]
        return render(request, 'ki/students.html', {'students': students_list})
    else:
        return redirect('login')

