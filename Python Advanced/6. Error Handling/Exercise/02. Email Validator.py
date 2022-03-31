from custom_errors_for_emails import MustContainAtSymbolError, NameTooShortError, DomainNameTooShort, InvalidDomainError


required_domains = {'com', 'bg', 'org', 'net'}
email = input()

while not email == 'End':

    if '@' not in email:
        raise MustContainAtSymbolError('"@" symbol missing')

    name, full_domain = email.split('@')

    if len(name) <= 4:
        raise NameTooShortError('recipient name must contain 5 or more element/s')

    domain_name, top_lvl_domain = full_domain.split('.')

    if len(domain_name) < 1:
        raise DomainNameTooShort('domain name must contain 1 or more element/s')

    if top_lvl_domain not in required_domains:
        raise InvalidDomainError('top-level domain incorrect, must contain one of following: .com, .bg, .org, .net')

    print(email)

    email = input()