# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/social_tags.pt'

__tokens = {22: (u'view/tags', 1, 22), 49: (u'tag', 1, 49)}

from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235435449424 = __compile_zt_expr
_static_140235435450064 = __C2ZContextWrapper
_static_140235489934800 = {}
_static_140235423366608 = set([])

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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373963408
            __attrs_140235373963408 = _static_140235489934800
            __backup_tag_140235427350736 = get('tag', __marker)

            # <Value u'view/tags' (1:22)> -> __iterator
            __token = 22
            try:
                __zt_tmp = __attrs_140235373963408
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140235435449424('path', u'view/tags', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            (__iterator, ____index_140235373963152, ) = getitem('repeat')(u'tag', __iterator)
            econtext['tag'] = None
            for __item in __iterator:
                econtext['tag'] = __item

                # <meta ... (0:0)
                # --------------------------------------------------------
                __append(u'<meta')

                # <Value u'tag' (1:49)> -> __cache_140235373962128
                __token = 49
                try:
                    __zt_tmp = __attrs_140235373963408
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140235373962128 = _static_140235435449424('path', u'tag', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_140235373961936 = __cache_140235373962128
                for (name, value, ) in __attr_140235373961936.items():
                    if ((name not in _static_140235423366608) and (value is not None)):
                        __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                __append(u' />')
                ____index_140235373963152 -= 1
                if (____index_140235373963152 > 0):
                    __append('\n')
            if (__backup_tag_140235427350736 is __marker):
                del econtext['tag']
            else:
                econtext['tag'] = __backup_tag_140235427350736
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }