from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from posts.models import Post
from rest_framework_api_key.models import APIKey

User = get_user_model()

class PostCreateViewTestCase(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword123')

        # Step 1: Login to get session cookies
        login_data = {'username': 'testuser', 'password': 'testpassword123'}
        response = self.client.post('/api/login/', login_data, format='json')
        response_1 = self.client.post('/api/token/', login_data, format='json')

        # Step 2: Check if login was successful and extract session cookies
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)  

        # Step 3: Get the sessionid and csrf token from the cookies
        self.sessionid = self.client.cookies['sessionid'].value
        self.csrftoken = self.client.cookies['csrftoken'].value
        self.access_token = response_1.data['access']

        #  Create an API key for the user (for testing API Key authentication)
        self.api_key, _ = APIKey.objects.create_key(name="TestAPIKey")

    def test_post_creation(self):
        # Step 5: Use sessionid and CSRF token for authenticated requests
        response = self.client.post(
            '/api/posts/create/', 
            {'title': 'Test Post', 'content': 'Test Content', "author": 1},
            HTTP_COOKIE=f'sessionid={self.sessionid}',  # Pass sessionid cookie
            HTTP_X_CSRFTOKEN=self.csrftoken
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_get(self):
            """Test creating a post as an authenticated user with JWT."""
            response = self.client.get(
                '/api/posts/', 
                HTTP_AUTHORIZATION=f'Bearer {self.access_token}'  # Use the access token for authentication
            )

            # Display the response content for debugging
            #print("Response Content (Create Post):", response.content)
            #print("Response Data (Create Post):", response.data)

            # Check the response status code
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            #print(response.content)

  
   

    def test_post_get_by_id(self):
            """Test creating a post as an authenticated user with JWT."""
            response = self.client.get(
                '/api/posts/', 
                HTTP_AUTHORIZATION=f'Bearer {self.access_token}'  # Use the access token for authentication
            )

            # Check the response status code
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            #print(response.content)


    def test_post_get_by_id_with_api_key(self):
            """Test retrieving a specific post by its ID with API Key authentication."""
           
            api_key_value = self.api_key.id
            print(api_key_value)
            response = self.client.get(
                f'/api/posts/1/', 
                HTTP_AUTHORIZATION=f'Api-Key {api_key_value}'
            )

            # Step 5: Verify the response
            self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    