import lib.parser as parser
from lib.base import *


a = Relation('qwe', [], Aim(RelationCall('abc', args=[Atom('cde')])))
b = Relation('qwe', [Atom('rty')], Aim(Aim(RelationCall('abc', args=[Atom('cde')])), '&&', Aim(RelationCall('def', args=[Atom('ghi')]))))


def test_relation():
    assert parser.relation.parse('qwe () {abc (cde)}') == a
    assert parser.relation.parse('qwe (rty) {[abc (cde) && def (ghi)]}') == b


def test_relation_repr():
    assert 'RELATION(qwe, [], AIM(CALL(abc, [ATOM(VAR, cde)])))' == str(a)
    assert 'RELATION(qwe, [ATOM(VAR, rty)], AIM(AIM(CALL(abc, [ATOM(VAR, cde)])), &&, AIM(CALL(def, [ATOM(VAR, ghi)]))))' == str(b)
