from django.db import models


class AttributeName(models.Model):
    DoesNotExist = None
    objects = None
    name = models.CharField(max_length=200, blank=True)
    code = models.CharField(max_length=200, blank=True)
    show = models.BooleanField(default=False)


class AttributeValue(models.Model):
    DoesNotExist = None
    objects = None
    hodnota = models.CharField(max_length=200, blank=True)


class Attribute(models.Model):
    DoesNotExist = None
    objects = None
    hodnota_atributu_id = models.IntegerField(blank=True, null=True)
    nazev_atributu_id = models.IntegerField(blank=True, null=True)


class Product(models.Model):
    DoesNotExist = None
    objects = None
    nazev = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    cena = models.CharField(max_length=200, blank=True)
    mena = models.CharField(max_length=200, blank=True)
    published_on = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)


class ProductAttributes(models.Model):
    DoesNotExist = None
    objects = None
    attribute = models.IntegerField(blank=True, null=True)
    product = models.IntegerField(blank=True, null=True)


class Image(models.Model):
    DoesNotExist = None
    objects = None
    obrazek = models.URLField(blank=True)
    nazev = models.CharField(max_length=200, blank=True)


class ProductImage(models.Model):
    DoesNotExist = None
    objects = None
    product = models.IntegerField(blank=True, null=True)
    obrazek_id = models.IntegerField(blank=True, null=True)
    nazev = models.CharField(max_length=200, blank=True)


#class Extend(models.Model):
    #products_ids = models.IntegerField()


class Catalog(models.Model):
    DoesNotExist = None
    objects = None
    nazev = models.CharField(max_length=200, blank=True)
    obrazek_id = models.IntegerField(blank=True, null=True)
    #products_ids = models.ForeignKey(Extend, on_delete=models.CASCADE, unique=True)
