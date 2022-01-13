# .\env\scripts\activate    (act env on ahell) 
# python manage.py shell
# exec(open('shUser.py').read()) 

from django.contrib.auth.models import User

User.objects.all()
user = User.objects.filter(username='Admin').filter()
user
user.profile