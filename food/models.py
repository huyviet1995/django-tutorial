from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=5000, null=True, blank=True, default="https://cdn-icons-png.flaticon.com/512/1377/1377194.png")

    def __str__(self):
        return self.item_name
