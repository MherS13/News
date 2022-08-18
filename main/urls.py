from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import DescriptionCreate, DescriptionDetail, DescriptionDelete

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path('all-news', views.all_news, name='all-news'),
    path('all-category', views.all_category, name='all-category'),
    path('category/<int:id>', views.category,  name='category'),
    path('task/<str:pk>/', DescriptionDetail.as_view(), name='task'),
    path('task-create/', DescriptionCreate.as_view(), name='task-create'),
    path('task-delete/<str:pk>/', DescriptionDelete.as_view(), name='task-delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)