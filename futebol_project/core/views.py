from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Time


@login_required
def lista_times(request):
    times = Time.objects.all()
    return render(request, 'times/lista.html', {'times': times})


@login_required
def criar_time(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cidade = request.POST.get('cidade')

        if not nome:
            messages.error(request, 'Nome é obrigatório')
        else:
            Time.objects.create(nome=nome, cidade=cidade)
            messages.success(request, 'Time criado com sucesso')
            return redirect('lista_times')

    return render(request, 'times/form.html')


@login_required
def editar_time(request, id):
    time = get_object_or_404(Time, id=id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cidade = request.POST.get('cidade')

        if not nome:
            messages.error(request, 'Nome é obrigatório')
        else:
            time.nome = nome
            time.cidade = cidade
            time.save()
            messages.success(request, 'Time atualizado com sucesso')
            return redirect('lista_times')

    return render(request, 'times/form.html', {'time': time})


@login_required
def deletar_time(request, id):
    time = get_object_or_404(Time, id=id)

    if request.method == 'POST':
        time.delete()
        messages.success(request, 'Time excluído com sucesso')
        return redirect('lista_times')

    return render(request, 'times/confirm_delete.html', {'time': time})