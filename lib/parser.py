# from base import *
import lib.base as base
from parsy import regex, generate, seq, string

s = regex(r'\s*').desc('space characters')

id_p = regex(r'[a-zA-Z]+([a-zA-Z]|[0-9])*').desc('id or variable name')
comma_p = (s >> string(',') << s).desc('comma')

open_curly_brace_p = (s >> string('{') << s).desc('open curly brace')
close_curly_brace_p = (s >> string('}') << s).desc('close curly brace')

open_square_brace_p = (s >> string('[') << s).desc('open open brace')
close_square_brace_p = (s >> string(']') << s).desc('close close brace')

open_brace_p = (s >> string('(') << s).desc('open curly brace')
close_brace_p = (s >> string(')') << s).desc('close curly brace')

and_operator_p = (s >> string('&&') << s).desc('and operator')
or_operator_p = (s >> string(r'||') << s).desc('or operator')
apply_operator_p = (s >> string('->') << s).desc('apply operator')

logic_operators_p = and_operator_p | or_operator_p


@generate
def atom():
    result = yield seq(id_p, open_curly_brace_p >> atom_list_p << close_curly_brace_p) | seq(id_p)
    return base.Atom(*result)


atom_list_p = (atom << comma_p.optional()).at_least(0)


@generate
def rel_call():
    result = yield seq(id_p, open_brace_p >> atom_list_p.optional() << close_brace_p)
    return base.RelationCall(*result)


@generate
def aim():
    apply_p = open_square_brace_p >> seq(atom, apply_operator_p, atom) << close_square_brace_p
    aim_p = open_square_brace_p >> seq(aim, logic_operators_p, aim) << close_square_brace_p
    result = yield apply_p | seq(rel_call) | aim_p
    return base.Aim(*result)


@generate
def relation():
    result = yield seq(id_p, open_brace_p >> atom_list_p << close_brace_p,
                       open_curly_brace_p >> aim << close_curly_brace_p)
    return base.Relation(*result)
