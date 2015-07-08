# ################################################################################
# ##
# ##  https://github.com/NetASM/NetASM-python
# ##
# ##  File:
# ##        dumper.py
# ##
# ##  Project:
# ##        NetASM: A Network Assembly Language for Programmable Dataplanes
# ##
# ##  Author:
# ##        Muhammad Shahbaz
# ##
# ##  Copyright notice:
# ##        Copyright (C) 2014 Princeton University
# ##      Network Operations and Internet Security Lab
# ##
# ##  Licence:
# ##        This file is a part of the NetASM development base package.
# ##
# ##        This file is free code: you can redistribute it and/or modify it under
# ##        the terms of the GNU Lesser General Public License version 2.1 as
# ##        published by the Free Software Foundation.
# ##
# ##        This package is distributed in the hope that it will be useful, but
# ##        WITHOUT ANY WARRANTY; without even the implied warranty of
# ##        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# ##        Lesser General Public License for more details.
# ##
# ##        You should have received a copy of the GNU Lesser General Public
# ##        License along with the NetASM source package.  If not, see
# ##        http://www.gnu.org/licenses/.

__author__ = 'shahbaz'

from optparse import OptionParser
from parser import Parser


def main():
    op = OptionParser()
    op.add_option('--ifile', action="store", dest="ifile")
    op.add_option('--ofile', action="store", dest="ofile")

    op.set_defaults(ofile='./dumped.out')
    options, args = op.parse_args()

    if not options.ifile:
        print '--ifile flag not specified.'
        exit(1)

    ifile = open(options.ifile)
    ofile = open(options.ofile, 'w')

    parser = Parser()
    policy, errors_cnt = parser.parse(ifile.read())

    ofile.write(str(policy))
    ofile.write('\n')
    ofile.write('Total errors: ' + str(errors_cnt))

    ifile.close()
    ofile.close()


main()
