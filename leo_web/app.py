from flask import Flask, jsonify
from werkzeug.routing import BaseConverter
app = Flask(__name__)
MAX_FIB_SEQUENCE_LENGTH = 1000

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

app.url_map.converters['regex'] = RegexConverter

def fibNthGen(n,a=0,b=1):
    while n>0:
        yield a
        a,b,n = b,a+b,n-1

@app.route('/<regex("-?\d+"):sequence_requested>')
def calculate_nth_fib(sequence_requested):
    sequence_requested = int(sequence_requested)
    if sequence_requested > -1 and sequence_requested < MAX_FIB_SEQUENCE_LENGTH:
        msg_obj = {'sequence_requested': sequence_requested, 'results': {i:fib for i, fib in enumerate(fibNthGen(sequence_requested))} }
    elif sequence_requested < 0:
        err_msg = 'sequence_requested must be a positive integer.'
        msg_obj = {'sequence_requested': sequence_requested, 'results': '', 'error': err_msg}
    else:
        err_msg = "The hampsters powering our CPUs need a rest. Keep your request below {0}.".format(MAX_FIB_SEQUENCE_LENGTH)
        msg_obj = {'sequence_requested': sequence_requested, 'results': '', 'error': err_msg}
    response = jsonify(**msg_obj)
    return(response)

if __name__ == '__main__':
    app.run()
