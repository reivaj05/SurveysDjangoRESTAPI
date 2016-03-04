from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from django.http import Http404
from django.shortcuts import redirect
from .utils import check_fields


class FormMessagesMixin(object):
    """
        Mixin to handle and show success/error messages on form validation
    """

    success_message = None
    error_message = None

    def __init__(self, *args, **kwargs):
        super(FormMessagesMixin, self).__init__(*args, **kwargs)
        check_fields(
            fields={
                'success_message': self.success_message,
                'error_message': self.error_message
            }
        )

    def form_valid(self, form):
        messages.add_message(
            request=self.request,
            level=messages.SUCCESS,
            message=self.success_message
        )
        return super(FormMessagesMixin, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(
            request=self.request,
            level=messages.ERROR,
            message=self.error_message
        )
        return super(FormMessagesMixin, self).form_invalid(form)


class LoginRequiredMixin(object):
    """
        Mixin to allow the user access to certain views,
        if it's logged in or restrict access otherwise
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            messages.add_message(
                request=self.request,
                level=messages.INFO,
                message='Please login to access that view'
            )
            return redirect_to_login(next=request.get_full_path())
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class PermissionRequiredMixin(object):
    """
        Mixin to allow the user access to certain views,
        if it has the permissions needed or restrict access otherwise
    """
    permission = None
    no_permission_url = None

    def dispatch(self, request, *args, **kwargs):
            check_fields(
                fields={
                    'permission': self.permission,
                    'no_permission_url': self.no_permission_url
                }
            )
            if request.user.has_perm(self.permission):
                return super(PermissionRequiredMixin, self).dispatch(
                    request, *args, **kwargs)
            else:
                messages.add_message(
                    request=self.request,
                    level=messages.INFO,
                    message='You do not have permission for this action'
                )
                return redirect(self.no_permission_url)


class DoesExistMixin(object):
    """
        Mixin to check if an objects exists, if the model object
        exists the user is redirected to the appropriate request
        otherwise an exception is raised
    """
    model = None

    def dispatch(self, request, *args, **kwargs):
        check_fields(
            fields={
                'model': self.model
            }
        )
        try:
            return super(DoesExistMixin, self).dispatch(
                request, *args, **kwargs)
        except self.model.DoesNotExist:
            raise Http404
