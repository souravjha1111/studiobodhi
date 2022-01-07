from django.conf.urls import url, include
from api import views

urlpatterns = [
    url('photo-url', views.get_post_pic, name='getPhotoUrl'),
    url('delete-photo-url/(?P<pk>[0-9]+)', views.deletephotourl.as_view(), name='delPhotoUrl'),
    url('blog-data', views.blogdata, name='blogData'),
    url('delete-blog-data/(?P<pk>[0-9]+)', views.deleteblogdata.as_view(), name='delblogData'),
    url('contact-save', views.contactsave, name='contactData'),
    url('delete-contact-save/(?P<pk>[0-9]+)', views.deletecontactsave.as_view(), name='delblogData'),

]