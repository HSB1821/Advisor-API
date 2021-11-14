from django.urls import include,path
from rest_framework import routers
from Experimental_API.views import AdvisorViewSet, UserViewSet,BookingViewSet

router = routers.DefaultRouter()
router.register(r'Advisor', AdvisorViewSet)
router.register(r'User', UserViewSet)
router.register(r'Booking', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
