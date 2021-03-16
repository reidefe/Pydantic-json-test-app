from django.urls import path, include
from testApp import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"actor", views.ActorViewSet)

router.register(r"film", views.FilmViewSet)

urlpatterns = [path("", include(router.urls))]
