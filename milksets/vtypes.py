# -*- coding: utf-8 -*-
# Copyright (C) 2009, Luís Pedro Coelho <lpc@cmu.edu>
# Software Distributed under the MIT License

'''
Value types: An hierarchy of value types.

Hierarchy:

vtype
  |- numeric
  |     |-ordinal
  |     |   |- ordinalrange
  |     |    - boolean
  |      -continuous
   - categorical
       - boolean

'''

class vtype(object):
    def __init__(self,name):
        self.name = name

class numeric(vtype):
    def __init__(self,name):
        vtype.__init__(self,name)

class continuous(numeric):
    def __init__(self,name):
        vtype.__init__(self,name)

class ordinal(numeric):
    def __init__(self,name):
        vtype.__init__(self,name)

class ordinalrange(ordinal):
    def __init__(self,name,max,min):
        ordinal.__init__(self,name)
        self.max = max
        self.min = min

class categorical(vtype):
    def __init__(self,name, categories):
        vtype.__init__(self,name)
        self.categories = categories

class boolean(categorical, ordinal):
    def __init__(self,name):
        vtype.__init__(self,name)


# vim: set ts=4 sts=4 sw=4 expandtab smartindent: