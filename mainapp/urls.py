from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, BlogViewSet, LoginView, RegisterView, AddMessageView, ViewMessageView, DeleteMessageView
from django.urls import path
router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'blogs', BlogViewSet, basename='blogs')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('add-message/', AddMessageView.as_view(), name='add-message'),
    path('view-messages/', ViewMessageView.as_view(), name='view-messages'),
    path('delete-message/<int:pk>/', DeleteMessageView.as_view(), name='delete-message'),
]

urlpatterns += router.urls
