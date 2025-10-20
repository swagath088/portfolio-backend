from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions, generics
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.views import APIView

from .models import Project, Blog, Contact, Skill
from .serializers import ProjectSerializer, BlogSerializer, ContactSerializer, SkillSerializer, UserSerializer

from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer

from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import viewsets

from rest_framework import viewsets, permissions
from .models import Project, Blog
from .serializers import ProjectSerializer, BlogSerializer
from rest_framework import viewsets, permissions
from .models import Project, Blog
from .serializers import ProjectSerializer, BlogSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


from rest_framework import viewsets, permissions
from .models import Blog
from .serializers import BlogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)




# Skills
class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.AllowAny]

# Register
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email", "")
        
        if not username or not password:
            return Response({"detail": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username).exists():
            return Response({"detail": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, password=password, email=email)
        token = Token.objects.create(user=user)
        
        return Response({
            "token": token.key,
            "is_superuser": user.is_superuser,
            "username": user.username
        })


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project, Blog, Contact
from .serializers import ProjectSerializer, BlogSerializer, ContactSerializer
from rest_framework import generics

class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class BlogList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_serializer_context(self):
        return {'request': self.request}

from rest_framework import generics, permissions
from .models import Message
from .serializers import MessageSerializer

# All users can send
class AddMessageView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]

# Only superusers can view all
class ViewMessageView(generics.ListAPIView):
    queryset = Message.objects.all().order_by('-created_at')
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAdminUser]




from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "is_superuser": user.is_superuser,
                "username": user.username
            })
        return Response({"detail": "Invalid credentials"}, status=400)


# mainapp/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import Message

# mainapp/views.py
from rest_framework import generics, permissions
from .models import Message
from .serializers import MessageSerializer

class DeleteMessageView(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAdminUser]  # Only superusers can delete

