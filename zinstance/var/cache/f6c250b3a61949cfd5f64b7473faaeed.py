# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/path_bar.pt'

__tokens = {116: (u'view/breadcrumbs', 3, 33), 444: (u'view/navigation_root_url', 10, 33), 519: (u'breadcrumbs', 12, 28), 561: (u'string:breadcrumbs-${repeat/crumb/number}', 13, 29), 644: (u'repeat/crumb/end', 14, 38), 697: (u' crumb/absolute_ur', 15, 35), 754: (u'e crumb/Tit', 16, 36), 859: (u'python:not is_last', 19, 29), 820: (u'not: url', 18, 28), 914: (u'url', 20, 35), 946: (u'title', 21, 27), 1065: (u'is_last', 25, 31), 1103: (u'title', 26, 29)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235373784144 = {u'href': u'view/navigation_root_url', }
_static_140235377037904 = {u'id': u'breadcrumbs-current', }
_static_140235489934800 = {}
_static_140235442515088 = {u'id': u'breadcrumbs-you-are-here', u'class': u'hiddenStructure', }
_static_140235435449424 = __compile_zt_expr
_static_140235442513936 = {u'class': u'container', }
_static_140235423364688 = {u'aria-labelledby': u'breadcrumbs-you-are-here', }
_static_140235431251856 = {u'id': u'portal-breadcrumbs', u'class': u'plone-breadcrumb', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235373784336 = {u'id': u'string:breadcrumbs-${repeat/crumb/number}', }
_static_140235423363728 = {u'id': u'breadcrumbs-home', }
_static_140235377038992 = {u'href': u'#', }

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

            # <Static value=<_ast.Dict object at 0x7f8b1b108f90> name=None at 7f8b1b108b10> -> __attrs_140235442513424
            __attrs_140235442513424 = _static_140235431251856
            __backup_breadcrumbs_140235385247696 = get('breadcrumbs', __marker)

            # <Value u'view/breadcrumbs' (3:33)> -> __value
            __token = 116
            try:
                __zt_tmp = __attrs_140235442513424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/breadcrumbs', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['breadcrumbs'] = __value
            __previous_i18n_domain_140235442514832 = __i18n_domain
            __i18n_domain = u'plone'

            # <nav ... (0:0)
            # --------------------------------------------------------
            __append(u'<nav id="portal-breadcrumbs" class="plone-breadcrumb">\n  ')

            # <Static value=<_ast.Dict object at 0x7f8b1bbc6810> name=None at 7f8b1bbc69d0> -> __attrs_140235442512656
            __attrs_140235442512656 = _static_140235442513936

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="container">\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b1bbc6c90> name=None at 7f8b1bbc6c50> -> __attrs_140235423365776
            __attrs_140235423365776 = _static_140235442515088

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span id="breadcrumbs-you-are-here" class="hiddenStructure">')
            __stream_140235442512720 = []
            __append_140235442512720 = __stream_140235442512720.append
            __append_140235442512720(u'You are here:')
            __msgid_140235442512720 = __re_whitespace(''.join(__stream_140235442512720)).strip()
            if u'you_are_here':
                __append(translate(u'you_are_here', mapping=None, default=__msgid_140235442512720, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b1a983650> name=None at 7f8b1a983250> -> __attrs_140235423366288
            __attrs_140235423366288 = _static_140235423364688

            # <ol ... (0:0)
            # --------------------------------------------------------
            __append(u'<ol aria-labelledby="breadcrumbs-you-are-here">\n      ')

            # <Static value=<_ast.Dict object at 0x7f8b1a983290> name=None at 7f8b1a983910> -> __attrs_140235373782352
            __attrs_140235373782352 = _static_140235423363728

            # <li ... (0:0)
            # --------------------------------------------------------
            __append(u'<li id="breadcrumbs-home">\n        ')

            # <Static value=<_ast.Dict object at 0x7f8b17a3ac50> name=None at 7f8b17a3a390> -> __attrs_140235373784720
            __attrs_140235373784720 = _static_140235373784144

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373783376
            __default_140235373783376 = _DEFAULT_MARKER

            # <Substitution u'view/navigation_root_url' (10:33)> -> __attr_href
            __token = 444
            try:
                __zt_tmp = __attrs_140235373784720
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140235435449424('path', u'view/navigation_root_url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u'>')
            __stream_140235373781520 = []
            __append_140235373781520 = __stream_140235373781520.append
            __append_140235373781520(u'Home')
            __msgid_140235373781520 = __re_whitespace(''.join(__stream_140235373781520)).strip()
            if u'tabs_home':
                __append(translate(u'tabs_home', mapping=None, default=__msgid_140235373781520, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</a>\n      </li>\n      ')

            # <Static value=<_ast.Dict object at 0x7f8b17a3ad10> name=None at 7f8b17a3a790> -> __attrs_140235374548944
            __attrs_140235374548944 = _static_140235373784336
            __backup_crumb_140235432292112 = get('crumb', __marker)

            # <Value u'breadcrumbs' (12:28)> -> __iterator
            __token = 519
            try:
                __zt_tmp = __attrs_140235374548944
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140235435449424('path', u'breadcrumbs', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            (__iterator, ____index_140235374547088, ) = getitem('repeat')(u'crumb', __iterator)
            econtext['crumb'] = None
            for __item in __iterator:
                econtext['crumb'] = __item

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li')

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235374548880
                __default_140235374548880 = _DEFAULT_MARKER

                # <Substitution u'string:breadcrumbs-${repeat/crumb/number}' (13:29)> -> __attr_id
                __token = 561
                try:
                    __zt_tmp = __attrs_140235374548944
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140235435449424('string', u'breadcrumbs-${repeat/crumb/number}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))
                __append(u'>\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374549200
                __attrs_140235374549200 = _static_140235489934800
                __backup_is_last_140235373353808 = get('is_last', __marker)

                # <Value u'repeat/crumb/end' (14:38)> -> __value
                __token = 644
                try:
                    __zt_tmp = __attrs_140235374549200
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'repeat/crumb/end', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['is_last'] = __value
                __backup_url_140235373353040 = get('url', __marker)

                # <Value u'crumb/absolute_url' (15:35)> -> __value
                __token = 697
                try:
                    __zt_tmp = __attrs_140235374549200
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'crumb/absolute_url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['url'] = __value
                __backup_title_140235442515344 = get('title', __marker)

                # <Value u'crumb/Title' (16:36)> -> __value
                __token = 754
                try:
                    __zt_tmp = __attrs_140235374549200
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'crumb/Title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['title'] = __value
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b17d55690> name=None at 7f8b17d552d0> -> __attrs_140235377037712
                __attrs_140235377037712 = _static_140235377038992

                # <Value u'python:not is_last' (19:29)> -> __condition
                __token = 859
                try:
                    __zt_tmp = __attrs_140235377037712
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('python', u'not is_last', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <Negate value=<Value u'not: url' (18:28)> at 7f8b17d55490> -> __cache_140235377038480

                    # <Value u'not: url' (18:28)> -> __cache_140235377038480
                    __token = 820
                    try:
                        __zt_tmp = __attrs_140235377037712
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235377038480 = _static_140235435449424('not', u' url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __cache_140235377038480 = not __cache_140235377038480
                    __condition = __cache_140235377038480
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235377038096
                        __default_140235377038096 = _DEFAULT_MARKER

                        # <Substitution u'url' (20:35)> -> __attr_href
                        __token = 914
                        try:
                            __zt_tmp = __attrs_140235377037712
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140235435449424('path', u'url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u'>')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235377041168
                    __default_140235377041168 = _DEFAULT_MARKER

                    # <Value u'title' (21:27)> -> __cache_140235374547728
                    __token = 946
                    try:
                        __zt_tmp = __attrs_140235377037712
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235374547728 = _static_140235435449424('path', u'title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'title' (21:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17af5610> -> __condition
                    __expression = __cache_140235374547728

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n                  crumb\n          ')
                    else:
                        __content = __cache_140235374547728
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __condition = __cache_140235377038480
                    if __condition:
                        __append(u'</a>')
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b17d55250> name=None at 7f8b17d55210> -> __attrs_140235377040656
                __attrs_140235377040656 = _static_140235377037904

                # <Value u'is_last' (25:31)> -> __condition
                __token = 1065
                try:
                    __zt_tmp = __attrs_140235377040656
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'is_last', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span id="breadcrumbs-current">')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235377038608
                    __default_140235377038608 = _DEFAULT_MARKER

                    # <Value u'title' (26:29)> -> __cache_140235377040848
                    __token = 1103
                    try:
                        __zt_tmp = __attrs_140235377040656
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235377040848 = _static_140235435449424('path', u'title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'title' (26:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17d55550> -> __condition
                    __expression = __cache_140235377040848

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'crumb')
                    else:
                        __content = __cache_140235377040848
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>')
                __append(u'\n        ')
                if (__backup_title_140235442515344 is __marker):
                    del econtext['title']
                else:
                    econtext['title'] = __backup_title_140235442515344
                if (__backup_url_140235373353040 is __marker):
                    del econtext['url']
                else:
                    econtext['url'] = __backup_url_140235373353040
                if (__backup_is_last_140235373353808 is __marker):
                    del econtext['is_last']
                else:
                    econtext['is_last'] = __backup_is_last_140235373353808
                __append(u'\n      </li>')
                ____index_140235374547088 -= 1
                if (____index_140235374547088 > 0):
                    __append('\n      ')
            if (__backup_crumb_140235432292112 is __marker):
                del econtext['crumb']
            else:
                econtext['crumb'] = __backup_crumb_140235432292112
            __append(u'\n    </ol>\n  </div>\n</nav>')
            __i18n_domain = __previous_i18n_domain_140235442514832
            if (__backup_breadcrumbs_140235385247696 is __marker):
                del econtext['breadcrumbs']
            else:
                econtext['breadcrumbs'] = __backup_breadcrumbs_140235385247696
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }