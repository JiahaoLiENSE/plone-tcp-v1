# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/browser/templates/footer.pt'

__tokens = {871: (u'nocall:modules/DateTime.DateTime', 19, 30), 932: (u' python:DateTime(', 20, 27), 974: (u'python:myTime.year()', 21, 22)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386070705680 = {u'href': u'http://creativecommons.org/licenses/GPL/2.0/', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386069972496 = {u'class': u'portlet portletClassic', u'id': u'portal-footer-signature', }
_static_140386069198288 = {u'href': u'http://plone.org/foundation', }
_static_140386070426832 = {u'href': u'http://plone.com', }
_static_140386186296528 = __compile_zt_expr
_static_140386070427536 = {u'title': u'Copyright', }
_static_140386070113104 = {u'lang': u'en', u'xmlns': u'http://www.w3.org/1999/xhtml', u'xml:lang': u'en', }
_static_140386069974096 = {u'class': u'portletContent', }
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

    def render_portlet(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7fae2dd50610> name=None at 7fae2dd50b90> -> __attrs_140386069971856
            __attrs_140386069971856 = _static_140386069972496

            # <aside ... (0:0)
            # --------------------------------------------------------
            __append(u'<aside class="portlet portletClassic" id="portal-footer-signature">\n    ')

            # <Static value=<_ast.Dict object at 0x7fae2dd50c50> name=None at 7fae2dd50650> -> __attrs_140386069973520
            __attrs_140386069973520 = _static_140386069974096

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="portletContent">\n      ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070427920
            __attrs_140386070427920 = _static_140386247937936
            __stream_140386072398016_plonecms = ''
            __stream_140386072398016_copyright = ''
            __stream_140386072398016_current_year = ''
            __stream_140386072398016_plonefoundation = ''
            __stream_140386069971600 = []
            __append_140386069971600 = __stream_140386069971600.append
            __append_140386069971600(u'\n      The\n      ')
            __stream_140386072398016_plonecms = []
            __append_140386072398016_plonecms = __stream_140386072398016_plonecms.append

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070425872
            __attrs_140386070425872 = _static_140386247937936
            __append_140386072398016_plonecms(u'\n           ')

            # <Static value=<_ast.Dict object at 0x7fae2ddbf4d0> name=None at 7fae2ddbf890> -> __attrs_140386070429648
            __attrs_140386070429648 = _static_140386070426832

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072398016_plonecms(u'<a href="http://plone.com">')
            __stream_140386070427728 = []
            __append_140386070427728 = __stream_140386070427728.append
            __append_140386070427728(u'Plone')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078150480
            __attrs_140386078150480 = _static_140386247937936

            # <sup ... (0:0)
            # --------------------------------------------------------
            __append_140386070427728(u'<sup>&reg;</sup> Open Source CMS/WCM')
            __msgid_140386070427728 = __re_whitespace(''.join(__stream_140386070427728)).strip()
            if u'label_plone_cms':
                __append_140386072398016_plonecms(translate(u'label_plone_cms', mapping=None, default=__msgid_140386070427728, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append_140386072398016_plonecms(u'</a>\n      ')
            __append_140386069971600(u'${plonecms}')
            __stream_140386072398016_plonecms = ''.join(__stream_140386072398016_plonecms)
            __append_140386069971600(u'\n      is\n      ')
            __stream_140386072398016_copyright = []
            __append_140386072398016_copyright = __stream_140386072398016_copyright.append

            # <Static value=<_ast.Dict object at 0x7fae2ddbf790> name=None at 7fae2ddbf750> -> __attrs_140386078150288
            __attrs_140386078150288 = _static_140386070427536

            # <abbr ... (0:0)
            # --------------------------------------------------------
            __append_140386072398016_copyright(u'<abbr')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078146960
            __default_140386078146960 = _DEFAULT_MARKER

            # <Translate msgid=u'title_copyright' node=<_ast.Str object at 0x7fae2e51cf10> at 7fae2e51c0d0> -> __attr_title
            __attr_title = u'Copyright'
            __attr_title = translate(u'title_copyright', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_title is not None):
                __append_140386072398016_copyright((u' title="%s"' % __attr_title))
            __append_140386072398016_copyright(u'>&copy;</abbr>')
            __append_140386069971600(u'${copyright}')
            __stream_140386072398016_copyright = ''.join(__stream_140386072398016_copyright)
            __append_140386069971600(u'\n      2000-')
            __stream_140386072398016_current_year = []
            __append_140386072398016_current_year = __stream_140386072398016_current_year.append

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078077392
            __attrs_140386078077392 = _static_140386247937936
            __backup_DateTime_140386069148496 = get('DateTime', __marker)

            # <Value u'nocall:modules/DateTime.DateTime' (19:30)> -> __value
            __token = 871
            try:
                __zt_tmp = __attrs_140386078077392
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('nocall', u'modules/DateTime.DateTime', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['DateTime'] = __value
            __backup_myTime_140386069150672 = get('myTime', __marker)

            # <Value u'python:DateTime()' (20:27)> -> __value
            __token = 932
            try:
                __zt_tmp = __attrs_140386078077392
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u'DateTime()', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['myTime'] = __value

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078080592
            __default_140386078080592 = _DEFAULT_MARKER

            # <Value u'python:myTime.year()' (21:22)> -> __cache_140386078079312
            __token = 974
            try:
                __zt_tmp = __attrs_140386078077392
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386078079312 = _static_140386186296528('python', u'myTime.year()', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:myTime.year()' (21:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e50bf90> -> __condition
            __expression = __cache_140386078079312

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140386078079312
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append_140386072398016_current_year(__content)
            if (__backup_myTime_140386069150672 is __marker):
                del econtext['myTime']
            else:
                econtext['myTime'] = __backup_myTime_140386069150672
            if (__backup_DateTime_140386069148496 is __marker):
                del econtext['DateTime']
            else:
                econtext['DateTime'] = __backup_DateTime_140386069148496
            __append_140386069971600(u'${current_year}')
            __stream_140386072398016_current_year = ''.join(__stream_140386072398016_current_year)
            __append_140386069971600(u'\n      by the\n      ')
            __stream_140386072398016_plonefoundation = []
            __append_140386072398016_plonefoundation = __stream_140386072398016_plonefoundation.append

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069197200
            __attrs_140386069197200 = _static_140386247937936
            __append_140386072398016_plonefoundation(u'\n           ')

            # <Static value=<_ast.Dict object at 0x7fae2dc935d0> name=None at 7fae2dc93650> -> __attrs_140386071777680
            __attrs_140386071777680 = _static_140386069198288

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072398016_plonefoundation(u'<a href="http://plone.org/foundation">')
            __stream_140386069199440 = []
            __append_140386069199440 = __stream_140386069199440.append
            __append_140386069199440(u'Plone Foundation')
            __msgid_140386069199440 = __re_whitespace(''.join(__stream_140386069199440)).strip()
            if u'label_plone_foundation':
                __append_140386072398016_plonefoundation(translate(u'label_plone_foundation', mapping=None, default=__msgid_140386069199440, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append_140386072398016_plonefoundation(u'</a>')
            __append_140386069971600(u'${plonefoundation}')
            __stream_140386072398016_plonefoundation = ''.join(__stream_140386072398016_plonefoundation)
            __append_140386069971600(u'\n      and friends.\n      ')
            __msgid_140386069971600 = __re_whitespace(''.join(__stream_140386069971600)).strip()
            if u'description_copyright':
                __append(translate(u'description_copyright', mapping={u'plonefoundation': __stream_140386072398016_plonefoundation, u'current_year': __stream_140386072398016_current_year, u'copyright': __stream_140386072398016_copyright, u'plonecms': __stream_140386072398016_plonecms, }, default=__msgid_140386069971600, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'\n\n      ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078078800
            __attrs_140386078078800 = _static_140386247937936
            __stream_140386072398016_license = ''
            __stream_140386070428880 = []
            __append_140386070428880 = __stream_140386070428880.append
            __append_140386070428880(u'\n      Distributed under the\n           ')
            __stream_140386072398016_license = []
            __append_140386072398016_license = __stream_140386072398016_license.append

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070706064
            __attrs_140386070706064 = _static_140386247937936
            __append_140386072398016_license(u'\n                ')

            # <Static value=<_ast.Dict object at 0x7fae2de03610> name=None at 7fae2de03950> -> __attrs_140386070706192
            __attrs_140386070706192 = _static_140386070705680

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072398016_license(u'<a href="http://creativecommons.org/licenses/GPL/2.0/">')
            __stream_140386070707344 = []
            __append_140386070707344 = __stream_140386070707344.append
            __append_140386070707344(u'GNU GPL license')
            __msgid_140386070707344 = __re_whitespace(''.join(__stream_140386070707344)).strip()
            if u'label_gnu_gpl_licence':
                __append_140386072398016_license(translate(u'label_gnu_gpl_licence', mapping=None, default=__msgid_140386070707344, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append_140386072398016_license(u'</a>')
            __append_140386070428880(u'${license}')
            __stream_140386072398016_license = ''.join(__stream_140386072398016_license)
            __append_140386070428880(u'.\n      ')
            __msgid_140386070428880 = __re_whitespace(''.join(__stream_140386070428880)).strip()
            if u'description_license':
                __append(translate(u'description_license', mapping={u'license': __stream_140386072398016_license, }, default=__msgid_140386070428880, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'\n    </div>\n  </aside>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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

            # <Static value=<_ast.Dict object at 0x7fae2dd72b50> name=None at 7fae2dd72c90> -> __attrs_140386070110928
            __attrs_140386070110928 = _static_140386070113104
            __previous_i18n_domain_140386070113360 = __i18n_domain
            __i18n_domain = u'plone'
            __append(u'\n\n  ')
            __token = None
            render_portlet(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n')
            __i18n_domain = __previous_i18n_domain_140386070113360
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_portlet': render_portlet, 'render': render, }