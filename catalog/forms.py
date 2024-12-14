import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Category, Product

forbidden_words = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "photo",
            "category",
            "purchase_price",
            "created_at",
        ]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Укажите наименования продукта",  # Текст подсказки внутри поля
            }
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Добавьте описание продукта"}
        )
        self.fields["photo"].widget.attrs.update({"class": "form-control"})
        self.fields["category"].widget.attrs.update({"class": "form-control"})
        self.fields["purchase_price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Укажите цену"}
        )
        self.fields["created_at"].widget.attrs.update(
            {"class": "form-control", "placeholder": datetime.date.today().isoformat()}
        )

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if any(word in name.lower() for word in forbidden_words):
            raise ValidationError("Название не должно содержать запрещенные слова.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if any(word in description.lower() for word in forbidden_words):
            raise ValidationError("Название не должно содержать запрещенные слова.")
        return description

    def clean_price(self):
        price = self.cleaned_data.get("purchase_price")
        if price < 0:
            raise ValidationError("Неверная цена")
        return price

    def clean_photo(self):
        image = self.cleaned_data.get("photo")
        if image:
            if image.size > 5 * 1024 * 1025:
                raise ValidationError("Файл больше 5МБ")
            if not (
                image.name.endswith(".jpg")
                or image.name.endswith(".jpeg")
                or image.name.endswith(".png")
            ):
                raise ValidationError("Файл не допустимого формата")
        return image


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]

class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['publication_status']