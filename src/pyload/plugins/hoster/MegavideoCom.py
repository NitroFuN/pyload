# -*- coding: utf-8 -*-

from pyload.plugins.internal.deadhoster import DeadHoster


class MegavideoCom(DeadHoster):
    __name__ = "MegavideoCom"
    __type__ = "hoster"
    __version__ = "0.26"
    __status__ = "stable"

    __pyload_version__ = "0.5"

    __pattern__ = r"http://(?:www\.)?megavideo\.com/\?.*&?(d|v)=\w+"
    __config__ = []  # TODO: Remove in 0.6.x

    __description__ = """Megavideo.com hoster plugin"""
    __license__ = "GPLv3"
    __authors__ = [("jeix", "jeix@hasnomail.de"), ("mkaay", "mkaay@mkaay.de")]
