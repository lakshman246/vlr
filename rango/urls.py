#from django.conf.urls.static import static
from django.conf.urls import url
from rango import views
urlpatterns = [
url(r'^$', views.index, name='index'),
#url(r'^admin/', admin.site.urls),
url(r'/',views.about,name='about'),
]
