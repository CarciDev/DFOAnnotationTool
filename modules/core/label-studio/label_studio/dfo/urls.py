# # dfo/urls.py
# from django.urls import path
# from .views import get_zoom_attributes

# app_name = 'dfo'

# urlpatterns = [
#     path('zoom/', get_zoom_attributes, name='get_zoom_attributes'),
# ]

# dfo/urls.py
from django.urls import path
from .views import ZoomDataDetail

urlpatterns = [
    path('zoomdata/', ZoomDataDetail.as_view(), name='zoomdata-detail'),
]