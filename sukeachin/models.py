from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.
class Category(models.Model):
    
    category_name = models.CharField(null=False,blank=False,unique=True ,max_length=100)
    category_created_date = models.DateTimeField(auto_now_add=True)
    category_updated_date = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return str(self.category_name)


class Product(models.Model):

    name = models.CharField(null=False,blank=False ,max_length=100)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(null=False,blank=False)
    product_description = models.TextField(null=False,blank=False)
    product_specification = models.TextField(null=False,blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="products/")
    product_created_date = models.DateTimeField(auto_now_add=True)
    product_updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('home')


class profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="images/profile/")
    bio = models.TextField(null=True)
      
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')

class Review(models.Model):

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    review_body = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.product.name, self.name)

    def total_reviews(self):
        return self.reviews.count()
    
    class Meta:
        ordering = ['-date_add']

class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-date_sent']

class order(models.Model):

    payment_methods = (
        
        ("cash_on_delivery", "cash_on_delivery"),
        ("paypal", "paypal"),
        
    
        )

    First_name = models.CharField(max_length=50,null=False,blank=False)
    Last_name = models.CharField(max_length=50,null=False,blank=False)
    Orderd_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    Mobile_no = models.CharField(max_length=50,null=False,blank=False)
    Adress=models.CharField(max_length=50,null=False,blank=False)
    City = models.CharField(max_length=50,null=False,blank=False)
    Product_name = models.CharField(max_length=150,null=False,blank=False)
    Price = models.CharField(max_length=250,null=False,blank=False)
    Quantity = models.CharField(max_length=150,null=False,blank=False)
    Total_price = models.CharField(max_length=250,null=False,blank=False)
    Shipping_cost = models.FloatField(null=True,blank=False)
    Sub_total = models.CharField(max_length=250,null=False,blank=False)
    Grand_total = models.CharField(max_length=250,null=False,blank=False)
    Orderd_date = models.DateTimeField(auto_now_add=True)
    Payment_method = models.CharField(max_length=50,
                  choices=payment_methods,
                  default="Cash on Delivery")
    def __str__(self):
        return str(self.First_name)

    class Meta:
        ordering = ['-Orderd_date']
