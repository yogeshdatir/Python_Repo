# Django Knox Authentication

1. Add user foreign key to the desired model:

   ```python
   from django.db import models 
   from django.utils import timezone 
   # import User model from auth package
   from django.contrib.auth.models import User
     
   class Todo(models.Model): 
       title=models.CharField(max_length=100) 
       description=models.TextField(default= None,null=True, blank=True) 
       creation_date=models.DateTimeField(default=timezone.now) 
       end_date=models.DateTimeField(null= True,blank=True)
       completed=models.BooleanField(default=False)
       deleted = models.BooleanField(default=False)
       # Add following field
       # null=True is for the entries which already created before this. Remove it after emptying the db/table.
       # related_name doc - https://docs.djangoproject.com/en/3.1/topics/db/queries/#following-relationships-backward
       owner = models.ForeignKey(User, related_name="client", on_delete=models.CASCADE, null=True)
     
       def __str__(self): 
           return self.title 
   ```

2. Run migrations.

3. Add permissions to the API viewset:

   ```python
   # Todo ViewSet
   
   class TodoViewSet(viewsets.ModelViewSet):
   	queryset = Todo.objects.all()
   	permission_classes = [
   		permissions.IsAuthenticated,
   	]
   	serializer_class = TodoSerializer
   
   	def get_queryset(self):
   		return self.request.user.client.all()
   
   	def perform_create(self, serializer):
   		serializer.save(owner=self.request.user)
   ```

4. Install django-rest-knox package.
   `pip install django-rest-knox`

   Update Setting file: Add knox and default authentication classes for DRF. 

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'todos',
       'rest_framework',
       'corsheaders',
       'knox'
   ]
   
   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': ['knox.auth.TokenAuthentication',]
   }
   ```

   **<u>Run migrations.</u>**

5. Create a django app - accounts:

   `py manage.py startapp accounts`

   Update Settings file:

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'todos',
       'rest_framework',
       'corsheaders',
       'knox',
       'accounts',
   ]
   ```

6. Create the serializers.py in accounts app:

   ```python
   from rest_framework import  serializers
   from django.contrib.auth.models import User
   from django.contrib.auth import authenticate
   
   # User Serializer
   class  UserSerializer(serializers.ModelSerializer):
     class Meta:
       model = User
       fields = ('id', 'username', 'email')
   
   
   
   # Register Serializer
   class RegisterSerializer(serializers.ModelSerializer):
     class Meta:
       model = User
       fields = ('id', 'username', 'email', 'password')
       extra_kwargs = {'password': {'write_only': True}}
   
     def create(self, validated_data):
       user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
       return user
   ```

7. Create api.py in accounts app:

   ```python
   from rest_framework import generics, permissions
   from rest_framework.response import Response
   from knox.models import AuthToken
   from .serializers import UserSerializer, RegisterSerializer
   
   # Register API
   class RegisterAPI(generics.GenericAPIView):
     serializer_class = RegisterSerializer
   
     def post(self, request, *args, **kwargs):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       user = serializer.save()
       return Response({
         "user": UserSerializer(user, context=self.get_serializer_context()).data,
         "token": AuthToken.objects.create(user)[1]
       })
   ```

8. Create urls.py file in accounts app:

   ```python
   from django.urls import path, include
   from .api import RegisterAPI
   from knox import views as knox_views
   
   urlpatterns = [
       path('api/auth', include('knox.urls')),
       path('api/auth/register', RegisterAPI.as_view())
   ]
   ```

9. Add urls in the root project urls.py file:

   ```python
   path('', include('accounts.urls'))
   ```

10. Add Login serializer:

    ```python
    # Login Serializer
    class LoginSerializer(serializers.Serializer):
      username = serializers.CharField()
      password = serializers.CharField()
    
      def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
          return user
        raise serializers.ValidationError("Incorrect Credentials")
    ```

11. Add Login API viewset:

    ```python
    # Login API
    class LoginAPI(generics.GenericAPIView):
      serializer_class = LoginSerializer
    
      def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
          "user": UserSerializer(user, context=self.get_serializer_context()).data,
          "token": AuthToken.objects.create(user)[1]
        })
    ```

12. Add the API endpoint in urls.py:

    ```python
    from django.urls import path, include
    from .api import RegisterAPI, LoginAPI
    from knox import views as knox_views
    
    urlpatterns = [
        path('apis/auth', include('knox.urls')),
        path('apis/auth/register', RegisterAPI.as_view()),
        path('apis/auth/login', LoginAPI.as_view()),
    ]
    ```

13. Create User API:

    ```python
    # Get Current Logged in User API
    class UserAPI(generics.RetrieveAPIView):
      permission_classes = [
        permissions.IsAuthenticated,
      ]  
      serializer_class = UserSerializer
    
      def get_object(self):
        return self.request.user
    ```

14. Add UserAPI end point in urls.py:

    ```python
    from django.urls import path, include
    from .api import RegisterAPI, LoginAPI, UserAPI
    from knox import views as knox_views
    
    urlpatterns = [
        path('apis/auth', include('knox.urls')),
        path('apis/auth/register', RegisterAPI.as_view()),
        path('apis/auth/login', LoginAPI.as_view()),
        path('apis/auth/user', UserAPI.as_view()),
    ]
    ```

15. Add LogoutAPI end pint in urls.py from knox:

    ```python
    from django.urls import path, include
    from .api import RegisterAPI, LoginAPI, UserAPI
    from knox import views as knox_views
    
    urlpatterns = [
        path('apis/auth', include('knox.urls')),
        path('apis/auth/register', RegisterAPI.as_view()),
        path('apis/auth/login', LoginAPI.as_view()),
        path('apis/auth/user', UserAPI.as_view()),
        path('apis/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    ]
    ```

    