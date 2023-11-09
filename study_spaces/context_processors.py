from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import get_user

def user_context_processor(request):
    user = get_user(request)

    if user.is_authenticated:
        social_accounts = SocialAccount.objects.filter(user=user)
        extra_data = {} 

        for social_account in social_accounts:
            extra_data = social_account.extra_data

        return {'googleUser': extra_data}
    else:
        return {}
