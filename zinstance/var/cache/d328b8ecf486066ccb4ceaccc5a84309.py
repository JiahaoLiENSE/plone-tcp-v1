# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/document_actions.pt'

__tokens = {166: (u'view/actions', 7, 39), 357: (u'nocall: context/@@plone/normalizeString', 13, 44), 441: (u'view/actions', 14, 42), 496: (u"python:'document-action-' + normalizeString(daction['id'])", 15, 41), 636: (u'daction/url', 17, 46), 696: (u' daction/link_target|nothin', 18, 47), 771: (u'e daction/descripti', 19, 45), 832: (u'daction/title', 20, 38), 980: (u'provider:plone.documentactions', 26, 36)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386069972880 = {u'class': u'documentActions', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386079223120 = {u'href': u'', u'target': u'daction/link_target|nothing', u'title': u'daction/description', }
_static_140386186296528 = __compile_zt_expr
_static_140386071889040 = {u'class': u'hiddenStructure', }
_static_140386070894544 = {u'id': u"python:'document-action-' + normalizeString(daction['id'])", }
_static_140386069972240 = {u'class': u'visualClear', }
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

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070659344
            __attrs_140386070659344 = _static_140386247937936
            __previous_i18n_domain_140386070662032 = __i18n_domain
            __i18n_domain = u'plone'
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae2dd50510> name=None at 7fae2dd50190> -> __attrs_140386069972368
            __attrs_140386069972368 = _static_140386069972240

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="visualClear"><!-- --></div>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae2dd50790> name=None at 7fae2dd500d0> -> __attrs_140386069972560
            __attrs_140386069972560 = _static_140386069972880

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="documentActions">\n        ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069973584
            __attrs_140386069973584 = _static_140386247937936

            # <Value u'view/actions' (7:39)> -> __condition
            __token = 166
            try:
                __zt_tmp = __attrs_140386069973584
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('path', u'view/actions', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:
                __append(u'\n\n            ')

                # <Static value=<_ast.Dict object at 0x7fae2df24490> name=None at 7fae2df249d0> -> __attrs_140386071890000
                __attrs_140386071890000 = _static_140386071889040

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p class="hiddenStructure">')
                __stream_140386071888976 = []
                __append_140386071888976 = __stream_140386071888976.append
                __append_140386071888976(u'\n              Document Actions\n            ')
                __msgid_140386071888976 = __re_whitespace(''.join(__stream_140386071888976)).strip()
                if u'heading_document_actions':
                    __append(translate(u'heading_document_actions', mapping=None, default=__msgid_140386071888976, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</p>\n\n            ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071889808
                __attrs_140386071889808 = _static_140386247937936
                __backup_normalizeString_140386078079760 = get('normalizeString', __marker)

                # <Value u'nocall: context/@@plone/normalizeString' (13:44)> -> __value
                __token = 357
                try:
                    __zt_tmp = __attrs_140386071889808
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('nocall', u' context/@@plone/normalizeString', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['normalizeString'] = __value

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul>\n                  ')

                # <Static value=<_ast.Dict object at 0x7fae2de317d0> name=None at 7fae2de31f90> -> __attrs_140386070893136
                __attrs_140386070893136 = _static_140386070894544
                __backup_daction_140386069902032 = get('daction', __marker)

                # <Value u'view/actions' (14:42)> -> __iterator
                __token = 441
                try:
                    __zt_tmp = __attrs_140386070893136
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140386186296528('path', u'view/actions', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                (__iterator, ____index_140386070893712, ) = getitem('repeat')(u'daction', __iterator)
                econtext['daction'] = None
                for __item in __iterator:
                    econtext['daction'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070895440
                    __default_140386070895440 = _DEFAULT_MARKER

                    # <Substitution u"python:'document-action-' + normalizeString(daction['id'])" (15:41)> -> __attr_id
                    __token = 496
                    try:
                        __zt_tmp = __attrs_140386070893136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140386186296528('python', u"'document-action-' + normalizeString(daction['id'])", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))
                    __append(u'>\n                      ')

                    # <Static value=<_ast.Dict object at 0x7fae2e622d50> name=None at 7fae2e622e10> -> __attrs_140386069198736
                    __attrs_140386069198736 = _static_140386079223120

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386079221200
                    __default_140386079221200 = _DEFAULT_MARKER

                    # <Substitution u'daction/url' (17:46)> -> __attr_href
                    __token = 636
                    try:
                        __zt_tmp = __attrs_140386069198736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140386186296528('path', u'daction/url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069198096
                    __default_140386069198096 = _DEFAULT_MARKER

                    # <Substitution u'daction/link_target|nothing' (18:47)> -> __attr_target
                    __token = 696
                    try:
                        __zt_tmp = __attrs_140386069198736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_target = _static_140386186296528('path', u'daction/link_target|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_target = __quote(__attr_target, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_target is not None):
                        __append((u' target="%s"' % __attr_target))

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069199696
                    __default_140386069199696 = _DEFAULT_MARKER

                    # <Substitution u'daction/description' (19:45)> -> __attr_title
                    __token = 771
                    try:
                        __zt_tmp = __attrs_140386069198736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140386186296528('path', u'daction/description', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))
                    __append(u'>')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386079221264
                    __default_140386079221264 = _DEFAULT_MARKER

                    # <Value u'daction/title' (20:38)> -> __cache_140386079220944
                    __token = 832
                    try:
                        __zt_tmp = __attrs_140386069198736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386079220944 = _static_140386186296528('path', u'daction/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'daction/title' (20:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e622cd0> -> __condition
                    __expression = __cache_140386079220944

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n                      ')
                    else:
                        __content = __cache_140386079220944
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</a>\n                  </li>')
                    ____index_140386070893712 -= 1
                    if (____index_140386070893712 > 0):
                        __append('\n                  ')
                if (__backup_daction_140386069902032 is __marker):
                    del econtext['daction']
                else:
                    econtext['daction'] = __backup_daction_140386069902032
                __append(u'\n            </ul>')
                if (__backup_normalizeString_140386078079760 is __marker):
                    del econtext['normalizeString']
                else:
                    econtext['normalizeString'] = __backup_normalizeString_140386078079760
                __append(u'\n        ')
            __append(u'\n\n        ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070894032
            __attrs_140386070894032 = _static_140386247937936

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070894736
            __default_140386070894736 = _DEFAULT_MARKER

            # <Value u'provider:plone.documentactions' (26:36)> -> __cache_140386071890192
            __token = 980
            try:
                __zt_tmp = __attrs_140386070894032
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386071890192 = _static_140386186296528('provider', u'plone.documentactions', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.documentactions' (26:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2df24fd0> -> __condition
            __expression = __cache_140386071890192

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140386071890192
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n    </div>\n')
            __i18n_domain = __previous_i18n_domain_140386070662032
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }