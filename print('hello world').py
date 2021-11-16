remap = {
    ord('b') : 'd',
    ord('c') : 'e',
    ord('d') : 'f',
    ord('e') : 'g',
    ord('f') : 'h',
    ord('g') : 'i',
    ord('h') : 'j',
    ord('i') : 'k',
    ord('j') : 'l',
    ord('k') : 'm',
    ord('l') : 'n',
    ord('m') : 'o',
    ord('n') : 'p',
    ord('o') : 'q',
    ord('p') : 'r',
    ord('q') : 's',
    ord('r') : 't',
    ord('s') : 'u',
    ord('t') : 'v',
    ord('u') : 'w',
    ord('v') : 'x',
    ord('w') : 'y',
    ord('x') : 'z',
    ord('y') : 'a',
    ord('z') : 'b',
    ord('a') : 'c',

}
s='map'
ans = s.translate(remap)
print(ans)