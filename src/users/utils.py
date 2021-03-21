from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class MyLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users:login')


def get_current_customer(obj):
    return None if obj.request.user.is_anonymous else obj.request.user
