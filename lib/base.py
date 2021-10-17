import attr


@attr.s(repr=False)
class Atom:
    name = attr.ib(validator=attr.validators.instance_of(str))
    args = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(list)), default=None)

    def __repr__(self):
        if self.args is None:
            return 'ATOM(VAR, {})'.format(self.name)
        else:
            return 'ATOM(CONS, {}, {})'.format(self.name, self.args)


@attr.s(repr=False)
class RelationCall:
    id = attr.ib(validator=attr.validators.instance_of(str))
    args = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(list)), default=None)

    def __repr__(self):
        return 'CALL({}, {})'.format(self.id, self.args)


@attr.s(repr=False)
class Aim:
    lhs = attr.ib()
    op = attr.ib(default=None)
    rhs = attr.ib(default=None)

    def __repr__(self):
        if self.rhs is None:
            assert isinstance(self.lhs, RelationCall)
            return 'AIM({})'.format(self.lhs)
        elif isinstance(self.rhs, Atom):
            assert isinstance(self.lhs, Atom)
            return 'AIM(UNIF, {}, {})'.format(self.lhs, self.rhs)
        elif isinstance(self.rhs, Aim):
            assert isinstance(self.lhs, Aim)
            assert self.op is not None
            return 'AIM({}, {}, {})'.format(self.lhs, self.op, self.rhs)
