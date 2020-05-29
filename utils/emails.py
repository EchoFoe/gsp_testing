from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from gsp_testing.settings import FROM_EMAIL, EMAIL_ADMIN
from emails.models import EmailSendingFact
from django.forms.models import model_to_dict


class SendingEmail(object):
    from_email = "ГСП <%s>" % FROM_EMAIL
    reply_to_emails = [from_email]
    target_emails = []
    bcc_emails = []

    def sending_email(self, type_id, email=None, new_offer=None):
        global subject, message
        if not email:
            email = EMAIL_ADMIN
        target_emails = [email]

        vars = dict()
        if type_id == 1:
            subject = "Новая заявка на публикацию заказа"
            vars["new_offer"] = new_offer
            subject = 'Клиент подал заявку на публикацию заказа'
            message = get_template('emails_templates/notification_admin.html').render(vars)

        elif type_id == 2:
            subject = 'Ваша заявка получена! Модератор уже её проверяет!'
            vars["new_offer"] = new_offer
            message = get_template('emails_templates/notification_customer.html').render(vars)

        msg = EmailMessage(subject, message, from_email=self.from_email, to=target_emails, bcc=self.bcc_emails, reply_to=self.reply_to_emails)
        msg.content_subtype = 'html'
        msg.mixed_subtype = 'related'
        msg.send()

        kwargs = {
            "type_id": type_id,
            "email": email
        }
        if new_offer:
            kwargs["offer"] = new_offer
        EmailSendingFact.objects.create(**kwargs)
