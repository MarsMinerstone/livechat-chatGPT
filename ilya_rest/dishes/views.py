from django.shortcuts import render
from dishes.models import Dish


# Create your views here.
def index(request):
	dish = Dish.objects.all()
	return render(request, 'ilya_rest/index_dishes.html', {'dish': dish})