from django.urls import path
from .views import add_bank, add_branch, list_all_banks, bank_details, branch_details

urlpatterns = [
    path('add/', add_bank, name='add_bank'),
    path('add_branch/', add_branch, name='add_branch'),
    path('', list_all_banks, name='list_banks'),
    path('<int:bank_id>/details/', bank_details, name='bank_details'),
    path('branch/<int:branch_id>/details/', branch_details, name='branch_details'),
]