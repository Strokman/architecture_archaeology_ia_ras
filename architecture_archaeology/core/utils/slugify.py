from django.utils.text import slugify as django_slugify

alphabet = {'а': 'a',
            'б': 'b',
            'в': 'v',
            'г': 'g',
            'д': 'd',
            'е': 'e',
            'ё': 'yo',
            'ж': 'zh',
            'з': 'z',
            'и': 'i',
            'й': 'j',
            'к': 'k',
            'л': 'l',
            'м': 'm',
            'н': 'n',
            'о': 'o',
            'п': 'p',
            'р': 'r',
            'с': 's',
            'т': 't',
            'у': 'u',
            'ф': 'f',
            'х': 'kh',
            'ц': 'ts',
            'ч': 'ch',
            'ш': 'sh',
            'щ': 'shch',
            'ь': '',
            'ъ': '',
            'ы': 'i',
            'э': 'e',
            'ю': 'yu',
            'я': 'ya'}


def slugify(s, *args, **kwargs):
    """
    Так как Django не умеет в кириллицу в случае с slug'ами, то сделал такую функцию
    для транслитерации.
    """
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()), *args, **kwargs)
