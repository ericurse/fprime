#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from Cheetah.compat import unicode

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.3'
__CHEETAH_versionTuple__ = (3, 2, 3, 'final', 0)
__CHEETAH_genTime__ = 1557938883.51008
__CHEETAH_genTimestamp__ = 'Wed May 15 09:48:03 2019'
__CHEETAH_src__ = 'Event.tmpl'
__CHEETAH_srcLastModified__ = 'Tue May 14 13:09:18 2019'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class Event(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(Event, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write('''# Created on ''')
        _v = VFFSL(SL,"date",True) # '${date}' on line 1, col 14
        if _v is not None: write(_filter(_v, rawExpr='${date}')) # from line 1, col 14.
        write('''
# Author: ''')
        _v = VFFSL(SL,"user",True) # '${user}' on line 2, col 11
        if _v is not None: write(_filter(_v, rawExpr='${user}')) # from line 2, col 11.
        write('''
''')
        _v = '#\n'
        if _v is not None: write(_filter(_v))
        write('''# THIS FILE IS AUTOMATICALLY GENERATED - DO NOT EDIT!!!
''')
        _v = '#\n'
        if _v is not None: write(_filter(_v))
        write('''# Component Source: ''')
        _v = VFFSL(SL,"source",True) # '${source}' on line 6, col 21
        if _v is not None: write(_filter(_v, rawExpr='${source}')) # from line 6, col 21.
        write('''

# COMPONENT: "''')
        _v = VFFSL(SL,"component_string",True) # '${component_string}' on line 8, col 15
        if _v is not None: write(_filter(_v, rawExpr='${component_string}')) # from line 8, col 15.
        write('''"
TELEMETRY ''')
        _v = VFFSL(SL,"target_caps",True) # '${target_caps}' on line 9, col 11
        if _v is not None: write(_filter(_v, rawExpr='${target_caps}')) # from line 9, col 11.
        write(''' ''')
        _v = VFFSL(SL,"evr_name",True) # '${evr_name}' on line 9, col 26
        if _v is not None: write(_filter(_v, rawExpr='${evr_name}')) # from line 9, col 26.
        write(''' ''')
        _v = VFFSL(SL,"endianness",True) # '${endianness}' on line 9, col 38
        if _v is not None: write(_filter(_v, rawExpr='${endianness}')) # from line 9, col 38.
        write(''' "''')
        _v = VFFSL(SL,"evr_desc",True) # '${evr_desc}' on line 9, col 53
        if _v is not None: write(_filter(_v, rawExpr='${evr_desc}')) # from line 9, col 53.
        write('''"
    <%=render "_''')
        _v = VFFSL(SL,"target_lower",True) # '${target_lower}' on line 10, col 30
        if _v is not None: write(_filter(_v, rawExpr='${target_lower}')) # from line 10, col 30.
        write('''_tlm_evr_hdr.txt", locals: {id: ''')
        _v = VFFSL(SL,"id",True) # '${id}' on line 10, col 77
        if _v is not None: write(_filter(_v, rawExpr='${id}')) # from line 10, col 77.
        write('''} %>

''')
        for name, desc, template_string, types, bit_offset, bits, type in VFFSL(SL,"evr_items",True): # generated from line 12, col 5
            if VFFSL(SL,"type",True) == 'BLOCK': # generated from line 13, col 5
                write('''    APPEND_ITEM EVR_ITEMS 0 BLOCK "Contains all other items"
''')
            elif not VFFSL(SL,"template_string",True) == '': # generated from line 15, col 5
                write('''      ITEM ''')
                _v = VFFSL(SL,"name",True) # '$name' on line 16, col 12
                if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 16, col 12.
                write(''' 0 0 DERIVED "''')
                _v = VFFSL(SL,"desc",True) # '$desc' on line 16, col 31
                if _v is not None: write(_filter(_v, rawExpr='$desc')) # from line 16, col 31.
                write('''"
        READ_CONVERSION multi_string_tlm_item_conversion.rb "''')
                _v = VFFSL(SL,"template_string",True) # '$template_string' on line 17, col 62
                if _v is not None: write(_filter(_v, rawExpr='$template_string')) # from line 17, col 62.
                write('''"
''')
                for type in VFFSL(SL,"types",True): # generated from line 18, col 9
                    write('''        STATE ''')
                    _v = VFFSL(SL,"type",True)[0] # '$type[0]' on line 19, col 15
                    if _v is not None: write(_filter(_v, rawExpr='$type[0]')) # from line 19, col 15.
                    write(''' ''')
                    _v = VFFSL(SL,"type",True)[1] # '$type[1]' on line 19, col 24
                    if _v is not None: write(_filter(_v, rawExpr='$type[1]')) # from line 19, col 24.
                    write('''
''')
            elif VFFSL(SL,"bit_offset",True) < 0: # generated from line 21, col 5
                write('''    ITEM ''')
                _v = VFFSL(SL,"name",True) # '$name' on line 22, col 10
                if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 22, col 10.
                write(''' ''')
                _v = VFFSL(SL,"bit_offset",True) # '$bit_offset' on line 22, col 16
                if _v is not None: write(_filter(_v, rawExpr='$bit_offset')) # from line 22, col 16.
                write(''' ''')
                _v = VFFSL(SL,"bits",True) # '$bits' on line 22, col 28
                if _v is not None: write(_filter(_v, rawExpr='$bits')) # from line 22, col 28.
                write(''' ''')
                _v = VFFSL(SL,"type",True) # '$type' on line 22, col 34
                if _v is not None: write(_filter(_v, rawExpr='$type')) # from line 22, col 34.
                write(''' "''')
                _v = VFFSL(SL,"desc",True) # '$desc' on line 22, col 41
                if _v is not None: write(_filter(_v, rawExpr='$desc')) # from line 22, col 41.
                write('''"
''')
                for type in VFFSL(SL,"types",True): # generated from line 23, col 7
                    write('''        STATE ''')
                    _v = VFFSL(SL,"type",True)[0] # '$type[0]' on line 24, col 15
                    if _v is not None: write(_filter(_v, rawExpr='$type[0]')) # from line 24, col 15.
                    write(''' ''')
                    _v = VFFSL(SL,"type",True)[1] # '$type[1]' on line 24, col 24
                    if _v is not None: write(_filter(_v, rawExpr='$type[1]')) # from line 24, col 24.
                    write('''
''')
            else: # generated from line 26, col 5
                write('''    APPEND_ITEM ''')
                _v = VFFSL(SL,"name",True) # '$name' on line 27, col 17
                if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 27, col 17.
                write(''' ''')
                _v = VFFSL(SL,"bits",True) # '$bits' on line 27, col 23
                if _v is not None: write(_filter(_v, rawExpr='$bits')) # from line 27, col 23.
                write(''' ''')
                _v = VFFSL(SL,"type",True) # '$type' on line 27, col 29
                if _v is not None: write(_filter(_v, rawExpr='$type')) # from line 27, col 29.
                write(''' "''')
                _v = VFFSL(SL,"desc",True) # '$desc' on line 27, col 36
                if _v is not None: write(_filter(_v, rawExpr='$desc')) # from line 27, col 36.
                write('''"
''')
                for type in VFFSL(SL,"types",True): # generated from line 28, col 7
                    write('''        STATE ''')
                    _v = VFFSL(SL,"type",True)[0] # '$type[0]' on line 29, col 15
                    if _v is not None: write(_filter(_v, rawExpr='$type[0]')) # from line 29, col 15.
                    write(''' ''')
                    _v = VFFSL(SL,"type",True)[1] # '$type[1]' on line 29, col 24
                    if _v is not None: write(_filter(_v, rawExpr='$type[1]')) # from line 29, col 24.
                    write('''
''')
        write('''
    ITEM MESSAGE 0 0 DERIVED "Formatted String for Argument"
      GENERIC_READ_CONVERSION_START STRING 0
        sprintf("''')
        _v = VFFSL(SL,"format_string",True) # '${format_string}' on line 36, col 18
        if _v is not None: write(_filter(_v, rawExpr='${format_string}')) # from line 36, col 18.
        write('''" ''')
        for name in VFFSL(SL,"nonlen_names",True): # generated from line 37, col 1
            write(""", packet.read('""")
            _v = VFFSL(SL,"name",True) # '$name' on line 38, col 16
            if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 38, col 16.
            write("""') """)
        write(''')
      GENERIC_READ_CONVERSION_END
      META FORMAT_STRING "''')
        _v = VFFSL(SL,"format_string",True) # '${format_string}' on line 42, col 27
        if _v is not None: write(_filter(_v, rawExpr='${format_string}')) # from line 42, col 27.
        write('''"
      META ARGS ''')
        for name in VFFSL(SL,"nonlen_names",True): # generated from line 44, col 1
            _v = VFFSL(SL,"name",True) # '$name' on line 45, col 1
            if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 45, col 1.
            write(''' ''')
        write('''
    ITEM EVR_SEVERITY 0 0 DERIVED "Severity"
      GENERIC_READ_CONVERSION_START STRING 0
        sprintf(\'''')
        _v = VFFSL(SL,"severity",True) # '${severity}' on line 50, col 18
        if _v is not None: write(_filter(_v, rawExpr='${severity}')) # from line 50, col 18.
        write("""')
      GENERIC_READ_CONVERSION_END
""")
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_Event = 'respond'

## END CLASS DEFINITION

if not hasattr(Event, '_initCheetahAttributes'):
    templateAPIClass = getattr(Event,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(Event)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=Event()).run()


