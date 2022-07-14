from django.urls import path
from . import views

urlpatterns = [
    # AttributeName
    path("detail/AttributeName/", views.attribute_name_det),
    path("detail/AttributeName/<str:pk>/", views.Attribute_name_det_id),
    # AttributeValue
    path("detail/AttributeValue/", views.attribute_value_det),
    path("detail/AttributeValue/<str:pk>/", views.attribute_value_det_id),
    # Attribute
    path("detail/Attribute/", views.attribute_det),
    path("detail/Attribute/<str:pk>/", views.attribute_det_id),
    # Product
    path("detail/Product/", views.product_det),
    path("detail/Product/<str:pk>/", views.product_det_id),
    # ProductAttributes
    path("detail/ProductAttributes/", views.product_attributes_det),
    path("detail/ProductAttributes/<str:pk>/", views.product_attributes_det_id),
    # Image
    path("detail/Image/", views.image_det),
    path("detail/Image/<str:pk>/", views.image_det_id),
    # ProductImage
    path("detail/ProductImage/", views.product_image_det),
    path("detail/ProductImage/<str:pk>/", views.product_image_det_id),
    # Catalog
    path("detail/Catalog/", views.catalog_det),
    path("detail/Catalog/<str:pk>/", views.catalog_det_id),
    # import
    path("import/", views.post_data),
]
