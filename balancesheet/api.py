from .models import BalanceSheet
from rest_framework import viewsets, permissions
from .serializers import BalanceSerializer


class BalanceViewSet(viewsets.ModelViewSet):
    queryset = BalanceSheet.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BalanceSerializer