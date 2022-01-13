# .\env\scripts\activate    (act env on ahell) 
# python manage.py shell
# exec(open('shUser.py').read())
# exit() 

from django.db import models
from django.contrib.auth.models import User
from blog.models import Post

User.objects.all()
User.objects.first()
User.objects.filter(username='Admin')
User.objects.filter(username='Admin').first()
xuser = User.objects.filter(username='Admin').first()
print(xuser)
print(xuser.id)
print(xuser.pk)

xuser = User.objects.get(id=1)


Post.objects.all()
post_1 = Post(title='Blog 1', content='Frist Post Content abc', author=xuser)
post_1.save()

print(Post.objects.all())

xuser = User.objects.get(id=2)
post_2 = Post(title='Blog 2', content='second Post Content efg', author=xuser)
post_2.save()

xuser = User.objects.get(id=3)
post_3 = Post(title='Blog 3', content='3 Post Content ggg', author=xuser)
post_3.save()

post = Post.objects.first()
post.date_posted

post.author
post.author.email

xuser.post_set
xuser.post_set.all()

#exit()