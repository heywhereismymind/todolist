from rest_framework import serializers 
from main.models import Task, Category
 
 
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id',
                  'name',
                  'description',
                  'file',
                  'created_at',
                  'category'
                  )
        

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id',
                  'name',
                  )
        