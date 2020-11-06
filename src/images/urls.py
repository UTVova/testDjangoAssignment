from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from .views import ImageViewSet

router = DefaultRouter()
router.register("images", ImageViewSet, basename="images")
urlpatterns = [path("", TemplateView.as_view(template_name="image_uploading.html")), path("api/", include(router.urls))]
