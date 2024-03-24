from django.shortcuts import render, redirect
from AppChismesitoLocal.models import Publicacion, Comentario, MeGusta
from AppChismesitoLocal.forms import PublicacionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout





def inicio(request):
    return render(request,'AppChismesitoLocal/inicio.html')

def exit(request):
    logout(request)
    return redirect('inicio')

@login_required
def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'AppChismesitoLocal/lista_publicaciones.html', {'publicaciones': publicaciones})

#@login_required
def detalle_publicacion(request, pk):
    try:
        publicacion = Publicacion.objects.get(pk=pk)
    except Publicacion.DoesNotExist:
        return redirect('lista_publicaciones')
    return render(request, 'AppChismesitoLocal/detalle_publicacion.html', {'publicacion': publicacion})


#@login_required
def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_publicaciones')
    else:
        form = PublicacionForm()
    return render(request, 'AppChismesitoLocal/crear_publicacion.html', {'form': form})


#@login_required
def editar_publicacion(request, pk):
    try:
        publicacion = Publicacion.objects.get(pk=pk)
    except Publicacion.DoesNotExist:
        return redirect('lista_publicaciones')

    if request.method == 'POST':
        form = PublicacionForm(request.POST, instance=publicacion)
        if form.is_valid():
            form.save()
            return redirect('lista_publicaciones')
    else:
        form = PublicacionForm(instance=publicacion)
    return render(request, 'AppChismesitoLocal/editar_publicacion.html', {'form': form})

#@login_required
def eliminar_publicacion(request, pk):
    try:
        publicacion = Publicacion.objects.get(pk=pk)
    except Publicacion.DoesNotExist:
        return redirect('lista_publicaciones')

    if request.method == 'POST':
        publicacion.delete()
        return redirect('lista_publicaciones')
    return render(request, 'AppChismesitoLocalconfirmar_eliminar.html', {'publicacion': publicacion})



def index(request):
    return render(request,'AppChismesitoLocal/index.html')


#@login_required
def buscar_por_categoria(request):
    if 'categoria' in request.GET:
        categoria = request.GET['categoria']
        chismes = Publicacion.objects.filter(categoria=categoria)
        return render(request, 'buscar_por_categoria.html', {'chismes': chismes, 'categoria': categoria})
    else:
    
        return render(request, 'AppChismesitoLocal/buscar_por_categoria.html', {'error': 'Por favor, seleccione una categoría para buscar chismes.'})