from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from blog.views import BlogPostListView
from catalog.apps import CatalogConfig
from catalog.views import (
    CategoryListView,
    ContactsView,
    HomeView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductsByCategoryListView,
    ProductUpdateView,
)

app_name = CatalogConfig.name


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path(
        "product/<int:pk>/",
        cache_page(60)(ProductDetailView.as_view()),
        name="product_details",
    ),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("blog/", BlogPostListView.as_view(), name="blog_list"),
    path(
        "product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"
    ),
    path(
        "product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("category/", CategoryListView.as_view(), name="category"),
    path(
        "category/<str:category_name>/",
        ProductsByCategoryListView.as_view(),
        name="products_by_category",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
