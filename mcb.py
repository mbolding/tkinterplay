#!/usr/bin/env python
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: mcb.py save <keyword> - Saves clipboard to keyword.
#        mcb.py <keyword> - Loads keyword to clipboard.
#        mcb.py list - list all keywords.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        print(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        print(mcbShelf[sys.argv[1]])
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
