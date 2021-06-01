#from gevent.pywsgi import WSGIServer
from app import app 


# Runs on DEBUG mode
app.run(host='0.0.0.0', port=5000, debug=False)

# http_server = WSGIServer(("0.0.0.0", 5000), app, log = None)
# http_server.serve_forever()

