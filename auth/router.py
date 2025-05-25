from rest_framework import routers

from auth.views import UserViewSet

router = routers.SimpleRouter()
router.register('user', UserViewSet)