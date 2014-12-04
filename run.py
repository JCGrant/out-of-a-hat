#!/usr/bin/env python2

import os

from out_of_a_hat import app

if __name__ == '__main__':
    if os.environ.get('DATABASE_URL') is None:
        app.run(debug=True, host='0.0.0.0')
    else:
        app.run()
