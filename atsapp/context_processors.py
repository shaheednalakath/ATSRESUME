# from .utils import get_user_photo
# from allauth.socialaccount.models import SocialAccount
#
# def user_profile_photo(request):
#     if request.user.is_authenticated:
#         from .utils import get_user_photo  # <-- moved inside
#         photo = get_user_photo(request.user)
#         return {'photo': photo}
#     return {'photo': None}
#
