#!/usr/bin/env python3
import sys
from whisperx.transcribe import cli

def main():
    return cli()

if __name__ == '__main__':
    sys.exit(main())

__all__ = ['main']
