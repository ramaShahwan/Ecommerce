# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from user.serializers import *

class BrandListView(APIView):
    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


###############################################################################################
    
# Add address
class AddressCreateView(APIView):
    def post(self, request, customer_id):
        # Check if the customer exists
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)

        # Copy the data from the request and add the customer ID
        data = request.data.copy()
        data['customer'] = customer.id  # Add the customer ID to the data

        # Create the address using the modified data
        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
# Edit specific address 

class EditAddressAPIView(APIView):
    def put(self, request, address_id):
        try:
            address = Address.objects.get(id=address_id)
        except Address.DoesNotExist:
            return Response({"error": "Address not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AddressSerializer(address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
# Display addresses of a specific customer
class CustomerAddressesAPIView(APIView):
    def get(self, request, customer_id):
        # Retrieve all addresses for the specific customer
        addresses = Address.objects.filter(customer_id=customer_id)
        
        # Check if the customer has any addresses
        if not addresses.exists():
            return Response({"error": "No addresses found for this customer."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
# Delete Specific Address
class DeleteAddressAPIView(APIView):
    def delete(self, request, address_id):
        try:
            address = Address.objects.get(id=address_id)
        except Address.DoesNotExist:
            return Response({"error": "Address not found"}, status=status.HTTP_404_NOT_FOUND)

        address.delete()
        return Response({"message": "Address deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
    
####################################################################################################

# Add CreditCard
class AddCreditCardAPIView(APIView):
    def post(self, request, customer_id):
        # Include the customer ID in the request data
        data = request.data.copy()
        data['customer'] = customer_id

        # Serialize the data
        serializer = CreditCardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#  Editing a Credit Card
class EditCreditCardAPIView(APIView):
    def put(self, request, credit_card_id):
        try:
            credit_card = CreditCard.objects.get(id=credit_card_id)
        except CreditCard.DoesNotExist:
            return Response({"error": "Credit card not found"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the data with the existing instance
        serializer = CreditCardSerializer(credit_card, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    

# Display credit cards of a specific customer
class CustomerCreditCardsAPIView(APIView):
    def get(self, request, customer_id):
        # Retrieve all credit cards for the specific customer
        credit_cards = CreditCard.objects.filter(customer_id=customer_id)
        
        # Check if the customer has any credit cards
        if not credit_cards.exists():
            return Response({"error": "No credit cards found for this customer."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CreditCardSerializer(credit_cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
