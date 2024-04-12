from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Usuario
from .forms import UsuarioForm
from django.db.models import Q

def home(request):
    usuarios = Usuario.objects.all()
    return render(request, 'index.html', {'usuarios': usuarios})

def pesquisar(request):
    search_query = request.GET.get('search')

    usuarios = Usuario.objects.all() 

    if search_query:  
        usuarios = Usuario.objects.filter(
            Q(nome__icontains=search_query) | Q(email__icontains=search_query) | Q(data_nascimento__icontains=search_query)
        )

    return render(request, 'pesquisar.html', {'usuarios': usuarios})


from django.shortcuts import render, redirect
from .models import Usuario

def atualizar(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)
    
    if request.method == 'POST':
        # Se o formulário for enviado, atualize os dados do usuário
        usuario.nome = request.POST.get("nome")
        usuario.email = request.POST.get("email")
        usuario.save()
        return redirect('home')  # Redirecione de volta para a página inicial após a atualização
    
    # Se não for um POST, exiba o formulário com os dados atuais do usuário
    return render(request, 'atualizar.html', {'usuario': usuario})


def deletar(request):
    if request.method == 'POST' and 'usuario_id' in request.POST:
        usuario_id = request.POST['usuario_id']
        usuario = Usuario.objects.get(pk=usuario_id)
        usuario.delete()
        return redirect('deletar')
    usuarios = Usuario.objects.all()
    return render(request, 'deletar.html', {'usuarios': usuarios})

def criar(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
            return render(request, 'criar.html', {'form': form})
    else:
        form = UsuarioForm()
        return render(request, 'criar.html', {'form': form})

def nova_view(request):
    search_query = request.GET.get('search')

    usuarios = Usuario.objects.all() 

    if search_query:  
        usuarios = Usuario.objects.filter(
            Q(nome__icontains=search_query) | Q(email__icontains=search_query) | Q(data_nascimento__icontains=search_query)
        )
    return render(request, 'novo_urls.html', {'usuarios': usuarios})