from rest_framework import viewsets
from rest_framework.serializers import Serializer
from .models import Product
from .serializer import ProductSerializer
# Create your views here.



class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("created_at")
    serializer_class = ProductSerializer
