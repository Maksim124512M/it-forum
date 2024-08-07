from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forum_app.urls')),
    path('accounts/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]



