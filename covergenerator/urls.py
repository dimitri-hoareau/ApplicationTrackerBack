from django.urls import path, include
from rest_framework.routers import DefaultRouter
from covergenerator.views import ApplicationViewSet

router = DefaultRouter()
router.register(r'applications', ApplicationViewSet, basename='applications')

urlpatterns = [
    path('', include(router.urls)),
]
