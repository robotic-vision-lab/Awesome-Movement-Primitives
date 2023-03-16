#!/usr/bin/env python3

import glob

#Purpose: reformat markdown file github link into awesome format

with open('README.md', 'r') as f:
    lines = f.readlines()

# convert github url to shields io link
match_str = 'https://github.com/'

for i, line in enumerate(lines):
    if len(line) > len(match_str):
        if match_str in line[:len(match_str)+1]:
            cl_line = line.split('\n')[0]
            authrepo = cl_line.split(match_str)[1]
            sg_ico = f"https://img.shields.io/github/stars/{authrepo}?style=social"
            lines[i] = f"[{authrepo}]({cl_line}):  [![GitHub stars]({sg_ico})]({sg_link}/stargazers/)\n"

# replace shield.io badges with local icos
icos = glob.glob('ico/*.png')

for i, line in enumerate(lines):
    if len(line) > 10:
        if '![' in line[:2]:
            desired_badge = line.split('[')[1].split(']')[0].lower()
            desired_badge = desired_badge.replace('+','p').replace(' notebook', '')
            badge = [b for b in icos if desired_badge in b][0]
            lines[i] = f'<img src="./{badge}" height="20" /> \n'


# update github badge to html image tag
match_ghs = '[![GitHub stars]'

for i, line in enumerate(lines):
    if len(line) > len(match_ghs):
        if match_ghs in line[:len(match_str)+1]:
            shield_link = line.split('(')[1].split(')')[0]
            stargazer_link = line.split(')')[1].split('(')[1]
            lines[i] = f'<a href="{stargazer_link}"><img src="{shield_link}" height="20" /></a> \n'


# wrap paragraph so badges are on same line

for i, line in enumerate(lines):
    if len(line) > 10 and i > 0:
        if '<img' in line[:10] and len(lines[i-1]) < 3:
            lines[i-1] = '\n<p float="left">\n'
        if '</a>' in line[-10:] and len(lines[i+1]) < 3:
            lines[i+1] = '</p>\n\n'

with open('README.md', 'w') as f:
    f.writelines(lines)
