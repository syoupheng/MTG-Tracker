from django.core.exceptions import ValidationError
import magic
from django.utils.deconstruct import deconstructible

def FileSizeValidator(file): # add this to some file where you can import it from
    limit = 2500000
    if file.size > limit:
        raise ValidationError('File too large. Size should not exceed 2,5 MiB')

@deconstructible
class FileTypeValidator(object):
    error_messages = {
     'content_type': "Files of type %(content_type)s are not supported.",
    }

    def __init__(self, content_types=()):
        self.content_types = content_types

    def __call__(self, data):
        if self.content_types:
            content_type = magic.from_buffer(data.read(2048), mime=True)
            data.seek(0)

            if content_type not in self.content_types:
                params = { 'content_type': content_type }
                raise ValidationError(self.error_messages['content_type'],
                                   'content_type', params)

    def __eq__(self, other):
        return (
            isinstance(other, FileTypeValidator) and
            self.content_types == other.content_types
        )