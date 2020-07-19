#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

print('Converts a decimal number to hexadecimal and creates a color code.')

color_code = '#'
arr = ['R', 'G', 'B']

for c in arr:
    print('input ' + c + ' (ex. 150)')
    try:
        input_num = int(input())

        if input_num > 255 or input_num < 0:
            raise Exception

    except Exception:
        print('invalid input')
        sys.exit()

    # dec -> hex & 0 padding
    input_hex = format(input_num, 'x').zfill(2)
    color_code += input_hex

print('color code : ' + color_code)
