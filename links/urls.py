from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    awesomelink_list,
    awesomelink_count,
    awesomelink_detail,
    awesomelink_flag,
    awesomelink_pending,
    awesomelink_rate,
    awesomelink_specific,
    awesomelink_submit,
    awesomelink_view,
)

urlpatterns = [
    path('', awesomelink_view),
    path('list', awesomelink_list),
    path('pending', awesomelink_pending),
    path('count', awesomelink_count),
    path('flag', awesomelink_flag),
    path('rate', awesomelink_rate),
    path('submit', awesomelink_submit),
    path('<int:pk>', awesomelink_specific),
    path('detail/<int:pk>', awesomelink_detail),
]

urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
urlpatterns = format_suffix_patterns(urlpatterns)
