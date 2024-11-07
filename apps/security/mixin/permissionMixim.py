from django.contrib.auth.mixins import LoginRequiredMixin


class PermissionMixin(LoginRequiredMixin):
    """
    Mixin que sirve para ver
    si el usuario se encuentra con permisos en el modulo""
    """

    login_url = '/login/'

    redirect_field_name = 'next'