# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/skins/plone_prefs/prefs_main_template.pt'

__tokens = {256: (u"python:request.set('disable_border',1)", 6, 43), 345: (u" python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel'", 7, 49), 482: (u'n controlPanel/maySeeSomeConfigle', 8, 51), 572: (u"ne python:request.set('disable_plone.leftcolumn',", 9, 53), 678: (u"two python:request.set('disable_plone.rightcolumn',not show_leftcol", 10, 52), 942: (u'here/portlet_prefs/macros/portlet', 16, 36), 942: (u'here/portlet_prefs/macros/portlet', 16, 36), 1410: (u'nothing', 26, 82), 1233: (u'context/@@main_template/macros/content', 24, 42), 1233: (u'context/@@main_template/macros/content', 24, 42), 85: (u'context/@@main_template/macros/master', 2, 30), 85: (u'context/@@main_template/macros/master', 2, 30)}

from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235321996496 = u'portlet'
_static_140235489934800 = {}
_static_140235435449424 = __compile_zt_expr
_static_140235374258256 = u'master'
_static_140235431244496 = u'content'
_static_140235435450064 = __C2ZContextWrapper

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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374257424
            __attrs_140235374257424 = _static_140235489934800
            __previous_i18n_domain_140235374257616 = __i18n_domain
            __i18n_domain = u'plone'
            __append(u'\n  ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374258384
            __attrs_140235374258384 = _static_140235489934800
            __backup_macroname_140235426739456 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f8b17aae850> name=None at 7f8b17aae290> -> __value
            __value = _static_140235374258256
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374260048
                __attrs_140235374260048 = _static_140235489934800
                __append(u'\n        ')
                if (__slot_top_slot is None):

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374259600
                    __attrs_140235374259600 = _static_140235489934800
                    __append(u'\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321997136
                    __attrs_140235321997136 = _static_140235489934800
                    __backup_dummy_140235321984656 = get('dummy', __marker)

                    # <Value u"python:request.set('disable_border',1)" (6:43)> -> __value
                    __token = 256
                    try:
                        __zt_tmp = __attrs_140235321997136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('python', u"request.set('disable_border',1)", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['dummy'] = __value
                    __backup_controlPanel_140235323258704 = get('controlPanel', __marker)

                    # <Value u"python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')" (7:49)> -> __value
                    __token = 345
                    try:
                        __zt_tmp = __attrs_140235321997136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('python', u"modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['controlPanel'] = __value
                    __backup_show_leftcolumn_140235323209296 = get('show_leftcolumn', __marker)

                    # <Value u'controlPanel/maySeeSomeConfiglets' (8:51)> -> __value
                    __token = 482
                    try:
                        __zt_tmp = __attrs_140235321997136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('path', u'controlPanel/maySeeSomeConfiglets', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['show_leftcolumn'] = __value
                    __backup_disable_column_one_140235451452752 = get('disable_column_one', __marker)

                    # <Value u"python:request.set('disable_plone.leftcolumn', 1)" (9:53)> -> __value
                    __token = 572
                    try:
                        __zt_tmp = __attrs_140235321997136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('python', u"request.set('disable_plone.leftcolumn', 1)", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['disable_column_one'] = __value
                    __backup_disable_column_two_140235368758480 = get('disable_column_two', __marker)

                    # <Value u"python:request.set('disable_plone.rightcolumn',not show_leftcolumn)" (10:52)> -> __value
                    __token = 678
                    try:
                        __zt_tmp = __attrs_140235321997136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('python', u"request.set('disable_plone.rightcolumn',not show_leftcolumn)", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['disable_column_two'] = __value
                    if (__backup_disable_column_two_140235368758480 is __marker):
                        del econtext['disable_column_two']
                    else:
                        econtext['disable_column_two'] = __backup_disable_column_two_140235368758480
                    if (__backup_disable_column_one_140235451452752 is __marker):
                        del econtext['disable_column_one']
                    else:
                        econtext['disable_column_one'] = __backup_disable_column_one_140235451452752
                    if (__backup_show_leftcolumn_140235323209296 is __marker):
                        del econtext['show_leftcolumn']
                    else:
                        econtext['show_leftcolumn'] = __backup_show_leftcolumn_140235323209296
                    if (__backup_controlPanel_140235323258704 is __marker):
                        del econtext['controlPanel']
                    else:
                        econtext['controlPanel'] = __backup_controlPanel_140235323258704
                    if (__backup_dummy_140235321984656 is __marker):
                        del econtext['dummy']
                    else:
                        econtext['dummy'] = __backup_dummy_140235321984656
                    __append(u'\n        ')
                else:
                    __slot_top_slot(__stream, econtext.copy(), rcontext)
                __append(u'\n    ')
            _slots = econtext[u'__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_portlets_two_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374260112
                __attrs_140235374260112 = _static_140235489934800
                __append(u'\n        ')
                if (__slot_column_two_slot is None):

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321997328
                    __attrs_140235321997328 = _static_140235489934800
                    __append(u'\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321996880
                    __attrs_140235321996880 = _static_140235489934800
                    __backup_macroname_140235423418560 = get('macroname', __marker)

                    # <Static value=<_ast.Str object at 0x7f8b148d74d0> name=None at 7f8b148d7c90> -> __value
                    __value = _static_140235321996496
                    econtext['macroname'] = __value

                    # <Value u'here/portlet_prefs/macros/portlet' (16:36)> -> __macro
                    __token = 942
                    try:
                        __zt_tmp = __attrs_140235321996880
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __macro = _static_140235435449424('path', u'here/portlet_prefs/macros/portlet', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __token = 942
                    __m = __macro.include
                    __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    if (__backup_macroname_140235423418560 is __marker):
                        del econtext['macroname']
                    else:
                        econtext['macroname'] = __backup_macroname_140235423418560
                    __append(u'\n        ')
                else:
                    __slot_column_two_slot(__stream, econtext.copy(), rcontext)
                __append(u'\n    ')
            _slots = econtext[u'__slot_portlets_two_slot'] = _deque((__fill_portlets_two_slot, ))

            def __fill_content(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321996752
                __attrs_140235321996752 = _static_140235489934800
                __append(u'\n        ')
                if (__slot_prefs_configlet_wrapper is None):

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321998352
                    __attrs_140235321998352 = _static_140235489934800
                    __append(u'\n          ')
                    if (__slot_prefs_configlet_content is None):

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235431247504
                        __attrs_140235431247504 = _static_140235489934800
                        __append(u'\n\n            ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235431244048
                        __attrs_140235431244048 = _static_140235489934800
                        __backup_macroname_140235437743152 = get('macroname', __marker)

                        # <Static value=<_ast.Str object at 0x7f8b1b1072d0> name=None at 7f8b1b107610> -> __value
                        __value = _static_140235431244496
                        econtext['macroname'] = __value

                        def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                            getitem = econtext.__getitem__
                            get = econtext.get

                            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235431247568
                            __attrs_140235431247568 = _static_140235489934800
                            __append(u'\n                ')
                            if (__slot_prefs_configlet_main is None):

                                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235432290704
                                __attrs_140235432290704 = _static_140235489934800

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431245200
                                __default_140235431245200 = _DEFAULT_MARKER

                                # <Value u'nothing' (26:82)> -> __cache_140235431245264
                                __token = 1410
                                try:
                                    __zt_tmp = __attrs_140235432290704
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140235431245264 = _static_140235435449424('path', u'nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                                # <BinOp left=<Value u'nothing' (26:82)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1b1077d0> -> __condition
                                __expression = __cache_140235431245264

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(u'\n                  Page body text\n                ')
                                else:
                                    __content = __cache_140235431245264
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
                            __zt_tmp = __attrs_140235431244048
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __macro = _static_140235435449424('path', u'context/@@main_template/macros/content', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        __token = 1233
                        __m = __macro.include
                        __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                        econtext.update(rcontext)
                        if (__backup_macroname_140235437743152 is __marker):
                            del econtext['macroname']
                        else:
                            econtext['macroname'] = __backup_macroname_140235437743152
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
                __zt_tmp = __attrs_140235374258384
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140235435449424('path', u'context/@@main_template/macros/master', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __token = 85
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140235426739456 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140235426739456
            __append(u'\n')
            __i18n_domain = __previous_i18n_domain_140235374257616
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