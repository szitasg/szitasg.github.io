#!python3

import urllib3
import requests


if __name__ == '__main__':
    urllib3.disable_warnings()

    stylesheet_file = './assets/css/main'

    with open(f'{stylesheet_file}.css', 'r') as input_file, \
            open(f'{stylesheet_file}.min.css', 'w', newline='\n') as output_file:
        r = requests.post('http://cssminifier.com/raw',
                          data={'input': input_file.read()},
                          verify=False)
        output_file.write(r.text)
        output_file.write('\n')
