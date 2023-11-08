
from django.contrib import admin
from django.urls import path , include
from django.conf import settings

from blog_app import views
from blog_app.views import HomeView, ArticleDetailsView, CreatePostView, UpdatePostView, DeletePostView, CreateCategaryView
from members.views import UserRegisterView, UpdateUserView, UserPasswordChangeView
#password reset imports
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(), name="home"),
    path('article/<int:pk>/', ArticleDetailsView.as_view(), name="article-detail"),
    path('add_post/', CreatePostView.as_view(), name="add_post"),
    path('add_catagary/',CreateCategaryView.as_view(), name="add_categary"),
    path('article/edit/<int:pk>/',UpdatePostView.as_view(),name="update_post"),
    path('article/<int:pk>/remove/', DeletePostView.as_view(), name="delete_post"),
    #members app url including here
   
    path('members/', include('django.contrib.auth.urls')),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('categary/<str:cats>/', views.CategaryView, name="categary"),
    path('like/<int:pk>/', views.LikeView, name='like_post'),
    path('edit_profile/', UpdateUserView.as_view(), name="edit_profile"),
    path('<int:user_id>/password/', UserPasswordChangeView.as_view(template_name='registration/change_password.html')),

    

]


# Add these lines at the end of your urls.py file to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
