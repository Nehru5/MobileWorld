from django.db import models

class UserProfile(models.Model):
  username = models.CharField(max_length=100)
  first_name = models.CharField(max_length=100)
  last_name  = models.CharField(max_length=100)
  email = models.EmailField()
  password = models.CharField(max_length=150)
  
  
  def __str__(self):
    return self.first_name
  
  
class UserDetails(models.Model):
  user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
  phone_number = models.CharField(max_length=15)
  address = models.TextField()
  pin_code = models.CharField(max_length=20)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  country = models.CharField(max_length=100)
  user_dp = models.ImageField(upload_to="users/", blank=True, null=True, default="")
  
  def __str__(self):
    return self.user.first_name
  
class Product(models.Model):

  product_name = models.CharField(max_length=100)
  specification = models.TextField()
  price = models.DecimalField(decimal_places=2, max_digits=10)
  location = models.CharField(max_length=100)
  product_image = models.ImageField(upload_to="products/", null=True, blank=True,default="")
  
  def __str__(self):
    return self.product_name
  
  
class Cart(models.Model):
  user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.user.first_name} added {self.product.product_name}"
  
class Order(models.Model):
  user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)
  date = models.DateTimeField(auto_now_add=True)
  
  
  def __str__(self):
    return f"{self.product.product_name} Ordered by {self.user.first_name}"
