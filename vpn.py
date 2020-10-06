# -*- coding: utf-8 -*-
"""
Display Active VPN using NetworkManager ActiveConnection

"""

import NetworkManager

class Py3status:

    def get_active_vpn(self):
        active_vpn = None
        for connection in NetworkManager.NetworkManager.ActiveConnections:
            if connection.Connection.GetSettings()['connection']['type'] == 'vpn':
                active_vpn = connection
        if active_vpn is None:
            output = "None"
            color = self.py3.COLOR_BAD
        else:
            output = active_vpn.Connection.GetSettings()['connection']['id']
            color = self.py3.COLOR_GOOD
        return {
            'full_text': 'VPN: %s' % (output),
            'color': color,
            'cached_until': self.py3.time_in(seconds=5)
        }


if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test
    module_test(Py3status)
