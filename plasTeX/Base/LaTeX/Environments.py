#!/usr/bin/env python

"""
C.1.2 Environments (p167)

"""

from plasTeX import Command, Environment
from plasTeX.Logging import getLogger

envlog = getLogger('parse.environments')

class begin(Command):
    """ Beginning of an environment """
    args = 'name:str'

    def invoke(self, tex):
        """ Parse the \\begin{...} """
#       name = self.parse(tex)['name']
        name = tex.readArgument(type=str)
        envlog.debug(name)

        # Instantiate the correct macro and let it know
        # that it came from a \begin{...} macro
        obj = tex.context[name]
        obj.macroMode = Command.MODE_BEGIN

        # Return the output of the instantiated macro in
        # place of self
        out = obj.invoke(tex)
        if out is None:
            return [obj]
        return out

class end(Command):
    """ End of an environment """
    args = 'name:str'

    def invoke(self, tex):
        """ Parse the \\end{...} """
#       name = self.parse(tex)['name']
        name = tex.readArgument(type=str)
        envlog.debug(name)

        # Instantiate the correct macro and let it know
        # that it came from a \end{...} macro
        obj = tex.context[name]
        obj.macroMode = Command.MODE_END

        # Return the output of the instantiated macro in
        # place of self
        out = obj.invoke(tex)
        if out is None:
            return [obj]
        return out