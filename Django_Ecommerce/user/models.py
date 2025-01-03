from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    phone = models.CharField("Phone Number", max_length=15, null=False)    
    email = models.EmailField("Email", null=False, blank=False)
    
    MALE, FEMALE = "Male", "Female"
    GENDER_OPTIONS = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )

    gender = models.CharField(
        "Gender", choices=GENDER_OPTIONS, max_length=10, null=False, blank=False
    )
    
    profile_image = models.ImageField(
        "Profile Image", upload_to="profile_images", null=True, blank=True,
    )
    
    
    def __str__(self):
        return f"{self.username} - {self.email}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['username']

        

class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=False, related_name="customer_user"
    )
    
    first_name = models.CharField(
        ('First Name'), max_length=150, null=False, blank=False)

    father_name = models.CharField(
        "Father Name", max_length=50, null=False, blank=False)

    last_name = models.CharField(
        ('Last Name'), max_length=150, null=False, blank=False)
      
    birth_date = models.DateField("Date of Birth", null=False, blank=False)
    
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user.username})"

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ['last_name', 'first_name']  