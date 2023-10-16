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
    condition = models.CharField(max_length=50, choices=CHOISE_GENRE)
    quatity = models.IntegerField()
    location = models.TextField(max_length=100)
    data_posted = models.DateField(auto_now=False)
    price = models.TextField(max_length=50)
    description = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='media/product_images')

    def __str__(self):
        return self.product_title


