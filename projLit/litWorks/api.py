from litWorks.models import LitWork
from rest_framework import viewsets, permissions
from .serializers import LitWorkSerializer

# LitWork Viewset
class LitWorkViewSet(viewsets.ModelViewSet):
    queryset = LitWork.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LitWorkSerializer