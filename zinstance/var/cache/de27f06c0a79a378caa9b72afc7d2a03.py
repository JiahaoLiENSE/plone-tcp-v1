# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/social_tags_body.pt'

__tokens = {128: (u'view/body_tags', 3, 24), 177: (u'tag/itemprop|nothing', 4, 33), 220: (u'tag/content|nothing', 5, 21)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235435449424 = __compile_zt_expr
_static_140235435450064 = __C2ZContextWrapper
_static_140235374549584 = {u'style': u'display: none', u'id': u'social-tags-body', u'itemscope': '', u'itemtype': u'http://schema.org/WebPage', }
_static_140235431275472 = {u'itemprop': u'tag/itemprop|nothing', }

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

            # <Static value=<_ast.Dict object at 0x7f8b17af5a50> name=None at 7f8b17af5510> -> __attrs_140235431274576
            __attrs_140235431274576 = _static_140235374549584

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span id="social-tags-body" style="display: none" itemscope itemtype="http://schema.org/WebPage">\n  ')

            # <Static value=<_ast.Dict object at 0x7f8b1b10ebd0> name=None at 7f8b1b10e690> -> __attrs_140235431276240
            __attrs_140235431276240 = _static_140235431275472
            __backup_tag_140235374547408 = get('tag', __marker)

            # <Value u'view/body_tags' (3:24)> -> __iterator
            __token = 128
            try:
                __zt_tmp = __attrs_140235431276240
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140235435449424('path', u'view/body_tags', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            (__iterator, ____index_140235431275344, ) = getitem('repeat')(u'tag', __iterator)
            econtext['tag'] = None
            for __item in __iterator:
                econtext['tag'] = __item

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span')

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431273104
                __default_140235431273104 = _DEFAULT_MARKER

                # <Substitution u'tag/itemprop|nothing' (4:33)> -> __attr_itemprop
                __token = 177
                try:
                    __zt_tmp = __attrs_140235431276240
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_itemprop = _static_140235435449424('path', u'tag/itemprop|nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_itemprop = __quote(__attr_itemprop, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_itemprop is not None):
                    __append((u' itemprop="%s"' % __attr_itemprop))
                __append(u'>')

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431272528
                __default_140235431272528 = _DEFAULT_MARKER

                # <Value u'tag/content|nothing' (5:21)> -> __cache_140235431276112
                __token = 220
                try:
                    __zt_tmp = __attrs_140235431276240
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140235431276112 = _static_140235435449424('path', u'tag/content|nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                # <BinOp left=<Value u'tag/content|nothing' (5:21)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1b10e550> -> __condition
                __expression = __cache_140235431276112

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140235431276112
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>')
                ____index_140235431275344 -= 1
                if (____index_140235431275344 > 0):
                    __append('\n  ')
            if (__backup_tag_140235374547408 is __marker):
                del econtext['tag']
            else:
                econtext['tag'] = __backup_tag_140235374547408
            __append(u'\n</span>\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }