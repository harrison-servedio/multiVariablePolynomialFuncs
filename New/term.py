
# term class

class term:

    # each term is of the following form:
    # t = [coefficient, {variable: exponent, variable, exponent}]
    # the term, [5, {x:5, y:4}] would be 5x^5y^4

    def __init__(self, term):
        # the operator determined by sign of term. only really used for displaying
        self.operator = '-' if term[0] < 0 else '+'
        # the coefficient is the first element of the term list
        self.coef = term[0]
        # the dictionary of vars is term.vars, therefore we can access specific vars or exponents by using term.vars.keys()[] or term.vars.values()[]
        self.vars = term[-1]
        # self.degree = sum(self.vars.values()) # the degree of on term is the sum of all exponents in a dictionary

    @property
    def degree(self):  # the degree of the term
        return sum(self.vars.values())

    __str__ = __repr__ = __format__ = __hash__ = __eq__ = __lt__ = __gt__ = __le__ = __ge__ = __ne__ = __add__ = __sub__ = __mul__ = __truediv__ = __floordiv__ = __mod__ = __pow__ = __radd__ = __rsub__ = __rmul__ = __rtruediv__ = __rfloordiv__ = __rmod__ = __rpow__ = __neg__ = __pos__ = __abs__ = __invert__ = __round__ = __floor__ = __ceil__ = __trunc__ = __getitem__ = __setitem__ = __delitem__ = __len__ = __contains__ = __iter__ = __reversed__ = __enter__ = __exit__ = __call__ = __getattr__ = __setattr__ = __delattr__ = __getattribute__ = __getstate__ = __setstate__ = __reduce__ = __copy__ = __deepcopy__ = __reduce_ex__ = __copy_reg__ = __deepcopy_reg__ = __getnewargs__ = __new__ = __init_subclass__ = __instancecheck__ = __subclasscheck__ = __del__ = __get__ = __set__ = __delete__ = __dir__ = __class__ = __get_class__ = __get_closure__ = __get_closure_this__ = __get_module__ = __get_origin__ = __get_parent__ = __get_preparer__ = __get_state__ = __get_dict__ = __get_doc__ = __get_dict__ = __get_name__ = __get_qualname__ = __get_newargs__ = __get_kwdefaults__ = __get_annotations__ = __get_kwonlydefaults__ = __get_signature__ = __get_defaults__ = __get_kwonlyargs__ = __get_annotations__ = __get_kwdefaults__ = __get_kwonlydefaults__ = __get_signature__ = __get_defaults__ = __get_kwonlyargs__ = __get_annotations__ = __