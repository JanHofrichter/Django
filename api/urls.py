from django.urls import path
from . import views

urlpatterns = [
    # AttributeName
    path("detail/<str:model>/", views.detail_model),
    path("detail/<str:model>/<str:pk>/", views.detail_model_id),
    path("import/", views.post_data),
]
