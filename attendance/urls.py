from django.contrib import admin
from django.urls import path
from dataset import views
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('student/', views.student_signup, name="student_signup"),
    path('faculty/', views.faculty_signup, name="faculty_signup"),
    path('home/', views.home, name="home"),
    path('viewattendace/', views.viewattendance, name="viewattendance"),
    path('download/<str:file_name>', serve, {'document_root': settings.STATIC_ROOT}),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
