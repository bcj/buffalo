"""
A novel about bison that bother.
"""
from argparse import ArgumentParser
from random import sample


WORDS = {
    'action': ('buffalo', 'bother'),
    'animal': ('buffalo', 'bison'),
    'city': ('Buffalo', 'Buffalo'),
}

SENTENCE_FORMS = {
    ('subject',),
    ('verb',),
    ('object',),
    ('subject', 'verb'),
    ('verb', 'object'),
    ('subject', 'verb', 'object')
}


COMPONENTS = {
    'subject': {
        ('animal',),
        ('city', 'animal'),
        ('subject', 'subject', 'verb'),
    },
    'verb': {
        ('action',)
    },
    'object': {
        ('animal',),
        ('city',),
        ('city', 'animal'),
        ('subject',),
    }
}

PUNCTUATION = {
    (('.', False),),
    (('!', False),),
    (('?', False), ('.', True)),
    (('?', False), ('!', True)),
    (('?', False), ('.', True), ('!', False)),
}


def capitalize(word):
    """
    Capitalize a word
    """
    return '{}{}'.format(word[0:1].upper(), word[1:])


def generate(expected, synonoms=False):
    sentences = []
    length = 0
    while length < expected:
        words = []

        parts = list(reversed(sample(SENTENCE_FORMS, 1)[0]))

        while parts:
            part = parts.pop()

            if part in WORDS:

                options = WORDS[part]

                words.append(options)
            else:
                parts.extend(reversed(sample(COMPONENTS[part], 1)[0]))

        for punctuation, use_synonyms in sample(PUNCTUATION, 1)[0]:
            length += len(words)
            index = synonoms and use_synonyms

            sentences.append(
                '{}{}'.format(
                    capitalize(
                        ' '.join(options[index] for options in words)
                    ),
                    punctuation
                )
            )

    return ' '.join(sentences)


def main():
    parser = ArgumentParser(description="Write a story about bison.")
    parser.add_argument(
        '--length', '-l', default=50000, type=int,
        help="Minimum length of the story."
    )
    parser.add_argument(
        '--allow-synonyms', '-s', action='store_true',
        help="Allow synonyms for buffalo?"
    )

    args = parser.parse_args()

    print(generate(args.length, args.allow_synonyms))


if __name__ == '__main__':
    main()
