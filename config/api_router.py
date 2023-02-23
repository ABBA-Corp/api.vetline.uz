from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from vetline.faqs.views import FaqViewset
from vetline.products.views import ProductViewSet, ProductCategoryListView, ProductResultsListView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("products", ProductViewSet)
router.register("results", ProductResultsListView)
router.register("categories", ProductCategoryListView)
router.register("faqs", FaqViewset)

app_name = "api"
urlpatterns = router.urls
