from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .serializers import Serializ
from .models import Task


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk, name):
    #tasks = Task.objects.get(id=pk).get(title=name)
    tasks = Task.objects.all().get(title=name)
    tasks2 = tasks.get(id=pk)
    serializer = TaskSerializer(tasks2, many=False)
    return Response(serializer.data)


#vraci jen 1 polozku!
@api_view(['GET'])
def allbyname(request, name):
    tasks = Task.objects.get(title=name)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


#funkcni
@api_view(['POST'])
def taskCreate(request):
    serializer = Serializ(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# @api_view(['DELETE'])
# def taskDelete(request, pk):
#     task = Task.objects.get(id=pk)
#     task.delete()
#
#     return Response('Item succsesfully delete!')
