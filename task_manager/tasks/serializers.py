from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """_summary_

    This serializer is responsible for validating and serializing task data. It ensures that
    certain fields, such as `status`, are handled appropriately during the creation and update
    of task instances. It also provides default values for specific fields like `status`.
    """
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = [
            'id',
            'name',
            'description',
            'status',
            'user',
        ]
        read_only_fields = ['user']

    def validate_status(self, value):
        
        if self.context['request'].method == 'POST' and value:
            raise serializers.ValidationError('You cannot set the status during creation.')
        return value

    def create(self, validated_data):
        
        if 'status' not in validated_data:
            validated_data['status'] = 'pending'  
        
        return super().create(validated_data)

    def update(self, instance, validated_data):
        
        if 'status' not in validated_data:
            validated_data['status'] = instance.status
        return super().update(instance, validated_data)