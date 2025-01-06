from django.db import models

# Create your models here.

class Bonus (models.Model):
    amount = models.IntegerField("Amount", null=False, blank=False)
    customer = models.ForeignKey(
        to='user.Customer', verbose_name="Customer", on_delete=models.CASCADE, null=False, blank=False)


    def __str__(self):
        return str(self.customer) + " " + str(self.amount)
    
    class Meta:
        verbose_name = "Bonus"
        verbose_name_plural = "Bonus"




class Complaint(models.Model):
    subject = models.CharField("Subject", max_length=25, null=False, blank=False)
    message = models.CharField("Message", max_length=1000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user_email = models.EmailField("Email", null=True, blank=True)


    def __str__(self):
        return f"{self.subject} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

    class Meta:
        verbose_name = "Complaint"
        verbose_name_plural = "Complaints"





class Address(models.Model):
    customer = models.ForeignKey(
        to='user.Customer',
        verbose_name="Customer",
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    street = models.CharField(max_length=255, verbose_name="Street Address", null=False, blank=False)
    neighborhood = models.CharField(max_length=100, verbose_name="Neighborhood", null=True, blank=True)
    building_number = models.CharField(max_length=50, verbose_name="Building Number", null=True, blank=True)
    city = models.CharField(max_length=100, verbose_name="City", null=False, blank=False)
    state = models.CharField(max_length=100, verbose_name="State/Province", null=False, blank=False)  # Can be used for regions 
    postal_code = models.CharField(max_length=20, verbose_name="Postal Code", null=False, blank=False)
    country = models.CharField(max_length=100, verbose_name="Country", null=False, blank=False)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
        ordering = ['customer', 'city']  # ordering

    def __str__(self):
        return f"{self.street}, {self.neighborhood}, {self.city}, {self.state}, {self.postal_code}, {self.country}"





class Brand(models.Model):
    name = models.CharField("Name", max_length=250, null=False, blank=False)



class Category(models.Model):
    name = models.CharField("Name", max_length=250, null=False, blank=False)





class Discount(models.Model):
    value = models.FloatField("Value", null=False, blank=False)
    start_date = models.DateField ("Start Date", null=False, blank=False)
    end_date = models.DateField ("End Date", null=False, blank=False)
    status = models.BooleanField(
        ('Is Active'),
        default=True,
        help_text='Indicates if the discount is currently active.',
        null=False,
        blank=False
    )
    
   
    def __str__(self):
        return f"Discount of {self.value} from {self.start_date} to {self.end_date} - {'Active' if self.status else 'Inactive'}"

    class Meta:
        verbose_name = "Discount"
        verbose_name_plural = "Discounts"
        
    def formatted_discount_display(self):
        """Return a formatted string for displaying discount details."""
        status_text = 'Active' if self.status else 'Inactive'
        return f"Discount Value: {self.value}, Start Date: {self.start_date}, End Date: {self.end_date}, Status: {status_text}"    
        



class Product(models.Model):
    name = models.CharField("Name", max_length=255, null=False, blank=False)
    description = models.TextField("Description", max_length=5000, null=True, blank=True)
    ram = models.CharField("RAM", max_length=50, null=True, blank=True)  # e.g., "8GB"
    processor = models.CharField("Processor", max_length=255, null=True, blank=True)
    screen_size = models.CharField("Screen Size", max_length=50, null=True, blank=True)  # e.g., "15.6 inches"
    price = models.FloatField("Price", null=False, blank=False)
    storage = models.CharField("Storage", max_length=50, null=True, blank=True)  # e.g., "512GB SSD"
    battery_life = models.CharField("Battery Life", max_length=50, null=True, blank=True)  # e.g., "10 hours"
    quantity_available = models.IntegerField("Quantity Available", null=False, blank=False)
    image = models.ImageField("Product Image", upload_to='products/', null=True, blank=True)
    warranty_period = models.CharField("Warranty Period", max_length=50, null=True, blank=True)  # e.g., "2 years"
    weight = models.FloatField("Weight", null=True, blank=True)  # in kilograms
    release_date = models.DateField("Release Date", null=True, blank=True)

    # rating = models.FloatField("Rating", null=True, blank=True)  # 0.0 to 5.0
    # tags = models.CharField("Tags", max_length=255, null=True, blank=True)  # e.g., "mobile, fast"  
    
      
  # Foreign keys for relationships
    id_discount = models.ForeignKey('Discount', verbose_name="Discount", on_delete=models.CASCADE, null=True, blank=True)
    id_brand = models.ForeignKey('Brand', verbose_name="Brand", on_delete=models.CASCADE, null=False, blank=False)
    id_category = models.ForeignKey('Category', verbose_name="Category", on_delete=models.CASCADE, null=False, blank=False)    
    

    
    def __str__(self):
        return f"{self.name} - {self.price} $"   

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name']  



from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class CreditCard(models.Model):
    card_number = models.CharField("Card Number", max_length=19, null=False, blank=False)
    cardholder_name = models.CharField("Cardholder Name", max_length=255, null=False, blank=False)
    expiration_date = models.DateField("Expiration Date", null=False, blank=False)
    cvv = models.CharField("CVV", max_length=4, null=False, blank=False,
                           validators=[RegexValidator(r'^\d{3,4}$', message="CVV must be 3 or 4 digits long and contain only numbers.")])
    billing_address = models.CharField("Billing Address", max_length=255, null=False, blank=False)
    customer = models.ForeignKey(
        to='user.Customer', verbose_name="Customer", on_delete=models.CASCADE, null=False, blank=False)
    balance = models.DecimalField("Balance", max_digits=10, decimal_places=2, default=0.00, null=False, blank=False)  # New field for balance


    def __str__(self):
        return f"{self.cardholder_name} - {self.card_number[-4:]}"
    
    



class ShoppingCart(models.Model):
    customer = models.OneToOneField(
        to='user.Customer',
        verbose_name="Customer",
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    
    created_at = models.DateTimeField("Created at", auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return f"Shopping Cart for {self.customer}"



class ShoppingCart_Items(models.Model):

    cart = models.ForeignKey(
        to='ShoppingCart', verbose_name="ShoppingCart", on_delete=models.CASCADE, null=False, blank=False)
    
    product = models.ForeignKey(
        to='Product', verbose_name="Product", on_delete=models.CASCADE, null=False, blank=False)
    
    quantity  = models.IntegerField("Quantity", null=False, blank=False)
    price = models.FloatField("Price", null=False, blank=False)
    
    

class Order(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('bonus', 'Bonus'),
    ]
    
    STATUS_CHOICES = [
        ('not_prepared', 'Not Prepared Yet'),  # لم يتم التجهيز بعد
        ('preparing', 'Preparing'),              # قيد التجهيز
        ('shipped', 'Shipped'),                  # تم الشحن
        ('delivered', 'Delivered'),               # تم التوصيل
    ]

    Very_Poor, Poor, Fair, Good, Very_Good = "Very Poor", "Poor", "Fair", "Good", "Very Good"
    EVALUATE_CHOICES = [
        (Very_Poor, "Very Poor"),
        (Poor, "Poor"),
        (Fair, "Fair"),
        (Good, "Good"),
        (Very_Good, "Very Good"),
    ]

    # id_order = models.AutoField(primary_key=True)
    order_date = models.DateTimeField("Order Date", auto_now_add=True, null=False, blank=False)
    total_amount = models.DecimalField("Total Amount", max_digits=10, decimal_places=2, null=False, blank=False)
    payment_status = models.BooleanField("Payment Status", default=False, 
                                        help_text="Indicates whether the payment has been completed.", 
                                        null=False, blank=False)
    
    payment_method = models.CharField("Payment Method", max_length=50, choices=PAYMENT_METHOD_CHOICES, null=False, blank=False)
    status = models.CharField("Order Status", max_length=50, default='not_prepared', null=False, blank=False, choices=STATUS_CHOICES)
    evaluate = models.CharField("Evaluate Service", max_length=50, default=None, null=True, blank=True, choices=EVALUATE_CHOICES)

    
    
    id_cart_product = models.ForeignKey(ShoppingCart_Items, on_delete=models.CASCADE, verbose_name="ShoppingCart_Item", null=False, blank=False)
    id_address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name="Address", null=False, blank=False)


    def __str__(self):
        return f"Order {self.id_order} - Total: {self.total_amount}"