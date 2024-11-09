from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('playbooks/', views.playbooks_view, name='playbooks'),
    path('playbooks/add/', views.add_playbook, name='add_playbook'),
    path('playbooks/remove/', views.remove_playbook, name='remove_playbook'),
    path('api/playbooks/', views.get_playbooks, name='get_playbooks'),
]
