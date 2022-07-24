from rest_framework import serializers
from .models import *


class AttributeNames(serializers.ModelSerializer):
    # nazev = serializers.CharField(source='name')
    # kod = serializers.CharField(source='code')
    # zobrazit = serializers.BooleanField(source='show')

    class Meta:
        model = AttributeName
        fields = "__all__"
            #('id', 'nazev', 'kod', 'zobrazit')


class AttributeValues(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = "__all__"


class Attributes(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = "__all__"


class Products(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductAttributess(serializers.ModelSerializer):
    objects = None

    class Meta:
        model = ProductAttributes
        fields = "__all__"


class Images(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class ProductImages(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class Catalogs(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = "__all__"
