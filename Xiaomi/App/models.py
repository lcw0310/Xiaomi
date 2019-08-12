from django.db import models

# Create your models here.
class Index(models.Model):
    id = models.AutoField(primary_key=True)
    menu = models.CharField(max_length=40,unique=True)
    mid = models.IntegerField()
    pay_menu = models.CharField(max_length=20,unique=True,default=menu)
    big_image = models.ImageField()
    image = models.ImageField()
    big_title = models.CharField(max_length=10,unique=True)
    pay_title = models.CharField(max_length=20,unique=True)
    select = models.CharField(max_length=20)
    title = models.CharField(max_length=50,unique=True)
    content = models.CharField(max_length=50,unique=True)
    price = models.IntegerField()
    plate_id = models.IntegerField()
    product_description = models.CharField(max_length=100)


    class Meta:
        db_table = 'Xiaomi_index'
