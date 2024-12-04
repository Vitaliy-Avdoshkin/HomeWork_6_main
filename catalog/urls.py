from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig


from catalog.views import HomeView, contacts, ProductDetailView


app_name = CatalogConfig.name


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_details"),
    path("contacts/", contacts, name="contacts"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
