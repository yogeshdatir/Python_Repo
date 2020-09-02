# Django - React Heroku Deployment

1. Make sure all the react app files are in root folder of the Django project.
   ![image-20200902103537364](F:\My workspace\Python_Repo\Deployment\Django - React Heroku Deployment.assets\image-20200902103537364.png)

2. Initialize git repo in the Django app. Push the Repo on GitHub and connect it with Heroku app.

3. Create a Heroku app.

4. Install Heroku cli.

5. Install gunicorn and whitenoise.
   `pip install guinicorn whitenoise`

6. Add requrement.txt file in the root folder.
   `pip freeze > requirement.txt`

7. Create runtime.txt to specify version of python.
   `runtime.txt`

   ```
   python-3.8.5
   ```

8. Create a new file named - Procfile : with no extension and capital P.
   `Procfile`

   ```
   release: python manage.py migrate
   web: gunicorn todoglobal.wsgi --log-file -
   ```

9. Add Domains in the settings.py

   Turn Debug mode to false and add allowed hosts - Heroku app URI, localhost.

   `todoglobal\settings.py`

   ```python
   # SECURITY WARNING: don't run with debug turned on in production!
   DEBUG = False
   
   ALLOWED_HOSTS = ['my-django-react-todo-app.herokuapp.com', 'localhost',]
   ```

10. Add build packs in the Heroku app:
    ![image-20200902074906739](F:\My workspace\Python_Repo\Deployment\Django - React Heroku Deployment.assets\image-20200902074906739.png)

11. Update settings.py with static root (to avoid collectstatics error in Heroku).

    ```python
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.1/howto/static-files/
    # Add Static root and storage here
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATIC_URL = '/static/'
    
    REACT_APP_DIR = BASE_DIR / 'frontend'
    
    STATICFILES_DIRS = [
        BASE_DIR / REACT_APP_DIR / 'build/static' ,
    ]
    ```

12. Add whitenoise middleware for static files in settings.py:

    ```python
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        # Add this middleware
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    ```

13. Run command to collect static file in static root folder:
    `python manage.py collectstatic`
    <u>Collecting static files needs to be done every time the react build is done.</u>

14. Add static URLs in urls.py

    ```python
    from django.contrib import admin
    from django.urls import path
    from django.views.generic import TemplateView
    # Add following imports
    from django.conf import settings
    from django.conf.urls.static import static
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', TemplateView.as_view(template_name='index.html'))
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    ```

    

15. In package.json file add postinstall script and engines

    ```react
    "scripts": {
        "start": "react-scripts start",
        "build": "react-scripts build",
        "test": "react-scripts test",
        "eject": "react-scripts eject",
        "postinstall": "npm run build"
     },
     "engines": {
       "node": "9.5.0",
       "npm": "6.4.1"
     },
    ```

16. Run following to get requirements:
    `pip freeze > requirements.txt`
    Make sure the file name is "requirements.txt".

17. Push the commits to the GitHub and deploy the branch on Heroku.



