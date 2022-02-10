# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers, views

# import everything from views
from .views import *

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'geeks', GeeksViewSet)
router.register(r'products', ProductsViewSet)

# specify URL Path for rest_framework
urlpatterns = [
	path('', include(router.urls)),

	path('geeks/<int:geek_id>/add-to-cart', GeeksViewSet.as_view({'post': 'add_to_cart'}), name="geeks_view_set"),
	path('geeks/<int:geek_id>/remove-from-cart', GeeksViewSet.as_view({'post': 'remove_from_cart'}), name="geeks_view_set"),

	path('api-auth/', include('rest_framework.urls')),
]
