#import bottle
#from bottle import response

def enable_cors():
  def decorator(function):
    def decorated(self, *args, **kwargs):
      self.set_header("Access-Control-Allow-Origin", "*")
      return function(self, *args, **kwargs)
    return decorated
  return decorator
