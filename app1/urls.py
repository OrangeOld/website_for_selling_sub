from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('mainpage',views.Subs.as_view(),name='mainpage'),
    path('post/<slug:post_slug>',views.show_post,name='post'),# for a particular post
    path('test-form/',views.handle_form,name='test-form'),
    path('Successful_rent/',views.Succesrent,name='succ'),
    path('login/',views.LoginUser.as_view(),name='login'),
    path('register/',views.RegisterUser.as_view(),name='register')
]


