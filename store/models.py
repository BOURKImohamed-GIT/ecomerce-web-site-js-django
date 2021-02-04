from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    def __str__(self):
        return self.title


class Blog(models.Model):
    titleOne=models.CharField(max_length=200, null=True)
    titleTow=models.CharField(max_length=200, null=True)
    imageBlog = models.ImageField(null=True, blank=True)
    image2Blog = models.ImageField(null=True, blank=True)
    textBlog = models.CharField(max_length=2000, null=True)
    def __str__(self):
        return self.titleOne

# image2Blog
    @property
    def imageBlogURL(self):
        try:
            url = self.imageBlog.url
        except:
            url = ''
        return url
    @property
    def image2BlogURL(self):
        try:
            url = self.image2Blog.url
        except:
            url = ''
        return url
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    # slug = models.SlugField(unique=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    priceavant = models.DecimalField(max_digits=8, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=400, null=True)
    profile = models.ImageField(null=True, blank=True)
    seed = models.CharField(max_length=500, null=True)
    views_count=models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name



    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def profileURL(self):
        try:
            url = self.profile.url
        except:
            url = ''
        return url
    @property
    def image2URL(self):
        try:
            url = self.image2.url
        except:
            url = ''
        return url

    @property
    def profile2URL(self):
        try:
            url = self.profile2.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    # here
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total



class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.address)
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
