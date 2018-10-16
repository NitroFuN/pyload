# -*- coding: utf-8 -*-

from pyload.plugins.internal.deadcrypter import DeadCrypter


class NetfolderIn(DeadCrypter):
    __name__ = "NetfolderIn"
    __type__ = "crypter"
    __version__ = "0.78"
    __status__ = "stable"

    __pyload_version__ = "0.5"

    __pattern__ = r"http://(?:www\.)?netfolder\.(in|me)/(folder\.php\?folder_id=)?(?P<ID>\w+)(?(1)|/\w+)"
    __config__ = [("activated", "bool", "Activated", True)]

    __description__ = """NetFolder.in decrypter plugin"""
    __license__ = "GPLv3"
    __authors__ = [
        ("RaNaN", "RaNaN@pyload.net"),
        ("fragonib", "fragonib[AT]yahoo[DOT]es"),
    ]
