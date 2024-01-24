import sys
import os
import subprocess
import yaml
import re
import importlib

bad_libraries = ["os", "posix", "subprocess",
                 "codecs", "inspect", "ast",
                 "json", "csv", "pathlib",
                 "shutil", "linecache", "glob",
                 "filecmp", "fileinput", "os.path",
                 "pickle", "marshal", "csv", "configparser",
                 "tomllib", "plistlib", "tarfile", "zipfile",
                 "lzma", "bz2", "gzip", "zlib", "mimetypes",
                 "html", "html.parser", "pdb", "builtins", "code",
                 "codeop", "importlib", "token", "tokenize", "syslog",
                 "tty", "pty"]

bad_libraries_audit = ["os", "commands", "pty" ,"posix", "subprocess", "codecs", "inspect", "ast", "pathlib", "shutil", "linecache", "glob", "filecmp", "fileinput", "os.path", "pickle", "tarfile", "zipfile", "pdb", "code", "token", "tokenize", "syslog"]

BAD = re.compile(r"(\_|import|open|\s|\}|\{|\]|\[)")

for b in bad_libraries:
    if b in sys.modules:
        sys.modules.pop(b)


def secure_importer(name, globals=None, locals=None, fromlist=(), level=0):
    if name in bad_libraries:
        raise ImportError("module '%s' is restricted." % name)
    return importlib.__import__(name, globals, locals, fromlist, level)


# just to make sure you dont use these
def audit(event, args):
    for bad in bad_libraries_audit:
        if bad in event:
            print("You are trying to escape!!")
            exit()


def do_eval(prompt, config):
    return eval(prompt, {'__builtins__':{},'globals': {}}, {'config':config, '__builtins__':{}})


def main():
    yaml_conf = ascii(input("yaml: "))[1:-1]
    if yaml_conf.count('/') > 1 or BAD.search(yaml_conf) or '.' in yaml_conf:
        print("BAD YAML!!")
        exit(1)

    config = yaml.load(yaml_conf, yaml.Loader)
    prompt = ascii(input(">>> "))[1:-1]
    sys.addaudithook(audit)

    if len(prompt) > 42:
        print("TOO LONG!!")
        exit(1)

    print(do_eval(prompt, config))

    while True:
        prompt = ascii(input(">>> "))[1:-1]
        if len(prompt) > 48 or BAD.search(prompt):
            print("TOO LONG OR BAD PROMPT!!")
            exit(1)

        print(do_eval(prompt, config))

__builtins__.__dict__['__import__'] = secure_importer

try:
    main()
except Exception as ext:
    print(ext)
    exit(1)
