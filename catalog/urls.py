from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig


from catalog.views import home, contacts, product_details


app_name = CatalogConfig.name


urlpatterns = [
    path("", home, name="home"),
    path("product/<int:pk>/", product_details, name="product_details"),
    path("contacts/", contacts, name="contacts"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
