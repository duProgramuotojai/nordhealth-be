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
	# path('products/', ProductsView.as_view(), name="products"),
	path('api-auth/', include('rest_framework.urls'))
]
