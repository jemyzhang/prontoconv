__author__ = 'jemyzhang'

from PalmDB import PalmDatabase
from PalmDB.Plugins.BasePlugin import DataRecord


class Novii:
    """
    convert Pronto Code to Novii code
    setpdb()

    while
    {
        addrec( makerec( conv(protocode), keyname))
    }

    savepdb()
    """
    def __init__(self):
        self.seq = list()
        self.pdb = PalmDatabase.PalmDatabase()
        self.recidx = 0

    def __str__(self):
        s = ''
        for i in self.seq:
            s += '{:04x}'.format(i)
            s += ' '
        return s

    def setpdb(self, path):
        f = open(path, 'rb')
        data = f.read()
        f.close()
        self.pdb.fromByteArray(data)
        self.recidx = len(self.pdb)
        for i in range(1,self.recidx):
            self.pdb.remove(self.pdb[1])
        self.recidx = 1
        print("%s[%s] %d records" % (path, self.pdb.getFilename(), self.recidx))

    def addrec(self, record):
        if self.recidx > 0xff:
            print 'record size error'
            return
        rec = DataRecord()
        hstr = bytearray.fromhex('00000000409f70')
        hstr.append(self.recidx)
        rec.fromByteArray(str(hstr), str(record))
        self.pdb.append(rec)
        self.recidx += 1

    def savedb(self, path, pdbname):
        self.pdb.setFilename(pdbname)
        f = open(path, 'wb')
        f.write(self.pdb.toByteArray())
        f.close()

    def conv(self, pronto):
        res = bytearray()
        if type(pronto) != list:
            return res
        if len(pronto) < 4:
            return res
        novii = list()
        novii.append(0x0001)
        novii_div = (pronto[1] >= 4 and (lambda x: x / 4 - 1) or (lambda x: 0))(pronto[1])
        novii.append(novii_div)
        codelen = (pronto[2] + pronto[3]) << 1
        novii.append(codelen)
        novii.append(codelen)
        count = 0
        for i in pronto[4:]:
            v = (count % 2) == 0 and \
                (lambda data: novii_div * data) or \
                (lambda data: (0xffff - (novii_div * data) + 1) & 0xffff)
            novii.append(v(i))
            count += 1
        self.seq = novii

        for i in novii:
            res.append((i >> 8) & 0xff)
            res.append(i & 0xff)
        return res

    def makerec(self, data, keyname):
        rec = bytearray()
        k = str(keyname).strip()
        if len(k) == 0:
            return rec
        # header
        rec += bytearray.fromhex('0002')
        # name string
        rec += k
        # strend, alignment
        if len(k) % 2:
            rec.append(0x00)
        else:
            rec += bytearray.fromhex('0000')
        # data
        rec += data
        return rec
