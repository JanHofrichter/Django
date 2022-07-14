from rest_framework import serializers
from .models import AttributeValue
from .models import AttributeName
from .models import Attribute
from .models import Product
from .models import ProductAttributes
from .models import Image
from .models import ProductImage
from .models import Catalog


class AttributeNameS(serializers.ModelSerializer):
    class Meta:
        model = AttributeName
        fields = '__all__'


class AttributeValueS(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = '__all__'

class AttributeS(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'


class ProductS(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductAttributesS(serializers.ModelSerializer):
    objects = None

    class Meta:
        model = ProductAttributes
        fields = '__all__'


class ImageS(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductImageS(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class CatalogS(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'
