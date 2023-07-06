# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/document_byline.pt'

__tokens = {105: (u'view/show', 4, 20), 163: (u'view/creator', 5, 46), 208: (u'creator_short_form', 6, 30), 271: (u'string:?author=${creator_short_form}', 7, 42), 350: (u" python:'/' in creator_short_for", 8, 41), 418: (u'd python:(creator_short_form, creator_long_form)[creator_is_openi', 9, 33), 773: (u'python:view.author() is None', 16, 23), 630: (u'string:${context/@@plone_portal_state/navigation_root_url}/author/${creator_id}', 14, 30), 733: (u'view/authorname', 15, 22), 954: (u'view/pub_date', 24, 31), 998: (u' context/ModificationDat', 25, 29), 1083: (u'published', 27, 23), 1252: (u'published', 32, 23), 1311: (u'modified', 34, 31), 1400: (u'modified', 38, 23), 1576: (u'modified', 43, 23), 1670: (u'view/isExpired', 49, 30), 1866: (u'context/Contributors', 56, 32), 1910: (u'contributors', 57, 22), 2061: (u"python: ', '.join(contributors)", 62, 23), 2161: (u'context/Rights', 67, 33), 2206: (u'rights', 68, 29), 2237: (u'rights', 69, 22)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235432552528 = {u'class': u'documentPublished', }
_static_140235427785424 = {u'class': u'documentAuthor', }
_static_140235377189648 = {u'data-pat-moment': u'format:relative;', u'class': u'pat-moment', }
_static_140235373759824 = {u'data-pat-moment': u'format:relative;', u'class': u'pat-moment', }
_static_140235489934800 = {}
_static_140235385325584 = {u'class': u'documentModified', }
_static_140235377039184 = {u'class': u'state-expired', }
_static_140235435449424 = __compile_zt_expr
_static_140235377038672 = {u'class': u'documentContributors', }
_static_140235424281552 = {u'href': u'#', }
_static_140235431314640 = {u'class': u'documentByLine', u'id': u'plone-document-byline', }
_static_140235435450064 = __C2ZContextWrapper

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

            # <Static value=<_ast.Dict object at 0x7f8b1b1184d0> name=None at 7f8b1b118550> -> __attrs_140235431313680
            __attrs_140235431313680 = _static_140235431314640

            # <Value u'view/show' (4:20)> -> __condition
            __token = 105
            try:
                __zt_tmp = __attrs_140235431313680
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('path', u'view/show', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140235431315152 = __i18n_domain
                __i18n_domain = u'plone'

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="documentByLine" id="plone-document-byline">\n  ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235431316944
                __attrs_140235431316944 = _static_140235489934800
                __backup_creator_short_form_140235373783120 = get('creator_short_form', __marker)

                # <Value u'view/creator' (5:46)> -> __value
                __token = 163
                try:
                    __zt_tmp = __attrs_140235431316944
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'view/creator', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['creator_short_form'] = __value

                # <Value u'creator_short_form' (6:30)> -> __condition
                __token = 208
                try:
                    __zt_tmp = __attrs_140235431316944
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'creator_short_form', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n  ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235427785232
                    __attrs_140235427785232 = _static_140235489934800
                    __backup_creator_long_form_140235368765008 = get('creator_long_form', __marker)

                    # <Value u'string:?author=${creator_short_form}' (7:42)> -> __value
                    __token = 271
                    try:
                        __zt_tmp = __attrs_140235427785232
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('string', u'?author=${creator_short_form}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['creator_long_form'] = __value
                    __backup_creator_is_openid_140235442513488 = get('creator_is_openid', __marker)

                    # <Value u"python:'/' in creator_short_form" (8:41)> -> __value
                    __token = 350
                    try:
                        __zt_tmp = __attrs_140235427785232
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('python', u"'/' in creator_short_form", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['creator_is_openid'] = __value
                    __backup_creator_id_140235431273040 = get('creator_id', __marker)

                    # <Value u'python:(creator_short_form, creator_long_form)[creator_is_openid]' (9:33)> -> __value
                    __token = 418
                    try:
                        __zt_tmp = __attrs_140235427785232
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('python', u'(creator_short_form, creator_long_form)[creator_is_openid]', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['creator_id'] = __value
                    __append(u'\n    ')

                    # <Static value=<_ast.Dict object at 0x7f8b1adbaad0> name=None at 7f8b1adba350> -> __attrs_140235432551184
                    __attrs_140235432551184 = _static_140235427785424

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="documentAuthor">\n      ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235432554000
                    __attrs_140235432554000 = _static_140235489934800
                    __stream_140235424597488_author = ''
                    __stream_140235432550992 = []
                    __append_140235432550992 = __stream_140235432550992.append
                    __append_140235432550992(u'\n      by\n      ')
                    __stream_140235424597488_author = []
                    __append_140235424597488_author = __stream_140235424597488_author.append

                    # <Static value=<_ast.Dict object at 0x7f8b1aa633d0> name=None at 7f8b1aa630d0> -> __attrs_140235424283856
                    __attrs_140235424283856 = _static_140235424281552

                    # <Negate value=<Value u'python:view.author() is None' (16:23)> at 7f8b1aa63f50> -> __cache_140235424284496

                    # <Value u'python:view.author() is None' (16:23)> -> __cache_140235424284496
                    __token = 773
                    try:
                        __zt_tmp = __attrs_140235424283856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235424284496 = _static_140235435449424('python', u'view.author() is None', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __cache_140235424284496 = not __cache_140235424284496
                    __condition = __cache_140235424284496
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append_140235424597488_author(u'<a')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235424282960
                        __default_140235424282960 = _DEFAULT_MARKER

                        # <Substitution u'string:${context/@@plone_portal_state/navigation_root_url}/author/${creator_id}' (14:30)> -> __attr_href
                        __token = 630
                        try:
                            __zt_tmp = __attrs_140235424283856
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140235435449424('string', u'${context/@@plone_portal_state/navigation_root_url}/author/${creator_id}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append_140235424597488_author((u' href="%s"' % __attr_href))
                        __append_140235424597488_author(u'>')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235424284176
                    __default_140235424284176 = _DEFAULT_MARKER

                    # <Value u'view/authorname' (15:22)> -> __cache_140235432552400
                    __token = 733
                    try:
                        __zt_tmp = __attrs_140235424283856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235432552400 = _static_140235435449424('path', u'view/authorname', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'view/authorname' (15:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1b246190> -> __condition
                    __expression = __cache_140235432552400

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append_140235424597488_author(u'Roland Barthes')
                    else:
                        __content = __cache_140235432552400
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140235424597488_author(__content)
                    __condition = __cache_140235424284496
                    if __condition:
                        __append_140235424597488_author(u'</a>')
                    __append_140235432550992(u'${author}')
                    __stream_140235424597488_author = ''.join(__stream_140235424597488_author)
                    __append_140235432550992(u'\n      ')
                    __msgid_140235432550992 = __re_whitespace(''.join(__stream_140235432550992)).strip()
                    if u'label_by_author':
                        __append(translate(u'label_by_author', mapping={u'author': __stream_140235424597488_author, }, default=__msgid_140235432550992, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n         \u2014\n    </span>\n  ')
                    if (__backup_creator_id_140235431273040 is __marker):
                        del econtext['creator_id']
                    else:
                        econtext['creator_id'] = __backup_creator_id_140235431273040
                    if (__backup_creator_is_openid_140235442513488 is __marker):
                        del econtext['creator_is_openid']
                    else:
                        econtext['creator_is_openid'] = __backup_creator_is_openid_140235442513488
                    if (__backup_creator_long_form_140235368765008 is __marker):
                        del econtext['creator_long_form']
                    else:
                        econtext['creator_long_form'] = __backup_creator_long_form_140235368765008
                    __append(u'\n  ')
                if (__backup_creator_short_form_140235373783120 is __marker):
                    del econtext['creator_short_form']
                else:
                    econtext['creator_short_form'] = __backup_creator_short_form_140235373783120
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235431315344
                __attrs_140235431315344 = _static_140235489934800
                __backup_published_140235374308816 = get('published', __marker)

                # <Value u'view/pub_date' (24:31)> -> __value
                __token = 954
                try:
                    __zt_tmp = __attrs_140235431315344
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'view/pub_date', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['published'] = __value
                __backup_modified_140235438233424 = get('modified', __marker)

                # <Value u'context/ModificationDate' (25:29)> -> __value
                __token = 998
                try:
                    __zt_tmp = __attrs_140235431315344
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'context/ModificationDate', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['modified'] = __value
                __append(u'\n  ')

                # <Static value=<_ast.Dict object at 0x7f8b1b246850> name=None at 7f8b1b246150> -> __attrs_140235424282576
                __attrs_140235424282576 = _static_140235432552528

                # <Value u'published' (27:23)> -> __condition
                __token = 1083
                try:
                    __zt_tmp = __attrs_140235424282576
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'published', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="documentPublished">\n    ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235377190288
                    __attrs_140235377190288 = _static_140235489934800

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140235377192848 = []
                    __append_140235377192848 = __stream_140235377192848.append
                    __append_140235377192848(u'\n      published\n    ')
                    __msgid_140235377192848 = __re_whitespace(''.join(__stream_140235377192848)).strip()
                    if u'box_published':
                        __append(translate(u'box_published', mapping=None, default=__msgid_140235377192848, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n    ')

                    # <Static value=<_ast.Dict object at 0x7f8b17d7a310> name=None at 7f8b17d7a650> -> __attrs_140235377189776
                    __attrs_140235377189776 = _static_140235377189648

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="pat-moment" data-pat-moment="format:relative;">')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235377192784
                    __default_140235377192784 = _DEFAULT_MARKER

                    # <Value u'published' (32:23)> -> __cache_140235377191696
                    __token = 1252
                    try:
                        __zt_tmp = __attrs_140235377189776
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235377191696 = _static_140235435449424('path', u'published', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'published' (32:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17d7a750> -> __condition
                    __expression = __cache_140235377191696

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n      Published\n    ')
                    else:
                        __content = __cache_140235377191696
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235385325968
                    __attrs_140235385325968 = _static_140235489934800

                    # <Value u'modified' (34:31)> -> __condition
                    __token = 1311
                    try:
                        __zt_tmp = __attrs_140235385325968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('path', u'modified', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:
                        __append(u',')
                    __append(u'\n  </span>')
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f8b1853c810> name=None at 7f8b17d7a910> -> __attrs_140235385323856
                __attrs_140235385323856 = _static_140235385325584

                # <Value u'modified' (38:23)> -> __condition
                __token = 1400
                try:
                    __zt_tmp = __attrs_140235385323856
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'modified', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="documentModified">\n    ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235426049104
                    __attrs_140235426049104 = _static_140235489934800

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140235426049360 = []
                    __append_140235426049360 = __stream_140235426049360.append
                    __append_140235426049360(u'\n      last modified\n    ')
                    __msgid_140235426049360 = __re_whitespace(''.join(__stream_140235426049360)).strip()
                    if u'box_last_modified':
                        __append(translate(u'box_last_modified', mapping=None, default=__msgid_140235426049360, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n    ')

                    # <Static value=<_ast.Dict object at 0x7f8b17a34d50> name=None at 7f8b17a34e90> -> __attrs_140235377039760
                    __attrs_140235377039760 = _static_140235373759824

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="pat-moment" data-pat-moment="format:relative;">')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235426046160
                    __default_140235426046160 = _DEFAULT_MARKER

                    # <Value u'modified' (43:23)> -> __cache_140235426048848
                    __token = 1576
                    try:
                        __zt_tmp = __attrs_140235377039760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235426048848 = _static_140235435449424('path', u'modified', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'modified' (43:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1ac126d0> -> __condition
                    __expression = __cache_140235426048848

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n      Modified\n    ')
                    else:
                        __content = __cache_140235426048848
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n  </span>')
                __append(u'\n  ')
                if (__backup_modified_140235438233424 is __marker):
                    del econtext['modified']
                else:
                    econtext['modified'] = __backup_modified_140235438233424
                if (__backup_published_140235374308816 is __marker):
                    del econtext['published']
                else:
                    econtext['published'] = __backup_published_140235374308816
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235426049424
                __attrs_140235426049424 = _static_140235489934800

                # <Value u'view/isExpired' (49:30)> -> __condition
                __token = 1670
                try:
                    __zt_tmp = __attrs_140235426049424
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'view/isExpired', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n    \u2014\n    ')

                    # <Static value=<_ast.Dict object at 0x7f8b17d55750> name=None at 7f8b17d55e90> -> __attrs_140235377039888
                    __attrs_140235377039888 = _static_140235377039184

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="state-expired">')
                    __stream_140235377038096 = []
                    __append_140235377038096 = __stream_140235377038096.append
                    __append_140235377038096(u'expired')
                    __msgid_140235377038096 = __re_whitespace(''.join(__stream_140235377038096)).strip()
                    if u'time_expired':
                        __append(translate(u'time_expired', mapping=None, default=__msgid_140235377038096, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n  ')
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f8b17d55550> name=None at 7f8b17d55c90> -> __attrs_140235426046928
                __attrs_140235426046928 = _static_140235377038672
                __backup_contributors_140235374581648 = get('contributors', __marker)

                # <Value u'context/Contributors' (56:32)> -> __value
                __token = 1866
                try:
                    __zt_tmp = __attrs_140235426046928
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'context/Contributors', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['contributors'] = __value

                # <Value u'contributors' (57:22)> -> __condition
                __token = 1910
                try:
                    __zt_tmp = __attrs_140235426046928
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'contributors', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="documentContributors">')
                    __stream_140235428632768_name = ''
                    __stream_140235377039696 = []
                    __append_140235377039696 = __stream_140235377039696.append
                    __append_140235377039696(u'\n    Contributors:\n    ')
                    __stream_140235428632768_name = []
                    __append_140235428632768_name = __stream_140235428632768_name.append

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235377039120
                    __attrs_140235377039120 = _static_140235489934800

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235377038416
                    __default_140235377038416 = _DEFAULT_MARKER

                    # <Value u"python: ', '.join(contributors)" (62:23)> -> __cache_140235373759568
                    __token = 2061
                    try:
                        __zt_tmp = __attrs_140235377039120
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235373759568 = _static_140235435449424('python', u" ', '.join(contributors)", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u"python: ', '.join(contributors)" (62:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17d55cd0> -> __condition
                    __expression = __cache_140235373759568

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append_140235428632768_name(u'\n      Mary\n    ')
                    else:
                        __content = __cache_140235373759568
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140235428632768_name(__content)
                    __append_140235377039696(u'${name}')
                    __stream_140235428632768_name = ''.join(__stream_140235428632768_name)
                    __append_140235377039696(u'\n  ')
                    __msgid_140235377039696 = __re_whitespace(''.join(__stream_140235377039696)).strip()
                    if u'text_contributors':
                        __append(translate(u'text_contributors', mapping={u'name': __stream_140235428632768_name, }, default=__msgid_140235377039696, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</div>')
                if (__backup_contributors_140235374581648 is __marker):
                    del econtext['contributors']
                else:
                    econtext['contributors'] = __backup_contributors_140235374581648
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235377037648
                __attrs_140235377037648 = _static_140235489934800
                __backup_rights_140235373353040 = get('rights', __marker)

                # <Value u'context/Rights' (67:33)> -> __value
                __token = 2161
                try:
                    __zt_tmp = __attrs_140235377037648
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'context/Rights', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['rights'] = __value

                # <Value u'rights' (68:29)> -> __condition
                __token = 2206
                try:
                    __zt_tmp = __attrs_140235377037648
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'rights', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n    ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235423487184
                    __attrs_140235423487184 = _static_140235489934800

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235423488784
                    __default_140235423488784 = _DEFAULT_MARKER

                    # <Value u'rights' (69:22)> -> __cache_140235423486352
                    __token = 2237
                    try:
                        __zt_tmp = __attrs_140235423487184
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235423486352 = _static_140235435449424('path', u'rights', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'rights' (69:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1a9a1510> -> __condition
                    __expression = __cache_140235423486352

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div>\n      Copyleft NiceCorp Inc.\n    </div>')
                    else:
                        __content = __cache_140235423486352
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n  ')
                if (__backup_rights_140235373353040 is __marker):
                    del econtext['rights']
                else:
                    econtext['rights'] = __backup_rights_140235373353040
                __append(u'\n\n</div>')
                __i18n_domain = __previous_i18n_domain_140235431315152
            __append(u'\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }