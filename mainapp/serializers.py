from rest_framework import serializers
from .models import Project, Blog, Contact, Skill
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Project, Blog

from rest_framework import serializers
from .models import Project, Blog, Contact
from rest_framework import serializers
from .models import Project
from rest_framework import serializers
from .models import Project, Blog

from rest_framework import serializers
from .models import Project

from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Project
        fields = "__all__"


# mainapp/serializers.py
class BlogSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Blog
        fields = "__all__"
        read_only_fields = ["author"]  # important!



from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'message', 'created_at']



class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user

from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'name', 'email', 'message', 'created_at']
