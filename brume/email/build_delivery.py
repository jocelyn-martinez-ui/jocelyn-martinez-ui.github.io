"""Build editable multipart .eml proofs with fully qualified asset and CTA URLs."""

from email.message import EmailMessage
from email.policy import SMTP
from pathlib import Path
import re
from urllib.parse import urljoin

BASE = 'https://jocelyn-martinez-ui.github.io/brume/email/'
ROOT = Path(__file__).resolve().parent
LETTERS = ('01-introduction', '02-material', '03-detail')


def absolute_reference(match):
    attribute, reference = match.groups()
    return f'{attribute}="{urljoin(BASE, reference)}"'


def build(slug):
    plain = (ROOT / f'{slug}.txt').read_text()
    first, _, body = plain.partition('\n\n')
    subject = first.splitlines()[0].removeprefix('Subject: ')
    html = (ROOT / f'{slug}.html').read_text().replace('<base target="_top">', '')
    html = re.sub(r'\b(src|href)="([^"\n]+)"', absolute_reference, html)
    message = EmailMessage(policy=SMTP)
    message['Subject'] = subject
    message['X-Unsent'] = '1'
    message.set_content(body)
    message.add_alternative(html, subtype='html')
    message.set_boundary(f'brume-studio-{slug}')
    (ROOT / 'sources' / f'{slug}.eml').write_bytes(message.as_bytes())


if __name__ == '__main__':
    (ROOT / 'sources').mkdir(exist_ok=True)
    for letter in LETTERS:
        build(letter)
