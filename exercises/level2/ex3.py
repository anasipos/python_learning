__author__ = 'anamaria.sipos'

import time
import logging

logging.basicConfig(filename='func_dec.log', level=logging.DEBUG)


def log(message):
    print message
    logging.debug(message)


current_milli_time = lambda: int(round(time.time() * 1000))


def time_slow(arg):
    if callable(arg):
        def newfn(*args, **kw):
            log('no threshold specified')
            start_time = current_milli_time()

            # executing user function
            result = arg(*args, **kw)

            end_time = current_milli_time()
            log('{} execution took {} milliseconds'.format(arg.__name__, end_time - start_time))

            return result

        return newfn
    else:
        def time_slow_2(fn):
            def newfn(*args, **kw):
                log('threshold is specified = {}'.format(arg))
                start_time = current_milli_time()

                # executing user function
                result = fn(*args, **kw)

                end_time = current_milli_time()
                message = '{} execution took {} milliseconds. '
                total_time = end_time - start_time
                threshold = int(arg)
                if total_time > threshold:
                    message += 'It is above the threshold {}'
                else:
                    message += 'If is under the threshold {}'
                log(message.format(fn.__name__, total_time, threshold))

                return result

            return newfn

        return time_slow_2