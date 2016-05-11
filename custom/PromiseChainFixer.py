# ParameterAfterBlockNewline.py
# Puts parameters following a block argument back on the same line instead of REALLY indenting on the next.
#
# If a filename is specified as a parameter, it will change that file in place.
# If input is provided through stdin, it will send the result to stdout.
# Copyright 2016 Square, Inc

from AbstractCustomFormatter import AbstractCustomFormatter

class PromiseChainFixer(AbstractCustomFormatter):
    def format_lines(self, lines):
        lines_to_write = []
        preceding_line_block_end = False

        for line in lines:
            stripped_line = line.strip()
            indentation_len = len(line) - len(line.lstrip())

            if (preceding_line_block_end and (stripped_line.startswith(".then") or stripped_line.startswith(".catch") or stripped_line.startswith(".finally"))):
                last = lines_to_write[-1]
                lines_to_write.pop()
                lines_to_write.append(last.rstrip() + line.lstrip())
            else:
                lines_to_write.append(line)

            if stripped_line == "})":
                preceding_line_block_end = True
            else:
                preceding_line_block_end = False

        return "".join(lines_to_write)

    
if __name__ == "__main__":
    PromiseChainFixer().run()