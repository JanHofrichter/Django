from django.db import models


class AttributeName(models.Model):
    id = models.IntegerField(primary_key=True)
    objects = None
    nazev = models.CharField(max_length=200, blank=True)
    kod = models.CharField(max_length=200, blank=True)
    zobrazit = models.BooleanField(default=False)

    def __str__(self):
        return self


class AttributeValue(models.Model):
    id = models.IntegerField(primary_key=True)
    objects = None
    hodnota = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self


class Attribute(models.Model):
    id = models.IntegerField(primary_key=True)
    objects = None
    hodnota_atributu_id = models.IntegerField()
    nazev_atributu_id = models.IntegerField()

    def __str__(self):
        return self


class Product(models.Model):
    objects = None
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    cena = models.CharField(max_length=200, blank=False)
    mena = models.CharField(max_length=200, blank=True)
    published_on = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(blank=True)

    def __str__(self):
        return self


class ProductAttributes(models.Model):
    objects = None
    id = models.IntegerField(primary_key=True)
    attribute = models.IntegerField(blank=False)
    product = models.IntegerField(blank=False)

    def __str__(self):
        return self


class Image(models.Model):
    objects = None
    id = models.IntegerField(primary_key=True)
    obrazek = models.URLField(blank=False)
    nazev = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self


class ProductImage(models.Model):
    objects = None
    id = models.IntegerField(primary_key=True)
    product = models.IntegerField(blank=False)
    obrazek_id = models.IntegerField(blank=False)
    nazev = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self


class Catalog(models.Model):
    objects = None
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=200, blank=True)
    obrazek_id = models.IntegerField(blank=True, null=True)
    products_ids = models.JSONField(blank=True, null=True)
    attributes_ids = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self

