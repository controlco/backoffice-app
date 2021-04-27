from property_manager.serializers import PropertySerializer
from rest_framework import viewsets
from property_manager.models import Property

# Create your views here.


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    # called when request POST
    def perform_create(self, serializer):
        print("CHAO")
        print(self.request.user)
        serializer.save(owner=self.request.user)
