from django.urls import path
from . import views

urlpatterns = [
    #AttributeName
    path('detail/AttributeName/', views.AttributeNameGet),
    path('detail/AttributeName/<str:pk>/', views.AttributeNameGetDet),
    #AttributeValue
    path('detail/AttributeValue/', views.AttributeValueGet),
    path('detail/AttributeValue/<str:pk>/', views.AttributeValueGetDet),
	#Attribute
    path('detail/Attribute/', views.AttributeGet),
    path('detail/Attribute/<str:pk>/', views.AttributeGetDet),

    path('import/', views.PostData),


]
