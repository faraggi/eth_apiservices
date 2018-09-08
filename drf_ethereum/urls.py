from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import login, logout

from api import views as api_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/login/', login, {'template_name': 'admin/login.html'}),
    path('users/logout/', logout),
    path('users/', include('django.contrib.auth.urls')),
    path('transactions/', api_views.TransactionView.as_view(), name="transactions"),
    path('transactions/new', api_views.NewTransactionView.as_view(), name="transactions"),
]
