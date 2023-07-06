# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/browser/templates/plone-overview.pt'

__tokens = {743: (u'string:${context/absolute_url}/++resource++plone-admin-ui.css', 17, 29), 843: (u'view/sites', 21, 24), 979: (u'string:${context/absolute_url}/++resource++plone-logo.png', 24, 29), 6927: (u'sites', 36, 38), 6975: (u'python:len(sites) == 1', 37, 40), 7042: (u'sites', 38, 42), 7369: (u'site/absolute_url', 43, 52), 7706: (u'python:view.outdated(site)', 49, 44), 8120: (u'python:view.upgrade_url(site)', 56, 57), 8202: (u'not:view/can_manage', 57, 50), 8346: (u'python:view.upgrade_url(site, can_manage=True)', 59, 57), 8816: (u'python:len(sites) &gt', 68, 41), 9026: (u'sites', 71, 45), 9188: (u'site/absolute_url', 75, 56), 9263: (u' site/Titl', 76, 56), 9325: (u'site/Title', 77, 48), 9528: (u'string:\u2013 ${site/getId}', 81, 51), 9611: (u'string:${site/absolute_url}/logoIcon.png', 82, 57), 9856: (u'python:view.outdated(site)', 86, 48), 10343: (u'python:view.upgrade_url(site)', 94, 62), 10430: (u'not:view/can_manage', 95, 55), 10584: (u'python:view.upgrade_url(site, can_manage=True)', 97, 62), 11166: (u'not:sites', 110, 55), 11317: (u'sites', 113, 55), 11557: (u"python: '' if not sites else len(sites) + 1", 119, 46), 11647: (u'string:${context/absolute_url}/@@plone-addsite', 120, 45), 11759: (u'Plone${site_number}', 121, 63), 11766: (u'site_number', 121, 70), 12063: (u'string:${context/absolute_url}/@@plone-addsite?site_id=Plone${site_number}&amp;advanc', 127, 44), 12338: (u'string:${context/absolute_url}/manage_main', 138, 29)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386175272272 = {u'href': u'#', u'title': u'site/Title', }
_static_140386200452304 = {u'charset': u'utf-8', }
_static_140386177529680 = {u'action': u'', u'style': u'display: inline;', u'method': u'get', }
_static_140386126985552 = {u'href': u'#', u'title': u'Go to the ZMI', }
_static_140386113769360 = {u'src': u'data:image/png;base64,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', u'alt': u'', }
_static_140386200377104 = {u'id': u'text', }
_static_140386200371600 = {u'type': u'submit', u'value': u'Create a new Plone site', }
_static_140386201097616 = {u'type': u'submit', u'class': u'plone-btn-secondary', u'value': u'Upgrade&hellip;', }
_static_140386175262800 = {u'class': u'prominent', }
_static_140386177527952 = {u'width': u'16', u'src': u'string:${site/absolute_url}/logoIcon.png', u'height': u'16', }
_static_140386204130256 = {u'content': u'width=device-width, initial-scale=1', u'name': u'viewport', }
_static_140386177519184 = {u'class': u'sites', }
_static_140386247937936 = {}
_static_140386201099408 = {u'id': u'multiple-sites', }
_static_140386200378128 = {u'src': u'/++resource++plone-logo.png', u'alt': u'Plone', u'height': u'28', u'width': u'108', }
_static_140386200449808 = {u'lang': u'en', u'xmlns': u'http://www.w3.org/1999/xhtml', u'xml:lang': u'en', }
_static_140386177585616 = {u'type': u'submit', u'class': u'plone-btn-secondary', u'value': u'Upgrade&hellip;', }
_static_140386177518864 = {u'class': u'prominent', }
_static_140386177529872 = {u'class': u'upgrade-warning', }
_static_140386126928656 = {u'action': u'#', u'id': u'add-plone-site', u'method': u'get', }
_static_140386126985104 = {u'href': u'string:${context/absolute_url}/@@plone-addsite?site_id=Plone${site_number}&advanced=1', u'class': u'discreet', }
_static_140386175274064 = {u'class': u'discreet', }
_static_140386204131216 = {u'href': u'/++resource++plone-admin-ui.css', u'type': u'text/css', u'rel': u'stylesheet', }
_static_140386113766800 = {u'class': u'circle running', }
_static_140386192640144 = {u'href': u'http://plone.com', u'target': u'_blank', u'title': u'Plone.com', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386175257680 = {u'action': u'', u'style': u'display: inline;', u'method': u'get', }
_static_140386192667856 = {u'href': u'http://plone.org', u'title': u'Plone Community Home', }
_static_140386201099792 = {u'type': u'hidden', u'name': u'came_from', u'value': u'python:view.upgrade_url(site, can_manage=True)', }
_static_140386201105104 = {u'id': u'box', }
_static_140386175264912 = {u'href': u'#', u'class': u'plone-btn', u'title': u'Go to your instance', }
_static_140386177586640 = {u'type': u'hidden', u'name': u'came_from', u'value': u'python:view.upgrade_url(site, can_manage=True)', }
_static_140386200372368 = {u'type': u'hidden', u'name': u'site_id', u'value': u'Plone${site_number}', }
_static_140386186296528 = __compile_zt_expr
_static_140386204130000 = {u'href': u'http://fonts.googleapis.com/css?family=Roboto:400,300,700', u'type': u'text/css', u'rel': u'stylesheet', }
_static_140386175258448 = {u'class': u'upgrade-warning', }

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
            __append(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n')

            # <Static value=<_ast.Dict object at 0x7fae359bf310> name=None at 7fae359bf350> -> __attrs_140386200451344
            __attrs_140386200451344 = _static_140386200449808
            __previous_i18n_domain_140386200451536 = __i18n_domain
            __i18n_domain = u'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386200451280
            __attrs_140386200451280 = _static_140386247937936

            # <head ... (0:0)
            # --------------------------------------------------------
            __append(u'<head>\n  ')

            # <Static value=<_ast.Dict object at 0x7fae359bfcd0> name=None at 7fae359bfe50> -> __attrs_140386122219216
            __attrs_140386122219216 = _static_140386200452304

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append(u'<meta charset="utf-8"/>\n  ')

            # <Static value=<_ast.Dict object at 0x7fae35d41bd0> name=None at 7fae35d41d50> -> __attrs_140386204130960
            __attrs_140386204130960 = _static_140386204130256

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append(u'<meta name="viewport" content="width=device-width, initial-scale=1"/>\n  ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386204128656
            __attrs_140386204128656 = _static_140386247937936

            # <title ... (0:0)
            # --------------------------------------------------------
            __append(u'<title>Plone</title>\n  ')

            # <Static value=<_ast.Dict object at 0x7fae35d41ad0> name=None at 7fae35d41a90> -> __attrs_140386204130704
            __attrs_140386204130704 = _static_140386204130000

            # <link ... (0:0)
            # --------------------------------------------------------
            __append(u"<link href='http://fonts.googleapis.com/css?family=Roboto:400,300,700' rel='stylesheet' type='text/css'/>\n  ")

            # <Static value=<_ast.Dict object at 0x7fae35d41f90> name=None at 7fae35d41fd0> -> __attrs_140386201106704
            __attrs_140386201106704 = _static_140386204131216

            # <link ... (0:0)
            # --------------------------------------------------------
            __append(u'<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386201106064
            __default_140386201106064 = _DEFAULT_MARKER

            # <Substitution u'string:${context/absolute_url}/++resource++plone-admin-ui.css' (17:29)> -> __attr_href
            __token = 743
            try:
                __zt_tmp = __attrs_140386201106704
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140386186296528('string', u'${context/absolute_url}/++resource++plone-admin-ui.css', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'/++resource++plone-admin-ui.css', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u' />\n</head>\n\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386201104848
            __attrs_140386201104848 = _static_140386247937936
            __backup_sites_140386177197328 = get('sites', __marker)

            # <Value u'view/sites' (21:24)> -> __value
            __token = 843
            try:
                __zt_tmp = __attrs_140386201104848
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/sites', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['sites'] = __value

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body>\n')

            # <Static value=<_ast.Dict object at 0x7fae35a5f2d0> name=None at 7fae35a5f050> -> __attrs_140386201107472
            __attrs_140386201107472 = _static_140386201105104

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="box">\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386201106448
            __attrs_140386201106448 = _static_140386247937936

            # <header ... (0:0)
            # --------------------------------------------------------
            __append(u'<header>')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386201105232
            __attrs_140386201105232 = _static_140386247937936

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append(u'<h1>')

            # <Static value=<_ast.Dict object at 0x7fae359adb10> name=None at 7fae359ad250> -> __attrs_140386200378256
            __attrs_140386200378256 = _static_140386200378128

            # <img ... (0:0)
            # --------------------------------------------------------
            __append(u'<img')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386200376464
            __default_140386200376464 = _DEFAULT_MARKER

            # <Substitution u'string:${context/absolute_url}/++resource++plone-logo.png' (24:29)> -> __attr_src
            __token = 979
            try:
                __zt_tmp = __attrs_140386200378256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140386186296528('string', u'${context/absolute_url}/++resource++plone-logo.png', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', u'/++resource++plone-logo.png', _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u' width="108" height="28" alt="Plone"/></h1>\n    </header>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386200379216
            __attrs_140386200379216 = _static_140386247937936

            # <article ... (0:0)
            # --------------------------------------------------------
            __append(u'<article>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae359ad710> name=None at 7fae359ad790> -> __attrs_140386200378512
            __attrs_140386200378512 = _static_140386200377104

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="text">\n        ')

            # <Static value=<_ast.Dict object at 0x7fae30714590> name=None at 7fae30714750> -> __attrs_140386113767952
            __attrs_140386113767952 = _static_140386113766800

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="circle running">\n            ')

            # <Static value=<_ast.Dict object at 0x7fae30714f90> name=None at 7fae30714fd0> -> __attrs_140386194589776
            __attrs_140386194589776 = _static_140386113769360

            # <img ... (0:0)
            # --------------------------------------------------------
            __append(u'<img alt="" src="data:image/png;base64,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" />\n        </div>\n        ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386194588496
            __attrs_140386194588496 = _static_140386247937936

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append(u'<h1>')
            __stream_140386200376848 = []
            __append_140386200376848 = __stream_140386200376848.append
            __append_140386200376848(u'\n            Plone is up and running.\n        ')
            __msgid_140386200376848 = __re_whitespace(''.join(__stream_140386200376848)).strip()
            if __msgid_140386200376848:
                __append(translate(__msgid_140386200376848, mapping=None, default=__msgid_140386200376848, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</h1>\n        ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386194588688
            __attrs_140386194588688 = _static_140386247937936

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append(u'<ul>\n            ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386194587728
            __attrs_140386194587728 = _static_140386247937936

            # <Value u'sites' (36:38)> -> __condition
            __token = 6927
            try:
                __zt_tmp = __attrs_140386194587728
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('path', u'sites', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:
                __append(u'\n                ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386194590480
                __attrs_140386194590480 = _static_140386247937936

                # <Value u'python:len(sites) == 1' (37:40)> -> __condition
                __token = 6975
                try:
                    __zt_tmp = __attrs_140386194590480
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('python', u'len(sites) == 1', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386194590608
                    __attrs_140386194590608 = _static_140386247937936
                    __backup_site_140386173878544 = get('site', __marker)

                    # <Value u'sites' (38:42)> -> __iterator
                    __token = 7042
                    try:
                        __zt_tmp = __attrs_140386194590608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140386186296528('path', u'sites', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    (__iterator, ____index_140386175266000, ) = getitem('repeat')(u'site', __iterator)
                    econtext['site'] = None
                    for __item in __iterator:
                        econtext['site'] = __item

                        # <tal ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<tal>\n                        ')

                        # <Static value=<_ast.Dict object at 0x7fae341ba050> name=None at 7fae341baad0> -> __attrs_140386175264464
                        __attrs_140386175264464 = _static_140386175262800

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="prominent">\n                            <!--<img tal:attributes="src string:${site/absolute_url}/logoIcon.png"\n                                 height="16" width="16"/>-->\n                            ')

                        # <Static value=<_ast.Dict object at 0x7fae341ba890> name=None at 7fae341ba950> -> __attrs_140386175266448
                        __attrs_140386175266448 = _static_140386175264912

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386175262992
                        __default_140386175262992 = _DEFAULT_MARKER

                        # <Substitution u'site/absolute_url' (43:52)> -> __attr_href
                        __token = 7369
                        try:
                            __zt_tmp = __attrs_140386175266448
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140386186296528('path', u'site/absolute_url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u' class="plone-btn"')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386175265552
                        __default_140386175265552 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<_ast.Str object at 0x7fae341baf10> at 7fae341baf90> -> __attr_title
                        __attr_title = u'Go to your instance'
                        __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        if (__attr_title is not None):
                            __append((u' title="%s"' % __attr_title))
                        __append(u'>')
                        __stream_140386175264848 = []
                        __append_140386175264848 = __stream_140386175264848.append
                        __append_140386175264848(u'View your Plone site')
                        __msgid_140386175264848 = __re_whitespace(''.join(__stream_140386175264848)).strip()
                        if __msgid_140386175264848:
                            __append(translate(__msgid_140386175264848, mapping=None, default=__msgid_140386175264848, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</a>\n                        </span>\n                        ')

                        # <Static value=<_ast.Dict object at 0x7fae341b8f50> name=None at 7fae341bac90> -> __attrs_140386175255376
                        __attrs_140386175255376 = _static_140386175258448

                        # <Value u'python:view.outdated(site)' (49:44)> -> __condition
                        __token = 7706
                        try:
                            __zt_tmp = __attrs_140386175255376
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140386186296528('python', u'view.outdated(site)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="upgrade-warning">\n                            ')

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386175256912
                            __attrs_140386175256912 = _static_140386247937936

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')
                            __stream_140386175257616 = []
                            __append_140386175257616 = __stream_140386175257616.append
                            __append_140386175257616(u'\n                            This site configuration is outdated and needs to be\n                            upgraded:')
                            __msgid_140386175257616 = __re_whitespace(''.join(__stream_140386175257616)).strip()
                            if __msgid_140386175257616:
                                __append(translate(__msgid_140386175257616, mapping=None, default=__msgid_140386175257616, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</span>\n                            ')

                            # <Static value=<_ast.Dict object at 0x7fae341b8c50> name=None at 7fae341b8c90> -> __attrs_140386175255120
                            __attrs_140386175255120 = _static_140386175257680

                            # <form ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<form')

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386175257872
                            __default_140386175257872 = _DEFAULT_MARKER

                            # <Substitution u'python:view.upgrade_url(site)' (56:57)> -> __attr_action
                            __token = 8120
                            try:
                                __zt_tmp = __attrs_140386175255120
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_action = _static_140386186296528('python', u'view.upgrade_url(site)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            __attr_action = __quote(__attr_action, '"', '&quot;', u'', _DEFAULT_MARKER)
                            if (__attr_action is not None):
                                __append((u' action="%s"' % __attr_action))
                            __append(u' style="display: inline;" method="get">\n                            ')

                            # <Static value=<_ast.Dict object at 0x7fae35a5de10> name=None at 7fae35a5d0d0> -> __attrs_140386201097424
                            __attrs_140386201097424 = _static_140386201099792

                            # <Value u'not:view/can_manage' (57:50)> -> __condition
                            __token = 8202
                            try:
                                __zt_tmp = __attrs_140386201097424
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140386186296528('not', u'view/can_manage', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            if __condition:

                                # <input ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<input type="hidden" name="came_from"')

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386201096272
                                __default_140386201096272 = _DEFAULT_MARKER

                                # <Substitution u'python:view.upgrade_url(site, can_manage=True)' (59:57)> -> __attr_value
                                __token = 8346
                                try:
                                    __zt_tmp = __attrs_140386201097424
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_value = _static_140386186296528('python', u'view.upgrade_url(site, can_manage=True)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_value is not None):
                                    __append((u' value="%s"' % __attr_value))
                                __append(u'/>')
                            __append(u'\n                            ')

                            # <Static value=<_ast.Dict object at 0x7fae35a5d590> name=None at 7fae35a5da10> -> __attrs_140386201099664
                            __attrs_140386201099664 = _static_140386201097616

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<input type="submit" class="plone-btn-secondary"')

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386201099728
                            __default_140386201099728 = _DEFAULT_MARKER

                            # <Translate msgid=u'label_upgrade_hellip' node=<_ast.Str object at 0x7fae35a5d250> at 7fae35a5d790> -> __attr_value
                            __attr_value = u'Upgrade&hellip;'
                            __attr_value = translate(u'label_upgrade_hellip', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            if (__attr_value is not None):
                                __append((u' value="%s"' % __attr_value))
                            __append(u' />\n                            </form>\n                            </div>')
                        __append(u'\n                    </tal>')
                        ____index_140386175266000 -= 1
                        if (____index_140386175266000 > 0):
                            __append('\n                    ')
                    if (__backup_site_140386173878544 is __marker):
                        del econtext['site']
                    else:
                        econtext['site'] = __backup_site_140386173878544
                    __append(u'\n                ')
                __append(u'\n                ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386175265744
                __attrs_140386175265744 = _static_140386247937936

                # <Value u'python:len(sites) > 1' (68:41)> -> __condition
                __token = 8816
                try:
                    __zt_tmp = __attrs_140386175265744
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('python', u'len(sites) > 1', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fae35a5dc90> name=None at 7fae35a5d350> -> __attrs_140386177517520
                    __attrs_140386177517520 = _static_140386201099408

                    # <h2 ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<h2 id="multiple-sites">')
                    __stream_140386201097104 = []
                    __append_140386201097104 = __stream_140386201097104.append
                    __append_140386201097104(u' You have multiple Plone sites:')
                    __msgid_140386201097104 = __re_whitespace(''.join(__stream_140386201097104)).strip()
                    if __msgid_140386201097104:
                        __append(translate(__msgid_140386201097104, mapping=None, default=__msgid_140386201097104, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</h2>\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fae343e0e50> name=None at 7fae343e0950> -> __attrs_140386177515856
                    __attrs_140386177515856 = _static_140386177519184

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<ul class="sites">\n                        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386177517136
                    __attrs_140386177517136 = _static_140386247937936
                    __backup_site_140386173882192 = get('site', __marker)

                    # <Value u'sites' (71:45)> -> __iterator
                    __token = 9026
                    try:
                        __zt_tmp = __attrs_140386177517136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140386186296528('path', u'sites', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    (__iterator, ____index_140386177517712, ) = getitem('repeat')(u'site', __iterator)
                    econtext['site'] = None
                    for __item in __iterator:
                        econtext['site'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li>\n                            ')

                        # <Static value=<_ast.Dict object at 0x7fae343e0d10> name=None at 7fae343e0c90> -> __attrs_140386177517200
                        __attrs_140386177517200 = _static_140386177518864

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="prominent">\n\n                                ')

                        # <Static value=<_ast.Dict object at 0x7fae341bc550> name=None at 7fae341bc3d0> -> __attrs_140386175272720
                        __attrs_140386175272720 = _static_140386175272272

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386175271440
                        __default_140386175271440 = _DEFAULT_MARKER

                        # <Substitution u'site/absolute_url' (75:56)> -> __attr_href
                        __token = 9188
                        try:
                            __zt_tmp = __attrs_140386175272720
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140386186296528('path', u'site/absolute_url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386175271504
                        __default_140386175271504 = _DEFAULT_MARKER

                        # <Substitution u'site/Title' (76:56)> -> __attr_title
                        __token = 9263
                        try:
                            __zt_tmp = __attrs_140386175272720
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_140386186296528('path', u'site/Title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((u' title="%s"' % __attr_title))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386175272144
                        __default_140386175272144 = _DEFAULT_MARKER

                        # <Value u'site/Title' (77:48)> -> __cache_140386175273296
                        __token = 9325
                        try:
                            __zt_tmp = __attrs_140386175272720
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386175273296 = _static_140386186296528('path', u'site/Title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'site/Title' (77:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae341bcb50> -> __condition
                        __expression = __cache_140386175273296

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n                                    Site title\n                                ')
                        else:
                            __content = __cache_140386175273296
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</a>\n                                ')

                        # <Static value=<_ast.Dict object at 0x7fae341bcc50> name=None at 7fae341bcd10> -> __attrs_140386175274896
                        __attrs_140386175274896 = _static_140386175274064

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="discreet">')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386175273104
                        __default_140386175273104 = _DEFAULT_MARKER

                        # <Value u'string:\u2013 ${site/getId}' (81:51)> -> __cache_140386175272912
                        __token = 9528
                        try:
                            __zt_tmp = __attrs_140386175274896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386175272912 = _static_140386186296528('string', u'\u2013 ${site/getId}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'string:\u2013 ${site/getId}' (81:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae341bca50> -> __condition
                        __expression = __cache_140386175272912

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140386175272912
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n                                ')

                        # <Static value=<_ast.Dict object at 0x7fae343e3090> name=None at 7fae343e3a10> -> __attrs_140386177529040
                        __attrs_140386177529040 = _static_140386177527952

                        # <img ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<img height="16" width="16"')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386177529232
                        __default_140386177529232 = _DEFAULT_MARKER

                        # <Substitution u'string:${site/absolute_url}/logoIcon.png' (82:57)> -> __attr_src
                        __token = 9611
                        try:
                            __zt_tmp = __attrs_140386177529040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_src = _static_140386186296528('string', u'${site/absolute_url}/logoIcon.png', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_src is not None):
                            __append((u' src="%s"' % __attr_src))
                        __append(u'/>\n                            </span>\n                            ')

                        # <Static value=<_ast.Dict object at 0x7fae343e3810> name=None at 7fae343e33d0> -> __attrs_140386177530960
                        __attrs_140386177530960 = _static_140386177529872

                        # <Value u'python:view.outdated(site)' (86:48)> -> __condition
                        __token = 9856
                        try:
                            __zt_tmp = __attrs_140386177530960
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140386186296528('python', u'view.outdated(site)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="upgrade-warning">\n                                ')

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386177530704
                            __attrs_140386177530704 = _static_140386247937936

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')
                            __stream_140386177531216 = []
                            __append_140386177531216 = __stream_140386177531216.append
                            __append_140386177531216(u'\n                                    This site configuration is outdated and\n                                    needs to be upgraded:\n                                ')
                            __msgid_140386177531216 = __re_whitespace(''.join(__stream_140386177531216)).strip()
                            if __msgid_140386177531216:
                                __append(translate(__msgid_140386177531216, mapping=None, default=__msgid_140386177531216, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</span>\n                                 ')

                            # <Static value=<_ast.Dict object at 0x7fae343e3750> name=None at 7fae343e39d0> -> __attrs_140386177587408
                            __attrs_140386177587408 = _static_140386177529680

                            # <form ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<form')

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386177589008
                            __default_140386177589008 = _DEFAULT_MARKER

                            # <Substitution u'python:view.upgrade_url(site)' (94:62)> -> __attr_action
                            __token = 10343
                            try:
                                __zt_tmp = __attrs_140386177587408
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_action = _static_140386186296528('python', u'view.upgrade_url(site)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            __attr_action = __quote(__attr_action, '"', '&quot;', u'', _DEFAULT_MARKER)
                            if (__attr_action is not None):
                                __append((u' action="%s"' % __attr_action))
                            __append(u' style="display: inline;" method="get">\n                                 ')

                            # <Static value=<_ast.Dict object at 0x7fae343f15d0> name=None at 7fae343f1690> -> __attrs_140386177588432
                            __attrs_140386177588432 = _static_140386177586640

                            # <Value u'not:view/can_manage' (95:55)> -> __condition
                            __token = 10430
                            try:
                                __zt_tmp = __attrs_140386177588432
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140386186296528('not', u'view/can_manage', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            if __condition:

                                # <input ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<input type="hidden" name="came_from"')

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386177587664
                                __default_140386177587664 = _DEFAULT_MARKER

                                # <Substitution u'python:view.upgrade_url(site, can_manage=True)' (97:62)> -> __attr_value
                                __token = 10584
                                try:
                                    __zt_tmp = __attrs_140386177588432
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_value = _static_140386186296528('python', u'view.upgrade_url(site, can_manage=True)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_value is not None):
                                    __append((u' value="%s"' % __attr_value))
                                __append(u'/>')
                            __append(u'\n                                 ')

                            # <Static value=<_ast.Dict object at 0x7fae343f11d0> name=None at 7fae343f1310> -> __attrs_140386126927888
                            __attrs_140386126927888 = _static_140386177585616

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<input type="submit" class="plone-btn-secondary"')

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386126928400
                            __default_140386126928400 = _DEFAULT_MARKER

                            # <Translate msgid=u'label_upgrade_hellip' node=<_ast.Str object at 0x7fae313a1ad0> at 7fae313a1950> -> __attr_value
                            __attr_value = u'Upgrade&hellip;'
                            __attr_value = translate(u'label_upgrade_hellip', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            if (__attr_value is not None):
                                __append((u' value="%s"' % __attr_value))
                            __append(u' />\n                                 </form>\n\n                            </div>')
                        __append(u'\n                        </li>')
                        ____index_140386177517712 -= 1
                        if (____index_140386177517712 > 0):
                            __append('\n                        ')
                    if (__backup_site_140386173882192 is __marker):
                        del econtext['site']
                    else:
                        econtext['site'] = __backup_site_140386173882192
                    __append(u'\n                    </ul>\n                ')
                __append(u'\n            ')
            __append(u'\n            ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386194588176
            __attrs_140386194588176 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append(u'<li>\n                ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386177586256
            __attrs_140386177586256 = _static_140386247937936

            # <Value u'not:sites' (110:55)> -> __condition
            __token = 11166
            try:
                __zt_tmp = __attrs_140386177586256
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('not', u'sites', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')
                __stream_140386177518224 = []
                __append_140386177518224 = __stream_140386177518224.append
                __append_140386177518224(u'\n                    Your Plone site has not been added yet:\n                ')
                __msgid_140386177518224 = __re_whitespace(''.join(__stream_140386177518224)).strip()
                if __msgid_140386177518224:
                    __append(translate(__msgid_140386177518224, mapping=None, default=__msgid_140386177518224, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>')
            __append(u'\n                ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386126925968
            __attrs_140386126925968 = _static_140386247937936

            # <Value u'sites' (113:55)> -> __condition
            __token = 11317
            try:
                __zt_tmp = __attrs_140386126925968
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('path', u'sites', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')
                __stream_140386126926480 = []
                __append_140386126926480 = __stream_140386126926480.append
                __append_140386126926480(u'\n                    You can add another Plone site:\n                ')
                __msgid_140386126926480 = __re_whitespace(''.join(__stream_140386126926480)).strip()
                if __msgid_140386126926480:
                    __append(translate(__msgid_140386126926480, mapping=None, default=__msgid_140386126926480, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>')
            __append(u'\n                ')

            # <Static value=<_ast.Dict object at 0x7fae313a1b10> name=None at 7fae313a1a50> -> __attrs_140386200374288
            __attrs_140386200374288 = _static_140386126928656
            __backup_site_number_140386173879632 = get('site_number', __marker)

            # <Value u"python: '' if not sites else len(sites) + 1" (119:46)> -> __value
            __token = 11557
            try:
                __zt_tmp = __attrs_140386200374288
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u" '' if not sites else len(sites) + 1", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['site_number'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append(u'<form id="add-plone-site" method="get"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386126927312
            __default_140386126927312 = _DEFAULT_MARKER

            # <Substitution u'string:${context/absolute_url}/@@plone-addsite' (120:45)> -> __attr_action
            __token = 11647
            try:
                __zt_tmp = __attrs_140386200374288
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140386186296528('string', u'${context/absolute_url}/@@plone-addsite', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', u'#', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((u' action="%s"' % __attr_action))
            __append(u'>\n                    ')

            # <Static value=<_ast.Dict object at 0x7fae359ac490> name=None at 7fae359ac050> -> __attrs_140386200374032
            __attrs_140386200374032 = _static_140386200372368

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="hidden" name="site_id"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386200373520
            __default_140386200373520 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution u'Plone${site_number}' (121:63)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fae359aca90> -> __attr_value
            __token = 11759
            __token = 11766
            try:
                __zt_tmp = __attrs_140386200374032
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140386186296528('path', u'site_number', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_value = ('%s%s' % (u'Plone', (__attr_value if (__attr_value is not None) else ''), ))
            if (__attr_value is None):
                pass
            else:
                if (__attr_value is _DEFAULT_MARKER):
                    __attr_value = None
                else:
                    __tt = type(__attr_value)
                    if ((__tt is int) or (__tt is float) or (__tt is long)):
                        __attr_value = unicode(__attr_value)
                    else:
                        if (__tt is str):
                            __attr_value = decode(__attr_value)
                        else:
                            if (__tt is not unicode):
                                try:
                                    __attr_value = __attr_value.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_value)
                                    __attr_value = (unicode(__attr_value) if (__attr_value is __converted) else __converted)
                                else:
                                    __attr_value = __attr_value()
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u' />\n                    ')

            # <Static value=<_ast.Dict object at 0x7fae359ac190> name=None at 7fae359acd90> -> __attrs_140386200373264
            __attrs_140386200373264 = _static_140386200371600

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="submit"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386200374096
            __default_140386200374096 = _DEFAULT_MARKER

            # <Translate msgid=None node=<_ast.Str object at 0x7fae359ac850> at 7fae359ac2d0> -> __attr_value
            __attr_value = u'Create a new Plone site'
            __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u' />\n                    ')

            # <Static value=<_ast.Dict object at 0x7fae313af790> name=None at 7fae313af510> -> __attrs_140386126985360
            __attrs_140386126985360 = _static_140386126985104

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a class="discreet"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386126983568
            __default_140386126983568 = _DEFAULT_MARKER

            # <Substitution u'string:${context/absolute_url}/@@plone-addsite?site_id=Plone${site_number}&advanced=1' (127:44)> -> __attr_href
            __token = 12063
            try:
                __zt_tmp = __attrs_140386126985360
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140386186296528('string', u'${context/absolute_url}/@@plone-addsite?site_id=Plone${site_number}&advanced=1', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u' >')
            __stream_140386200373456 = []
            __append_140386200373456 = __stream_140386200373456.append
            __append_140386200373456(u'Advanced')
            __msgid_140386200373456 = __re_whitespace(''.join(__stream_140386200373456)).strip()
            if __msgid_140386200373456:
                __append(translate(__msgid_140386200373456, mapping=None, default=__msgid_140386200373456, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</a>\n                </form>')
            if (__backup_site_number_140386173879632 is __marker):
                del econtext['site_number']
            else:
                econtext['site_number'] = __backup_site_number_140386173879632
            __append(u'\n            </li>\n\n        </ul>\n    </div>\n  </article>\n  ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386194589072
            __attrs_140386194589072 = _static_140386247937936

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append(u'<footer>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386126983632
            __attrs_140386126983632 = _static_140386247937936

            # <p ... (0:0)
            # --------------------------------------------------------
            __append(u'<p>\n      ')

            # <Static value=<_ast.Dict object at 0x7fae313af950> name=None at 7fae313af6d0> -> __attrs_140386126987152
            __attrs_140386126987152 = _static_140386126985552

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386126986448
            __default_140386126986448 = _DEFAULT_MARKER

            # <Substitution u'string:${context/absolute_url}/manage_main' (138:29)> -> __attr_href
            __token = 12338
            try:
                __zt_tmp = __attrs_140386126987152
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140386186296528('string', u'${context/absolute_url}/manage_main', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386126986832
            __default_140386126986832 = _DEFAULT_MARKER

            # <Translate msgid=None node=<_ast.Str object at 0x7fae313afd90> at 7fae313afdd0> -> __attr_title
            __attr_title = u'Go to the ZMI'
            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))
            __append(u'>')
            __stream_140386126984336 = []
            __append_140386126984336 = __stream_140386126984336.append
            __append_140386126984336(u'Management Interface')
            __msgid_140386126984336 = __re_whitespace(''.join(__stream_140386126984336)).strip()
            if u'label_zmi_link':
                __append(translate(u'label_zmi_link', mapping=None, default=__msgid_140386126984336, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</a>\n      ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386192638544
            __attrs_140386192638544 = _static_140386247937936

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140386192638224 = []
            __append_140386192638224 = __stream_140386192638224.append
            __append_140386192638224(u' &#151; low-level technical configuration.')
            __msgid_140386192638224 = __re_whitespace(''.join(__stream_140386192638224)).strip()
            if u'label_zmi_link_description':
                __append(translate(u'label_zmi_link_description', mapping=None, default=__msgid_140386192638224, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n    </p>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386192638928
            __attrs_140386192638928 = _static_140386247937936

            # <p ... (0:0)
            # --------------------------------------------------------
            __append(u'<p>\n      ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386192639760
            __attrs_140386192639760 = _static_140386247937936

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140386192639440 = []
            __append_140386192639440 = __stream_140386192639440.append
            __append_140386192639440(u' For an introduction to Plone, success stories, demos, providers, visit')
            __msgid_140386192639440 = __re_whitespace(''.join(__stream_140386192639440)).strip()
            if u'label_plone_com_description':
                __append(translate(u'label_plone_com_description', mapping=None, default=__msgid_140386192639440, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n      ')

            # <Static value=<_ast.Dict object at 0x7fae3524c890> name=None at 7fae3524c850> -> __attrs_140386192641616
            __attrs_140386192641616 = _static_140386192640144

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a href="http://plone.com"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386192641104
            __default_140386192641104 = _DEFAULT_MARKER

            # <Translate msgid=u'label_plone_com_title' node=<_ast.Str object at 0x7fae3524cb90> at 7fae3524cbd0> -> __attr_title
            __attr_title = u'Plone.com'
            __attr_title = translate(u'label_plone_com_title', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))
            __append(u' target="_blank">plone.com</a>.\n    </p>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386192642000
            __attrs_140386192642000 = _static_140386247937936

            # <p ... (0:0)
            # --------------------------------------------------------
            __append(u'<p>\n      ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386192667472
            __attrs_140386192667472 = _static_140386247937936

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140386192667152 = []
            __append_140386192667152 = __stream_140386192667152.append
            __append_140386192667152(u' For documentation, add-ons, support, community, visit')
            __msgid_140386192667152 = __re_whitespace(''.join(__stream_140386192667152)).strip()
            if u'label_plone_org_description':
                __append(translate(u'label_plone_org_description', mapping=None, default=__msgid_140386192667152, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n      ')

            # <Static value=<_ast.Dict object at 0x7fae352534d0> name=None at 7fae35253490> -> __attrs_140386192669008
            __attrs_140386192669008 = _static_140386192667856

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a href="http://plone.org"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386192668688
            __default_140386192668688 = _DEFAULT_MARKER

            # <Translate msgid=u'label_plone_org_title' node=<_ast.Str object at 0x7fae35253750> at 7fae35253790> -> __attr_title
            __attr_title = u'Plone Community Home'
            __attr_title = translate(u'label_plone_org_title', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))
            __append(u'>plone.org</a>.\n    </p>\n  </footer>\n</div>\n</body>')
            if (__backup_sites_140386177197328 is __marker):
                del econtext['sites']
            else:
                econtext['sites'] = __backup_sites_140386177197328
            __append(u'\n</html>')
            __i18n_domain = __previous_i18n_domain_140386200451536
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }