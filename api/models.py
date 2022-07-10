from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title


class AttributeName(models.Model):
    nazev = models.CharField(max_length=200)
    kod = models.CharField(max_length=200)
    zobrazit = models.BooleanField()


class AttributeValue(models.Model):
    hodnota = models.CharField(max_length=200)


class Attribute(models.Model):
    nazev_atributu_id = models.IntegerField()
    hodnota_atributu_id = id


class Product(models.Model):
    nazev = models.CharField(max_length=200)
    description = models.TextField()
    cena = models.CharField(max_length=200)
    mena = models.CharField(max_length=200)
    published_on = models.DateTimeField()
    is_published = models.BooleanField()


class ProductAttributes(models.Model):
    attribute = models.IntegerField()
    product = models.IntegerField()


class Image(models.Model):
    obrazek = models.ImageField()
    nazev = models.CharField(max_length=200)


class ProductImage(models.Model):
    product = models.IntegerField()
    obrazek_id = id
    nazev = models.CharField(max_length=200)


class Catalog(models.Model):
    nazev = models.CharField(max_length=200)
    obrazek_id = models.IntegerField()
    #products_ids = models.CommaSeparatedIntegerField()
    #attributes_ids = models.CommaSeparatedIntegerField()
