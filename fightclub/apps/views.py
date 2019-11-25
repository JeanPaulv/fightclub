from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserChangeForm , UserCreationForm
from apps.forms import EditPerfilForm

# Create your views here.

def index(request):
    return render(request,'index.html')

def index2(request):
    return render(request,'indexeng.html')

def jugar(request):
    return render(request,'jugar.html')

def jugar2(request):
    return render(request,'jugareng.html')


def registro(request):
    if request.method == 'POST':
        username= request.POST['nombre_usuario']
        nombre = request.POST['nombre']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Usuario ya se encuentra registrado')
                return redirect('registro')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Correo ya se encuentra registrado')
                return redirect ('registro')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=nombre)
                user.save();
                print('user created')
                return redirect('index')
        
        else:
            messages.info(request,'Las contraseñas no coinciden')
            return redirect('registro')

        return redirect('/')

    else:
        messages.info(request,'')
        return render(request,'registro.html')

def registro2(request):
    if request.method == 'POST':
        username= request.POST['nombre_usuario']
        nombre = request.POST['nombre']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Usuario ya se encuentra registrado')
                return redirect('registro2')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Correo ya se encuentra registrado')
                return redirect ('registro2')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=nombre)
                user.save();
                print('user created')
                return redirect('index2')
        
        else:
            messages.info(request,'Las contraseñas no coinciden')
            return redirect('registro2')

        return redirect('/')

    else:
        messages.info(request,'')
        return render(request,'registroeng.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['nombre_usuario']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password) 

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:   
         messages.info(request,'Ingrese sus datos correctamente')
         return redirect ('index')
    else:

       return render(request,'index.html')




def logout(request):
    auth.logout(request)
    return redirect('/')

def perfil(request):
    return render(request,'perfil.html')

def jugar(request):
    return render(request,'jugar.html')

def edit(request):
    if request.method == 'POST':
        form = EditPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            return redirect('perfil')
    else:
        form = EditPerfilForm(instance=request.user)
        args = {'form':form}
        return render(request,'edit.html',args)
