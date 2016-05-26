import os
import sys
import atexit
from time import sleep


class Writer(object):
    def __init__(self, out_file):
        self.out_file = file(out_file, 'w')

    def write(self, text):
        self.out_file.write(text)
        self.out_file.flush()

    def close(self):
        self.out_file.close()


def daemonize(**options):
    """
    Cache decorator
    """
    def cache_inside(fn, **kwargs):
        def wrapper(*args, **kwargs):
            log_file = options.get('log_file', 'out.log')
            w = Writer(log_file)
            sys.stdout = w

            fpid = os.fork()
            if fpid > 0:
                sys.exit(0)
            else:
                def on_exit():
                    w.close()

                atexit.register(on_exit)
                ret = fn(*args, **kwargs)
                return ret
        return wrapper
    return cache_inside


@daemonize(log_file='customlog.log')
def daemon_test():
    for i in range(10):
        print 'hello from daemon'
        sleep(1)


if __name__ == "__main__":
    daemon_test()
