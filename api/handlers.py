from piston.handler import BaseHandler
from piston.utils import require_mime, rc
from django.core.exceptions import ObjectDoesNotExist
from postfixadmin.users.models import User
from postfixadmin.aliases.models import Alias
from postfixadmin.domains.models import Domain
from postfixadmin.autoresponse.models import Response

class AutoResponseHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Response

    def read(self, request):
        base = model.objects.filter(enabled=True)
        return base.all()

