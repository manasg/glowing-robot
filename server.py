from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import datetime

# thank you coding horror!
import re
pattern = re.compile('(x+x+)+y')
def compute_regex(str_len=20):
    string = "x" * str_len
    result = pattern.match

    if result:
        return result.span()
    else:
        return "no_match"

import math
def compute_factorial(x=20):
    return math.factorial(x)

class ReqHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        start = datetime.datetime.now()
        
        num_digits = len(str(compute_factorial(x=80000)))
        resp = "Number of digits %d " % num_digits
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(resp)

        end = datetime.datetime.now()
        print "Took %s seconds for req" % str(end - start)

import SocketServer
class ThreadingSimpleServer(SocketServer.ThreadingMixIn, HTTPServer):
    pass


def serve():
    server = ThreadingSimpleServer(('localhost',9090), ReqHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print "terminated!"


if __name__ == "__main__":
    serve() 
