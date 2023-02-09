from pathlib import Path
from links.models import AwesomeLink

path = Path('./bin/data/urls.txt')
urls = [line.strip() for line in open(path, 'r', encoding='utf-8').readlines()]
for url in urls:
    formatted = url.strip()
    try:
        link = AwesomeLink.objects.get(url=formatted)
        link.is_approved = True
        link.save()
        print(f'Link already exists: {link}')
    except AwesomeLink.DoesNotExist:
        link = AwesomeLink(url=formatted, is_approved=True)
        link.save()
        print(f'Created link: {link}')
