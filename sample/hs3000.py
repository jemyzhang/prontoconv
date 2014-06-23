__author__ = 'jemyzhang'

import os
import sys

root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, '../'))

from ProntoConv import ProntoConv
from NoviiDB import Novii

customcode = 0xbf00

keys = [
    ('1', 0x01), ('2', 0x02), ('3', 0x03), ('4', 0x04),
    ('5', 0x05), ('6', 0x06), ('7', 0x07), ('8', 0x08),
    ('9', 0x09), ('0', 0x00),
    ('Recall', 0x0b),
    ('*', 0x0c),
    ('Power On', 0x0d),
    ('Mute', 0x0e),
    ('Freeze', 0x0f),
    ('Pic Mode', 0x10),
    ('Sound Mode', 0x11),
    ('Input', 0x12),
    ('Zoom', 0x13),
    ('Menu', 0x14),
    ('Ok', 0x15),
    ('Up', 0x16),
    ('Down', 0x17),
    ('Right', 0x18),
    ('Left', 0x19),
    ('Sleep', 0x1a),
    ('TV', 0x1b),
    ('Saving Mode', 0x1c),
    ('Guide', 0x1d),
    ('Favorite', 0x1e),
    ('Subtitle', 0x1f),
    ('Vol+', 0x44),
    ('Vol-', 0x43),
    ('Back', 0x48),
    ('Language', 0x49),
    ('Ch+', 0x4a),
    ('Ch-', 0x4b),
    ('Audio Track', 0x4c),
    ('DMP', 0x4d),
    ('Play', 0x4e),
    ('Application', 0x4f),
    ('Red', 0x52),
    ('Green', 0x53),
    ('Yellow', 0x54),
    ('Blue', 0x55),
    ('Forward', 0x56),
    ('Rewind', 0x57),
    ('Page Up', 0x58),
    ('Page Down', 0x59),
    ('Stop', 0x5a),
    ('Exit', 0x5c),
    ('Broadcast', 0x5d),
    ('Record', 0x5e),
    ('3D', 0x5f),
]

custfact = 0xfc00
keyfacts = [
    ('fLeave', 0x47),
    ('fMac', 0x0a),
    ('fMode', 0x00),
    ('fBalance', 0x06),
    ('fAdc', 0x40),
    ('fScreenTest', 0x58),
    ('fBurnIn', 0x15),
    ('fSavingMode', 0x60),
    ('fIP', 0x4e),
    ('fPC', 0x18),
    ('fHDMI', 0x52),
    ('fComponent', 0x01),
    ('fAV', 0x05),
    ('fF1', 0x5d),
    ('fF2', 0x24),
    ('fF3', 0x56),
    ('fF4', 0x48),
    ('fF5', 0x53),
    ('fF6', 0x1d),
    ('fF7', 0x4f),
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
    # factory
    for n, k in keyfacts:
        prontocode = pronto.conv(customcode, k)
        noviidata = novii.conv(prontocode)
        rec = novii.makerec(noviidata, n)
        novii.addrec(rec)
    novii.savedb('hs3000.pdb', 'HS3000')
