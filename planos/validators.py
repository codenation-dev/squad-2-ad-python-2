from django.core.exceptions import ValidationError


def validate_percent_max_menor_que_percent_min(percent_max, percent_min):
    """
    Valida se o percentual máximo é menor que o percentual mínimo
    """
    if (percent_max < percent_min):
        raise ValidationError(
            "O percentual mínimo é maior que o percentual máximo.")
