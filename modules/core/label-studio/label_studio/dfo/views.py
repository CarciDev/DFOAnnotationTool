# # views.py
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# from .models import ZoomAttributes
# from .serializers import ZoomAttributesSerializer

# @csrf_exempt
# def get_zoom_attributes(request):
#     if request.method == 'GET':
#         # # Replace with actual logic to get the zoom attributes
#         # zoom_attributes = {
#         #     'zooming_position_x': 100,  # Example value
#         #     'zooming_position_y': 200,  # Example value
#         #     'zoom_scale': 1.5,          # Example value
#         # }
#         zoom_attributes = ZoomAttributes.objects.all()
#         serializer = ZoomAttributesSerializer(zoom_attributes, many=True)
#         return JsonResponse(serializer.data)
#     return JsonResponse({'error': 'Invalid request'}, status=400)

# dfo/views.py
from rest_framework import generics
from .models import ZoomData
from .serializers import ZoomDataSerializer

class ZoomDataDetail(generics.RetrieveUpdateAPIView):
    queryset = ZoomData.objects.all()
    serializer_class = ZoomDataSerializer

    def get_object(self):
        # Ensure there's only one instance
        obj, created = ZoomData.objects.get_or_create(id=1)
        return obj