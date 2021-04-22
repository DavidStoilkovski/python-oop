import re


class EmailValidator:
    __EMAIL_SPLIT_REGEX = '[@.]'

    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name):
        return len(name) >= self.min_length

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains

    def validate(self, email):
        (name, mail, domain) = re.split(EmailValidator.__EMAIL_SPLIT_REGEX, email)
        return EmailValidator.__validate_name(self, name) and \
               EmailValidator.__validate_mail(self, mail) and \
               EmailValidator.__validate_domain(self, domain)

# Test code
# mails = ["gmail", "softuni"]
# domains = ["com", "bg"]
# email_validator = EmailValidator(6, mails, domains)
# print(email_validator.validate("pe77er@gmail.com"))
# print(email_validator.validate("georgios@gmail.net"))
# print(email_validator.validate("stamatito@abv.net"))
# print(email_validator.validate("abv@softuni.bg"))
