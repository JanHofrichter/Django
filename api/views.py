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
@api_view(["GET"])
def attribute_name_det(request):
    data = AttributeName.objects.all()
    serializer = AttributeNameS(data, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def Attribute_name_det_id(request, pk):
    data = AttributeName.objects.get(id=pk)
    serializer = AttributeNameS(data, many=False)
    return Response(serializer.data)


# AttributeValue
@api_view(["GET"])
def attribute_value_det(request):
    data = AttributeValue.objects.all()
    serializer = AttributeValueS(data, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def attribute_value_det_id(request, pk):
    data = AttributeValue.objects.get(id=pk)
    serializer = AttributeValueS(data, many=False)
    return Response(serializer.data)


# Attribute
@api_view(["GET"])
def attribute_det(request):
    data = Attribute.objects.all()
    serializer = AttributeS(data, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def attribute_det_id(request, pk):
    data = Attribute.objects.get(id=pk)
    serializer = AttributeS(data, many=False)
    return Response(serializer.data)


# Product
@api_view(["GET"])
def product_det(request):
    data = Product.objects.all()
    serializer = ProductS(data, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def product_det_id(request, pk):
    data = Product.objects.get(id=pk)
    serializer = ProductS(data, many=False)
    return Response(serializer.data)


# ProductAttributes
@api_view(["GET"])
def product_attributes_det(request):
    data = ProductAttributes.objects.all()
    serializer = ProductAttributesS(data, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def product_attributes_det_id(request, pk):
    data = ProductAttributes.objects.get(id=pk)
    serializer = ProductAttributesS(data, many=False)
    return Response(serializer.data)


# Image
@api_view(["GET"])
def image_det(request):
    data = Image.objects.all()
    serializer = ImageS(data, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def image_det_id(request, pk):
    data = Image.objects.get(id=pk)
    serializer = ImageS(data, many=False)
    return Response(serializer.data)


# ProductImage
@api_view(["GET"])
def product_image_det(request):
    data = ProductImage.objects.all()
    serializer = ProductImageS(data, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def product_image_det_id(request, pk):
    data = ProductImage.objects.get(id=pk)
    serializer = ProductImageS(data, many=False)
    return Response(serializer.data)


# Catalog
@api_view(["GET"])
def catalog_det(request):
    data = Catalog.objects.all()
    serializer = CatalogS(data, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def catalog_det_id(request, pk):
    data = Catalog.objects.get(id=pk)
    serializer = CatalogS(data, many=False)
    return Response(serializer.data)


# Merge attributes with same id
def collect_attributes_by_id(input_data):
    dictionary = {item["id"]: item for item in input_data}
    for element in input_data:
        dictionary[element["id"]].update(element)
    return list(dictionary.values())


@api_view(["POST"])
def post_data(request):
    final_an: list = []
    final_av: list = []
    final_a: list = []
    final_p: list = []
    final_pa: list = []
    final_i: list = []
    final_pi: list = []
    final_c: list = []

    # Check if data format is valid
    if not ((type(request.data) == list) and (type(request.data[0]) == dict)):
        return Response("Invalid request; wrong data posted!")
    data = request.data

    # divide element in several models
    for element in data:
        if "AttributeName" in element:
            final_an.append(element["AttributeName"])

        elif "AttributeValue" in element:
            final_av.append(element["AttributeValue"])

        elif "Attribute" in element:
            final_a.append(element["Attribute"])

        elif "Product" in element:
            final_p.append(element["Product"])

        elif "ProductAttributes" in element:
            final_pa.append(element["ProductAttributes"])

        elif "Image" in element:
            final_i.append(element["Image"])

        elif "ProductImage" in element:
            final_pi.append(element["ProductImage"])

        elif "Catalog" in element:
            final_c.append(element["Catalog"])

    # Save final_an in AttributeName
    serializer_an = AttributeNameS(data=collect_attributes_by_id(final_an), many=True)
    serializer_an.is_valid(raise_exception=True)
    serializer_an.save()

    # Save final_av in AttributeValue
    serializer_av = AttributeValueS(data=collect_attributes_by_id(final_av), many=True)
    serializer_av.is_valid(raise_exception=True)
    serializer_av.save()

    # Save final_a in Attribute
    serializer_a = AttributeS(data=collect_attributes_by_id(final_a), many=True)
    serializer_a.is_valid(raise_exception=True)
    serializer_a.save()

    # Save final_p in Product
    serializer_p = ProductS(data=collect_attributes_by_id(final_p), many=True)
    serializer_p.is_valid(raise_exception=True)
    serializer_p.save()

    # Save final_pa in ProductAttributes
    serializer_pa = ProductAttributesS(
        data=collect_attributes_by_id(final_pa), many=True
    )
    serializer_pa.is_valid(raise_exception=True)
    serializer_pa.save()

    # Save final_i in Image
    serializer_i = ImageS(data=collect_attributes_by_id(final_i), many=True)
    serializer_i.is_valid(raise_exception=True)
    serializer_i.save()

    # Save final_pi in ProductImage
    serializer_pi = ProductImageS(data=collect_attributes_by_id(final_pi), many=True)
    serializer_pi.is_valid(raise_exception=True)
    serializer_pi.save()

    # Save final_c in Catalog
    serializer_c = CatalogS(data=collect_attributes_by_id(final_c), many=True)
    serializer_c.is_valid(raise_exception=True)
    serializer_c.save()

    return Response("Import done")
