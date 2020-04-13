from django.middleware import csrf
class SetCSRFMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    csrf.get_token(request)
    response = self.get_response(request)
    return response