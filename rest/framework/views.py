from django.shortcuts import render
from django.http import JsonResponse, response

from rest_framework.decorators import api_view #this is restframework feature
from rest_framework.response import Response



from .serializers import taskSerializer

from .models import task

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)


@api_view(['GET'])
def tasklist(request):
    tasks = task.objects.all()
    serializer = taskSerializer(tasks, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def taskdetail(request,pk):
    tasks = task.objects.get(id=pk)
    serializer = taskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request,pk):
    serializer = taskSerializer(data=request.data)
    if serializer.is_valid():
	    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskupdate(request, pk):
	tasks = task.objects.get(id=pk)
	serializer = taskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskdelete(request, pk):
	tasks = task.objects.get(id=pk)
	tasks.delete()

	return Response('Item succsesfully delete!')

    

	





# Create your views here.
