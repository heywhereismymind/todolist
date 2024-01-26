from .views import TaskViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = router.urls
