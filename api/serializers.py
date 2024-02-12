from rest_framework import serializers
from .models import Employee
import re

# to read all employee records
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'position', 'department']
    
    
    def validate_name(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        if not re.match("^[a-zA-Z]+(?: [a-zA-Z]+)?$", value.strip()):
            raise serializers.ValidationError("Name must contain only letters and a single space between words.")
        return value

# TO create a new employee record
class EmployeeCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Employee
        fields = ['name', 'position', 'department','user']
    
    def validate_name(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        if not re.match("^[a-zA-Z]+(?: [a-zA-Z]+)?$", value.strip()):
            raise serializers.ValidationError("Name must contain only letters and a single space between words.")
        return value