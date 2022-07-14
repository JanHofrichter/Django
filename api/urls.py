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

    path('detail/Product/', views.ProductGet),
    path('detail/Product/<str:pk>/', views.ProductGetDet),

    path('detail/ProductAttributes/', views.ProductAttributesGet),
    path('detail/ProductAttributes/<str:pk>/', views.ProductAttributesGetDet),

    path('detail/Image/', views.ImageGet),
    path('detail/Image/<str:pk>/', views.ImageGetDet),

    path('detail/ProductImage/', views.ProductImageGet),
    path('detail/ProductImage/<str:pk>/', views.ProductImageGetDet),

    path('detail/Catalog/', views.CatalogGet),
    path('detail/Catalog/<str:pk>/', views.CatalogGetDet),

    path('import/', views.PostData),

]
