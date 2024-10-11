from django.db.models import BooleanField
from django.forms import ModelForm, ValidationError

from catalog.models import Product, Version

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар',]


class StyleFormMixin:
    """Стилизация форм"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                #field.widget.attrs['class'] = 'form-check-input'
                ...
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

        def clean_name(self):
            clean_data = self.cleaned_data['name']

            for word in FORBIDDEN_WORDS:
                if word in clean_data:
                    raise ValidationError(f'Нельзя использовать слово {word} в названии')

            return clean_data

        def clean_description(self):
            clean_data = self.cleaned_data['description']

            for word in FORBIDDEN_WORDS:
                if word in clean_data:
                    raise ValidationError(f'Нельзя использовать слово {word} в описании')

            return clean_data


class VersionForms(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'