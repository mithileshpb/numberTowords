from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .utils import convert_number_to_words_util
from .serializers import NumberSerializer
from rest_framework.response import Response

@api_view(['POST'])
def convert_number_to_words_view(request):
    if request.method == 'POST':
        serializer = NumberSerializer(data=request.data)
        if serializer.is_valid():
            number = serializer.validated_data['number']
            language = serializer.validated_data.get('language', 'en')
            words = convert_number_to_words_util(number, language)
            return Response({'words': words}, status=200)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)
@api_view()
def also_known(request):
    return Response({"1 Million = 10 Lakh",
                     "1 Billion = 100 crore",
                     "1 Trillion = 100 Arab"})