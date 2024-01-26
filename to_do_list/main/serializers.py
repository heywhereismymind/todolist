from rest_framework import serializers 
from main.models import To_Do_List
 
 
class ToDoListSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = To_Do_List
        fields = ('id',
                  'task_name',
                  'task_description',
                  'date_created')
        