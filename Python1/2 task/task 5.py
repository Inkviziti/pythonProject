from tld import get_tld

def get_domains(url):
    domain = get_tld(url, as_object=True)
    domains = [domain.domain]
    while domain.subdomain:
        domain = get_tld(domain.subdomain, as_object=True)
        domains.insert(0, domain.domain)
    return domains

url = input("Введите домен сайта"     )
domains = get_domains(url)
for domain in domains:
    print(domain)