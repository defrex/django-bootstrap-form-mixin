#!/usr/bin/env python
import sys

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    sys.argv += ['--settings=settings', '--pythonpath=../']

    execute_from_command_line(sys.argv)
