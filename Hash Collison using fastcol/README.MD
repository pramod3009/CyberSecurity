A Hash Collision Attack

The collision attack lets us generate two messages with the same MD5 hash and an arbitrary but
identical prefix. (More expensive attacks allow generating collisions with different chosen prefixes.)
Due to MD5’s length-extension behavior, we can append any suffix to both messages and know that
the longer messages will also collide. This lets us construct files that differ only in a binary “blob”
in the middle and have the same MD5 hash, i.e. prefix k blob A k suffix and prefix k blob B k suffix.
We can leverage this to create two programs that have identical MD5 hashes but arbitrarily different
behaviors. We’ll use Python 3, but almost any language would do. Put the following three lines into
a file called prefix:
#!/usr/bin/python3
# coding: latin-1
blob = """

and put these three lines into a file called suffix:

"""
from hashlib import sha256
print(sha256(blob.encode("latin-1")).hexdigest())
Now use fastcoll to generate two files with the same MD5 hash that both begin with prefix.
($ fastcoll -p prefix -o col1 col2). Then append the suffix to both ($ cat col1 suffix
> file1.py; cat col2 suffix > file2.py). Verify that file1.py and file2.py have the
same MD5 hash but generate different output.
Extend this technique to produce a pair of programs, good.py and evil.py, that have identical
MD5 hashes. good.py should execute a benign payload: print("Use SHA-256 instead!").
evil.py should execute a pretend malicious payload: print("MD5 is perfectly secure!").
Ensure that your programs output only these messages, and that they exactly match what is specified.



https://www.win.tue.nl/hashclash/fastcoll_v1.0.0.5.exe.zip (Windows executable)
https://www.win.tue.nl/hashclash/fastcoll_v1.0.0.5-1_source.zip (source code)
If you are building fastcoll from source, you can compile using this makefile: https://
ecen4133.org/static/project1/Makefile. You will also need the Boost libraries. On Ubuntu,
you can install these using apt-get install libboost-all-dev. On OS X, you can install
Boost via the Homebrew package manager using brew install boost.

Generate your own collision with this tool.
($ time fastcoll -o file1 file2)
