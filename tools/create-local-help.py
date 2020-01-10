#!/usr/bin/env python3


from pathlib import Path
import os
import re


def read_file(filename):
    f = open(filename, 'r')
    content = f.read()
    f.close()
    return content


def write_file(filename, content):
    f = open(filename, 'w')
    f.write(content)
    f.close()


def generate_file(destdir, lang, file):
    print("generate local help in " + destdir + "/" + lang + "/" + file)

    content = read_file("../_site/" + lang + "/" + file + ".html")

    content = re.sub(r"^.*<div id=\"content\">.*<h1>.*?</h1>.*?<ul.*?>",
                       "<!DOCTYPE html>\n"
                     + "<html>"
                     +   "<head>"
                     +     "<meta charset=\"UTF-8\" />"
                     +     "<link rel=\"stylesheet\" href=\"../help.css\" />"
                     +   "</head>"
                     +   "<body>"
                     +     "<ul id=\"top\">",
                     content,
                     flags=re.MULTILINE|re.DOTALL)

    content = re.sub(r"</div>.*?</body>.*</html>.*$",
                         "</body>"
                     + "</html>",
                     content,
                     flags=re.MULTILINE|re.DOTALL)

    write_file(destdir + "/" + lang + "/" + file + ".html", content)


def generate_lang(destdir, lang):
    generate_file(destdir, lang, "help")


def generate_help(destdir):
    generate_lang(destdir, "en")


if __name__ == "__main__":

    # if we're not inside the tools directory, go in
    if Path('tools').exists():
        os.chdir('tools')

    generate_help("../../deltachat-android/assets/help")