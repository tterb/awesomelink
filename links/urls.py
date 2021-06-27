from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    AwesomeLinkList,
    AwesomeLinkCount,
    AwesomeLinkDetail,
    AwesomeLinkFlag,
    AwesomeLinkRate,
    AwesomeLinkRedirect,
    AwesomeLinkSpecific,
    AwesomeLinkSubmit
)

urlpatterns = [
    path('', AwesomeLinkRedirect),
    path('list', AwesomeLinkList.as_view()),
    path('<int:pk>', AwesomeLinkSpecific),
    path('rate', AwesomeLinkRate),
    path('flag/<int:pk>', AwesomeLinkFlag),
    path('detail/<int:pk>', AwesomeLinkDetail),
    path('count', AwesomeLinkCount),
    path('submit', AwesomeLinkSubmit),
]

urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
urlpatterns = format_suffix_patterns(urlpatterns)
