# -*- coding: utf-8 -*-
import os
import configparser

class Py3status:

    def gcloudcontext(self):
        GCLOUDCONFIG_DIR = os.getenv('HOME') + '/.config/gcloud'
        GCLOUDCONFIG = GCLOUDCONFIG_DIR + '/active_config'
        f = open(GCLOUDCONFIG, 'r')
        gcloud_activeconfig=f.read()
        f.close()
        gcloud_config = configparser.ConfigParser()
        gcloud_config.read(GCLOUDCONFIG_DIR + '/configurations/config_' + gcloud_activeconfig)
        gcloud_project = ''
        try:
            gcloud_project = ':' + gcloud_config['core']['project']
        except KeyError:
            pass
        return {
            'full_text': 'gcloud:' + gcloud_activeconfig + gcloud_project,
            'cached_until': self.py3.time_in(seconds=5)
        }

if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test
    module_test(Py3status)
