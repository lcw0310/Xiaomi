from django.db import models

# Create your models here.
class Index(models.Model):
    id = models.AutoField(primary_key=True)
    menu = models.CharField(max_length=40)
    mid = models.IntegerField()
    pay_menu = models.CharField(max_length=20)
    image = models.CharField(max_length=100)
    big_title = models.CharField(max_length=10)
    pay_title = models.CharField(max_length=20)
    select = models.CharField(max_length=20,null=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    price = models.IntegerField()
    plate_id = models.IntegerField(null=True)
    product_description = models.CharField(max_length=100)
    big_image = models.CharField(max_length=100,null=True)

    class Meta:
        db_table = 'Xiaomi_index'

class Paymenu(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=100)
    content = models.CharField(max_length=50)
    pid = models.ImageField()

    class Meta:
        db_table = 'xiaomi_PayTitle'

class List(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    price = models.IntegerField()
    pid = models.IntegerField()

    class Meta:
        db_table = 'xiaomi_list'

class Detail(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=100)
    image_1 = models.CharField(max_length=100)
    image_2 = models.CharField(max_length=100)
    image_3 = models.CharField(max_length=100)
    image_4 = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    delivery = models.CharField(max_length=100)
    quantity = models.IntegerField()
    # overview = models.CharField(max_length=100)
    # comment = models.CharField(max_length=100)
    pid = models.IntegerField()

    class Meta:
        db_table = 'xiaomi_detail'