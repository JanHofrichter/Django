from rest_framework import serializers
from .models import Task
from .models import AttributeName


class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields ='__all__'

class Serializ(serializers.ModelSerializer):
	class Meta:
		model = AttributeName
		fields ='__all__'