from django.db import models


class Product(models.Model):
	name = models.CharField(max_length = 20)
	count = models.IntegerField()
	description = models.CharField(max_length = 255)
	#user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)

	def __str__(self):
		return self.name