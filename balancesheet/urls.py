from rest_framework import routers
from .api import BalanceViewSet

app_name = 'balancesheet'
router = routers.DefaultRouter()
router.register('api/balance', BalanceViewSet, 'tasks')

urlpatterns = router.urls