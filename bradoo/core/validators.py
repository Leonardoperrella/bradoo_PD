from django.core.exceptions import ValidationError


def validate_cnpj(value):
        if not value.isdigit():
            raise ValidationError('CNPJ must have only numbers.', 'digits')

        if len(value) != 14:
            raise ValidationError('CNPJ must have 14 digits.', 'length')