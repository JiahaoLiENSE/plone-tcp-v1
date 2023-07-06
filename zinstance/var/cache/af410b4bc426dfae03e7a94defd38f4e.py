# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/contentviews.pt'

__tokens = {40: (u'context/@@plone', 1, 40), 91: (u'ploneview/showToolbar', 2, 33), 183: (u'view/tabSet1', 5, 29), 231: (u'python: view.menu_template(actions=actions)', 6, 32), 347: (u'provider:plone.contentmenu', 9, 32), 429: (u'view/tabSet2', 11, 29), 477: (u'python: view.menu_template(actions=actions)', 12, 32)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235435449424 = __compile_zt_expr
_static_140235435450064 = __C2ZContextWrapper
_static_140235489934800 = {}

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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235427767888
            __attrs_140235427767888 = _static_140235489934800
            __backup_ploneview_140235385300240 = get('ploneview', __marker)

            # <Value u'context/@@plone' (1:40)> -> __value
            __token = 40
            try:
                __zt_tmp = __attrs_140235427767888
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'context/@@plone', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['ploneview'] = __value

            # <Value u'ploneview/showToolbar' (2:33)> -> __condition
            __token = 91
            try:
                __zt_tmp = __attrs_140235427767888
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('path', u'ploneview/showToolbar', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140235427769296 = __i18n_domain
                __i18n_domain = u'plone'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235368736080
                __attrs_140235368736080 = _static_140235489934800
                __backup_actions_140235385295248 = get('actions', __marker)

                # <Value u'view/tabSet1' (5:29)> -> __value
                __token = 183
                try:
                    __zt_tmp = __attrs_140235368736080
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'view/tabSet1', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['actions'] = __value
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235426060240
                __attrs_140235426060240 = _static_140235489934800

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235426061456
                __default_140235426061456 = _DEFAULT_MARKER

                # <Value u'python: view.menu_template(actions=actions)' (6:32)> -> __cache_140235426062160
                __token = 231
                try:
                    __zt_tmp = __attrs_140235426060240
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140235426062160 = _static_140235435449424('python', u' view.menu_template(actions=actions)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                # <BinOp left=<Value u'python: view.menu_template(actions=actions)' (6:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1ac15e90> -> __condition
                __expression = __cache_140235426062160

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div />')
                else:
                    __content = __cache_140235426062160
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n  ')
                if (__backup_actions_140235385295248 is __marker):
                    del econtext['actions']
                else:
                    econtext['actions'] = __backup_actions_140235385295248
                __append(u'\n  ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235426059856
                __attrs_140235426059856 = _static_140235489934800
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235426059920
                __attrs_140235426059920 = _static_140235489934800

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235426059984
                __default_140235426059984 = _DEFAULT_MARKER

                # <Value u'provider:plone.contentmenu' (9:32)> -> __cache_140235426059408
                __token = 347
                try:
                    __zt_tmp = __attrs_140235426059920
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140235426059408 = _static_140235435449424('provider', u'plone.contentmenu', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                # <BinOp left=<Value u'provider:plone.contentmenu' (9:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1ac15e50> -> __condition
                __expression = __cache_140235426059408

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div />')
                else:
                    __content = __cache_140235426059408
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n  \n  ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235426061520
                __attrs_140235426061520 = _static_140235489934800
                __backup_actions_140235428377552 = get('actions', __marker)

                # <Value u'view/tabSet2' (11:29)> -> __value
                __token = 429
                try:
                    __zt_tmp = __attrs_140235426061520
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'view/tabSet2', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['actions'] = __value
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374545552
                __attrs_140235374545552 = _static_140235489934800

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235374544528
                __default_140235374544528 = _DEFAULT_MARKER

                # <Value u'python: view.menu_template(actions=actions)' (12:32)> -> __cache_140235374544208
                __token = 477
                try:
                    __zt_tmp = __attrs_140235374545552
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140235374544208 = _static_140235435449424('python', u' view.menu_template(actions=actions)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                # <BinOp left=<Value u'python: view.menu_template(actions=actions)' (12:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17af4ad0> -> __condition
                __expression = __cache_140235374544208

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div />')
                else:
                    __content = __cache_140235374544208
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n  ')
                if (__backup_actions_140235428377552 is __marker):
                    del econtext['actions']
                else:
                    econtext['actions'] = __backup_actions_140235428377552
                __append(u'\n\n')
                __i18n_domain = __previous_i18n_domain_140235427769296
            if (__backup_ploneview_140235385300240 is __marker):
                del econtext['ploneview']
            else:
                econtext['ploneview'] = __backup_ploneview_140235385300240
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }