import requests

from  requests.exceptions import MissingSchema
from http import HTTPStatus


class BadUrlError(Exception):
    """Raise if HTTPStatus is not OK"""

class Report(object):
    def __init__(self, url, keyword):
        self.keyword = keyword
        try:
            response = requests.get(url)
        except MissingSchema as exception:
            raise BadUrlError(
                'Нет соединения с {0}: {1}'.format(url, exception),
            )

        if response.status_code == HTTPStatus.OK:
            self.url = url
        else:
            raise BadUrlError('Нет соединения с {0}'.format(url))

    def _get_data(self):
        pass

    def _validate(self):
        pass

    def _format_data(self):
        """  """
        pass

    def get_report(self):
        pass


report = Report('https://krasnodar.hh.ru/', 'python')
print(report.get_report())  # noqa: WPS421
