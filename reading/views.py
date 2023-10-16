from .models import Reading
from django.http import HttpResponseRedirect 
from django.http import JsonResponse
from .serializers import ElpaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import ReadingForm
from django.shortcuts import render



@api_view(['GET', 'POST'])
def reading_list(request):
    # get all Reading 
    # serialize them
    # return json
    if request.method == 'GET':
        
        reading=Reading.objects.all()
        serializer =ElpaSerializer(reading, many=True)
        return JsonResponse({'reading':serializer.data})
    if request.method == 'POST':
        serializer=ElpaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
def add_reading(request):
    submitted = False
    form = ReadingForm
    if request.method == "POST":
        form = ReadingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_reading?submitted=True')
        else:
            form= ReadingForm
            if 'submitted' in request.GET:
                submitted=True
        return render(request,'add_reading.html',{"form":form, 'submitted':submitted})
            
    return render(request, 'add_reading.html',{'form':form})

def view_reading(request):
    readings =Reading.objects.all()
    
    return render(request,'table.html',{'read':readings})

    