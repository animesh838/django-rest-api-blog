from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Post, Comment
from .serializers import (
    PostSerializer, PostCreateSerializer, CommentSerializer,
    UserSerializer
)
import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response

logger = logging.getLogger(__name__)


@api_view(['GET'])
def test_api(request):
    """Simple test endpoint to check if API is working"""
    return Response({
        'message': 'API is working!',
        'status': 'success',
        'posts_count': Post.objects.count()
    })


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]  # Allow all users to access posts

    def get_serializer_class(self):
        if self.action == 'create':
            return PostCreateSerializer
        return PostSerializer

    def perform_create(self, serializer):
        try:
            # For unauthenticated users, create a default author or use None
            if self.request.user.is_authenticated:
                serializer.save(author=self.request.user)
                logger.info(f"Post created by authenticated user: {self.request.user.username}")
            else:
                # Create post without author (or you can create a default user)
                serializer.save(author=None)
                logger.info("Post created by anonymous user")
        except Exception as e:
            logger.error(f"Error creating post: {str(e)}")
            raise

    def create(self, request, *args, **kwargs):
        try:
            logger.info(f"Creating post with data: {request.data}")
            response = super().create(request, *args, **kwargs)
            logger.info("Post created successfully")
            return response
        except Exception as e:
            logger.error(f"Error in create method: {str(e)}")
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=True, methods=['post'])
    def add_comment(self, request, pk=None):
        post = self.get_object()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False)
    def published(self, request):
        posts = Post.objects.filter(is_published=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]  # Allow all users to comment


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Keep user data protected
