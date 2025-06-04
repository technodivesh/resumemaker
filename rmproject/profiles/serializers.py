from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    user_email = serializers.SerializerMethodField()
    created_by_email = serializers.SerializerMethodField()
    updated_by_email = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = [
            'guid',
            'created_at',
            'updated_at',
            'user',
            'created_by',
            'updated_by',
            'full_name',
            'email',
            'phone',
            'address',
            'summary',
            'linkedin',
            'github',
            'portfolio',
            'is_active',
            'user_email',
            'created_by_email',
            'updated_by_email',
        ]
        read_only_fields = ['user', 'created_by', 'updated_by', 'created_at', 'updated_at']

    def get_user_email(self, obj):
        return obj.user.email if obj.user else None

    def get_created_by_email(self, obj):
        return obj.created_by.email if obj.created_by else None

    def get_updated_by_email(self, obj):
        return obj.updated_by.email if obj.updated_by else None

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        validated_data['created_by'] = user
        validated_data['updated_by'] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['updated_by'] = self.context['request'].user
        return super().update(instance, validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

