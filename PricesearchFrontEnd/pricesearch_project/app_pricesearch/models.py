from django.db import models


class Produto(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    site = models.TextField(max_length=255)
    quotation_date = models.DateField()
    image_link = models.TextField(
        max_length=500, default='https://via.placeholder.com/150')
