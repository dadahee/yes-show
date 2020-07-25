from django.contrib import admin
from django.urls import path, include
import content.views
import account.urls 

from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', content.views.main, name="main"),
    path('account/', include(account.urls)),
    path('content/', include(content.urls)),
]
