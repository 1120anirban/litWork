from rest_framework import routers
from .api import LitWorkViewSet

router = routers.DefaultRouter()
router.register('api/litWorks', LitWorkViewSet, 'litWorks')

urlpatterns = router.urls