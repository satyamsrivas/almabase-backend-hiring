from rest_framework import serializers
from .models import JobType, Customer,CustomerType


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        exclude = ('object_status')
        read_only_fields = ('id','created_at','modified_at')


class CustomerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerType
        exclude = ('object_status')
        read_only_fields = ('id','created_at','modified_at')
