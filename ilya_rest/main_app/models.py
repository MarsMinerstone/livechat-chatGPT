from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Product
from dishes.models import Dish


class User(AbstractUser):
	is_Personal = models.BooleanField(default=False)
	def __str__(self):
		return self.username

"""class Cart(models.Model):

	owner = models.ForeignKey('User', verbose_name = 'Owner', on_delete = models.CASCADE)
	c_dishes = models.ManyToManyField(Product, blank = True, related_name = 'Related_cart')
	total_dishes = models.PositiveIntegerField(default = 0)
	final_price = models.DecimalField(max_digits = 9, default = 0, decimal_places = 2, verbose_name = "Total Price")
	in_order = models.BooleanField(default = False)
	for_anonimous_user = models.BooleanField(default = False)
	def __str__(self):
		return str(self.id)"""

class Comment(models.Model):



	is_visible = models.BooleanField(default=True)

	com = models.TextField(verbose_name='Comment')

	def __str__(self):
		return str(self.id)

class Order(models.Model):

	c_dishes = models.ManyToManyField(Dish, blank = True, related_name = 'Related_cart')
	in_order = models.BooleanField(default = False)
	addition = models.TextField(default = "", verbose_name='Comment')
	def __str__(self):
		return str(self.id)