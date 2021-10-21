from django.db import models
import uuid
from django.db.models.deletion import CASCADE

# Create your models here.
class Product(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    product_name = models.CharField(max_length=30)
    discription = models.TextField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name


class Tags(models.Model):
    TAGS = (
        ('Electronics', 'Electronics'),
        ('Clothing', 'Clothing'),
        ('Footware', 'Footware'),
        ('Trending', 'Trending')
    )

    # id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    tag = models.CharField(max_length=100, choices=TAGS)
    project = models.ForeignKey(Product, on_delete=CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag


