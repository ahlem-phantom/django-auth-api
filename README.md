# Django Authentication API

This project demonstrates how to implement three different authentication methods in a Django REST Framework (DRF) API: JWT (JSON Web Token), API key, and user session. The project includes three different API endpoints that require different types of authentication. The endpoints allow you to manage and interact with posts created by users.

### 📐 Project Features 

- **User Authentication**: Custom user model inheriting from `AbstractUser` with fields `username`, `email`, `password`, `first_name`, `last_name`, and `api_key`.
- **Post Model**: Model for posts with `title`, `content`, `author` (a foreign key to the User model), and `created_at` (auto-generated).
- **Three API Endpoints**:
  - `/posts/` (GET): Returns a list of all posts (requires JWT authentication).
  - `/posts/<id>/` (GET): Returns a specific post by ID (requires API key authentication).
  - `/posts/create/` (POST): Creates a new post (requires user session authentication).

## Authentication Methods

- **JWT Authentication**: Users can obtain a JWT token by logging in via `/api/token/`. This token is used to authenticate requests to the `/posts/` endpoint.
- **API Key Authentication**: Users can obtain an API key by accessing the Django admin panel (`/admin/`) and creating a new API key for the user. This API key is used to authenticate requests to the `/posts/<id>/` endpoint.
- **Session Authentication**: Users can log in with a username and password to obtain a session cookie. This cookie is used to authenticate requests to the `/posts/create/` endpoint.

## ✨ Getting Started
To get a local copy up and running follow these simple example steps.


### 🚧 Prerequisites

You may find below the list of things required for this project :
- **Python**: 3.9 or higher
- **Django**: 4.2 or higher
- **Django REST Framework**: The primary package for building the API
- **Simple JWT**: For JWT-based authentication (`django-rest-framework-simplejwt` version 5.2.2)
- **django-rest-framework-api-key**: For API key-based authentication
- **Django's built-in authentication system**: For user session authentication


 ### 🛠 Installation
_In order to install the app you need to follow the instructions below :_
1. Clone the repo
   ```sh
   git clone https://github.com/ahlem-phantom/django-travel-agency.git
   ```

2. Create a virtual environement and activate it 
   ```sh
   ($) python3 -m venv venv
   ($) .\venv\Scripts\activate.bat
   ```  
3. Install flask dependecies using the file "requirements.txt"
   ```sh
   pip install -r requirements.txt
   ```

4. Run Django Migrations 
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a Superuser Account for Admin Access
   ```sh
   python manage.py createsuperuser
   ```
You'll be prompted to enter a username, email, and password for the admin account. After the superuser is created, you'll be able to log in to the Django admin dashboard.

6. Run the django server
   ```sh
   python manage.py runserver
   ```

7. Open localhost:8000 to enjoy the app.


## ⚡ Usage
  - `/token/`  - Token Obtain Pair: Get JWT access and refresh tokens using username and password.
  - ` /token/refresh/`  - Token Refresh: Refresh an expired access token using a refresh token.
  - ` /login/`  - User Login: Authenticate and get a session cookie for session-based authentication.
  - ` /posts/`  - Get All Posts: Retrieve a list of all posts.
  - `/posts/<int:id>/`  - Get Post By ID: Retrieve a specific post by its ID.
  - `/posts/create/`  - Create a New Post: Create a new post with authentication. give me readme just this one


In this step, I logged in to get the session cookies (including the session ID and CSRF token). These cookies were then used to authenticate a request for creating a new post.
| <img src="https://github.com/user-attachments/assets/10013867-4057-470e-8e33-399e9408f706" /><br> **Login to get session cookies **| <img src="https://github.com/user-attachments/assets/e18daf12-11d7-4393-8dd8-e518c8e507ee" />  <br>**Create Post**| 
| ------------- | ------------- | 

After logging in, I generated a JWT token from the token endpoint. This token was then used to authenticate and fetch all posts.
| <img src="https://github.com/user-attachments/assets/06ed6a87-38bc-4c72-b594-4a02040df8de" /><br> **Get the JWT token from the token endpoint**| <img src="https://github.com/user-attachments/assets/4cc552a6-cac8-4eb1-92bd-dde8f819343a" />  <br>**Get All Posts**| 
| ------------- | ------------- | 

Finally, I manually created an API key through the Django admin dashboard to authenticate requests using API key-based authentication.
| <img src="https://github.com/user-attachments/assets/ac732a65-74d6-46c3-98e7-ca3f65321df4" /><br> **Get Post By ID**|
| ------------- | 



<!-- CONTACT -->
## 💌 Contact

<b>Project Author :</b> 
| <img src="https://user-images.githubusercontent.com/78981558/157719496-9aec4730-512f-4188-87ca-8dbe6271ebfc.jpg" width="150" height="150"/>  <br> **Ahlem Laajili**| 
| ------------- |
|<div align="center"><a href="mailto:ahlem.laajili@esprit.tn"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail Badge"/></a><a href="https://github.com/ahlem-phantom"><img title="Follow on GitHub" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/></a></div>  |


<p align="right">(<a href="#top">back to top</a>)</p>




Developed with 💕 by **ahlem-phantom**.
