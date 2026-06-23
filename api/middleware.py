import time


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        # Called once when Django starts up.
        # get_response is a callable — calling it runs the next
        # middleware in the chain (or the view itself if we're last).
        self.get_response = get_response

    def __call__(self, request):
        # Code here runs BEFORE the view
        start_time = time.time()

        # This line actually calls the view (or next middleware)
        response = self.get_response(request)

        # Code here runs AFTER the view returns
        duration_ms = (time.time() - start_time) * 1000

        print(
            f"[{request.method}] {request.path} "
            f"→ {response.status_code} "
            f"({duration_ms:.2f}ms)"
        )

        return response