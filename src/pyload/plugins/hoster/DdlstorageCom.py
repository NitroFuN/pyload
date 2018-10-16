# -*- coding: utf-8 -*-

from pyload.plugins.internal.deadhoster import DeadHoster


class DdlstorageCom(DeadHoster):
    __name__ = "DdlstorageCom"
    __type__ = "hoster"
    __version__ = "1.07"
    __status__ = "stable"

    __pyload_version__ = "0.5"

    __pattern__ = r"https?://(?:www\.)?ddlstorage\.com/\w+"
    __config__ = []  # TODO: Remove in 0.6.x

    __description__ = """DDLStorage.com hoster plugin"""
    __license__ = "GPLv3"
    __authors__ = [
        ("zoidberg", "zoidberg@mujmail.cz"),
        ("stickell", "l.stickell@yahoo.it"),
    ]
