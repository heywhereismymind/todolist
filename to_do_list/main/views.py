from django.http import JsonResponse
from main.models import To_Do_List

from rest_framework.parsers import JSONParser 
from rest_framework import status
 

from main.serializers import ToDoListSerializer
from rest_framework.decorators import api_view

    
@api_view(['GET', 'POST'])
def todolist_list(request):
    if request.method == 'GET':
        to_do_list = To_Do_List.objects.all()
        
        title = request.query_params.get('task_name', None)
        if title is not None:
            to_do_list = to_do_list.filter(title__icontains=title)
        
        to_do_list_serializer = ToDoListSerializer(to_do_list, many=True)
        return JsonResponse(to_do_list_serializer.data, safe=False)
    
    elif request.method == 'POST':
        to_do_list_data = JSONParser().parse(request)
        to_do_list_serializer = ToDoListSerializer(data=to_do_list_data)
        if to_do_list_serializer.is_valid():
            to_do_list_serializer.save()
            return JsonResponse(to_do_list_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(to_do_list_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def to_do_list_detail(request, pk):
    try: 
        to_do_list = To_Do_List.objects.get(pk=pk) 
    except To_Do_List.DoesNotExist: 
        return JsonResponse({'message': f'#{pk} task does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        to_do_list_serializer = ToDoListSerializer(to_do_list) 
        return JsonResponse(to_do_list_serializer.data) 
 
    elif request.method == 'PUT': 
        to_do_list_data = JSONParser().parse(request) 
        to_do_list_serializer = ToDoListSerializer(to_do_list, data=to_do_list_data) 
        if to_do_list_serializer.is_valid(): 
            to_do_list_serializer.save() 
            return JsonResponse(to_do_list_serializer.data) 
        return JsonResponse(to_do_list_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        to_do_list.delete() 
        return JsonResponse({'message': f'# {pk} was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
