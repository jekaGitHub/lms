from rest_framework.serializers import ValidationError


class UrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val not in ('youtube.com',):
            raise ValidationError("Нельзя использовать ссылки на сторонние ресурсы.")
