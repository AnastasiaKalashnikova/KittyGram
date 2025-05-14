# urls.py
from rest_framework.routers import DefaultRouter # type: ignore
 
from django.urls import include, path # type: ignore

from cats.views import CatViewSet, OwnerViewSet


router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 