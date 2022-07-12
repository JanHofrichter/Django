from django.urls import path
from . import views

urlpatterns = [
    # path('', views.apiOverview, name="api-overview"),
    #AttributeName
    path('detail/AttributeName/', views.AttributeNameGet),
    path('detail/AttributeName/<str:pk>/', views.AttributeNameGetDet),
    #AttributeValue
    path('detail/AttributeValue/', views.AttributeValueGet),
    path('detail/AttributeValue/<str:pk>/', views.AttributeValueGetDet),
	#Attribute
    path('detail/Attribute/', views.AttributeGet),
    path('detail/Attribute/<str:pk>/', views.AttributeGetDet),

    path('import/', views.AttributeNamePost),

    # path('task-detail/<str:name>/<str:pk>/', views.taskDetail, name="task-detail"),
    # path('allbyname/<str:name>/', views.allbyname, name="all tasks with name"),
    # path('task-create/', views.taskCreate, name="task-create"),
    # # path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    # path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
    # path('task-list/', views.taskList, name="task-list"),

]
