# -*- coding: utf-8 -*-

from pyload.plugins.internal.simplecrypter import SimpleCrypter
import json


class NitroflareComFolder(SimpleCrypter):
    __name__ = "NitroflareComFolder"
    __type__ = "crypter"
    __version__ = "0.08"
    __status__ = "testing"

    __pyload_version__ = "0.5"

    __pattern__ = (
        r"https?://(?:www\.)?nitroflare\.com/folder/(?P<USER>\d+)/(?P<ID>[\w=]+)"
    )
    __config__ = [
        ("activated", "bool", "Activated", True),
        ("use_premium", "bool", "Use premium account if available", True),
        (
            "folder_per_package",
            "Default;Yes;No",
            "Create folder for each package",
            "Default",
        ),
        ("max_wait", "int", "Reconnect if waiting time is greater than minutes", 10),
    ]

    __description__ = """Nitroflare.com folder decrypter plugin"""
    __license__ = "GPLv3"
    __authors__ = [("Walter Purcaro", "vuolter@gmail.com")]

    def get_links(self):
        html = self.load(
            "http://nitroflare.com/ajax/folder.php",
            post={
                "userId": self.info["pattern"]["USER"],
                "folder": self.info["pattern"]["ID"],
                "page": 1,
                "perPage": 10000,
            },
        )
        res = json.loads(html)
        if res["name"]:
            self.pyfile.name = res["name"]
        else:
            self.offline()

        return [link["url"] for link in res["files"]] if "files" in res else None
