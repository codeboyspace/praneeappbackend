from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import uuid
import os
from django.core.files.storage import default_storage

# Store uploaded files temporarily
UPLOADS = {}

@csrf_exempt
def generate_qr(request):
    upload_id = str(uuid.uuid4())
    UPLOADS[upload_id] = None
    return JsonResponse({"upload_id": upload_id})

UPLOADS = {}

@csrf_exempt
def upload_photo(request, upload_id):
    if request.method == "POST":
        if "photo" not in request.FILES:
            return JsonResponse({"error": "No file part"}, status=400)

        photo = request.FILES["photo"]
        file_path = os.path.join('media', photo.name)
        if not os.path.exists('media'):
            os.makedirs('media')  # ✅ Create 'media' directory if it doesn't exist

        default_storage.save(file_path, photo)
        UPLOADS[upload_id] = f"/media/{photo.name}"
        return JsonResponse({"success": True, "photo_url": UPLOADS[upload_id]})

    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def get_uploaded_photo(request, upload_id):
    try:
        photo_url = UPLOADS.get(upload_id)
        if photo_url:
            # Assuming photo_url is something like 'media/filename.jpg'
            full_photo_url = f"https://praneeappbackend.onrender.com/media/media/{photo_url.split('/')[-1]}"
            return JsonResponse({"photo_url": full_photo_url})
        return JsonResponse({"error": "Photo not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
