from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.views import BlogPostListView
from catalog.apps import CatalogConfig


from catalog.views import HomeView, ContactsView, ProductDetailView


app_name = CatalogConfig.name


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_details"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("blog/", BlogPostListView.as_view(), name="blog_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
