# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/z3c.form-3.7.1-py2.7.egg/z3c/form/browser/select_hidden.pt'

__tokens = {138: (u'view/id', 4, 22), 170: (u' string:${view/name}:lis', 5, 23), 221: (u'view/items', 6, 24), 327: (u'item/selected', 8, 24), 370: (u'item/id', 9, 28), 383: (u' nam', 9, 41), 394: (u'e item/val', 9, 52), 509: (u'string:${view/name}-empty-marker', 12, 28)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235323209744 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140235319993744 = {u'class': u'hidden-widget', u'type': u'hidden', u'id': u'', u'value': u'', u'name': u'', }
_static_140235489934800 = {}
_static_140235435449424 = __compile_zt_expr
_static_140235435450064 = __C2ZContextWrapper
_static_140235323207824 = {u'type': u'hidden', u'name': u'field-empty-marker', u'value': u'1', }

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

            # <Static value=<_ast.Dict object at 0x7f8b149ff810> name=None at 7f8b149ff290> -> __attrs_140235323210000
            __attrs_140235323210000 = _static_140235323209744
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235323209552
            __attrs_140235323209552 = _static_140235489934800
            __backup_id_140235385335952 = get('id', __marker)

            # <Value u'view/id' (4:22)> -> __value
            __token = 138
            try:
                __zt_tmp = __attrs_140235323209552
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/id', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['id'] = __value
            __backup_name_140235322701968 = get('name', __marker)

            # <Value u'string:${view/name}:list' (5:23)> -> __value
            __token = 170
            try:
                __zt_tmp = __attrs_140235323209552
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('string', u'${view/name}:list', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['name'] = __value
            __backup_item_140235320907600 = get('item', __marker)

            # <Value u'view/items' (6:24)> -> __iterator
            __token = 221
            try:
                __zt_tmp = __attrs_140235323209552
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140235435449424('path', u'view/items', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            (__iterator, ____index_140235319993232, ) = getitem('repeat')(u'item', __iterator)
            econtext['item'] = None
            for __item in __iterator:
                econtext['item'] = __item
                __append(u'\n  ')

                # <Static value=<_ast.Dict object at 0x7f8b146ee590> name=None at 7f8b146ee610> -> __attrs_140235322132112
                __attrs_140235322132112 = _static_140235319993744

                # <Value u'item/selected' (8:24)> -> __condition
                __token = 327
                try:
                    __zt_tmp = __attrs_140235322132112
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'item/selected', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235319994512
                    __default_140235319994512 = _DEFAULT_MARKER

                    # <Substitution u'item/id' (9:28)> -> __attr_id
                    __token = 370
                    try:
                        __zt_tmp = __attrs_140235322132112
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140235435449424('path', u'item/id', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235319992976
                    __default_140235319992976 = _DEFAULT_MARKER

                    # <Substitution u'name' (9:41)> -> __attr_name
                    __token = 383
                    try:
                        __zt_tmp = __attrs_140235322132112
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_name = _static_140235435449424('path', u'name', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_name = __quote(__attr_name, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_name is not None):
                        __append((u' name="%s"' % __attr_name))

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235319993808
                    __default_140235319993808 = _DEFAULT_MARKER

                    # <Substitution u'item/value' (9:52)> -> __attr_value
                    __token = 394
                    try:
                        __zt_tmp = __attrs_140235322132112
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140235435449424('path', u'item/value', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u'  value="%s"' % __attr_value))
                    __append(u' class="hidden-widget" type="hidden" />')
                __append(u'\n')
                ____index_140235319993232 -= 1
                if (____index_140235319993232 > 0):
                    __append('')
            if (__backup_item_140235320907600 is __marker):
                del econtext['item']
            else:
                econtext['item'] = __backup_item_140235320907600
            if (__backup_name_140235322701968 is __marker):
                del econtext['name']
            else:
                econtext['name'] = __backup_name_140235322701968
            if (__backup_id_140235385335952 is __marker):
                del econtext['id']
            else:
                econtext['id'] = __backup_id_140235385335952
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x7f8b149ff090> name=None at 7f8b149ffa50> -> __attrs_140235319828560
            __attrs_140235319828560 = _static_140235323207824

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235319831824
            __default_140235319831824 = _DEFAULT_MARKER

            # <Substitution u'string:${view/name}-empty-marker' (12:28)> -> __attr_name
            __token = 509
            try:
                __zt_tmp = __attrs_140235319828560
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140235435449424('string', u'${view/name}-empty-marker', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', u'field-empty-marker', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))
            __append(u' type="hidden" value="1" />\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }