from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('<int:id>', views.candidate.as_view(), name='candidate'),
    path('delete/<int:id>', views.DeleteCandedate, name='delete'),
    path('update/<int:id>', views.UpdateCandedate, name='update'),
    path('api/',include('app.api.urls')),    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

