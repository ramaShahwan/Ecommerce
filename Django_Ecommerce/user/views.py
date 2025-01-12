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
        
        
        
   
        
        
from rest_framework.parsers import MultiPartParser, FormParser
class CustomerEditProfileAPI(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def put(self, request, customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return Response({'detail': 'Customer not found'}, status=404)

        serializer = CustomerProfileSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
        
        

from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

class PasswordUpdateView(APIView):
    def put(self, request, customer_id):
        serializer = PasswordUpdateSerializer(data=request.data)
        if serializer.is_valid():
            user = Customer.objects.get(id=customer_id)
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']

            if not user.user.check_password(old_password):
                return Response({'error': 'Invalid old password.'}, status=400)

            user.user.set_password(new_password)
            user.user.save()

            return Response({'message': 'Password updated successfully.'}, status=200)
        else:
            return Response(serializer.errors, status=400)
        


# View to send the username via email
class CustomerForgotUsernameView(APIView):
    def post(self, request):
        email = request.data.get("email")
        
        try:
            # Fetch the user based on the email
            user = User.objects.get(email=email)
            customer = user.customer_user  # Get the associated Customer instance

            # Prepare the email content
            subject = "Your Username Request"
            message = (
                f"Hello {customer.first_name},\n\n"
                f"Your username is: {user.username}\n\n"
                "If you did not request this email, please ignore it."
            )

            # Send the email
            send_mail(subject, message, 'no-reply@yourdomain.com', [user.email])

            return JsonResponse({"message": "Username sent to your email."}, status=200)
        
        except User.DoesNotExist:
            return JsonResponse({"error": "No user found with this email."}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

################################################################

from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.hashers import make_password
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from rest_framework.views import APIView
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model

User = get_user_model()

# View to send the password reset email
class CustomerForgotPasswordView(APIView):
    def post(self, request):
        email = request.data.get("email")
        try:
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_link = f"http://localhost:8000/User/page-reset-password/{uid}/{token}/"
            subject = "Password Reset Requested"
            message = f"Hello,\n\nClick below to reset your password:\n{reset_link}\n\nIf you didn’t request this, ignore it."
            send_mail(subject, message, 'no-reply@yourdomain.com', [user.email])

            return JsonResponse({"message": "Password reset email sent."}, status=200)

        except User.DoesNotExist:
            return JsonResponse({"error": "No user found with this email."}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

# View to save the new password
class CustomerResetPasswordView(APIView):
    def post(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)

            # Verify the token
            if not default_token_generator.check_token(user, token):
                return JsonResponse({"error": "Invalid or expired token."}, status=400)

            new_password = request.data.get("new_password")
            if not new_password:
                return JsonResponse({"error": "New password not provided."}, status=400)

            user.password = make_password(new_password)
            user.save()

            return JsonResponse({"message": "Password has been reset successfully."}, status=200)

        except User.DoesNotExist:
            return JsonResponse({"error": "Invalid user ID."}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

# View to render the password reset form
class CustomerPasswordResetFormView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                return render(request, 'reset_password.html', {'uidb64': uidb64, 'token': token})
                #return render(request, 'e_commerce/reset_password.html', {'uidb64': uidb64, 'token': token})
            else:
                return render(request, 'error.html', {'message': 'Invalid or expired token.'})
        except Exception as e:
            return render(request, 'error.html', {'message': str(e)})