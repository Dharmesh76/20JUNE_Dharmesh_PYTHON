from django.db import models

# Create your models here.
class Product_mst(models.Model):
    product_name=models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.product_name
    
class  product_sub_category_details(models.Model):
    product=models.ForeignKey(Product_mst,on_delete=models.CASCADE)
    product_price=models.DecimalField(max_digits=10,decimal_places=2)
    product_image=models.FileField(upload_to="product_images")
    product_model=models.CharField(max_length=30)
    product_ram=models.CharField(max_length=20)


    def __str__(self) -> str:
        return self.product.product_name


