# Blog

# Данный проект позволяет пользователям создавать, редактировать и удалять записи. На домашней странице сайта дается список всех записей блога, для каждой отдельной записи также будет предусмотрена детализированная страница.

Начиная создания нового проекта blog_projec:

cd ~/Desktop
mkdir blog
cd blog
poetry add django ~= 3.2
poetry shell

# Новое приложение

python manage.py startapp <appname>

  
# Сообщим Django о новом приложении. Для этого откроем в текстовом редакторе файл settings.py и добавим в конце переменной INSTALLED_APPS наше приложение:
  
  INSTALLED_APPS = [
                 # ...
                 < appname >,
]
                   
# Модель базы данных

модели дизайна
<имя приложения>/models.py

применять миграцию БД новых моделей
  
python manage.py makemigrations <appname>
python manage.py migrate <appname>
  
  
# Aдминистратор для блога на Django
  
  python manage.py createsuperuser
  
 # зарегистрировать модели приложений в администраторе приложения 
  
  from .models import < model >  # etc

  admin.site.register( < model >)
  
# URLs
  
  # blog/urls.py
from django.urls import path
 
from .views import BlogListView
 
urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
]
  
# Представления — BlogListView для отображения записей блога
  # blog/views.py
from django.views.generic import ListView
 
from .models import Post
 
 
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
  
 # Создание шаблона для блога на Django
mkdir templates
touch templates/base.html
touch templates/home.html
  
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # новое
        ...
    },
]
