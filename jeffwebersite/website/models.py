from django.db import models

# Create your models here.


class Category (models.Model):
    name = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Product (models.Model):
    CHOISE_GENRE = (
        ('used', "used"),
        ('new', "new"),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_title = models.TextField(max_length=1000)
    condition = models.TextField()
    quantity = models.TextField()
    location = models.TextField(max_length=100)
    data_posted = models.DateField(auto_now=False)
    price = models.TextField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='media/product_images', null=True, blank=True)

    def __str__(self):
        return self.product_title


