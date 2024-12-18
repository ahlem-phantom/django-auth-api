
from django.test import TestCase
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()

class UserModelTestCase(TestCase):

    def setUp(self):
        """Create a user for testing."""
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123',
            'first_name': 'Test',
            'last_name': 'User',
            'api_key': 'test-api-key-12345',
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_user_creation(self):
        """Test that the user is created successfully."""
        user = self.user
        self.assertEqual(user.username, self.user_data['username'])
        self.assertEqual(user.email, self.user_data['email'])
        self.assertEqual(user.first_name, self.user_data['first_name'])
        self.assertEqual(user.last_name, self.user_data['last_name'])
        self.assertEqual(user.api_key, self.user_data['api_key'])
    
    def test_user_password_is_hashed(self):
        """Test that the user's password is hashed."""
        user = self.user
        self.assertNotEqual(user.password, self.user_data['password'])  # Password should be hashed
        self.assertTrue(user.check_password(self.user_data['password']))  # Password should match after hashing

    def test_unique_api_key(self):
        """Test that the API key is unique."""
        new_user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123',
            'first_name': 'New',
            'last_name': 'User',
            'api_key': 'test-api-key-12345',  # Same API key as the first user
        }
        with self.assertRaises(Exception):  # Expect an error because API key should be unique
            User.objects.create_user(**new_user_data)



class PostModelTestCase(TestCase):

    def setUp(self):
        """Create a user and a post for testing."""
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123',
            'first_name': 'Test',
            'last_name': 'User',
        }
        self.user = User.objects.create_user(**self.user_data)
        self.post_data = {
            'title': 'Test Post',
            'content': 'This is the content of the test post.',
            'author': self.user,
        }
        self.post = Post.objects.create(**self.post_data)

    def test_post_creation(self):
        """Test that the post is created successfully."""
        post = self.post
        self.assertEqual(post.title, self.post_data['title'])
        self.assertEqual(post.content, self.post_data['content'])
        self.assertEqual(post.author, self.user)
        self.assertIsNotNone(post.created_at)  # created_at should be set automatically

    def test_post_str_method(self):
        """Test the __str__ method of Post."""
        post = self.post
        self.assertEqual(str(post), self.post_data['title'])  # Should return title of the post
