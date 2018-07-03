#!/usr/bin/python3

# timed input function
# Tested on Windows and Linux; python2.7 and python3.6

from __future__ import print_function
try:
    input = raw_input # python2
except NameError:
    pass

#test for OS
try:
    # test for Unix-like
    import signal

    class TimeOutError(Exception): pass

    def _signal_handler(signum=None, frame=None):
        raise TimeOutError

    def timed_input(prompt='', timeout=None):
        """
        timed_input([prompt], [timeout]) -> string

        Read a string from standard input. The trailing newline is stripped.
        If the user does not press return in :timeout: seconds, None is returned.
        """
        if timeout is None:
            return input(prompt)
        try:
            signal.signal(signal.SIGALRM, _signal_handler)
            signal.alarm(timeout) # raise an error in timeout seconds
            data = input(prompt)
            signal.alarm(0) # cancel alarm
            return data
        except TimeOutError:
            print()

except ImportError:
    # signal is not available ... must be Windows-like OS
    from msvcrt import kbhit, getwch
    import time
    import sys

    def _print_flush(*args):
        print(*args, end='')
        sys.stdout.flush()

    def timed_input(prompt='', timeout=None):
        """
        timed_input([prompt], [timeout]) -> string

        Read a string from standard input. The trailing newline is stripped.
        If the user does not press return in :timeout: seconds, None is returned.

        The Windows version does not support arrow keys
        """
        if timeout is None:
            return input(prompt)
        _print_flush(prompt)
        start = time.time()
        response = ''
        while time.time() - start < timeout:
            if kbhit():
                char = getwch()
                if char == '\r':
                    break
                elif char == '\x08': # backspace
                    if response:
                        _print_flush(char, char)
                        response = response[:-1]
                else:
                    _print_flush(char)
                    response += char
            time.sleep(0.01)
        else:
            response = None
        print()
        return response


### Test / Demo code:
def main():
    key = 'pass'
    time_limit = 4 # in seconds
    validation = timed_input('Enter your verification code here: ', time_limit)

    if validation == key:
        print('Success! Please continue to download.')
    elif validation is None:
        print('you have exceeded your time limit')
    else:
        print('Wrong verification code. Access Denied.')

if __name__ == '__main__':
    main()
