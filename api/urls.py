from django.urls import path
from . import views

urlpatterns = [
    # AttributeName
    path('detail/AttributeName/', views.AttributeNameGet),
    path('detail/AttributeName/<str:pk>/', views.AttributeNameGetDet),

    # AttributeValue
    path('detail/AttributeValue/', views.AttributeValueGet),
    path('detail/AttributeValue/<str:pk>/', views.AttributeValueGetDet),

    # Attribute
    path('detail/Attribute/', views.AttributeGet),
    path('detail/Attribute/<str:pk>/', views.AttributeGetDet),

    # Product
    path('detail/Product/', views.ProductGet),
    path('detail/Product/<str:pk>/', views.ProductGetDet),

    # ProductAttributes
    path('detail/ProductAttributes/', views.ProductAttributesGet),
    path('detail/ProductAttributes/<str:pk>/', views.ProductAttributesGetDet),

    # Image
    path('detail/Image/', views.ImageGet),
    path('detail/Image/<str:pk>/', views.ImageGetDet),

    # ProductImage
    path('detail/ProductImage/', views.ProductImageGet),
    path('detail/ProductImage/<str:pk>/', views.ProductImageGetDet),

    # Catalog
    path('detail/Catalog/', views.CatalogGet),
    path('detail/Catalog/<str:pk>/', views.CatalogGetDet),

    # import
    path('import/', views.post_data),

]
