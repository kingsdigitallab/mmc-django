from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as documents_urls

from cms.views import SearchView
from ddhldap.signal_handlers import (
    register_signal_handlers as ddhldap_register_signal_handlers,
)

admin.autodiscover()
ddhldap_register_signal_handlers()

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^digger/", include("activecollab_digger.urls")),
]

# -----------------------------------------------------------------------------
# Wagtail CMS
# -----------------------------------------------------------------------------

urlpatterns += [
    url(r"^wagtail/", include(wagtailadmin_urls)),
    url(r"^documents/", include(documents_urls)),
    url(r"^search/", SearchView.as_view()),
    url(r"", include(wagtail_urls)),
]
# -----------------------------------------------------------------------------
# Django Debug Toolbar URLS
# -----------------------------------------------------------------------------
try:
    if settings.DEBUG:
        import debug_toolbar

        urlpatterns += [
            url(r"^__debug__/", include(debug_toolbar.urls)),
        ]

except ImportError:
    pass

# -----------------------------------------------------------------------------
# Static file DEBUGGING
# -----------------------------------------------------------------------------
if settings.DEBUG:
    import os.path

    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL + "images/",
        document_root=os.path.join(settings.MEDIA_ROOT, "images"),
    )
