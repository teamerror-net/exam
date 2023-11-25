from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
admin.site.site_header = 'ADMIN PANEL'
admin.site.site_title = 'ONLINE EXAMINATION SYSTEM'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('dashboard/', include("dashboard.urls")),
    path('quiz/', include("quiz.urls")),
    path('history/', include("history.urls")),
    path('ranking/', include("ranking.urls")),
    path('profile/', include("userprofile.urls")),
    path('settings/', include("usersettings.urls")),
    path('account/', include("useraccount.urls")),
    path('contact/', include("contact.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
