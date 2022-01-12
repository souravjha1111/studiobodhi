from django.conf.urls import url, include
from api import views

urlpatterns = [
    url('photo-url/(?P<pk>[0-9]+)', views.get_post_pic, name='getPhotoUrl'),
    url('blog-data/(?P<pk>[0-9]+)', views.blogdata, name='blogData'),
    url('contact-save/(?P<pk>[0-9]+)', views.contactsave, name='contactData'),

]
