


'''
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_api_key.models import APIKey
from .models import Post
from posts.models import User

class PostAPITestCase(APITestCase):
    def setUp(self):
        # Log in a User
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.api_client = APIClient()

        # Create API Key for HasAPIKey permission
        self.api_key, _ = APIKey.objects.create_key(name="Test API Key")

        # Create a sample post
        self.post = Post.objects.create(title="Test Post", content="This is a test post.", author=self.user)

        # Create URLs for testing
        self.post_list_url = reverse('post-list')
        self.post_detail_url = reverse('post-detail', kwargs={'id': self.post.id})
        self.post_create_url = reverse('post-create')

    def test_post_list_authenticated(self):
        """Test the post list view with JWT authentication."""
        # Obtain JWT token for login
        refresh = RefreshToken.for_user(self.user)
        jwt_token = str(refresh.access_token)

        # Authenticate with JWT
        self.api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt_token)
        response = self.api_client.get(self.post_list_url)
        
        # Assert the response status code and content
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Post")

    def test_post_list_unauthenticated(self):
        """Test the post list view without authentication."""
        response = self.api_client.get(self.post_list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_detail_with_api_key(self):
        """Test post detail view with API key authentication."""
        # Set API key in the header
        print("here")
        print(self.api_key)
        response = self.api_client.get(self.post_detail_url, HTTP_X_API_KEY=self.api_key)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Post')

    def test_post_detail_unauthenticated(self):
        """Test post detail view without API key."""
        response = self.api_client.get(self.post_detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_create_authenticated(self):
        """Test the post create view with session authentication."""
        self.api_client.login(username='testuser', password='testpassword')
        data = {
            'title': 'New Post',
            'content': 'This is a new post created via test.'
        }
        response = self.api_client.post(self.post_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) #here
        self.assertEqual(response.data['title'], 'New Post')

    def test_post_create_unauthenticated(self):
        """Test the post create view without authentication."""
        data = {
            'title': 'Unauthorized Post',
            'content': 'This post should not be created without login.'
        }
        response = self.api_client.post(self.post_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    
    def test_login_failure(self):
        """Test login view with invalid credentials."""
        data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.api_client.post(reverse('login'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
'''