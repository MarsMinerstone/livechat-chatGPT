from django.shortcuts import render
#from orders.models import Dishes
from rest_framework.viewsets import ModelViewSet
#from orders.serializers import OrderSerializer

"""
def orders_page(request):
	return render(request, 'index.html', {'orders': Dishes.objects.all()})

class OrderView(ModelViewSet):
	queryset = Dishes.objects.all()
	serializer_class = OrderSerializer

def orders_app(request):
	return render(request, 'main_app.html')
	"""