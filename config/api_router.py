from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from vetline.products.views import ProductViewSet, ProductCategoryListView, ProductBannerListView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("products", ProductViewSet)
router.register("banners", ProductBannerListView)
router.register("categories", ProductCategoryListView)

app_name = "api"
urlpatterns = router.urls
