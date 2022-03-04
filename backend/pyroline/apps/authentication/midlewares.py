from .models import User
from django.utils import timezone


class UpdateLastActivityMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs,):
        assert hasattr(
            request, 'user'), 'The UpdateLastActivityMiddleware requires authentication middleware to be installed.'
        if request.user.is_authenticated() & request.user.is_staff():
            User.objects.filter(user_id=request.user.id)\
                .update(last_activity=timezone.now())
