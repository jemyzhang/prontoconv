__author__ = 'jemyzhang'

import os
import sys

root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, '../'))

from ProntoConv import ProntoConv
from NoviiDB import Novii

customcode = 0x9f00

keynames = ('Power', 'Notification', 'Rewind', 'Forward',
            'Up', 'Down', 'Left', 'Right',
            'Center', 'Menu', 'Home', 'Back',
            'Vol+', 'Vol-')
keycodes = (0x57, 0x5b, 0x0b, 0x0f,
            0x43, 0x0a, 0x06, 0x0e,
            0x02, 0x16, 0x47, 0x4f,
            0xff, 0x5d)

if __name__ == '__main__':
    keys = zip(keynames, keycodes)
    pronto = ProntoConv()
    novii = Novii()
    novii.setpdb('sample.pdb')
    for n, k in keys:
        prontocode = pronto.conv(customcode, k)
        noviidata = novii.conv(prontocode)
        rec = novii.makerec(noviidata, n)
        novii.addrec(rec)
    novii.savedb('Tmall.pdb', 'Tmall_new')
