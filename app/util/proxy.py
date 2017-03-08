# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import socks
import socket

from app.you_get.common import set_http_proxy

__author__ = "ingbyr"


def m_set_socks_proxy(address, port):
    socks.set_default_proxy(socks.SOCKS5, address, int(port))
    socket.socket = socks.socksocket
    def getaddrinfo(*args):
        return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]
    socket.getaddrinfo = getaddrinfo


def m_set_http_proxy(address, port):
    set_http_proxy(address + ':' + port)


def disable_proxy():
    set_http_proxy('')
    #socks.set_default_proxy()
    #socket.socket = socks.socksocket
