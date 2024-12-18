from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from posts.serializers import UserSerializer, PostSerializer
from posts.models import Post 

User = get_user_model()

class UserSerializerTestCase(APITestCase):
    def setUp(self):
        """Setup user and data for testing."""
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123',
            'first_name': 'Test',
            'last_name': 'User',
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_user_serialization(self):
        """Test the serialization of the User model."""
        serializer = UserSerializer(self.user)
        data = serializer.data
        
        # Check if all the fields are present in the serialized data
        self.assertEqual(set(data.keys()), set(['id', 'username', 'email', 'first_name', 'last_name', 'api_key']))
        self.assertEqual(data['username'], self.user.username)
        self.assertEqual(data['email'], self.user.email)
        self.assertEqual(data['first_name'], self.user.first_name)
        self.assertEqual(data['last_name'], self.user.last_name)
    
    def test_user_deserialization(self):
        """Test the deserialization of user data."""
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123',
            'first_name': 'New',
            'last_name': 'User',
        }
        
        # Deserialize data
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        
        # Check if the user is created correctly
        user = serializer.save()
        self.assertEqual(user.username, data['username'])
        self.assertEqual(user.email, data['email'])
        self.assertEqual(user.first_name, data['first_name'])
        self.assertEqual(user.last_name, data['last_name'])
        
    def test_user_missing_required_fields(self):
        """Test user serialization with missing fields."""
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            # Missing 'password', 'first_name', 'last_name'
        }
        serializer = UserSerializer(data=data)
        self.assertFalse(serializer.is_valid())  # This should now fail if fields are missing
        
        # Check for missing required fields
        self.assertIn('password', serializer.errors)
        self.assertIn('first_name', serializer.errors)
        self.assertIn('last_name', serializer.errors)

    def test_user_password_is_not_serialized(self):
        """Test that password is not serialized."""
        serializer = UserSerializer(self.user)
        self.assertNotIn('password', serializer.data)


class PostSerializerTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.post = Post.objects.create(title="Test Post", content="Test Content", author=self.user)

    def test_post_serialization(self):
        serializer = PostSerializer(self.post)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'title', 'content', 'author', 'created_at']))
        self.assertEqual(data['title'], self.post.title)
        self.assertEqual(data['content'], self.post.content)