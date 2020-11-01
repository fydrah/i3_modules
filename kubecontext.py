# -*- coding: utf-8 -*-
import os
import yaml

class Py3status:

    def _getns(self, ctxname):
        for ctxtmp in self.kube['contexts']:
            if ctxtmp['name'] == ctxname:
                if 'namespace' in ctxtmp['context'].keys():
                    return ctxtmp['context']['namespace']
                else:
                    return 'default'

    def kubestatus(self):
        SYMBOL = u'\u2388'
        KUBECONFIG = os.getenv('HOME') + "/.kube/config"
        f = open(KUBECONFIG, 'r')
        self.kube = yaml.load(f)
        f.close()
        return {
            'full_text': SYMBOL + ' ' + self.kube['current-context'] + ':' + self._getns(self.kube['current-context']),
            'cached_until': self.py3.time_in(seconds=5)
        }

if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test
    module_test(Py3status)
