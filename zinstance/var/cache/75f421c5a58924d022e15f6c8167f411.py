# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/anontools.pt'

__tokens = {42: (u'python:view.user_actions and view.anonymous', 1, 42), 138: (u'view/user_actions', 4, 34), 208: (u'action', 6, 29), 242: (u'action/title', 7, 26)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386070915280 = set([])
_static_140386073253008 = {u'id': u'portal-anontools', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386186296528 = __compile_zt_expr
_static_140386071167056 = {u'href': u'', }
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

            # <Static value=<_ast.Dict object at 0x7fae2e071490> name=None at 7fae2e071cd0> -> __attrs_140386071807696
            __attrs_140386071807696 = _static_140386073253008

            # <Value u'python:view.user_actions and view.anonymous' (1:42)> -> __condition
            __token = 42
            try:
                __zt_tmp = __attrs_140386071807696
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('python', u'view.user_actions and view.anonymous', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="portal-anontools">\n  ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071809232
                __attrs_140386071809232 = _static_140386247937936

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul>\n    ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386135461392
                __attrs_140386135461392 = _static_140386247937936

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li>\n      ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386075006672
                __attrs_140386075006672 = _static_140386247937936
                __backup_action_140386078080528 = get('action', __marker)

                # <Value u'view/user_actions' (4:34)> -> __iterator
                __token = 138
                try:
                    __zt_tmp = __attrs_140386075006672
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140386186296528('path', u'view/user_actions', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                (__iterator, ____index_140386075005072, ) = getitem('repeat')(u'action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7fae2de74050> name=None at 7fae2de74950> -> __attrs_140386071169104
                    __attrs_140386071169104 = _static_140386071167056

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Value u'action' (6:29)> -> __cache_140386071168592
                    __token = 208
                    try:
                        __zt_tmp = __attrs_140386071169104
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386071168592 = _static_140386186296528('path', u'action', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if (u'href' not in __chain(__cache_140386071168592)):
                        __append(u' href=""')
                    __attr_140386071169872 = __cache_140386071168592
                    for (name, value, ) in __attr_140386071169872.items():
                        if ((name not in _static_140386070915280) and (value is not None)):
                            __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                    __append(u'>')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071170576
                    __default_140386071170576 = _DEFAULT_MARKER

                    # <Value u'action/title' (7:26)> -> __cache_140386071168400
                    __token = 242
                    try:
                        __zt_tmp = __attrs_140386071169104
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386071168400 = _static_140386186296528('path', u'action/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'action/title' (7:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2de74390> -> __condition
                    __expression = __cache_140386071168400

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n              action title\n          ')
                    else:
                        __content = __cache_140386071168400
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</a>\n      ')
                    ____index_140386075005072 -= 1
                    if (____index_140386075005072 > 0):
                        __append('')
                if (__backup_action_140386078080528 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_140386078080528
                __append(u'\n    </li>\n  </ul>\n</div>')
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }