#
#
# from allauth.socialaccount.models import SocialAccount
#
# def get_user_photo(user):
#     try:
#         from allauth.socialaccount.models import SocialAccount  # <-- moved inside
#         social_account = SocialAccount.objects.get(user=user, provider='google')
#         return social_account.extra_data.get('picture')
#     except Exception:
#         return None
