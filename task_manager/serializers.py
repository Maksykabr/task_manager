from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=100)
    # description = serializers.DictField()
    # selected_data = serializers.DateField()
    # start_time = serializers.TimeField()
    # end_time = serializers.TimeField()
    # completed = serializers.BooleanField(default=False)

    class Meta:
        model = Task
        fields = '__all__'

    # def get_fields(self):
    #     fields = super().get_fields()
    #     for field_name, field in fields.items():
    #         field.required = True
    #     return fields
