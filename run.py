#!/usr/bin/env python3

import subprocess
import shutil
import sys

with open('stdout.txt', 'w') as stdout:
    p = subprocess.run(['Rectify.sh', 'input_0.png', 'input_1.png'], stdout=stdout, stderr=stdout)

if p.returncode != 0:
    with open('demo_failure.txt', 'w') as file:
        file.write("No Match Error")
        sys.exit(0) 

mv_map = {'input_0.png_input_1.png_pairs_orsa.txt' : 'orsa.txt',
            'input_0.png_h.txt' : 'output_0.txt',
            'input_1.png_h.txt' : 'output_1.txt',
            'H_input_0.png' : 'output_0.png',
            'H_input_1.png' : 'output_1.png',
            'show_H_input_0.png' : 'output_0_annotated.png',
            'show_H_input_1.png' : 'output_1_annotated.png'}
for (src, dst) in mv_map.items():
    shutil.move(src, dst)
