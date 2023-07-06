# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/document_byline.pt'

__tokens = {105: (u'view/show', 4, 20), 163: (u'view/creator', 5, 46), 208: (u'creator_short_form', 6, 30), 271: (u'string:?author=${creator_short_form}', 7, 42), 350: (u" python:'/' in creator_short_for", 8, 41), 418: (u'd python:(creator_short_form, creator_long_form)[creator_is_openi', 9, 33), 773: (u'python:view.author() is None', 16, 23), 630: (u'string:${context/@@plone_portal_state/navigation_root_url}/author/${creator_id}', 14, 30), 733: (u'view/authorname', 15, 22), 954: (u'view/pub_date', 24, 31), 998: (u' context/ModificationDat', 25, 29), 1083: (u'published', 27, 23), 1252: (u'published', 32, 23), 1311: (u'modified', 34, 31), 1400: (u'modified', 38, 23), 1576: (u'modified', 43, 23), 1670: (u'view/isExpired', 49, 30), 1866: (u'context/Contributors', 56, 32), 1910: (u'contributors', 57, 22), 2061: (u"python: ', '.join(contributors)", 62, 23), 2161: (u'context/Rights', 67, 33), 2206: (u'rights', 68, 29), 2237: (u'rights', 69, 22)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386071753488 = {u'class': u'documentContributors', }
_static_140386069148944 = {u'data-pat-moment': u'format:relative;', u'class': u'pat-moment', }
_static_140386071742864 = {u'class': u'documentAuthor', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386070841296 = {u'href': u'#', }
_static_140386070839632 = {u'class': u'documentPublished', }
_static_140386186296528 = __compile_zt_expr
_static_140386069452752 = {u'class': u'documentModified', }
_static_140386069974032 = {u'class': u'state-expired', }
_static_140386078184464 = {u'class': u'documentByLine', u'id': u'plone-document-byline', }
_static_140386069974416 = {u'data-pat-moment': u'format:relative;', u'class': u'pat-moment', }
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

            # <Static value=<_ast.Dict object at 0x7fae2e525410> name=None at 7fae2e525b90> -> __attrs_140386071753424
            __attrs_140386071753424 = _static_140386078184464

            # <Value u'view/show' (4:20)> -> __condition
            __token = 105
            try:
                __zt_tmp = __attrs_140386071753424
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('path', u'view/show', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140386071753872 = __i18n_domain
                __i18n_domain = u'plone'

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="documentByLine" id="plone-document-byline">\n  ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071756304
                __attrs_140386071756304 = _static_140386247937936
                __backup_creator_short_form_140386070483664 = get('creator_short_form', __marker)

                # <Value u'view/creator' (5:46)> -> __value
                __token = 163
                try:
                    __zt_tmp = __attrs_140386071756304
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'view/creator', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['creator_short_form'] = __value

                # <Value u'creator_short_form' (6:30)> -> __condition
                __token = 208
                try:
                    __zt_tmp = __attrs_140386071756304
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'creator_short_form', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n  ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071743248
                    __attrs_140386071743248 = _static_140386247937936
                    __backup_creator_long_form_140386070486928 = get('creator_long_form', __marker)

                    # <Value u'string:?author=${creator_short_form}' (7:42)> -> __value
                    __token = 271
                    try:
                        __zt_tmp = __attrs_140386071743248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('string', u'?author=${creator_short_form}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['creator_long_form'] = __value
                    __backup_creator_is_openid_140386071743312 = get('creator_is_openid', __marker)

                    # <Value u"python:'/' in creator_short_form" (8:41)> -> __value
                    __token = 350
                    try:
                        __zt_tmp = __attrs_140386071743248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('python', u"'/' in creator_short_form", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['creator_is_openid'] = __value
                    __backup_creator_id_140386071170256 = get('creator_id', __marker)

                    # <Value u'python:(creator_short_form, creator_long_form)[creator_is_openid]' (9:33)> -> __value
                    __token = 418
                    try:
                        __zt_tmp = __attrs_140386071743248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('python', u'(creator_short_form, creator_long_form)[creator_is_openid]', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['creator_id'] = __value
                    __append(u'\n    ')

                    # <Static value=<_ast.Dict object at 0x7fae2df00990> name=None at 7fae2df00050> -> __attrs_140386078167248
                    __attrs_140386078167248 = _static_140386071742864

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="documentAuthor">\n      ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070841104
                    __attrs_140386070841104 = _static_140386247937936
                    __stream_140386072229600_author = ''
                    __stream_140386070840016 = []
                    __append_140386070840016 = __stream_140386070840016.append
                    __append_140386070840016(u'\n      by\n      ')
                    __stream_140386072229600_author = []
                    __append_140386072229600_author = __stream_140386072229600_author.append

                    # <Static value=<_ast.Dict object at 0x7fae2de247d0> name=None at 7fae2de24d90> -> __attrs_140386070840528
                    __attrs_140386070840528 = _static_140386070841296

                    # <Negate value=<Value u'python:view.author() is None' (16:23)> at 7fae2de24bd0> -> __cache_140386070842320

                    # <Value u'python:view.author() is None' (16:23)> -> __cache_140386070842320
                    __token = 773
                    try:
                        __zt_tmp = __attrs_140386070840528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386070842320 = _static_140386186296528('python', u'view.author() is None', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __cache_140386070842320 = not __cache_140386070842320
                    __condition = __cache_140386070842320
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append_140386072229600_author(u'<a')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070840848
                        __default_140386070840848 = _DEFAULT_MARKER

                        # <Substitution u'string:${context/@@plone_portal_state/navigation_root_url}/author/${creator_id}' (14:30)> -> __attr_href
                        __token = 630
                        try:
                            __zt_tmp = __attrs_140386070840528
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140386186296528('string', u'${context/@@plone_portal_state/navigation_root_url}/author/${creator_id}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append_140386072229600_author((u' href="%s"' % __attr_href))
                        __append_140386072229600_author(u'>')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070841232
                    __default_140386070841232 = _DEFAULT_MARKER

                    # <Value u'view/authorname' (15:22)> -> __cache_140386070842128
                    __token = 733
                    try:
                        __zt_tmp = __attrs_140386070840528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386070842128 = _static_140386186296528('path', u'view/authorname', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'view/authorname' (15:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2de24c90> -> __condition
                    __expression = __cache_140386070842128

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append_140386072229600_author(u'Roland Barthes')
                    else:
                        __content = __cache_140386070842128
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140386072229600_author(__content)
                    __condition = __cache_140386070842320
                    if __condition:
                        __append_140386072229600_author(u'</a>')
                    __append_140386070840016(u'${author}')
                    __stream_140386072229600_author = ''.join(__stream_140386072229600_author)
                    __append_140386070840016(u'\n      ')
                    __msgid_140386070840016 = __re_whitespace(''.join(__stream_140386070840016)).strip()
                    if u'label_by_author':
                        __append(translate(u'label_by_author', mapping={u'author': __stream_140386072229600_author, }, default=__msgid_140386070840016, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n         \u2014\n    </span>\n  ')
                    if (__backup_creator_id_140386071170256 is __marker):
                        del econtext['creator_id']
                    else:
                        econtext['creator_id'] = __backup_creator_id_140386071170256
                    if (__backup_creator_is_openid_140386071743312 is __marker):
                        del econtext['creator_is_openid']
                    else:
                        econtext['creator_is_openid'] = __backup_creator_is_openid_140386071743312
                    if (__backup_creator_long_form_140386070486928 is __marker):
                        del econtext['creator_long_form']
                    else:
                        econtext['creator_long_form'] = __backup_creator_long_form_140386070486928
                    __append(u'\n  ')
                if (__backup_creator_short_form_140386070483664 is __marker):
                    del econtext['creator_short_form']
                else:
                    econtext['creator_short_form'] = __backup_creator_short_form_140386070483664
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078169360
                __attrs_140386078169360 = _static_140386247937936
                __backup_published_140386070486992 = get('published', __marker)

                # <Value u'view/pub_date' (24:31)> -> __value
                __token = 954
                try:
                    __zt_tmp = __attrs_140386078169360
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'view/pub_date', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['published'] = __value
                __backup_modified_140386070735312 = get('modified', __marker)

                # <Value u'context/ModificationDate' (25:29)> -> __value
                __token = 998
                try:
                    __zt_tmp = __attrs_140386078169360
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'context/ModificationDate', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['modified'] = __value
                __append(u'\n  ')

                # <Static value=<_ast.Dict object at 0x7fae2de24150> name=None at 7fae2de24990> -> __attrs_140386069149136
                __attrs_140386069149136 = _static_140386070839632

                # <Value u'published' (27:23)> -> __condition
                __token = 1083
                try:
                    __zt_tmp = __attrs_140386069149136
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'published', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="documentPublished">\n    ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069148752
                    __attrs_140386069148752 = _static_140386247937936

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140386069149072 = []
                    __append_140386069149072 = __stream_140386069149072.append
                    __append_140386069149072(u'\n      published\n    ')
                    __msgid_140386069149072 = __re_whitespace(''.join(__stream_140386069149072)).strip()
                    if u'box_published':
                        __append(translate(u'box_published', mapping=None, default=__msgid_140386069149072, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n    ')

                    # <Static value=<_ast.Dict object at 0x7fae2dc87510> name=None at 7fae2dc87910> -> __attrs_140386069149840
                    __attrs_140386069149840 = _static_140386069148944

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="pat-moment" data-pat-moment="format:relative;">')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069151120
                    __default_140386069151120 = _DEFAULT_MARKER

                    # <Value u'published' (32:23)> -> __cache_140386069149328
                    __token = 1252
                    try:
                        __zt_tmp = __attrs_140386069149840
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386069149328 = _static_140386186296528('path', u'published', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'published' (32:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dc87110> -> __condition
                    __expression = __cache_140386069149328

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n      Published\n    ')
                    else:
                        __content = __cache_140386069149328
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069454672
                    __attrs_140386069454672 = _static_140386247937936

                    # <Value u'modified' (34:31)> -> __condition
                    __token = 1311
                    try:
                        __zt_tmp = __attrs_140386069454672
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('path', u'modified', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:
                        __append(u',')
                    __append(u'\n  </span>')
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fae2dcd17d0> name=None at 7fae2dc87e10> -> __attrs_140386069450960
                __attrs_140386069450960 = _static_140386069452752

                # <Value u'modified' (38:23)> -> __condition
                __token = 1400
                try:
                    __zt_tmp = __attrs_140386069450960
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'modified', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="documentModified">\n    ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069452432
                    __attrs_140386069452432 = _static_140386247937936

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140386069451344 = []
                    __append_140386069451344 = __stream_140386069451344.append
                    __append_140386069451344(u'\n      last modified\n    ')
                    __msgid_140386069451344 = __re_whitespace(''.join(__stream_140386069451344)).strip()
                    if u'box_last_modified':
                        __append(translate(u'box_last_modified', mapping=None, default=__msgid_140386069451344, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n    ')

                    # <Static value=<_ast.Dict object at 0x7fae2dd50d90> name=None at 7fae2dd50f90> -> __attrs_140386069974672
                    __attrs_140386069974672 = _static_140386069974416

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="pat-moment" data-pat-moment="format:relative;">')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069974736
                    __default_140386069974736 = _DEFAULT_MARKER

                    # <Value u'modified' (43:23)> -> __cache_140386069973008
                    __token = 1576
                    try:
                        __zt_tmp = __attrs_140386069974672
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386069973008 = _static_140386186296528('path', u'modified', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'modified' (43:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dd50410> -> __condition
                    __expression = __cache_140386069973008

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n      Modified\n    ')
                    else:
                        __content = __cache_140386069973008
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n  </span>')
                __append(u'\n  ')
                if (__backup_modified_140386070735312 is __marker):
                    del econtext['modified']
                else:
                    econtext['modified'] = __backup_modified_140386070735312
                if (__backup_published_140386070486992 is __marker):
                    del econtext['published']
                else:
                    econtext['published'] = __backup_published_140386070486992
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069453264
                __attrs_140386069453264 = _static_140386247937936

                # <Value u'view/isExpired' (49:30)> -> __condition
                __token = 1670
                try:
                    __zt_tmp = __attrs_140386069453264
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'view/isExpired', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n    \u2014\n    ')

                    # <Static value=<_ast.Dict object at 0x7fae2dd50c10> name=None at 7fae2dd50890> -> __attrs_140386069974096
                    __attrs_140386069974096 = _static_140386069974032

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="state-expired">')
                    __stream_140386069972240 = []
                    __append_140386069972240 = __stream_140386069972240.append
                    __append_140386069972240(u'expired')
                    __msgid_140386069972240 = __re_whitespace(''.join(__stream_140386069972240)).strip()
                    if u'time_expired':
                        __append(translate(u'time_expired', mapping=None, default=__msgid_140386069972240, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n  ')
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fae2df03310> name=None at 7fae2df03b50> -> __attrs_140386078119696
                __attrs_140386078119696 = _static_140386071753488
                __backup_contributors_140386070158160 = get('contributors', __marker)

                # <Value u'context/Contributors' (56:32)> -> __value
                __token = 1866
                try:
                    __zt_tmp = __attrs_140386078119696
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'context/Contributors', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['contributors'] = __value

                # <Value u'contributors' (57:22)> -> __condition
                __token = 1910
                try:
                    __zt_tmp = __attrs_140386078119696
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'contributors', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="documentContributors">')
                    __stream_140386072229120_name = ''
                    __stream_140386071754512 = []
                    __append_140386071754512 = __stream_140386071754512.append
                    __append_140386071754512(u'\n    Contributors:\n    ')
                    __stream_140386072229120_name = []
                    __append_140386072229120_name = __stream_140386072229120_name.append

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071777680
                    __attrs_140386071777680 = _static_140386247937936

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071777360
                    __default_140386071777360 = _DEFAULT_MARKER

                    # <Value u"python: ', '.join(contributors)" (62:23)> -> __cache_140386071777552
                    __token = 2061
                    try:
                        __zt_tmp = __attrs_140386071777680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386071777552 = _static_140386186296528('python', u" ', '.join(contributors)", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u"python: ', '.join(contributors)" (62:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2df09b10> -> __condition
                    __expression = __cache_140386071777552

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append_140386072229120_name(u'\n      Mary\n    ')
                    else:
                        __content = __cache_140386071777552
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140386072229120_name(__content)
                    __append_140386071754512(u'${name}')
                    __stream_140386072229120_name = ''.join(__stream_140386072229120_name)
                    __append_140386071754512(u'\n  ')
                    __msgid_140386071754512 = __re_whitespace(''.join(__stream_140386071754512)).strip()
                    if u'text_contributors':
                        __append(translate(u'text_contributors', mapping={u'name': __stream_140386072229120_name, }, default=__msgid_140386071754512, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</div>')
                if (__backup_contributors_140386070158160 is __marker):
                    del econtext['contributors']
                else:
                    econtext['contributors'] = __backup_contributors_140386070158160
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071779472
                __attrs_140386071779472 = _static_140386247937936
                __backup_rights_140386071167888 = get('rights', __marker)

                # <Value u'context/Rights' (67:33)> -> __value
                __token = 2161
                try:
                    __zt_tmp = __attrs_140386071779472
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'context/Rights', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['rights'] = __value

                # <Value u'rights' (68:29)> -> __condition
                __token = 2206
                try:
                    __zt_tmp = __attrs_140386071779472
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'rights', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n    ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070519952
                    __attrs_140386070519952 = _static_140386247937936

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078077712
                    __default_140386078077712 = _DEFAULT_MARKER

                    # <Value u'rights' (69:22)> -> __cache_140386078080016
                    __token = 2237
                    try:
                        __zt_tmp = __attrs_140386070519952
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386078080016 = _static_140386186296528('path', u'rights', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'rights' (69:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e50b750> -> __condition
                    __expression = __cache_140386078080016

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div>\n      Copyleft NiceCorp Inc.\n    </div>')
                    else:
                        __content = __cache_140386078080016
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n  ')
                if (__backup_rights_140386071167888 is __marker):
                    del econtext['rights']
                else:
                    econtext['rights'] = __backup_rights_140386071167888
                __append(u'\n\n</div>')
                __i18n_domain = __previous_i18n_domain_140386071753872
            __append(u'\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }