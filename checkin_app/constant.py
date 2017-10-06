from django.utils.translation import ugettext as _

NOT_INVOLVED = 0
IN_APPLICATION = 1
HAVE_JOINED = 2
EXITED = 3


STATUS_CHOICES = (
    (NOT_INVOLVED, _('not involved')),
    (IN_APPLICATION, _('in application')),
    (HAVE_JOINED, _('have joined')),
    (EXITED, _('exited'))
)
