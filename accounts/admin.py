from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy



class TrafficAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('Master Plan-KE site admin')

    # Text to put in each page's <h1>.
    site_header = ugettext_lazy('Master Plan-KE Site Administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Master Plan-KE Site Administration')

admin_site = TrafficAdminSite()
