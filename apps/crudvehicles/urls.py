from rest_framework import routers

from apps.crudvehicles.apiviews import AutoMakerView

app_name = 'vehicles'
router = routers.DefaultRouter()
router.register(r'auto-makers', AutoMakerView, base_name='AutoMaker')


urlpatterns = router.urls