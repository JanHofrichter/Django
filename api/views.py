from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *


# AttributeName
@api_view(["GET"])
def detail_model(request, model):
    specific = model.lower()
    if specific == 'attributename':
        data = AttributeName.objects.all()
        serializer = AttributeNames(data, many=True)
        return Response(serializer.data)

    elif specific == 'attributevalue':
        data = AttributeValue.objects.all()
        serializer = AttributeValues(data, many=True)
        return Response(serializer.data)

    elif specific == 'attribute':
        data = Attribute.objects.all()
        serializer = Attributes(data, many=True)
        return Response(serializer.data)

    elif specific == 'product':
        data = Product.objects.all()
        serializer = Products(data, many=True)
        return Response(serializer.data)

    elif specific == 'productattributes':
        data = ProductAttributes.objects.all()
        serializer = ProductAttributess(data, many=True)
        return Response(serializer.data)

    elif specific == 'image':
        data = Image.objects.all()
        serializer = Images(data, many=True)
        return Response(serializer.data)

    elif specific == 'productimage':
        data = ProductImage.objects.all()
        serializer = ProductImages(data, many=True)
        return Response(serializer.data)

    elif specific == 'catalog':
        data = Catalog.objects.all()
        serializer = Catalogs(data, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def detail_model_id(request, model, pk):
    specific = model.lower()
    if specific == 'attributename':
        try:
            data = AttributeName.objects.get(id=pk)
        except AttributeName.DoesNotExist:
            return Response("This object does not exist")
        serializer = AttributeNames(data, many=False)
        return Response(serializer.data)

    elif specific == 'attributevalue':
        try:
            data = AttributeValue.objects.get(id=pk)
        except AttributeValue.DoesNotExist:
            return Response("This object does not exist")
        serializer = AttributeValues(data, many=False)
        return Response(serializer.data)

    elif specific == 'attribute':
        try:
            data = Attribute.objects.get(id=pk)
        except Attribute.DoesNotExist:
            return Response("This object does not exist")
        serializer = Attributes(data, many=False)
        return Response(serializer.data)

    elif specific == 'product':
        try:
            data = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response("This object does not exist")
        serializer = Products(data, many=False)
        return Response(serializer.data)

    elif specific == 'productattributes':
        try:
            data = ProductAttributes.objects.get(id=pk)
        except ProductAttributes.DoesNotExist:
            return Response("This object does not exist")
        serializer = ProductAttributess(data, many=False)
        return Response(serializer.data)

    elif specific == 'image':
        try:
            data = Image.objects.get(id=pk)
        except Image.DoesNotExist:
            return Response("This object does not exist")
        serializer = Images(data, many=False)
        return Response(serializer.data)

    elif specific == 'productimage':
        try:
            data = ProductImage.objects.get(id=pk)
        except ProductImage.DoesNotExist:
            return Response("This object does not exist")
        serializer = ProductImages(data, many=False)
        return Response(serializer.data)

    elif specific == 'catalog':
        try:
            data = Catalog.objects.get(id=pk)
        except Catalog.DoesNotExist:
            return Response("This object does not exist")
        serializer = Catalogs(data, many=False)
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
    serializer_an = AttributeNames(data=collect_attributes_by_id(final_an), many=True)
    serializer_an.is_valid(raise_exception=True)
    serializer_an.save()

    # Save final_av in AttributeValue
    serializer_av = AttributeValues(data=collect_attributes_by_id(final_av), many=True)
    serializer_av.is_valid(raise_exception=True)
    serializer_av.save()

    # Save final_a in Attribute
    serializer_a = Attributes(data=collect_attributes_by_id(final_a), many=True)
    serializer_a.is_valid(raise_exception=True)
    serializer_a.save()

    # Save final_p in Product
    serializer_p = Products(data=collect_attributes_by_id(final_p), many=True)
    serializer_p.is_valid(raise_exception=True)
    serializer_p.save()

    # Save final_pa in ProductAttributes
    serializer_pa = ProductAttributess(data=collect_attributes_by_id(final_pa), many=True)
    serializer_pa.is_valid(raise_exception=True)
    serializer_pa.save()

    # Save final_i in Image
    serializer_i = Images(data=collect_attributes_by_id(final_i), many=True)
    serializer_i.is_valid(raise_exception=True)
    serializer_i.save()

    # Save final_pi in ProductImage
    serializer_pi = ProductImages(data=collect_attributes_by_id(final_pi), many=True)
    serializer_pi.is_valid(raise_exception=True)
    serializer_pi.save()

    # Save final_c in Catalog
    serializer_c = Catalogs(data=collect_attributes_by_id(final_c), many=True)
    serializer_c.is_valid(raise_exception=True)
    serializer_c.save()

    return Response("Import done")
