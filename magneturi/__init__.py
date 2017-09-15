#!/usr/bin/env python3
"""Produce magnet URIs for Bittorrent files

inspired from http://stackoverflow.com/a/12480263/107049
"""
import os
from magneturi import bencode
import hashlib
import base64
import urllib.parse


def from_torrent_data(torrent_contents):
    """
    return a magnet URI given Bittorrent torrent file content
    """
    metadata = bencode.bdecode(torrent_contents)
    hash_contents = bencode.bencode(metadata['info'])
    digest = hashlib.sha1(hash_contents).digest()
    b32hash = base64.b32encode(digest)

    if 'announce-list' in metadata:
        tracker_list = ''.join(['&tr='+urllib.parse.quote_plus(t[0]) \
                                for t in metadata['announce-list']])
    elif 'announce' in metadata:
        tracker_list = '&tr='+urllib.parse.quote_plus(metadata['announce'])
    else:
        tracker_list = ''

    result = ''.join([b32hash.decode('ASCII'), tracker_list])
    return 'magnet:?xt=urn:btih:%s' % result


def from_torrent_file(torrent_file):
    """
    return a magnet URI given Bittorrent torrent file
    """
    assert os.path.isfile(torrent_file)
    with open(torrent_file, "rb") as f:
        torrent_contents = f.read()
    return from_torrent_data(torrent_contents)
