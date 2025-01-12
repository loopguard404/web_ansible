from django.contrib import admin
from django.urls import path, include
from web_ansible.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', dashboard, name='dashboard'),
]
