#!/usr/bin/env python
import json
import sys

result = ''
trans_dic = {}
with open('trans.json', 'r') as f:
    trans_dic = json.load(f, encoding='utf-8')

args = sys.argv
if len(trans_dic) > 0 and len(args) > 1:
    s = args[1]
    s = s.lower()
    for c in s:
        if c in trans_dic:
            ct = trans_dic[c]
        else:
            ct = c
        result += ct
        # sys.stdout.write(ct)
        # sys.stdout.flush()

print(result)
# sys.stdout.write('\n')
# sys.stdout.flush()
