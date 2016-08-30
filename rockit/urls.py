from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns

#handler400 = 'noq.site.views.error.bad_request'
# handler403 = 'noq.site.views.error.permission_denied'
# handler404 = 'noq.site.views.error.page_not_found'
# handler500 = 'noq.site.views.error.server_error'

urlpatterns = [
    url(r'^api/', include('noq.core.urls')),
    url(r'', include('noq.site.urls.generic'))
]