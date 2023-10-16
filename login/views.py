from .models import Auth
from django.http import HttpResponseRedirect 
from django.http import JsonResponse
from .serializers import AuthSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def login(request):
    # get all Reading 
    # serialize them
    # return json
    if request.method == 'GET':
        
        auth=Auth.objects.all()
        serializer =AuthSerializer(auth, many=True)
        return JsonResponse({'auth':serializer.data})
