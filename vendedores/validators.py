import re
from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.utils.translation import ugettext_lazy as _

error_messages = {
    "invalid": _("CPF  Inválido."),
    "digits_only": _("Digite apenas dígitos."),
    "max_digits": _("Digite no máximo 11 digitos."),
}

invalid = [
    "11111111111",
    "22222222222",
    "33333333333",
    "44444444444",
    "55555555555",
    "66666666666",
    "77777777777",
    "88888888888",
    "99999999999",
    "00000000000",
]


def DV_maker(v):
    if v >= 2:
        return 11 - v
    return 0


def validate_CPF(value):
    """
    Value can be either a string in the format XXX.XXX.XXX-XX or an
    11-digit number.
    """

    if value in EMPTY_VALUES:
        return u""
    if not value.isdigit():
        value = re.sub("[-\.]", "", value)
    orig_value = value[:]
    try:
        int(value)
    except ValueError:
        raise ValidationError(error_messages["digits_only"])
    if len(value) != 11:
        raise ValidationError(error_messages["max_digits"])
    if value in invalid:
        raise ValidationError(error_messages["invalid"])
    orig_dv = value[-2:]

    new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(range(10, 1, -1))])
    new_1dv = DV_maker(new_1dv % 11)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(range(11, 1, -1))])
    new_2dv = DV_maker(new_2dv % 11)
    value = value[:-1] + str(new_2dv)
    if value[-2:] != orig_dv:
        raise ValidationError(error_messages["invalid"])

    return "{}.{}.{}-{}".format(
        orig_value[:3], orig_value[3:6], orig_value[6:9], orig_value[9:]
    )
