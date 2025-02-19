from django.urls import path
from .views import generate_qr, upload_photo, get_uploaded_photo

urlpatterns = [
    path('api/generate_qr/', generate_qr, name='generate_qr'),
    path('api/upload_photo/<str:upload_id>/', upload_photo, name='upload_photo'),
    path('api/get_uploaded_photo/<str:upload_id>/', get_uploaded_photo, name='get_uploaded_photo'),
]
