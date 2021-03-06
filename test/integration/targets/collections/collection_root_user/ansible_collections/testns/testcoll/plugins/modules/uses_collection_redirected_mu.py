#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import json
import sys

from ansible_collections.testns.testcoll.plugins.module_utils.moved_out_root import importme


def main():
    mu_result = importme()
    print(json.dumps(dict(changed=False, source='user', mu_result=mu_result)))

    sys.exit()


if __name__ == '__main__':
    main()
