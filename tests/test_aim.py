import lib.parser as parser
from lib.base import Atom, RelationCall, Aim

a = Aim(RelationCall('abc', args=[Atom('cde')]))
b = Aim(Aim(RelationCall('abc', args=[Atom('cde')])), '&&', Aim(RelationCall('def', args=[Atom('ghi')])))
c = Aim(Aim(RelationCall('abc', args=[Atom('cde')])), '||', Aim(RelationCall('def', args=[Atom('ghi')])))
d = Aim(Atom('abc'), '->', Atom('cde'))
e = Aim(b, '&&', c)


def test_aim():
    assert parser.aim.parse('abc (cde)') == a
    assert parser.aim.parse('[abc (cde) && def (ghi)]') == b
    assert parser.aim.parse('[abc (cde) || def (ghi)]') == c
    assert parser.aim.parse('[abc -> cde]') == d
    assert parser.aim.parse('[[abc (cde) && def (ghi)] && [abc (cde) || def (ghi)]]') == e


def test_aim_repr():
    assert 'AIM(CALL(abc, [ATOM(VAR, cde)]))' == str(a)
    assert 'AIM(AIM(CALL(abc, [ATOM(VAR, cde)])), &&, AIM(CALL(def, [ATOM(VAR, ghi)])))' == str(b)
    assert 'AIM(AIM(CALL(abc, [ATOM(VAR, cde)])), ||, AIM(CALL(def, [ATOM(VAR, ghi)])))' == str(c)
    assert 'AIM(UNIF, ATOM(VAR, abc), ATOM(VAR, cde))' == str(d)
    assert 'AIM(AIM(AIM(CALL(abc, [ATOM(VAR, cde)])), &&, AIM(CALL(def, [ATOM(VAR, ghi)]))), &&, AIM(AIM(CALL(abc, [ATOM(VAR, cde)])), ||, AIM(CALL(def, [ATOM(VAR, ghi)]))))' == str(e)
