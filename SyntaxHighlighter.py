# Syntax highlighter - convert python code into html entities
# At the moment this is just a code viewer, but before long,  it'll be something awesome.

import keyword # Contains a list of all the python keywords.
import re

class DocumentObj:
    def __init__(self, text = ''):
        self.text = text

    def robust_split(self, string, sep):
        # sep as a list of seperation strings
        output_list = []

        last_break_index = 0

        for index, char in enumerate(string):
            for s in sep:
                if char == s[0]:
                    if string[index:index+len(s)] == s:
                        #Break the string here
                        output_list.append(string[last_break_index:index])
                        last_break_index = index
        output_list.append(string[last_break_index:])
        return output_list

    def convert_to_html(self):
        # Work on a line-by-line basis
        outlines = []
        inlines = self.text.splitlines(keepends=True)
        seperation = [" ", ":", ".", "(",")"]
        italic_list = ['self', 'super', 'int', 'str', 'bool']

        for inline in inlines:
            outline = ''
            # Anything in brackets should be in italics
            tmpinline = inline
            inline = ''
            for c in tmpinline:
                if c == "(":
                    inline += "(<em>"
                elif c == ")":
                    inline += "</em>)"
                else:
                    inline += c

                if c == "\t":
                    inline += "&nbsp;"*4

            for index, word in enumerate(self.robust_split(inline, seperation)):
                if "#" in word:
                    outline += "<em>"+"".join(self.robust_split(inline, seperation)[index:])+"</em>"
                    break
                test_word = word.strip("".join(seperation))
                if test_word in keyword.kwlist:
                    outline += "<strong>{0}</strong>".format(word)
                elif test_word in italic_list:
                    outline += "<strong>{0}</strong>".format(word)
                else:
                    outline += word #+" "
            outlines.append(outline)

        return outlines
