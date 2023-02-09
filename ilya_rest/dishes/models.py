from django.db import models
from products.models import Product

class Dish(models.Model):
	d_name = models.CharField(max_length=50, verbose_name='Dish name')



	#id_Company = models.ForeignKey(Employer, on_delete=models.CASCADE, verbose_name='Company name')
	price = models.IntegerField()

	products = models.ManyToManyField(Product)



	is_visible = models.BooleanField(default=True)

	d_image = models.ImageField(verbose_name='Dish image')

	description = models.TextField(verbose_name='Description')

	def __str__(self):
		return self.d_name