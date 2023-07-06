# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/social_tags.pt'

__tokens = {22: (u'view/tags', 1, 22), 49: (u'tag', 1, 49)}

from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386186297040 = __C2ZContextWrapper
_static_140386071211216 = set([])
_static_140386186296528 = __compile_zt_expr
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

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071312464
            __attrs_140386071312464 = _static_140386247937936
            __backup_tag_140386071839504 = get('tag', __marker)

            # <Value u'view/tags' (1:22)> -> __iterator
            __token = 22
            try:
                __zt_tmp = __attrs_140386071312464
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140386186296528('path', u'view/tags', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            (__iterator, ____index_140386071312592, ) = getitem('repeat')(u'tag', __iterator)
            econtext['tag'] = None
            for __item in __iterator:
                econtext['tag'] = __item

                # <meta ... (0:0)
                # --------------------------------------------------------
                __append(u'<meta')

                # <Value u'tag' (1:49)> -> __cache_140386071313168
                __token = 49
                try:
                    __zt_tmp = __attrs_140386071312464
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140386071313168 = _static_140386186296528('path', u'tag', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __attr_140386071312912 = __cache_140386071313168
                for (name, value, ) in __attr_140386071312912.items():
                    if ((name not in _static_140386071211216) and (value is not None)):
                        __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                __append(u' />')
                ____index_140386071312592 -= 1
                if (____index_140386071312592 > 0):
                    __append('\n')
            if (__backup_tag_140386071839504 is __marker):
                del econtext['tag']
            else:
                econtext['tag'] = __backup_tag_140386071839504
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }