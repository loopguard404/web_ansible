import os
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Путь к директории с плейбуками
PLAYBOOKS_DIR = '/etc/ansible/playbooks/'

# Функция для входа
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Функция для отображения списка плейбуков
def playbooks_view(request):
    try:
        playbooks = [f for f in os.listdir(PLAYBOOKS_DIR) if f.endswith('.yml') or f.endswith('.yaml')]
    except FileNotFoundError:
        playbooks = []
    return render(request, 'accounts/playbooks.html', {'playbooks': playbooks})

# Функция для возвращения списка плейбуков в формате JSON
def get_playbooks(request):
    try:
        playbooks = [f for f in os.listdir(PLAYBOOKS_DIR) if f.endswith('.yml') or f.endswith('.yaml')]
    except FileNotFoundError:
        playbooks = []
    return JsonResponse({'playbooks': playbooks})

# Функция для добавления плейбука
@csrf_exempt
def add_playbook(request):
    if request.method == 'POST':
        playbook_name = request.POST.get('playbook_name')
        return JsonResponse({'message': f'Playbook {playbook_name} добавлен.'})
    return JsonResponse({'error': 'Недопустимый запрос'}, status=400)

# Функция для удаления плейбука
@csrf_exempt
def remove_playbook(request):
    if request.method == 'POST':
        playbook_name = request.POST.get('playbook_name')
        return JsonResponse({'message': f'Playbook {playbook_name} удален.'})
    return JsonResponse({'error': 'Недопустимый запрос'}, status=400)
