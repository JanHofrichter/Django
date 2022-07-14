import json
import json.encoder
import os

from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AttributeNameS
from .models import AttributeName
from .serializers import AttributeValueS
from .models import AttributeValue
from .serializers import AttributeS
from .models import Attribute
from .serializers import ProductS
from .models import Product
from .serializers import ProductAttributesS
from .models import ProductAttributes
from .serializers import ImageS
from .models import Image
from .serializers import ProductImageS
from .models import ProductImage
from .serializers import CatalogS
from .models import Catalog


# AttributeName
@api_view(['GET'])
def AttributeNameGet(request):
    data = AttributeName.objects.all()
    serializer = AttributeNameS(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def AttributeNameGetDet(request, pk):
    data = AttributeName.objects.get(id=pk)
    serializer = AttributeNameS(data, many=False)
    return Response(serializer.data)


# AttributeValue
@api_view(['GET'])
def AttributeValueGet(request):
    data = AttributeValue.objects.all()
    serializer = AttributeValueS(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def AttributeValueGetDet(request, pk):
    data = AttributeValue.objects.get(id=pk)
    serializer = AttributeValueS(data, many=False)
    return Response(serializer.data)


# Attribute
@api_view(['GET'])
def AttributeGet(request):
    data = Attribute.objects.all()
    serializer = AttributeS(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def AttributeGetDet(request, pk):
    data = Attribute.objects.get(id=pk)
    serializer = AttributeS(data, many=False)
    return Response(serializer.data)


# Product
@api_view(['GET'])
def ProductGet(request):
    data = Product.objects.all()
    serializer = ProductS(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ProductGetDet(request, pk):
    data = Product.objects.get(id=pk)
    serializer = ProductS(data, many=False)
    return Response(serializer.data)


# ProductAttributes
@api_view(['GET'])
def ProductAttributesGet(request):
    data = ProductAttributes.objects.all()
    serializer = ProductAttributesS(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ProductAttributesGetDet(request, pk):
    data = ProductAttributes.objects.get(id=pk)
    serializer = ProductAttributesS(data, many=False)
    return Response(serializer.data)


# Image
@api_view(['GET'])
def ImageGet(request):
    data = Image.objects.all()
    serializer = ImageS(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ImageGetDet(request, pk):
    data = Image.objects.get(id=pk)
    serializer = ImageS(data, many=False)
    return Response(serializer.data)


# ProductImage
@api_view(['GET'])
def ProductImageGet(request):
    data = ProductImage.objects.all()
    serializer = ProductImageS(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ProductImageGetDet(request, pk):
    data = ProductImage.objects.get(id=pk)
    serializer = ProductImageS(data, many=False)
    return Response(serializer.data)


# Catalog
@api_view(['GET'])
def CatalogGet(request):
    data = Catalog.objects.all()
    serializer = CatalogS(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def CatalogGetDet(request, pk):
    data = Catalog.objects.get(id=pk)
    serializer = CatalogS(data, many=False)
    return Response(serializer.data)


def collect_attributes_by_id(x):
    data = x
    dict_1 = {item["id"]: item for item in data}
    for d in data:
        dict_1[d["id"]].update(d)
    return list(dict_1.values())


@api_view(['POST'])
def post_data(request):
    final_an: list = []
    final_av: list = []
    final_a: list = []
    final_p: list = []
    final_pa: list = []
    final_i: list = []
    final_pi: list = []
    final_c: list = []

    data = request.data

    for element in data:
        if "AttributeName" in element:
            final_an.append(element['AttributeName'])

        elif "AttributeValue" in element:
            final_av.append(element['AttributeValue'])

        elif "Attribute" in element:
            final_a.append(element['Attribute'])

        elif "Product" in element:
            final_p.append(element['Product'])

        elif "ProductAttributes" in element:
            final_pa.append(element['ProductAttributes'])

        elif "Image" in element:
            final_i.append(element['Image'])

        elif "ProductImage" in element:
            final_pi.append(element['ProductImage'])

        elif "Catalog" in element:
            final_c.append(element['Catalog'])

    # AttributeName
    serializer_an = AttributeNameS(data=collect_attributes_by_id(final_an), many=True)
    serializer_an.is_valid(raise_exception=True)
    serializer_an.save()

    # AttributeValue
    serializer_av = AttributeValueS(data=collect_attributes_by_id(final_av), many=True)
    serializer_av.is_valid(raise_exception=True)
    serializer_av.save()

    # Attribute
    serializer_a = AttributeS(data=collect_attributes_by_id(final_a), many=True)
    serializer_a.is_valid(raise_exception=True)
    serializer_a.save()

    # Product
    serializer_p = ProductS(data=collect_attributes_by_id(final_p), many=True)
    serializer_p.is_valid(raise_exception=True)
    serializer_p.save()

    # ProductAttributes
    serializer_pa = ProductAttributesS(data=collect_attributes_by_id(final_pa), many=True)
    serializer_pa.is_valid(raise_exception=True)
    serializer_pa.save()

    # Image
    serializer_i = ImageS(data=collect_attributes_by_id(final_i), many=True)
    serializer_i.is_valid(raise_exception=True)
    serializer_i.save()

    # ProductImage
    serializer_pi = ProductImageS(data=collect_attributes_by_id(final_pi), many=True)
    serializer_pi.is_valid(raise_exception=True)
    serializer_pi.save()

    # Catalog
    serializer_c = CatalogS(data=collect_attributes_by_id(final_c), many=True)
    serializer_c.is_valid(raise_exception=True)
    serializer_c.save()

    return Response("OK")
