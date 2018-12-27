#!/usr/bin/env python
# plaintext.py - removes formatting and converts to plaintext
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

pyperclip.copy(text)
