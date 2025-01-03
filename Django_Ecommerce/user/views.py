from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from services.models import *
from .serializers import *

class CustomerSignup(APIView):
    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            # Save the customer
            customer = serializer.save()
            
            # Create a bonus for the customer with amount set to 0
            Bonus.objects.create(customer=customer, amount=0)

            # Create an empty shopping cart for the customer
            ShoppingCart.objects.create(customer=customer)

            response_data = {
                'message': 'Signup successful',
                'Customer_id': customer.id
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        



from django.contrib.auth import authenticate
class CustomerLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        customer = Customer.objects.filter(user__username=username).first()

        if customer is not None:
            user = customer.user

            if user is not None:
                authenticated_user = authenticate(request, username=username, password=password)

                if authenticated_user is not None and authenticated_user == user:
                    # Authentication successful
                    customer_data = CustomerSerializer(customer).data
                    return Response({
                        'detail': 'Login successful',
                        'customer_id': customer.id,
                        'customer_data': customer_data
                    })
                else:
                    # Invalid credentials
                    return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                # User not found
                return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Customer not found
            return Response({'detail': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)