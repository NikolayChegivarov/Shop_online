# from django.contrib.auth.forms import PasswordResetForm
#
#
# class CustomPasswordResetForm(PasswordResetForm):
#     def send_mail(self, subject_template_name, email_template_name,
#                   context, from_email, to_email, html_email_template_name=None):
#         send_password_reset_token.delay(context['user'].id)