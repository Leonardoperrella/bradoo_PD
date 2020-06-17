from bradoo.core.views import VendorsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('vendors', VendorsViewSet)