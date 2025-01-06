# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('api/brands/', BrandListView.as_view(), name='brand-list'),
    path('api/categories/', CategoryListView.as_view(), name='category-list'),
    
    
    path('api/customers/<int:customer_id>/add-address/', AddressCreateView.as_view(), name='add-address'),
    path('api/customers/<int:address_id>/edit-address/', EditAddressAPIView.as_view(), name='edit-address'),
    path('api/customers/<int:customer_id>/addresses/', CustomerAddressesAPIView.as_view(), name='customer-addresses'),
    path('api/customers/<int:address_id>/delete-address/', DeleteAddressAPIView.as_view(), name='delete-address'),
    
    
    path('api/customers/<int:customer_id>/credit-cards/', AddCreditCardAPIView.as_view(), name='add-credit-card'),
    path('api/credit-cards/<int:credit_card_id>/', EditCreditCardAPIView.as_view(), name='edit-credit-card'),
    path('api/customers/<int:customer_id>/credit-cards-list/', CustomerCreditCardsAPIView.as_view(), name='list-customer-credit-cards'),
    
    
    
    
    
    
    
    
    
    
    
    
    
]