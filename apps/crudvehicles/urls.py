from rest_framework import routers

from apps.crudvehicles.apiviews import AutoMakerView, VehicleModelView

app_name = 'vehicles'
router = routers.DefaultRouter()
router.register(r'auto-makers', AutoMakerView, base_name='AutoMaker')
router.register(r'vehicles-models', VehicleModelView, base_name='VehicleModel')

urlpatterns = router.urls
