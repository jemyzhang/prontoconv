__author__ = 'jemyzhang'

import os
import sys

root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, '../'))

from ProntoConv import ProntoConv
from NoviiDB import Novii

customcode = 0xdf20

keys = [
        ('Vol-' , 0x01),
        ('Vol+' , 0x02),
        ('Mute' , 0x04),
        ('LR-R' , 0x05),
        ('LR-L'  , 0x0c),
        ('Center-' , 0x06),
        ('Center+' , 0x35),
        ('TREB+' , 0x07),
        ('TREB-' , 0x2e),
        ('S.L-'  , 0x0d),
        ('S.L+'  , 0x11),
        ('S.R-' , 0x16),
        ('S.R+' , 0x17),
        ('BASS-' , 0x18),
        ('BASS+' , 0x45),
        ('SWF+' , 0x26),
        ('SWF-' , 0x36),
        ('Class' , 0x09),
        ('Pop' , 0x15),
        ('Hall' , 0x3e),
        ('Normal' , 0x2a),
        ('Power On' , 0x12),
        ('Input' , 0x2c),
        ('AUX' , 0x13),
        ('AC-3' , 0x49),
        ('Mode' , 0x22),
        ('2.1ch' , 0x28),
        ('3.1ch' , 0x2f),
        ('5.1ch' , 0x3f),
        ('Reset' , 0x1b),
        ('OK.Menu'   , 0x0f),
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
    novii.savedb('Kele_Amp.pdb', 'Amp_Kele')
