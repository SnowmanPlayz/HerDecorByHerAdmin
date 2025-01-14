from django.conf import settings
from django.db import models

TAG_CHOICES = (
    ('N','New'),
    ('F','Featured')
)

TAG_COLOR_CHOICES = (
    ('R','Red'),
    ('P','Pink'),
    ('C','Cyan')
)

class Item(models.Model):
    title = models.CharField(max_length=75)
    price = models.FloatField()
    tag = models.CharField(choices=TAG_CHOICES, max_length=1)
    tag_color = models.CharField(choices=TAG_COLOR_CHOICES, max_length=1)

    def __str__(self):
        return self.title

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.title