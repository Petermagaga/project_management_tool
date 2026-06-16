
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/',include("accounts.urls")),
    path("api/workspaces/",include("workspaces.urls")),
    path("api/projects/",include("projects.urls")),
    path("api/boards/",include ("boards.urls")),
    path("api/tasks/",include("tasks.urls")),
    path("api/comments/",include("comments.urls")),
    path("api/activity/",include("notifications.urls"))

]

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

