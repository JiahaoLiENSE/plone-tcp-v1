# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/globalstatusmessage.pt'

__tokens = {36: (u'view/messages', 1, 36), 75: (u'messages', 2, 24), 114: (u'message/type | nothing', 4, 27), 169: (u'string:portalMessage ${mtype}', 5, 30), 293: (u'python:mtype.capitalize()', 8, 43), 389: (u'message/message | nothing', 10, 25)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235431250960 = {u'class': u'content', }
_static_140235435449424 = __compile_zt_expr
_static_140235435450064 = __C2ZContextWrapper
_static_140235489934800 = {}
_static_140235438233296 = {u'class': u'string:portalMessage ${mtype}', }

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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235438233360
            __attrs_140235438233360 = _static_140235489934800
            __backup_messages_140235373800912 = get('messages', __marker)

            # <Value u'view/messages' (1:36)> -> __value
            __token = 36
            try:
                __zt_tmp = __attrs_140235438233360
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/messages', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['messages'] = __value
            __backup_message_140235373783312 = get('message', __marker)

            # <Value u'messages' (2:24)> -> __iterator
            __token = 75
            try:
                __zt_tmp = __attrs_140235438233360
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140235435449424('path', u'messages', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            (__iterator, ____index_140235438234320, ) = getitem('repeat')(u'message', __iterator)
            econtext['message'] = None
            for __item in __iterator:
                econtext['message'] = __item
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1b7b16d0> name=None at 7f8b1b7b12d0> -> __attrs_140235438232592
                __attrs_140235438232592 = _static_140235438233296
                __backup_mtype_140235385247504 = get('mtype', __marker)

                # <Value u'message/type | nothing' (4:27)> -> __value
                __token = 114
                try:
                    __zt_tmp = __attrs_140235438232592
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'message/type | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['mtype'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div')

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235438235536
                __default_140235438235536 = _DEFAULT_MARKER

                # <Substitution u'string:portalMessage ${mtype}' (5:30)> -> __attr_class
                __token = 169
                try:
                    __zt_tmp = __attrs_140235438232592
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140235435449424('string', u'portalMessage ${mtype}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((u' class="%s"' % __attr_class))
                __append(u'>\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235431250256
                __attrs_140235431250256 = _static_140235489934800
                __previous_i18n_domain_140235431249616 = __i18n_domain
                __i18n_domain = u'plone'

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append(u'<strong>')

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431248400
                __default_140235431248400 = _DEFAULT_MARKER

                # <Value u'python:mtype.capitalize()' (8:43)> -> __cache_140235438235088
                __token = 293
                try:
                    __zt_tmp = __attrs_140235431250256
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140235438235088 = _static_140235435449424('python', u'mtype.capitalize()', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                # <BinOp left=<Value u'python:mtype.capitalize()' (8:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1b108fd0> -> __condition
                __expression = __cache_140235438235088

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'Info')
                else:
                    __content = __cache_140235438235088
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</strong>')
                __i18n_domain = __previous_i18n_domain_140235431249616
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b1b108c10> name=None at 7f8b1b108cd0> -> __attrs_140235431249104
                __attrs_140235431249104 = _static_140235431250960

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431249744
                __default_140235431249744 = _DEFAULT_MARKER

                # <Value u'message/message | nothing' (10:25)> -> __cache_140235431251088
                __token = 389
                try:
                    __zt_tmp = __attrs_140235431249104
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140235431251088 = _static_140235435449424('path', u'message/message | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                # <BinOp left=<Value u'message/message | nothing' (10:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1b1089d0> -> __condition
                __expression = __cache_140235431251088

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="content">\n            The status message.\n        </span>')
                else:
                    __content = __cache_140235431251088
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n    </div>')
                if (__backup_mtype_140235385247504 is __marker):
                    del econtext['mtype']
                else:
                    econtext['mtype'] = __backup_mtype_140235385247504
                __append(u'\n\n')
                ____index_140235438234320 -= 1
                if (____index_140235438234320 > 0):
                    __append('')
            if (__backup_message_140235373783312 is __marker):
                del econtext['message']
            else:
                econtext['message'] = __backup_message_140235373783312
            if (__backup_messages_140235373800912 is __marker):
                del econtext['messages']
            else:
                econtext['messages'] = __backup_messages_140235373800912
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }