import ast

from also import also
from also import AlsoMetaClass

from utils import value_of

class ConstantFinder(ast.NodeVisitor):
    __metaclass__ = AlsoMetaClass

    def __init__(self, env, assignmentManager):
        self.env = env
        self._assignmentManager = assignmentManager

    @also('visit_Num')
    @also('visit_Str')
    def visit_Constant(self, node):
        if not hasattr(node, 'isdoc'):
            value = value_of(node)
            return self.addConstant(node, value)

    @also('visit_ClassDef')
    def visit_FunctionDef(self, node):
        if (isinstance(node.body[0], ast.Expr) and
            isinstance(node.body[0].value, ast.Str)):
            node.body[0].value.isdoc = True
        self.generic_visit(node)

    def addConstant(self, node, value):
        if value not in self.env.constants and not hasattr(node, 'isdoc'):
            decl = self.env.generate_new_decl()
            self._assignmentManager.add_assignment(decl.name, node)
            self.env.constants[value] = decl

