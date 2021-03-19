from blog import views
from django.urls import path

urlpatterns = [
    path('', views.postList, name = 'home'),
    path('<slug:slug>/', views.postDetail, name = 'post_detail'),
    path(r'email/subscribe/', views.email, name = 'email'),
    path("posts/extras/", views.extras, name = 'extras'),
    path("posts/extras/<slug:slug>/", views.extrasDetail, name='extras_detail'),
    path('blog/about/', views.about, name='about'),
]