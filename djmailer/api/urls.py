
from django.db import router
from django.urls import path,include

from .views import HelloWorldView,HelloFBVAPIView,SubscriberView,SubscriberRetrieveUpdateDestroyView, SubscriberViewSet,login

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('subscribers',SubscriberViewSet)

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name="hello_world"),
    path('fbv/',HelloFBVAPIView,name="fbv_hello"),
    path('subscriber/',SubscriberView.as_view(),name = "subscriber_view"),
    path('subscriberdetail/<int:id>/',SubscriberRetrieveUpdateDestroyView.as_view(),name = "detail_subscriber"),

    path('', include(router.urls)),
    path('login/',login),
] 


# SubscriberViewSet.as_view({'get': 'list', 'post':'create'}) # For: /api/subscriber
# SubscriberViewSet.as_view({'get': 'retrieve', 'put':'update'}) # For: /api/subscriber/1
