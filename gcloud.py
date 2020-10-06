# -*- coding: utf-8 -*-
import os

class Py3status:

    def gcloudcontext(self):
        GCLOUDCONFIG = os.getenv('HOME') + "/.config/gcloud/active_config"
        f = open(GCLOUDCONFIG, 'r')
        GCLOUDACTIVECONFIG=f.read()
        f.close()
        return {
            'full_text': 'gcloud:' + GCLOUDACTIVECONFIG,
            'cached_until': self.py3.time_in(seconds=5)
        }

if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test
    module_test(Py3status)
