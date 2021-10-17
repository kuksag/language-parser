import lib.parser as parser
from lib.base import Atom


def test_atom_constructor():
    assert parser.atom.parse('abcd') == Atom(name='abcd')
    assert parser.atom.parse('abcd {defg}') == Atom(name='abcd', args=[Atom('defg')])
    assert parser.atom.parse('abcd {defg, xyz}') == Atom(name='abcd', args=[Atom('defg'),
                                                                            Atom('xyz')])
    assert parser.atom.parse('abcd {defg, xyz {vbn}}') == Atom(name='abcd', args=[Atom('defg'),
                                                                                  Atom('xyz', args=[
                                                                                      Atom('vbn')])])


def test_atom_repr():
    assert str(Atom(name='abcd')) == 'ATOM(VAR, abcd)'
    assert str(parser.atom.parse('abcd {defg}')) == 'ATOM(CONS, abcd, [ATOM(VAR, defg)])'
    assert str(parser.atom.parse('abcd {defg, xyz}')) == 'ATOM(CONS, abcd, [ATOM(VAR, defg), ATOM(VAR, xyz)])'
    assert str(parser.atom.parse(
        'abcd {defg, xyz {vbn}}')) == 'ATOM(CONS, abcd, [ATOM(VAR, defg), ATOM(CONS, xyz, [ATOM(VAR, vbn)])])'
