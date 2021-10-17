import lib.parser as parser
from lib.base import Atom, RelationCall

a = RelationCall(id='uio',
                 args=[Atom(name='abcd',
                            args=[Atom('defg'),
                                  Atom('xyz',
                                       args=[
                                           Atom(
                                               'vbn')])])])

b = RelationCall(id='lop',
                 args=[
                     Atom(name='abcd',
                          args=[Atom(
                              'defg'),
                              Atom(
                                  'xyz')])])

c = RelationCall(id='kek', args=[])

d = RelationCall(id='cdef', args=[Atom(name='abcd')])

e = RelationCall(id='hjk',
                 args=[Atom(name='abcd', args=[Atom('defg')])])


def test_rel_call():
    assert parser.rel_call.parse('uio (abcd {defg, xyz {vbn}})') == a
    assert parser.rel_call.parse('lop (abcd {defg, xyz})') == b
    assert parser.rel_call.parse('kek ()') == c
    assert parser.rel_call.parse('cdef (abcd)') == d
    assert parser.rel_call.parse('hjk (abcd {defg})') == e


def test_rel_call_repr():
    assert 'CALL(uio, [ATOM(CONS, abcd, [ATOM(VAR, defg), ATOM(CONS, xyz, [ATOM(VAR, vbn)])])])' == str(a)
    assert 'CALL(lop, [ATOM(CONS, abcd, [ATOM(VAR, defg), ATOM(VAR, xyz)])])' == str(b)
    assert 'CALL(kek, [])' == str(c)
    assert 'CALL(cdef, [ATOM(VAR, abcd)])' == str(d)
    assert 'CALL(hjk, [ATOM(CONS, abcd, [ATOM(VAR, defg)])])' == str(e)
