from rest_framework import routers
from registerApp.views import *


router = routers.DefaultRouter()

router.register(r'user', UserViewSet)