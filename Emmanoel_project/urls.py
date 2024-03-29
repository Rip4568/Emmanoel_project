from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #rotas para a sessão de administração
    path('admin/', admin.site.urls),
    #rotas para os aplicativos django
    path('',include('Core_app.urls')),
    #url para o Django-rest funcionar
    path('api-auth/', include('rest_framework.urls')),#ESSE TEMQUE ESTAR
    #url para o dj-rest-auth funcionar
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    #api para registramento
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))

    #essas dependencias foram depreciadas
    #path('rest-auth/', include('rest_auth.urls')),
    #path('rest-auth/registration/', include('rest_auth.registration.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#se estiver em modo de desenvolvimentosirva os arquivos estaticos
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)