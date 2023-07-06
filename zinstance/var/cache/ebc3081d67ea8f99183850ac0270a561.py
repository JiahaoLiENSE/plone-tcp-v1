# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/skins/plone_prefs/prefs_main_template.pt'

__tokens = {256: (u"python:request.set('disable_border',1)", 6, 43), 345: (u" python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel'", 7, 49), 482: (u'n controlPanel/maySeeSomeConfigle', 8, 51), 572: (u"ne python:request.set('disable_plone.leftcolumn',", 9, 53), 678: (u"two python:request.set('disable_plone.rightcolumn',not show_leftcol", 10, 52), 942: (u'here/portlet_prefs/macros/portlet', 16, 36), 942: (u'here/portlet_prefs/macros/portlet', 16, 36), 1410: (u'nothing', 26, 82), 1233: (u'context/@@main_template/macros/content', 24, 42), 1233: (u'context/@@main_template/macros/content', 24, 42), 85: (u'context/@@main_template/macros/master', 2, 30), 85: (u'context/@@main_template/macros/master', 2, 30)}

from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386076993104 = u'portlet'
_static_140386077035344 = u'master'
_static_140386186297040 = __C2ZContextWrapper
_static_140386186296528 = __compile_zt_expr
_static_140386076985872 = u'content'
_static_140386247937936 = {}

import re
import functools
from itertools import chain as __chain
from sys import exc_clear as __exc_clear
__default = intern('__default__')
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(modules, nothing, tales, zope_version_4_8_7_):

    def render_master(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is long)):
                target = unicode(target)
            else:
                if (__tt is str):
                    target = decode(target)
                else:
                    if (__tt is not unicode):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (unicode(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is long)):
                target = unicode(target)
            else:
                if (__tt is str):
                    target = decode(target)
                else:
                    if (__tt is not unicode):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (unicode(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        decode = econtext['__decode']
        convert = econtext['__convert']
        translate = econtext['__translate']
        on_error_handler = econtext['__on_error_handler']
        try:
            __slot_prefs_configlet_main = econtext[u'__slot_prefs_configlet_main'].pop()
        except:
            __slot_prefs_configlet_main = None

        try:
            __slot_column_two_slot = econtext[u'__slot_column_two_slot'].pop()
        except:
            __slot_column_two_slot = None

        try:
            __slot_top_slot = econtext[u'__slot_top_slot'].pop()
        except:
            __slot_top_slot = None

        try:
            __slot_prefs_configlet_wrapper = econtext[u'__slot_prefs_configlet_wrapper'].pop()
        except:
            __slot_prefs_configlet_wrapper = None

        try:
            __slot_prefs_configlet_content = econtext[u'__slot_prefs_configlet_content'].pop()
        except:
            __slot_prefs_configlet_content = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077033616
            __attrs_140386077033616 = _static_140386247937936
            __previous_i18n_domain_140386077033808 = __i18n_domain
            __i18n_domain = u'plone'
            __append(u'\n  ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077034192
            __attrs_140386077034192 = _static_140386247937936
            __backup_macroname_140386118799440 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7fae2e40cb50> name=None at 7fae2e40c510> -> __value
            __value = _static_140386077035344
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077035920
                __attrs_140386077035920 = _static_140386247937936
                __append(u'\n        ')
                if (__slot_top_slot is None):

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386076995024
                    __attrs_140386076995024 = _static_140386247937936
                    __append(u'\n            ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386076995088
                    __attrs_140386076995088 = _static_140386247937936
                    __backup_dummy_140386069379600 = get('dummy', __marker)

                    # <Value u"python:request.set('disable_border',1)" (6:43)> -> __value
                    __token = 256
                    try:
                        __zt_tmp = __attrs_140386076995088
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('python', u"request.set('disable_border',1)", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['dummy'] = __value
                    __backup_controlPanel_140386076999824 = get('controlPanel', __marker)

                    # <Value u"python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')" (7:49)> -> __value
                    __token = 345
                    try:
                        __zt_tmp = __attrs_140386076995088
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('python', u"modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['controlPanel'] = __value
                    __backup_show_leftcolumn_140386079996496 = get('show_leftcolumn', __marker)

                    # <Value u'controlPanel/maySeeSomeConfiglets' (8:51)> -> __value
                    __token = 482
                    try:
                        __zt_tmp = __attrs_140386076995088
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('path', u'controlPanel/maySeeSomeConfiglets', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['show_leftcolumn'] = __value
                    __backup_disable_column_one_140386077075152 = get('disable_column_one', __marker)

                    # <Value u"python:request.set('disable_plone.leftcolumn', 1)" (9:53)> -> __value
                    __token = 572
                    try:
                        __zt_tmp = __attrs_140386076995088
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('python', u"request.set('disable_plone.leftcolumn', 1)", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['disable_column_one'] = __value
                    __backup_disable_column_two_140386069380880 = get('disable_column_two', __marker)

                    # <Value u"python:request.set('disable_plone.rightcolumn',not show_leftcolumn)" (10:52)> -> __value
                    __token = 678
                    try:
                        __zt_tmp = __attrs_140386076995088
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('python', u"request.set('disable_plone.rightcolumn',not show_leftcolumn)", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['disable_column_two'] = __value
                    if (__backup_disable_column_two_140386069380880 is __marker):
                        del econtext['disable_column_two']
                    else:
                        econtext['disable_column_two'] = __backup_disable_column_two_140386069380880
                    if (__backup_disable_column_one_140386077075152 is __marker):
                        del econtext['disable_column_one']
                    else:
                        econtext['disable_column_one'] = __backup_disable_column_one_140386077075152
                    if (__backup_show_leftcolumn_140386079996496 is __marker):
                        del econtext['show_leftcolumn']
                    else:
                        econtext['show_leftcolumn'] = __backup_show_leftcolumn_140386079996496
                    if (__backup_controlPanel_140386076999824 is __marker):
                        del econtext['controlPanel']
                    else:
                        econtext['controlPanel'] = __backup_controlPanel_140386076999824
                    if (__backup_dummy_140386069379600 is __marker):
                        del econtext['dummy']
                    else:
                        econtext['dummy'] = __backup_dummy_140386069379600
                    __append(u'\n        ')
                else:
                    __slot_top_slot(__stream, econtext.copy(), rcontext)
                __append(u'\n    ')
            _slots = econtext[u'__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_portlets_two_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386076995408
                __attrs_140386076995408 = _static_140386247937936
                __append(u'\n        ')
                if (__slot_column_two_slot is None):

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386076993616
                    __attrs_140386076993616 = _static_140386247937936
                    __append(u'\n            ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386076992464
                    __attrs_140386076992464 = _static_140386247937936
                    __backup_macroname_140386187143040 = get('macroname', __marker)

                    # <Static value=<_ast.Str object at 0x7fae2e402650> name=None at 7fae2e402410> -> __value
                    __value = _static_140386076993104
                    econtext['macroname'] = __value

                    # <Value u'here/portlet_prefs/macros/portlet' (16:36)> -> __macro
                    __token = 942
                    try:
                        __zt_tmp = __attrs_140386076992464
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __macro = _static_140386186296528('path', u'here/portlet_prefs/macros/portlet', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __token = 942
                    __m = __macro.include
                    __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    if (__backup_macroname_140386187143040 is __marker):
                        del econtext['macroname']
                    else:
                        econtext['macroname'] = __backup_macroname_140386187143040
                    __append(u'\n        ')
                else:
                    __slot_column_two_slot(__stream, econtext.copy(), rcontext)
                __append(u'\n    ')
            _slots = econtext[u'__slot_portlets_two_slot'] = _deque((__fill_portlets_two_slot, ))

            def __fill_content(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386076992976
                __attrs_140386076992976 = _static_140386247937936
                __append(u'\n        ')
                if (__slot_prefs_configlet_wrapper is None):

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386076992336
                    __attrs_140386076992336 = _static_140386247937936
                    __append(u'\n          ')
                    if (__slot_prefs_configlet_content is None):

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386076983696
                        __attrs_140386076983696 = _static_140386247937936
                        __append(u'\n\n            ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386076985616
                        __attrs_140386076985616 = _static_140386247937936
                        __backup_macroname_140386118072352 = get('macroname', __marker)

                        # <Static value=<_ast.Str object at 0x7fae2e400a10> name=None at 7fae2e400a50> -> __value
                        __value = _static_140386076985872
                        econtext['macroname'] = __value

                        def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                            getitem = econtext.__getitem__
                            get = econtext.get

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386076985424
                            __attrs_140386076985424 = _static_140386247937936
                            __append(u'\n                ')
                            if (__slot_prefs_configlet_main is None):

                                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386076984400
                                __attrs_140386076984400 = _static_140386247937936

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386076986512
                                __default_140386076986512 = _DEFAULT_MARKER

                                # <Value u'nothing' (26:82)> -> __cache_140386076986960
                                __token = 1410
                                try:
                                    __zt_tmp = __attrs_140386076984400
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140386076986960 = _static_140386186296528('path', u'nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                                # <BinOp left=<Value u'nothing' (26:82)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e400750> -> __condition
                                __expression = __cache_140386076986960

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(u'\n                  Page body text\n                ')
                                else:
                                    __content = __cache_140386076986960
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                            else:
                                __slot_prefs_configlet_main(__stream, econtext.copy(), rcontext)
                            __append(u'\n              ')
                        _slots = econtext[u'__slot_main'] = _deque((__fill_main, ))

                        # <Value u'context/@@main_template/macros/content' (24:42)> -> __macro
                        __token = 1233
                        try:
                            __zt_tmp = __attrs_140386076985616
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __macro = _static_140386186296528('path', u'context/@@main_template/macros/content', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __token = 1233
                        __m = __macro.include
                        __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                        econtext.update(rcontext)
                        if (__backup_macroname_140386118072352 is __marker):
                            del econtext['macroname']
                        else:
                            econtext['macroname'] = __backup_macroname_140386118072352
                        __append(u'\n\n          ')
                    else:
                        __slot_prefs_configlet_content(__stream, econtext.copy(), rcontext)
                    __append(u'\n        ')
                else:
                    __slot_prefs_configlet_wrapper(__stream, econtext.copy(), rcontext)
                __append(u'\n    ')
            _slots = econtext[u'__slot_content'] = _deque((__fill_content, ))

            # <Value u'context/@@main_template/macros/master' (2:30)> -> __macro
            __token = 85
            try:
                __zt_tmp = __attrs_140386077034192
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140386186296528('path', u'context/@@main_template/macros/master', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __token = 85
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140386118799440 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140386118799440
            __append(u'\n')
            __i18n_domain = __previous_i18n_domain_140386077033808
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is long)):
                target = unicode(target)
            else:
                if (__tt is str):
                    target = decode(target)
                else:
                    if (__tt is not unicode):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (unicode(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is long)):
                target = unicode(target)
            else:
                if (__tt is str):
                    target = decode(target)
                else:
                    if (__tt is not unicode):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (unicode(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        decode = econtext['__decode']
        convert = econtext['__convert']
        translate = econtext['__translate']
        on_error_handler = econtext['__on_error_handler']
        try:
            getitem = econtext.__getitem__
            get = econtext.get
            __token = None
            render_master(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_master': render_master, 'render': render, }