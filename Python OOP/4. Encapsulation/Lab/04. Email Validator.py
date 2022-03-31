def get_email_parts(email):
    email_parts = email.split('@')
    mail_domain_parts = email_parts[1].split('.')

    username = email_parts[0]
    mail = mail_domain_parts[0]
    domain = mail_domain_parts[1]

    return username, mail, domain


class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, username):
        return len(username) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):

        username, mail, domain = get_email_parts(email)

        if self.__is_name_valid(username) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain):
            return True
        return False


mails = ['gmail', 'softuni']
domains = ['com', 'bg']
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate('pe77er@gmail.com'))
print(email_validator.validate('georgios@gmail.net'))
print(email_validator.validate('stamatito@abv.net'))
print(email_validator.validate('abv@softuni.bg'))