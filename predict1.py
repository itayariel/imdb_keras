from cnvrg import Endpoint

def predict(*args):
    e = Endpoint()
    print("got {}".format(args[0]))
    e.log_metric("accuracy", args[0])
    return args[0]
