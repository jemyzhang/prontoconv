__author__ = 'jemyzhang'

import sys


class ProntoConv:
    """ Converter for Pronto code format, from NEC IR code
    default carrier freq: 38kHz
    """

    def __init__(self, carrierfreq=38000.0, reverse=0):
        self.reverse = reverse
        self.wFmtID = 0
        self.wFrqDiv = int(round(4145146 / carrierfreq))  # carrier frequency divider: 4.145146Mhz/ 37kHz
        self.nOnceSeq = 1 + 16 + 8 + 8  # lead + 16bit custom + 8bit keycode + 8bit reverse keycode
        self.nRepeatSeq = 2

        pulseus = int(round(1000 * 1000 / carrierfreq))  # uS for one pulse

        leadcode_flash = int(round(9.0 * 1000 / pulseus))  # flash time of lead pulse
        leadcode_off = int(round(4.5 * 1000 / pulseus))  # off time of lead pulse
        self.leadcode = (leadcode_flash, leadcode_off)

        logic1code_flash = int(round(560 / pulseus))  # flash time of logic 1: 560us
        logic1code_off = int(round((2.25 * 1000 - 560) / pulseus))  # off time of logic 0: 2.25ms-560us
        self.logic1code = (logic1code_flash, logic1code_off)

        logic0code_flash = logic1code_flash  # flash time of logic 0: 560us
        logic0code_off = logic0code_flash  # off time of logic 0: 560us
        self.logic0code = (logic0code_flash, logic0code_off)

        repeatcode_flash = int(round(9 * 1000 / pulseus))
        repeatcode_off = int(round(2.25 * 1000 / pulseus))
        repeatcode_flash_end = int(round(560 / pulseus))
        repeatcode_off_end = 0
        self.repeatcode = (repeatcode_flash, repeatcode_off, repeatcode_flash_end, repeatcode_off_end)

        # result
        self.result = list()


    def char2seq(self, data):
        result = list()
        for i in range(0, 8):
            if self.reverse:
                if (data & (0x80 >> i)) == 0:
                    result.append(self.logic0code)
                else:
                    result.append(self.logic1code)
            else:
                if (data & (0x1 << i)) == 0:
                    result.append(self.logic0code)
                else:
                    result.append(self.logic1code)
        return result

    def flat(self, seq, r=list()):
        for i in seq:
            if type(i) == list or type(i) == tuple:
                r = self.flat(i, r)
            else:
                r.append(i)
        return r

    def conv(self, customcode, keycode):
        seq = list()
        seq.append(self.wFmtID)
        seq.append(self.wFrqDiv)

        seq.append(self.nOnceSeq)
        seq.append(self.nRepeatSeq)
        seq.append(self.leadcode)
        if self.reverse:
            seq.append(self.char2seq((customcode >> 8) & 0xff))
            seq.append(self.char2seq(customcode & 0xff))
        else:
            seq.append(self.char2seq(customcode & 0xff))
            seq.append(self.char2seq((customcode >> 8) & 0xff))
        seq.append(self.char2seq(keycode))
        seq.append(self.char2seq(0xff ^ keycode))
        seq.append(self.repeatcode)
        self.result = list()
        self.flat(seq, self.result)
        return self.result

    def __str__(self):
        s = ''
        for i in self.result:
            s += '{:04x}'.format(i)
            s += ' '
        return s


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: %s cutomcode keycode' % sys.argv[0])
    else:
        p = ProntoConv()
        p.conv(int(sys.argv[1], base=16), int(sys.argv[2], base=16))

