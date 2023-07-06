# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/browser/templates/footer.pt'

__tokens = {871: (u'nocall:modules/DateTime.DateTime', 19, 30), 932: (u' python:DateTime(', 20, 27), 974: (u'python:myTime.year()', 21, 22)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235431279632 = {u'class': u'portlet portletClassic', u'id': u'portal-footer-signature', }
_static_140235428378704 = {u'href': u'http://plone.org/foundation', }
_static_140235489934800 = {}
_static_140235435449424 = __compile_zt_expr
_static_140235431287376 = {u'href': u'http://creativecommons.org/licenses/GPL/2.0/', }
_static_140235431251856 = {u'title': u'Copyright', }
_static_140235368752016 = {u'lang': u'en', u'xmlns': u'http://www.w3.org/1999/xhtml', u'xml:lang': u'en', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235374259152 = {u'class': u'portletContent', }
_static_140235431249168 = {u'href': u'http://plone.com', }

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

            # <Static value=<_ast.Dict object at 0x7f8b1b10fc10> name=None at 7f8b1b10fd10> -> __attrs_140235374259536
            __attrs_140235374259536 = _static_140235431279632

            # <aside ... (0:0)
            # --------------------------------------------------------
            __append(u'<aside class="portlet portletClassic" id="portal-footer-signature">\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b17aaebd0> name=None at 7f8b17aaed90> -> __attrs_140235374257616
            __attrs_140235374257616 = _static_140235374259152

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="portletContent">\n      ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374259408
            __attrs_140235374259408 = _static_140235489934800
            __stream_140235322660576_plonecms = ''
            __stream_140235322660576_copyright = ''
            __stream_140235322660576_current_year = ''
            __stream_140235322660576_plonefoundation = ''
            __stream_140235374258960 = []
            __append_140235374258960 = __stream_140235374258960.append
            __append_140235374258960(u'\n      The\n      ')
            __stream_140235322660576_plonecms = []
            __append_140235322660576_plonecms = __stream_140235322660576_plonecms.append

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235431251792
            __attrs_140235431251792 = _static_140235489934800
            __append_140235322660576_plonecms(u'\n           ')

            # <Static value=<_ast.Dict object at 0x7f8b1b108510> name=None at 7f8b1b108f10> -> __attrs_140235431250960
            __attrs_140235431250960 = _static_140235431249168

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140235322660576_plonecms(u'<a href="http://plone.com">')
            __stream_140235431248528 = []
            __append_140235431248528 = __stream_140235431248528.append
            __append_140235431248528(u'Plone')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374094672
            __attrs_140235374094672 = _static_140235489934800

            # <sup ... (0:0)
            # --------------------------------------------------------
            __append_140235431248528(u'<sup>&reg;</sup> Open Source CMS/WCM')
            __msgid_140235431248528 = __re_whitespace(''.join(__stream_140235431248528)).strip()
            if u'label_plone_cms':
                __append_140235322660576_plonecms(translate(u'label_plone_cms', mapping=None, default=__msgid_140235431248528, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append_140235322660576_plonecms(u'</a>\n      ')
            __append_140235374258960(u'${plonecms}')
            __stream_140235322660576_plonecms = ''.join(__stream_140235322660576_plonecms)
            __append_140235374258960(u'\n      is\n      ')
            __stream_140235322660576_copyright = []
            __append_140235322660576_copyright = __stream_140235322660576_copyright.append

            # <Static value=<_ast.Dict object at 0x7f8b1b108f90> name=None at 7f8b1b108190> -> __attrs_140235374095184
            __attrs_140235374095184 = _static_140235431251856

            # <abbr ... (0:0)
            # --------------------------------------------------------
            __append_140235322660576_copyright(u'<abbr')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235374095120
            __default_140235374095120 = _DEFAULT_MARKER

            # <Translate msgid=u'title_copyright' node=<_ast.Str object at 0x7f8b17a86d10> at 7f8b17a867d0> -> __attr_title
            __attr_title = u'Copyright'
            __attr_title = translate(u'title_copyright', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_title is not None):
                __append_140235322660576_copyright((u' title="%s"' % __attr_title))
            __append_140235322660576_copyright(u'>&copy;</abbr>')
            __append_140235374258960(u'${copyright}')
            __stream_140235322660576_copyright = ''.join(__stream_140235322660576_copyright)
            __append_140235374258960(u'\n      2000-')
            __stream_140235322660576_current_year = []
            __append_140235322660576_current_year = __stream_140235322660576_current_year.append

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374095696
            __attrs_140235374095696 = _static_140235489934800
            __backup_DateTime_140235377130448 = get('DateTime', __marker)

            # <Value u'nocall:modules/DateTime.DateTime' (19:30)> -> __value
            __token = 871
            try:
                __zt_tmp = __attrs_140235374095696
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('nocall', u'modules/DateTime.DateTime', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['DateTime'] = __value
            __backup_myTime_140235385297488 = get('myTime', __marker)

            # <Value u'python:DateTime()' (20:27)> -> __value
            __token = 932
            try:
                __zt_tmp = __attrs_140235374095696
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u'DateTime()', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['myTime'] = __value

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235374095504
            __default_140235374095504 = _DEFAULT_MARKER

            # <Value u'python:myTime.year()' (21:22)> -> __cache_140235374094736
            __token = 974
            try:
                __zt_tmp = __attrs_140235374095696
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235374094736 = _static_140235435449424('python', u'myTime.year()', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:myTime.year()' (21:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17a86ad0> -> __condition
            __expression = __cache_140235374094736

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140235374094736
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append_140235322660576_current_year(__content)
            if (__backup_myTime_140235385297488 is __marker):
                del econtext['myTime']
            else:
                econtext['myTime'] = __backup_myTime_140235385297488
            if (__backup_DateTime_140235377130448 is __marker):
                del econtext['DateTime']
            else:
                econtext['DateTime'] = __backup_DateTime_140235377130448
            __append_140235374258960(u'${current_year}')
            __stream_140235322660576_current_year = ''.join(__stream_140235322660576_current_year)
            __append_140235374258960(u'\n      by the\n      ')
            __stream_140235322660576_plonefoundation = []
            __append_140235322660576_plonefoundation = __stream_140235322660576_plonefoundation.append

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374096336
            __attrs_140235374096336 = _static_140235489934800
            __append_140235322660576_plonefoundation(u'\n           ')

            # <Static value=<_ast.Dict object at 0x7f8b1ae4b850> name=None at 7f8b1ae4bd50> -> __attrs_140235428379536
            __attrs_140235428379536 = _static_140235428378704

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140235322660576_plonefoundation(u'<a href="http://plone.org/foundation">')
            __stream_140235428379600 = []
            __append_140235428379600 = __stream_140235428379600.append
            __append_140235428379600(u'Plone Foundation')
            __msgid_140235428379600 = __re_whitespace(''.join(__stream_140235428379600)).strip()
            if u'label_plone_foundation':
                __append_140235322660576_plonefoundation(translate(u'label_plone_foundation', mapping=None, default=__msgid_140235428379600, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append_140235322660576_plonefoundation(u'</a>')
            __append_140235374258960(u'${plonefoundation}')
            __stream_140235322660576_plonefoundation = ''.join(__stream_140235322660576_plonefoundation)
            __append_140235374258960(u'\n      and friends.\n      ')
            __msgid_140235374258960 = __re_whitespace(''.join(__stream_140235374258960)).strip()
            if u'description_copyright':
                __append(translate(u'description_copyright', mapping={u'plonefoundation': __stream_140235322660576_plonefoundation, u'current_year': __stream_140235322660576_current_year, u'copyright': __stream_140235322660576_copyright, u'plonecms': __stream_140235322660576_plonecms, }, default=__msgid_140235374258960, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'\n\n      ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374095824
            __attrs_140235374095824 = _static_140235489934800
            __stream_140235322660576_license = ''
            __stream_140235374258576 = []
            __append_140235374258576 = __stream_140235374258576.append
            __append_140235374258576(u'\n      Distributed under the\n           ')
            __stream_140235322660576_license = []
            __append_140235322660576_license = __stream_140235322660576_license.append

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235431285648
            __attrs_140235431285648 = _static_140235489934800
            __append_140235322660576_license(u'\n                ')

            # <Static value=<_ast.Dict object at 0x7f8b1b111a50> name=None at 7f8b1b111f90> -> __attrs_140235431286352
            __attrs_140235431286352 = _static_140235431287376

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140235322660576_license(u'<a href="http://creativecommons.org/licenses/GPL/2.0/">')
            __stream_140235431284880 = []
            __append_140235431284880 = __stream_140235431284880.append
            __append_140235431284880(u'GNU GPL license')
            __msgid_140235431284880 = __re_whitespace(''.join(__stream_140235431284880)).strip()
            if u'label_gnu_gpl_licence':
                __append_140235322660576_license(translate(u'label_gnu_gpl_licence', mapping=None, default=__msgid_140235431284880, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append_140235322660576_license(u'</a>')
            __append_140235374258576(u'${license}')
            __stream_140235322660576_license = ''.join(__stream_140235322660576_license)
            __append_140235374258576(u'.\n      ')
            __msgid_140235374258576 = __re_whitespace(''.join(__stream_140235374258576)).strip()
            if u'description_license':
                __append(translate(u'description_license', mapping={u'license': __stream_140235322660576_license, }, default=__msgid_140235374258576, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
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

            # <Static value=<_ast.Dict object at 0x7f8b1756e390> name=None at 7f8b1756ef50> -> __attrs_140235368753808
            __attrs_140235368753808 = _static_140235368752016
            __previous_i18n_domain_140235368751568 = __i18n_domain
            __i18n_domain = u'plone'
            __append(u'\n\n  ')
            __token = None
            render_portlet(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n')
            __i18n_domain = __previous_i18n_domain_140235368751568
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_portlet': render_portlet, 'render': render, }