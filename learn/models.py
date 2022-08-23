from django.db import models


# Create your models here.
class Purchase(models.Model):
    product_id= models.AutoField
    product_name = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


    






    
