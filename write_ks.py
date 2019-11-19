#!/usr/bin/env python
import os
import sys

sys.path.append(os.path.expanduser('~/git/compute-image-tools/daisy_workflows/image_build/enterprise_linux'))

import ks_helpers

ks_content = ks_helpers.BuildKsConfig('rhel7', 'stable', False, False, True)
def WriteFile(file_path, content, mode='w'):
    with open(file_path, mode) as fp:
        fp.write(content)

WriteFile('/tmp/rhel7-uefi.ks.cfg', ks_helpers.BuildKsConfig('rhel7', 'stable', False, False, True))
WriteFile('/tmp/rhel7.ks.cfg', ks_helpers.BuildKsConfig('rhel7', 'stable', False, False, False))
