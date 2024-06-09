# Write up for quoter challenge

## Description
You can read some quotes from famous guys and also you can view their picture :)

## Solve

Three steps to read the flag

1. bypass LFI check
2. open the flag.txt file with */image* or */* path
3. read the flag.txt file with `/proc/self/fd/<FDNUMBER>`


because the `../` replace with `""`, we can bypass this check with `..././` and after replacing `../`, the path becomes `../`

The main idea of this challenge is to read the flag.txt with file-descriptors for current running process: `/proc/self/fd/...`

because the code will open the given file and store it into an global variable, the targeted file will be open always and will never close, so as you may know, when you open a file in linux, a link-file to target file will created in */proc/self/fd* directory

```python
>>> import os
>>> file = open("/etc/passwd") # open file and donot close it
>>> os.listdir("/proc/self/fd")
['0', '1', '2', '3', '4'] # here 0,1,2 are (stdin, stdout, stderr)
>>> with open("/proc/self/fd/3", "r") as fdfile:
...		print(fdfile.read())
...
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
...
>>> # the /etc/passwd contnet will print out
```


the final script "solve.py"