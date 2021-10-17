import lib.parser as parser
from parsy import ParseError
import pytest


def test_square_braces():
    assert parser.open_square_brace_p.parse('[') == '['
    assert parser.open_square_brace_p.parse('   [     ') == '['
    assert parser.close_square_brace_p.parse(']') == ']'
    assert parser.close_square_brace_p.parse('   ]     ') == ']'


def test_curly_braces():
    assert parser.open_curly_brace_p.parse('{') == '{'
    assert parser.open_curly_brace_p.parse('   {     ') == '{'
    assert parser.close_curly_brace_p.parse('}') == '}'
    assert parser.close_curly_brace_p.parse('   }     ') == '}'


def test_braces():
    assert parser.open_brace_p.parse('(') == '('
    assert parser.open_brace_p.parse('   (     ') == '('
    assert parser.close_brace_p.parse(')') == ')'
    assert parser.close_brace_p.parse('   )     ') == ')'


def test_logic_operators():
    assert parser.logic_operators_p.parse('&&') == '&&'
    assert parser.logic_operators_p.parse('||') == '||'
    assert parser.logic_operators_p.parse('       &&   ') == '&&'
    assert parser.logic_operators_p.parse('       ||   ') == '||'


def test_apply_operator():
    assert parser.apply_operator_p.parse('->') == '->'
    assert parser.apply_operator_p.parse('   -> ') == '->'


def test_comma():
    assert parser.comma_p.parse(',') == ','
    assert parser.comma_p.parse('      ,  ') == ','


def test_name():
    assert parser.id_p.parse('abcd') == 'abcd'
    with pytest.raises(ParseError):
        parser.id_p.parse('123abcd')
    with pytest.raises(ParseError):
        parser.id_p.parse(' abcvd')
