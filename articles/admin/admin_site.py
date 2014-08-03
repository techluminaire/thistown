from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from django.contrib.auth.admin import UserAdmin,GroupAdmin
from django.contrib.auth.models import User, Group

class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = 'ThisTown site admin'

    # Text to put in each page's <h1>.
    site_header = ugettext_lazy('ThisTown administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Site administration')

admin_site = MyAdminSite()
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)