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


# import json


# AttributeName
@api_view(['GET'])
def AttributeNameGet(request):
    object = AttributeName.objects.all()
    serializer = AttributeNameS(object, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def AttributeNameGetDet(request, pk):
    object = AttributeName.objects.get(id=pk)
    serializer = AttributeNameS(object, many=False)
    return Response(serializer.data)


# AttributeValue

@api_view(['GET'])
def AttributeValueGet(request):
    object = AttributeValue.objects.all()
    serializer = AttributeValueS(object, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def AttributeValueGetDet(request, pk):
    object = AttributeValue.objects.get(id=pk)
    serializer = AttributeValueS(object, many=False)
    return Response(serializer.data)


# Attribute
@api_view(['GET'])
def AttributeGet(request):
    object = Attribute.objects.all()
    serializer = AttributeS(object, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def AttributeGetDet(request, pk):
    object = Attribute.objects.get(id=pk)
    serializer = AttributeS(object, many=False)
    return Response(serializer.data)


# Product

@api_view(['GET'])
def ProductGet(request):
    object = Product.objects.all()
    serializer = ProductS(object, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ProductGetDet(request, pk):
    object = Product.objects.get(id=pk)
    serializer = ProductS(object, many=False)
    return Response(serializer.data)


# ProductAttributes

@api_view(['GET'])
def ProductAttributesGet(request):
    object = ProductAttributes.objects.all()
    serializer = ProductAttributesS(object, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ProductAttributesGetDet(request, pk):
    object = ProductAttributes.objects.get(id=pk)
    serializer = ProductAttributesS(object, many=False)
    return Response(serializer.data)


# Image

@api_view(['GET'])
def ImageGet(request):
    object = Image.objects.all()
    serializer = ImageS(object, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ImageGetDet(request, pk):
    object = Image.objects.get(id=pk)
    serializer = ImageS(object, many=False)
    return Response(serializer.data)


# ProductImage

@api_view(['GET'])
def ProductImageGet(request):
    object = ProductImage.objects.all()
    serializer = ProductImageS(object, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ProductImageGetDet(request, pk):
    object = ProductImage.objects.get(id=pk)
    serializer = ProductImageS(object, many=False)
    return Response(serializer.data)


# Catalog

@api_view(['GET'])
def CatalogGet(request):
    object = Catalog.objects.all()
    serializer = CatalogS(object, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def CatalogGetDet(request, pk):
    object = Catalog.objects.get(id=pk)
    serializer = CatalogS(object, many=False)
    return Response(serializer.data)


#
@api_view(['POST'])
@parser_classes([JSONParser])
def PostData(request):
    finalAN: list = []
    finalAV: list = []
    finalA: list = []
    finalP: list = []
    finalPA: list = []
    finalI: list = []
    finalPI: list = []
    finalC: list = []

    data = request.data

    for object in data:
        if "AttributeName" in object:
            finalAN.append(object['AttributeName'])

        elif "AttributeValue" in object:
            finalAV.append(object['AttributeValue'])

        elif "Attribute" in object:
            finalA.append(object['Attribute'])

        elif "Product" in object:
            finalP.append(object['Product'])

        elif "ProductAttributes" in object:
            finalPA.append(object['ProductAttributes'])

        elif "Image" in object:
            finalI.append(object['Image'])

        elif "ProductImage" in object:
            finalPI.append(object['ProductImage'])

        elif "Catalog" in object:
            finalC.append(object['Catalog'])

    serializer1 = AttributeNameS(data=finalAN, many=True)
    serializer1.is_valid(raise_exception=True)
    serializer1.save()

    serializer2 = AttributeValueS(data=finalAV, many=True)
    serializer2.is_valid(raise_exception=True)
    serializer2.save()

    # django.db.utils.OperationalError: table api_attribute has no column named hodnota_atributu_id
    serializer3 = AttributeS(data=finalA, many=True)
    serializer3.is_valid(raise_exception=True)
    serializer3.save()

    serializer4 = ProductS(data=finalP, many=True)
    serializer4.is_valid(raise_exception=True)
    serializer4.save()
    # Field 'id' expected a number but got ()
    serializer5 = ProductAttributesS(data=finalPA, many=True)
    serializer5.is_valid(raise_exception=True)
    serializer5.save()

    serializer6 = ImageS(data=finalI, many=True)
    serializer6.is_valid(raise_exception=True)
    serializer6.save()

    serializer7 = ProductImageS(data=finalPI, many=True)
    serializer7.is_valid(raise_exception=True)
    serializer7.save()
    return Response("OK")
    # serializer8 = CatalogS(data=finalC, many=True)
    # serializer8.is_valid(raise_exception=True)
    # serializer8.save()
