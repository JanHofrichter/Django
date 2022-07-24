from django.db import models


class AttributeName(models.Model):
    DoesNotExist = None
    id = models.IntegerField(primary_key=True)
    objects = None
    nazev = models.CharField(max_length=200, blank=True)
    kod = models.CharField(max_length=200, blank=True)
    zobrazit = models.BooleanField(default=False)


class AttributeValue(models.Model):
    DoesNotExist = None
    id = models.IntegerField(primary_key=True)
    objects = None
    hodnota = models.CharField(max_length=200, blank=True)


class Attribute(models.Model):
    DoesNotExist = None
    id = models.IntegerField(primary_key=True)
    objects = None
    hodnota_atributu_id = models.IntegerField(null=True)
    nazev_atributu_id = models.IntegerField(blank=True)


class Product(models.Model):
    DoesNotExist = None
    objects = None
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    cena = models.CharField(max_length=200, blank=True)
    mena = models.CharField(max_length=200, blank=True)
    published_on = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)


class ProductAttributes(models.Model):
    DoesNotExist = None
    objects = None
    id = models.IntegerField(primary_key=True)
    attribute = models.IntegerField(blank=True)
    product = models.IntegerField(blank=True)


class Image(models.Model):
    DoesNotExist = None
    objects = None
    id = models.IntegerField(primary_key=True)
    obrazek = models.URLField(blank=True)
    nazev = models.CharField(max_length=200, blank=True)


class ProductImage(models.Model):
    DoesNotExist = None
    objects = None
    id = models.IntegerField(primary_key=True)
    product = models.IntegerField(blank=True)
    obrazek_id = models.IntegerField(blank=True)
    nazev = models.CharField(max_length=200, blank=True)


class Catalog(models.Model):
    DoesNotExist = None
    objects = None
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=200, blank=True)
    obrazek_id = models.IntegerField(blank=True, null=True)
    #products_ids = models.JSONField(blank=True, null=True)
    #attributes_ids = models.JSONField(blank=True, null=True)


# class Extend(models.Model):
#     products_ids = models.ManyToManyField(Catalog, blank=True, related_name="product_ids")
#     attributes_ids = models.ManyToManyField(Catalog, blank=True, related_name="attributes_ids")
