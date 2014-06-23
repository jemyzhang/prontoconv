__author__ = 'jemyzhang'

import os
import sys

root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, '../'))

from ProntoConv import ProntoConv
from NoviiDB import Novii

customcode = 0x9f00

keys = [
    ('Power On', 0x57),
    ('Notification', 0x5b),
    ('Rewind', 0x0b),
    ('Forward', 0x0f),
    ('Up', 0x43),
    ('Down', 0x0a),
    ('Left', 0x06),
    ('Right', 0x0e),
    ('Center', 0x02),
    ('Menu', 0x16),
    ('Home', 0x47),
    ('Back', 0x4f),
    ('Vol+', 0xff),
    ('Vol-', 0x5d)
]

if __name__ == '__main__':
    pronto = ProntoConv()
    novii = Novii()
    novii.setpdb('sample.pdb')
    for n, k in keys:
        prontocode = pronto.conv(customcode, k)
        noviidata = novii.conv(prontocode)
        rec = novii.makerec(noviidata, n)
        novii.addrec(rec)
    novii.savedb('Tmall.pdb', 'TmallBox')
