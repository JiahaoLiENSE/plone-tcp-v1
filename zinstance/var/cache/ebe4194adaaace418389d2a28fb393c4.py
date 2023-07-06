# -*- coding: utf-8 -*-
__filename = 'login_form'

__tokens = {166: (u'string:${here/absolute_url}/login', 11, 33), 291: (u'request/came_from | string:', 14, 35)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386078042064 = {u'cellpadding': u'2', }
_static_140386079189840 = {u'type': u'hidden', u'name': u'came_from', u'value': u'', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386079188432 = {u'action': u'', u'method': u'post', }
_static_140386186296528 = __compile_zt_expr
_static_140386079086224 = {u'colspan': u'2', }
_static_140386078095312 = {u'type': u'text', u'name': u'__ac_name', u'size': u'30', }
_static_140386079182992 = {u'type': u'submit', u'value': u' Log In ', }
_static_140386079085520 = {u'type': u'password', u'name': u'__ac_password', u'size': u'30', }
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

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078101072
            __attrs_140386078101072 = _static_140386247937936

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html>\n  ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078099984
            __attrs_140386078099984 = _static_140386247937936

            # <head ... (0:0)
            # --------------------------------------------------------
            __append(u'<head>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386079189584
            __attrs_140386079189584 = _static_140386247937936

            # <title ... (0:0)
            # --------------------------------------------------------
            __append(u'<title> Login Form </title>\n  </head>\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386079190096
            __attrs_140386079190096 = _static_140386247937936

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386079190672
            __attrs_140386079190672 = _static_140386247937936

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append(u'<h3> Please log in </h3>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae2e61a5d0> name=None at 7fae2e61ad90> -> __attrs_140386079189648
            __attrs_140386079189648 = _static_140386079188432

            # <form ... (0:0)
            # --------------------------------------------------------
            __append(u'<form method="post"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386079189456
            __default_140386079189456 = _DEFAULT_MARKER

            # <Substitution u'string:${here/absolute_url}/login' (11:33)> -> __attr_action
            __token = 166
            try:
                __zt_tmp = __attrs_140386079189648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140386186296528('string', u'${here/absolute_url}/login', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((u' action="%s"' % __attr_action))
            __append(u'>\n\n      ')

            # <Static value=<_ast.Dict object at 0x7fae2e61ab50> name=None at 7fae2e61a050> -> __attrs_140386078041424
            __attrs_140386078041424 = _static_140386079189840

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="hidden" name="came_from"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078043792
            __default_140386078043792 = _DEFAULT_MARKER

            # <Substitution u'request/came_from | string:' (14:35)> -> __attr_value
            __token = 291
            try:
                __zt_tmp = __attrs_140386078041424
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140386186296528('path', u'request/came_from | string:', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u'/>\n      ')

            # <Static value=<_ast.Dict object at 0x7fae2e5027d0> name=None at 7fae2e502790> -> __attrs_140386078040464
            __attrs_140386078040464 = _static_140386078042064

            # <table ... (0:0)
            # --------------------------------------------------------
            __append(u'<table cellpadding="2">\n        ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078042192
            __attrs_140386078042192 = _static_140386247937936

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append(u'<tr>\n          ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078097040
            __attrs_140386078097040 = _static_140386247937936

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078093968
            __attrs_140386078093968 = _static_140386247937936

            # <b ... (0:0)
            # --------------------------------------------------------
            __append(u'<b>Login:</b> </td>\n          ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078096272
            __attrs_140386078096272 = _static_140386247937936

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>')

            # <Static value=<_ast.Dict object at 0x7fae2e50f7d0> name=None at 7fae2e50f4d0> -> __attrs_140386078093648
            __attrs_140386078093648 = _static_140386078095312

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="text" name="__ac_name" size="30" /></td>\n        </tr>\n        ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078096464
            __attrs_140386078096464 = _static_140386247937936

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append(u'<tr>\n          ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078094288
            __attrs_140386078094288 = _static_140386247937936

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386079086928
            __attrs_140386079086928 = _static_140386247937936

            # <b ... (0:0)
            # --------------------------------------------------------
            __append(u'<b>Password:</b></td>\n          ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386079088208
            __attrs_140386079088208 = _static_140386247937936

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>')

            # <Static value=<_ast.Dict object at 0x7fae2e6013d0> name=None at 7fae2e601c10> -> __attrs_140386079085776
            __attrs_140386079085776 = _static_140386079085520

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="password" name="__ac_password" size="30" /></td>\n        </tr>\n        ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386079085008
            __attrs_140386079085008 = _static_140386247937936

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append(u'<tr>\n          ')

            # <Static value=<_ast.Dict object at 0x7fae2e601690> name=None at 7fae2e6015d0> -> __attrs_140386079185232
            __attrs_140386079185232 = _static_140386079086224

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td colspan="2">\n            ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386079183952
            __attrs_140386079183952 = _static_140386247937936

            # <br ... (0:0)
            # --------------------------------------------------------
            __append(u'<br />\n            ')

            # <Static value=<_ast.Dict object at 0x7fae2e619090> name=None at 7fae2e619a10> -> __attrs_140386079186704
            __attrs_140386079186704 = _static_140386079182992

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="submit" value=" Log In " />\n          </td>\n        </tr>\n      </table>\n\n    </form>\n\n  </body>\n\n</html>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }