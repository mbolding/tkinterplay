#!/usr/bin/env python

file = open("e/p022_names.txt")
lines = sorted(file.read().split(","))


file.close()
lines[0].replace('"', "")
[ord(c) - 64 for c in lines[0] if c != '"']

for i in range(11):
    print(lines[i], sum([ord(c) - 64 for c in lines[i] if c != '"']))

idx = 0
for line in lines:
    idx += 1
    if line == '"COLIN"':
        break
idx
sum([ord(c) - 64 for c in '"COLIN"' if c != '"'])

idx = 0
total = 0
for line in lines:
    idx += 1
    total += idx * sum([ord(c) - 64 for c in line.replace('"', "")])

total
idx
