__author__ = 'jemyzhang'

import prontoconv

customcode = 0x9f00

keynames = ('power', 'notification', 'rewind', 'forward',
            'up', 'down', 'left', 'right',
            'center', 'menu', 'home', 'back',
            'volume up', 'volume down')
keycodes = (0x57, 0x5b, 0x0b, 0x0f,
            0x43, 0x0a, 0x06, 0x0e,
            0x02, 0x16, 0x47, 0x4f,
            0xff, 0x5d)

if __name__ == '__main__':
    keys = zip(keynames, keycodes)
    for n, k in keys:
        print('#[%02X]%s' % (k, n))
        prontoconv.show_result(prontoconv.protoconv(customcode, k))
        print('')
        print('')
