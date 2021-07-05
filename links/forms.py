from django.forms import (
    Form,
    ModelForm,
    IntegerField,
    ValidationError,
)
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)
from .constants import (
    AWESOMELINK_UNIQUE_ERROR,
    INVALID_RATING_ERROR,
    MAX_REDIRECT_COUNT,
    MAX_REDIRECT_ERROR,
    URL_STATUS_ERROR
)
from .helpers import (
    flatten_redirects,
    is_alive,
)
from .models import AwesomeLink
from .validators import (
    validate_awesomeness,
    validate_url,
)


class AwesomeLinkForm(ModelForm):
    class Meta:
        model = AwesomeLink
        fields = ['url']
        error_messages = {
            'url': {
                'unique': AWESOMELINK_UNIQUE_ERROR,
            },
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        validate_url(url)
        url, redirect_count = flatten_redirects(url)
        if redirect_count > MAX_REDIRECT_COUNT:
            raise ValidationError(MAX_REDIRECT_ERROR, code=400)
        if not is_alive(url):
            raise ValidationError(URL_STATUS_ERROR, code=400)
        validate_awesomeness(url)
        return url

class FlagForm(Form):
    pk = IntegerField()

class RatingForm(Form):
    pk = IntegerField()
    rating = IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        error_messages={
            'min_value': INVALID_RATING_ERROR,
            'max_value': INVALID_RATING_ERROR,
        }
    )
