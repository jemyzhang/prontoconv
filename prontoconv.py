__author__ = 'jemyzhang'

import sys

carrierfreq = 38000.0  # 38kHz

wFmtID = 0
wFrqDiv = int(round(4145146 / carrierfreq))  # carrier frequency divider: 4.145146Mhz/ 37kHz
nOnceSeq = 1 + 16 + 8 + 8  # lead + 16bit custom + 8bit keycode + 8bit reverse keycode
nRepeatSeq = 2

pulseus = int(round(1000*1000/carrierfreq))     # uS for one pulse

leadcode_flash = int(round(9.0*1000/pulseus))  # flash time of lead pulse
leadcode_off = int(round(4.5*1000/pulseus))    # off time of lead pulse
leadcode = (leadcode_flash, leadcode_off)

logic1code_flash = int(round(560/pulseus))     # flash time of logic 1: 560us
logic1code_off = int(round((2.25*1000 - 560)/pulseus))  # off time of logic 0: 2.25ms-560us
logic1code = (logic1code_flash, logic1code_off)

logic0code_flash = logic1code_flash            # flash time of logic 0: 560us
logic0code_off = logic0code_flash              # off time of logic 0: 560us
logic0code = (logic0code_flash, logic0code_off)

repeatcode_flash = int(round(9*1000/pulseus))
repeatcode_off = int(round(2.25*1000/pulseus))
repeatcode_flash_end = int(round(560/pulseus))
repeatcode_off_end = 0
repeatcode = (repeatcode_flash, repeatcode_off, repeatcode_flash_end, repeatcode_off_end)


def char2seq(data):
    result = list()
    for i in range(0, 8):
        if (data & (0x80 >> i)) == 0:
            result.append(logic0code)
        else:
            result.append(logic1code)
    return result


def protoconv(customcode, keycode):
    seq = list()
    seq.append(wFmtID)
    seq.append(wFrqDiv)

    seq.append(nOnceSeq)
    seq.append(nRepeatSeq)
    seq.append(leadcode)
    seq.append(char2seq((customcode >> 8) & 0xff))
    seq.append(char2seq(customcode & 0xff))
    seq.append(char2seq(keycode))
    seq.append(char2seq(0xff ^ keycode))
    seq.append(repeatcode)

    return seq


def show_result(r):
    for i in r:
        if type(i) == list or type(i) == tuple:
            show_result(i)
        else:
            print('{:04x}'.format(i)),

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: %s cutomcode keycode' % sys.argv[0])
    else:
        show_result(protoconv(int(sys.argv[1], base=16), int(sys.argv[2], base=16)))
