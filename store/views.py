from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Producto,Categoria
from .forms import CreateUserForm
from .forms import Producto_Form
from .forms import Categoria_Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages




def store(request):     
     producto = Producto.objects.all()
     data = {'producto' : producto}
     return render(request, 'store/store.html', data)

def cart(request):
     context = {}
     return render(request, 'store/cart.html', context)

def checkout(request):

     context = {}
     return render(request, 'store/checkout.html', context)


def registrar_usuario(request):

     form= CreateUserForm()
     if request.method == 'POST':
          form =CreateUserForm(request.POST)
          if form.is_valid():
               form.save()
               user= form.cleaned_data.get('username')
               messages.success(request, 'Se a Creado con exito' + user  )
               return redirect(logins)

     context ={'form':form}
     return render(request, 'store/registrar_usuario.html', context)



def logins(request):
     if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')
          user =authenticate(request, username=username, password=password)
          if user is not None:
               login (request, user)
               return redirect('checkout')
          else:
                    messages.info(request, 'el usuario es incorrecto ')
     context ={}
     return render(request,'store/logins.html', context)  

#PRODUCTOS
     

def nuevo_producto(request):
     data = {
          'form':Producto_Form()
     }
     if request.method == 'POST':
          form = Producto_Form(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               messages.success(request, 'Producto Agregado ')
               
          else:
               data["from"] = form     
               
     return render(request, 'store/nuevo_producto.html', data )

def lista_produtos(request):
     producto = Producto.objects.all()
     data = {'producto' : producto}
     return render(request,'store/lista_produtos.html', data)


def editar_produtos(request, id ):
     productos = get_object_or_404(Producto, id=id)

     data = {
          'form':Producto_Form(instance=productos)
     }
     if request.method == 'POST':
          form = Producto_Form(data=request.POST, instance=productos, files=request.FILES)
          if form.is_valid():
               form.save()
               messages.success(request, 'Producto Modificado ')
               return redirect  ("lista" )
               
          data ['form'] = 'form'

     return render(request, 'store/modificar.html',data ) 



def elimanar_producto(request, id):
     productos = get_object_or_404(Producto, id=id)
     productos.delete()
     messages.success(request, 'Producto Eliminado ')
     return redirect  ("lista" )


#CATEGORIA
def nueva_categoria(request):
     data = {
          'form':Categoria_Form()
     }
     if request.method == 'POST':
          form = Categoria_Form(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               messages.success(request, 'Categoria Agregado ')
               
          else:
               data["from"] = form     
               
     return render(request, 'store/nueva_categoria.html', data )


def lista_categoria(request):
     categoria = Categoria.objects.all().order_by('-id')
     data = {'categoria' : categoria}
     return render(request,'store/lista_categoria.html', data)
     
def editar_categoria(request, id ):
     categoria = get_object_or_404(Categoria, id=id)

     data = {
          'form':Categoria_Form(instance=categoria)
     }
     if request.method == 'POST':
          form = Categoria_Form(data=request.POST, instance=categoria, files=request.FILES)
          if form.is_valid():
               form.save()
               messages.success(request, 'Categoria Modificado ')
               return redirect  ("listar" )
               
          data ['form'] = 'form'

     return render(request, 'store/modificarcate.html',data ) 




def elimina_categoria(request, id):
     categoria = get_object_or_404(Categoria, id=id)
     categoria.delete()
     messages.success(request, 'Categoria Eliminado ')
     return redirect  ("listar" )

