import time
import json
import logging
from django.utils.deprecation import MiddlewareMixin

request_logger = logging.getLogger('django.request')


class RequestLogMiddleware(MiddlewareMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def process_request(self, request):
        request.start_time = time.time()
        request_logger.info(json.dumps(self.extract_log_info(request)))

    def extract_log_info(self, request, response=None, exception=None):
        log_data = {
            'request_time': request.start_time,
            'request_method': request.method,
            'request_path': request.get_full_path(),
            'request_user': request.user.username,
            'remote_address': request.META['REMOTE_ADDR'],
            'request_body': request.body.decode(),
        }
        return log_data
