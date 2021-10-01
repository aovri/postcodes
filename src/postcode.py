import re


# NOTE: Must pass all rules below
basic_checks = [
    # Just a basic check
    '^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$',
    # The letters Q, V and X are not used in the first position
    # The letters I, J and Z are not used in the second position
    # Last two characters must exclude C, I, K, M, O or V
    '^([A-PR-UWYZ][A-HK-Y1-9]?([0-9][A-Z0-9]?) ?[0-9][ABD-HJLNP-UW-Z]{2})$',
]

# NOTE: Rules for outward codes only
left_checks = [
    # AA9A
    '^((?:EC1|EC2|EC3|EC4|SW1)[ABEHMNPRVWXY])$',
    '^((?:WC1|WC2)[ABEHMNPRVWXY])$',
    'NW1W',
    'SE1P',

    # A9A
    '^(W1[ABCDEFGHJKPSTUW])$',
    'N1C',
    'N1P',
    'E1W',

    # A9
    '^((?:[BEGLMNSW])[1-9])$',

    # A99
    '^((?:[BEGLMNSW])[1-9]{2})$',

    # AA9
    '^((?:BL|BS|CM|CR|FY|HA|PR|SL|SS)0)$', # the only codes that can have 0
    '^((?:BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WN|ZE)[1-9])$',
    '^((?:(?!AB|LL|SO)[a-zA-Z]{2})[1-9])$', # AB|LL|SO can only have two digits

    # AA99
    '^((?:AB|LL|SO)[1-9]{2})$',
    '^((?:(?!BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WN|ZE)[a-zA-Z]{2})[1-9]{2})$', # BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WN|ZE can only have a single digit digit

    # Special cases
    # TODO: This is broken as it passes codes like FY11 (that can only have a single digit)
    '^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$',
]


def _is_left_valid(s):
    for p in left_checks:
        if m := re.match(p, s):
            return True
    return False

def _is_basic_valid(s):
    for p in basic_checks:
        if not (m := re.match(p, s)):
            return False
    return True

def is_valid(code):
    if not code or not isinstance(code, str):
        return False

    # NOTE: My regex patterns rely on upper
    cleancode = code.replace(' ', '').upper()
    if not _is_basic_valid(cleancode):
        return False

    # I don't really need right, so can actually drop it
    left, right = cleancode[:-3], cleancode[-3:]
    if not _is_left_valid(left):
        return False

    return True
