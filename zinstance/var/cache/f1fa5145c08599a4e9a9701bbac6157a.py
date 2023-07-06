# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/browser/templates/error_message.pt'

__tokens = {390: (u'options/error_type|nothing', 11, 26), 441: (u' options/error_tb|nothin', 12, 23), 494: (u'd options/error_log_id|nothi', 13, 26), 567: (u"python:err_type == 'NotFound'", 15, 39), 651: (u'nocall:view/@@plone_redirector_view', 17, 51), 1690: (u'string:${context/portal_url}/contact-info', 35, 48), 2046: (u'redirection_view/find_first_parent', 43, 58), 2140: (u' redirection_view/search_for_simila', 44, 58), 2232: (u'w context/@@plo', 45, 54), 2302: (u'ry context/portal_regis', 46, 51), 2387: (u"ion python:registry['plone.types_use_view_action_in_listin", 47, 57), 2503: (u"ngth python:registry['plone.search_results_description_len", 48, 52), 2623: (u'tring nocall:plone_view/normalize', 49, 55), 2713: (u'python:first_parent is not None or similar_items', 50, 48), 3022: (u'first_parent/absolute_url | nothing', 56, 52), 3115: (u'first_parent/absolute_url', 57, 55), 3197: (u" python:hasattr(first_parent, 'getTypeInfo') and first_parent.getTypeInfo().getId(", 58, 55), 3328: (u"l python:result_url + '/view' if result_type in use_view_action else result_u", 59, 46), 3457: (u'result_type', 60, 47), 3587: (u"python:' state-' + context.portal_workflow.getInfoFor(first_parent, 'review_state', '')", 62, 67), 3512: (u'${url}', 61, 41), 3514: (u'url', 61, 43), 3734: (u"python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", 63, 57), 3810: (u'${first_parent/Title}', 63, 133), 3812: (u'first_parent/Title', 63, 135), 3887: (u'python:plone_view.cropText(first_parent.Description(), desc_length)', 64, 51), 4125: (u'similar_items', 68, 53), 4196: (u'similar/getURL', 69, 55), 4267: (u' similar/portal_typ', 70, 55), 4335: (u"l python:result_url + '/view' if result_type in use_view_action else result_u", 71, 46), 4534: (u'string: state-${similar/review_state}', 73, 67), 4459: (u'${url}', 72, 41), 4461: (u'url', 72, 43), 4631: (u"python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", 74, 57), 4707: (u'${similar/pretty_title_or_id}', 74, 133), 4709: (u'similar/pretty_title_or_id', 74, 135), 4792: (u"python:plone_view.cropText(similar.Description or '', desc_length)", 75, 51), 5260: (u'view/is_manager', 89, 35), 5193: (u"python: err_type != 'NotFound'", 88, 41), 5548: (u'isManager', 97, 36), 5747: (u'err_tb', 102, 37), 5821: (u'not:isManager', 105, 40), 6222: (u'string:${context/portal_url}/contact-info', 111, 44), 261: (u'context/@@main_template/macros/master', 6, 23), 261: (u'context/@@main_template/macros/master', 6, 23)}

from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386175274320 = {u'href': u'${url}', u'class': u"python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", }
_static_140386178040912 = {u'class': u'discreet', }
_static_140386194998544 = {u'class': u'documentFirstHeading', }
_static_140386177531088 = u'master'
_static_140386178043408 = {u'id': u'content-core', }
_static_140386201105680 = {u'class': u'discreet', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386201097424 = {u'class': u'documentFirstHeading', }
_static_140386204877968 = {u'href': u'#', }
_static_140386201098576 = {u'id': u'page-not-found-list', }
_static_140386186296528 = __compile_zt_expr
_static_140386201107728 = {u'href': u'#', }
_static_140386194999312 = {u'id': u'content-core', }
_static_140386194998800 = {u'class': u'description', }
_static_140386178006544 = {u'class': u'discreet', }
_static_140386178005776 = {u'href': u'${url}', u'class': u"python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", }
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

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386177529808
            __attrs_140386177529808 = _static_140386247937936
            __previous_i18n_domain_140386177528720 = __i18n_domain
            __i18n_domain = u'plone'
            __backup_macroname_140386120928704 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7fae343e3cd0> name=None at 7fae343e3d90> -> __value
            __value = _static_140386177531088
            econtext['macroname'] = __value

            def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386175264592
                __attrs_140386175264592 = _static_140386247937936
                __backup_err_type_140386173878416 = get('err_type', __marker)

                # <Value u'options/error_type|nothing' (11:26)> -> __value
                __token = 390
                try:
                    __zt_tmp = __attrs_140386175264592
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'options/error_type|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['err_type'] = __value
                __backup_err_tb_140386173480208 = get('err_tb', __marker)

                # <Value u'options/error_tb|nothing' (12:23)> -> __value
                __token = 441
                try:
                    __zt_tmp = __attrs_140386175264592
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'options/error_tb|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['err_tb'] = __value
                __backup_err_log_id_140386179295888 = get('err_log_id', __marker)

                # <Value u'options/error_log_id|nothing' (13:26)> -> __value
                __token = 494
                try:
                    __zt_tmp = __attrs_140386175264592
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'options/error_log_id|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['err_log_id'] = __value
                __append(u'\n\n        ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386195057104
                __attrs_140386195057104 = _static_140386247937936

                # <Value u"python:err_type == 'NotFound'" (15:39)> -> __condition
                __token = 567
                try:
                    __zt_tmp = __attrs_140386195057104
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('python', u"err_type == 'NotFound'", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n\n            ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386195056528
                    __attrs_140386195056528 = _static_140386247937936
                    __backup_redirection_view_140386173968784 = get('redirection_view', __marker)

                    # <Value u'nocall:view/@@plone_redirector_view' (17:51)> -> __value
                    __token = 651
                    try:
                        __zt_tmp = __attrs_140386195056528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('nocall', u'view/@@plone_redirector_view', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['redirection_view'] = __value
                    __append(u'\n\n                ')

                    # <Static value=<_ast.Dict object at 0x7fae3548c510> name=None at 7fae3548c290> -> __attrs_140386195000656
                    __attrs_140386195000656 = _static_140386194998544

                    # <h1 ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<h1 class="documentFirstHeading">')
                    __stream_140386194998672 = []
                    __append_140386194998672 = __stream_140386194998672.append
                    __append_140386194998672(u'\n                    This page does not seem to exist&hellip;\n                ')
                    __msgid_140386194998672 = __re_whitespace(''.join(__stream_140386194998672)).strip()
                    if u'heading_site_there_seems_to_be_an_error':
                        __append(translate(u'heading_site_there_seems_to_be_an_error', mapping=None, default=__msgid_140386194998672, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</h1>\n\n                ')

                    # <Static value=<_ast.Dict object at 0x7fae3548c810> name=None at 7fae3548c3d0> -> __attrs_140386194998096
                    __attrs_140386194998096 = _static_140386194999312

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="content-core">\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fae3548c610> name=None at 7fae3548cf90> -> __attrs_140386194998160
                    __attrs_140386194998160 = _static_140386194998800

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="description">')
                    __stream_140386195000400 = []
                    __append_140386195000400 = __stream_140386195000400.append
                    __append_140386195000400(u'\n \t                    We apologize for the inconvenience, but the page you were trying to access is not at this address.\n                        You can use the links below to help you find what you are looking for.\n                     ')
                    __msgid_140386195000400 = __re_whitespace(''.join(__stream_140386195000400)).strip()
                    if u'description_site_error':
                        __append(translate(u'description_site_error', mapping=None, default=__msgid_140386195000400, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</p>\n\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fae35a5f510> name=None at 7fae3548cc90> -> __attrs_140386201107280
                    __attrs_140386201107280 = _static_140386201105680

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="discreet">')
                    __stream_140386135920720_site_admin = ''
                    __stream_140386194997584 = []
                    __append_140386194997584 = __stream_140386194997584.append
                    __append_140386194997584(u'\n                        If you are certain you have the correct web address but are encountering an error, please\n                        contact the ')
                    __stream_140386135920720_site_admin = []
                    __append_140386135920720_site_admin = __stream_140386135920720_site_admin.append

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386201104464
                    __attrs_140386201104464 = _static_140386247937936

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140386135920720_site_admin(u'<span>\n                        ')

                    # <Static value=<_ast.Dict object at 0x7fae35a5fd10> name=None at 7fae35a5f8d0> -> __attrs_140386201104528
                    __attrs_140386201104528 = _static_140386201107728

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140386135920720_site_admin(u'<a')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386201108048
                    __default_140386201108048 = _DEFAULT_MARKER

                    # <Substitution u'string:${context/portal_url}/contact-info' (35:48)> -> __attr_href
                    __token = 1690
                    try:
                        __zt_tmp = __attrs_140386201104528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140386186296528('string', u'${context/portal_url}/contact-info', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140386135920720_site_admin((u' href="%s"' % __attr_href))
                    __append_140386135920720_site_admin(u'>')
                    __stream_140386201105168 = []
                    __append_140386201105168 = __stream_140386201105168.append
                    __append_140386201105168(u'site administration')
                    __msgid_140386201105168 = __re_whitespace(''.join(__stream_140386201105168)).strip()
                    if u'label_site_admin':
                        __append_140386135920720_site_admin(translate(u'label_site_admin', mapping=None, default=__msgid_140386201105168, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append_140386135920720_site_admin(u'</a></span>')
                    __append_140386194997584(u'${site_admin}')
                    __stream_140386135920720_site_admin = ''.join(__stream_140386135920720_site_admin)
                    __append_140386194997584(u'.\n                    ')
                    __msgid_140386194997584 = __re_whitespace(''.join(__stream_140386194997584)).strip()
                    if u'description_site_error_mail_site_admin':
                        __append(translate(u'description_site_error_mail_site_admin', mapping={u'site_admin': __stream_140386135920720_site_admin, }, default=__msgid_140386194997584, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</p>\n\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386201104976
                    __attrs_140386201104976 = _static_140386247937936

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p>')
                    __stream_140386201106384 = []
                    __append_140386201106384 = __stream_140386201106384.append
                    __append_140386201106384(u'\n                    Thank you.\n                    ')
                    __msgid_140386201106384 = __re_whitespace(''.join(__stream_140386201106384)).strip()
                    if u'description_site_error_thank_you':
                        __append(translate(u'description_site_error_thank_you', mapping=None, default=__msgid_140386201106384, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</p>\n\n                    <!-- Offer search results for suggestions -->\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386201105744
                    __attrs_140386201105744 = _static_140386247937936
                    __backup_first_parent_140386135649552 = get('first_parent', __marker)

                    # <Value u'redirection_view/find_first_parent' (43:58)> -> __value
                    __token = 2046
                    try:
                        __zt_tmp = __attrs_140386201105744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('path', u'redirection_view/find_first_parent', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['first_parent'] = __value
                    __backup_similar_items_140386135649936 = get('similar_items', __marker)

                    # <Value u'redirection_view/search_for_similar' (44:58)> -> __value
                    __token = 2140
                    try:
                        __zt_tmp = __attrs_140386201105744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('path', u'redirection_view/search_for_similar', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['similar_items'] = __value
                    __backup_plone_view_140386135649680 = get('plone_view', __marker)

                    # <Value u'context/@@plone' (45:54)> -> __value
                    __token = 2232
                    try:
                        __zt_tmp = __attrs_140386201105744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('path', u'context/@@plone', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['plone_view'] = __value
                    __backup_registry_140386135649808 = get('registry', __marker)

                    # <Value u'context/portal_registry' (46:51)> -> __value
                    __token = 2302
                    try:
                        __zt_tmp = __attrs_140386201105744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('path', u'context/portal_registry', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['registry'] = __value
                    __backup_use_view_action_140386135650064 = get('use_view_action', __marker)

                    # <Value u"python:registry['plone.types_use_view_action_in_listings']" (47:57)> -> __value
                    __token = 2387
                    try:
                        __zt_tmp = __attrs_140386201105744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('python', u"registry['plone.types_use_view_action_in_listings']", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['use_view_action'] = __value
                    __backup_desc_length_140386135466064 = get('desc_length', __marker)

                    # <Value u"python:registry['plone.search_results_description_length']" (48:52)> -> __value
                    __token = 2503
                    try:
                        __zt_tmp = __attrs_140386201105744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('python', u"registry['plone.search_results_description_length']", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['desc_length'] = __value
                    __backup_normalizeString_140386176017872 = get('normalizeString', __marker)

                    # <Value u'nocall:plone_view/normalizeString' (49:55)> -> __value
                    __token = 2623
                    try:
                        __zt_tmp = __attrs_140386201105744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('nocall', u'plone_view/normalizeString', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['normalizeString'] = __value

                    # <Value u'python:first_parent is not None or similar_items' (50:48)> -> __condition
                    __token = 2713
                    try:
                        __zt_tmp = __attrs_140386201105744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('python', u'first_parent is not None or similar_items', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n\n                        ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386201097296
                        __attrs_140386201097296 = _static_140386247937936

                        # <h2 ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<h2>')
                        __stream_140386201096272 = []
                        __append_140386201096272 = __stream_140386201096272.append
                        __append_140386201096272(u'You might have been looking for&hellip;')
                        __msgid_140386201096272 = __re_whitespace(''.join(__stream_140386201096272)).strip()
                        if u'heading_not_found_suggestions':
                            __append(translate(u'heading_not_found_suggestions', mapping=None, default=__msgid_140386201096272, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</h2>\n                        ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386201098512
                        __attrs_140386201098512 = _static_140386247937936

                        # <nav ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<nav>\n                        ')

                        # <Static value=<_ast.Dict object at 0x7fae35a5d950> name=None at 7fae35a5d090> -> __attrs_140386201099856
                        __attrs_140386201099856 = _static_140386201098576

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<ul id="page-not-found-list">\n\n                        ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386175271056
                        __attrs_140386175271056 = _static_140386247937936

                        # <Value u'first_parent/absolute_url | nothing' (56:52)> -> __condition
                        __token = 3022
                        try:
                            __zt_tmp = __attrs_140386175271056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140386186296528('path', u'first_parent/absolute_url | nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        if __condition:
                            __append(u'\n                            ')

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386175272656
                            __attrs_140386175272656 = _static_140386247937936
                            __backup_result_url_140386136765456 = get('result_url', __marker)

                            # <Value u'first_parent/absolute_url' (57:55)> -> __value
                            __token = 3115
                            try:
                                __zt_tmp = __attrs_140386175272656
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140386186296528('path', u'first_parent/absolute_url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            econtext['result_url'] = __value
                            __backup_result_type_140386135466128 = get('result_type', __marker)

                            # <Value u"python:hasattr(first_parent, 'getTypeInfo') and first_parent.getTypeInfo().getId()" (58:55)> -> __value
                            __token = 3197
                            try:
                                __zt_tmp = __attrs_140386175272656
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140386186296528('python', u"hasattr(first_parent, 'getTypeInfo') and first_parent.getTypeInfo().getId()", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            econtext['result_type'] = __value
                            __backup_url_140386136768272 = get('url', __marker)

                            # <Value u"python:result_url + '/view' if result_type in use_view_action else result_url" (59:46)> -> __value
                            __token = 3328
                            try:
                                __zt_tmp = __attrs_140386175272656
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140386186296528('python', u"result_url + '/view' if result_type in use_view_action else result_url", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            econtext['url'] = __value

                            # <Value u'result_type' (60:47)> -> __condition
                            __token = 3457
                            try:
                                __zt_tmp = __attrs_140386175272656
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140386186296528('path', u'result_type', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            if __condition:

                                # <li ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<li>\n                                ')

                                # <Static value=<_ast.Dict object at 0x7fae341bcd50> name=None at 7fae341bcfd0> -> __attrs_140386175274128
                                __attrs_140386175274128 = _static_140386175274320
                                __backup_item_wf_state_class_140386136765776 = get('item_wf_state_class', __marker)

                                # <Value u"python:' state-' + context.portal_workflow.getInfoFor(first_parent, 'review_state', '')" (62:67)> -> __value
                                __token = 3587
                                try:
                                    __zt_tmp = __attrs_140386175274128
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __value = _static_140386186296528('python', u"' state-' + context.portal_workflow.getInfoFor(first_parent, 'review_state', '')", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                econtext['item_wf_state_class'] = __value

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<a')

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386175273424
                                __default_140386175273424 = _DEFAULT_MARKER

                                # <Interpolation value=<Substitution u'${url}' (61:41)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fae341bc790> -> __attr_href
                                __token = 3512
                                __token = 3514
                                try:
                                    __zt_tmp = __attrs_140386175274128
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_140386186296528('path', u'url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                                __attr_href = __attr_href
                                if (__attr_href is None):
                                    pass
                                else:
                                    if (__attr_href is _DEFAULT_MARKER):
                                        __attr_href = None
                                    else:
                                        __tt = type(__attr_href)
                                        if ((__tt is int) or (__tt is float) or (__tt is long)):
                                            __attr_href = unicode(__attr_href)
                                        else:
                                            if (__tt is str):
                                                __attr_href = decode(__attr_href)
                                            else:
                                                if (__tt is not unicode):
                                                    try:
                                                        __attr_href = __attr_href.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__attr_href)
                                                        __attr_href = (unicode(__attr_href) if (__attr_href is __converted) else __converted)
                                                    else:
                                                        __attr_href = __attr_href()
                                if (__attr_href is not None):
                                    __append((u' href="%s"' % __attr_href))

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386175273168
                                __default_140386175273168 = _DEFAULT_MARKER

                                # <Substitution u"python:'contenttype-' + normalizeString(result_type) + item_wf_state_class" (63:57)> -> __attr_class
                                __token = 3734
                                try:
                                    __zt_tmp = __attrs_140386175274128
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_140386186296528('python', u"'contenttype-' + normalizeString(result_type) + item_wf_state_class", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_class is not None):
                                    __append((u' class="%s"' % __attr_class))
                                __append(u'>')

                                # <Interpolation value=<Substitution u'${first_parent/Title}' (63:133)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fae34457510> -> __content_140386296014144
                                __token = 3810
                                __token = 3812
                                try:
                                    __zt_tmp = __attrs_140386175274128
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_140386296014144 = _static_140386186296528('path', u'first_parent/Title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                __content_140386296014144 = __quote(__content_140386296014144, '\x00', '&#0;', None, None)
                                __content_140386296014144 = __content_140386296014144
                                if (__content_140386296014144 is None):
                                    pass
                                else:
                                    if (__content_140386296014144 is None):
                                        __content_140386296014144 = None
                                    else:
                                        __tt = type(__content_140386296014144)
                                        if ((__tt is int) or (__tt is float) or (__tt is long)):
                                            __content_140386296014144 = unicode(__content_140386296014144)
                                        else:
                                            if (__tt is str):
                                                __content_140386296014144 = decode(__content_140386296014144)
                                            else:
                                                if (__tt is not unicode):
                                                    try:
                                                        __content_140386296014144 = __content_140386296014144.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__content_140386296014144)
                                                        __content_140386296014144 = (unicode(__content_140386296014144) if (__content_140386296014144 is __converted) else __converted)
                                                    else:
                                                        __content_140386296014144 = __content_140386296014144()
                                if (__content_140386296014144 is not None):
                                    __append(__content_140386296014144)
                                __append(u'</a>')
                                if (__backup_item_wf_state_class_140386136765776 is __marker):
                                    del econtext['item_wf_state_class']
                                else:
                                    econtext['item_wf_state_class'] = __backup_item_wf_state_class_140386136765776
                                __append(u'\n                                ')

                                # <Static value=<_ast.Dict object at 0x7fae34457e10> name=None at 7fae34457d90> -> __attrs_140386178006608
                                __attrs_140386178006608 = _static_140386178006544

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span class="discreet">')

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386178005392
                                __default_140386178005392 = _DEFAULT_MARKER

                                # <Value u'python:plone_view.cropText(first_parent.Description(), desc_length)' (64:51)> -> __cache_140386178003472
                                __token = 3887
                                try:
                                    __zt_tmp = __attrs_140386178006608
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140386178003472 = _static_140386186296528('python', u'plone_view.cropText(first_parent.Description(), desc_length)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                                # <BinOp left=<Value u'python:plone_view.cropText(first_parent.Description(), desc_length)' (64:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae34457d10> -> __condition
                                __expression = __cache_140386178003472

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(u' Description ')
                                else:
                                    __content = __cache_140386178003472
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</span>\n                            </li>')
                            if (__backup_url_140386136768272 is __marker):
                                del econtext['url']
                            else:
                                econtext['url'] = __backup_url_140386136768272
                            if (__backup_result_type_140386135466128 is __marker):
                                del econtext['result_type']
                            else:
                                econtext['result_type'] = __backup_result_type_140386135466128
                            if (__backup_result_url_140386136765456 is __marker):
                                del econtext['result_url']
                            else:
                                econtext['result_url'] = __backup_result_url_140386136765456
                            __append(u'\n                        ')
                        __append(u'\n\n                        ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386175274768
                        __attrs_140386175274768 = _static_140386247937936
                        __backup_similar_140386135632976 = get('similar', __marker)

                        # <Value u'similar_items' (68:53)> -> __iterator
                        __token = 4125
                        try:
                            __zt_tmp = __attrs_140386175274768
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140386186296528('path', u'similar_items', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        (__iterator, ____index_140386175274064, ) = getitem('repeat')(u'similar', __iterator)
                        econtext['similar'] = None
                        for __item in __iterator:
                            econtext['similar'] = __item
                            __append(u'\n                            ')

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386178005968
                            __attrs_140386178005968 = _static_140386247937936
                            __backup_result_url_140386136767568 = get('result_url', __marker)

                            # <Value u'similar/getURL' (69:55)> -> __value
                            __token = 4196
                            try:
                                __zt_tmp = __attrs_140386178005968
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140386186296528('path', u'similar/getURL', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            econtext['result_url'] = __value
                            __backup_result_type_140386135632720 = get('result_type', __marker)

                            # <Value u'similar/portal_type' (70:55)> -> __value
                            __token = 4267
                            try:
                                __zt_tmp = __attrs_140386178005968
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140386186296528('path', u'similar/portal_type', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            econtext['result_type'] = __value
                            __backup_url_140386136736400 = get('url', __marker)

                            # <Value u"python:result_url + '/view' if result_type in use_view_action else result_url" (71:46)> -> __value
                            __token = 4335
                            try:
                                __zt_tmp = __attrs_140386178005968
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140386186296528('python', u"result_url + '/view' if result_type in use_view_action else result_url", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            econtext['url'] = __value

                            # <li ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<li>\n                                ')

                            # <Static value=<_ast.Dict object at 0x7fae34457b10> name=None at 7fae344577d0> -> __attrs_140386178040720
                            __attrs_140386178040720 = _static_140386178005776
                            __backup_item_wf_state_class_140386136243920 = get('item_wf_state_class', __marker)

                            # <Value u'string: state-${similar/review_state}' (73:67)> -> __value
                            __token = 4534
                            try:
                                __zt_tmp = __attrs_140386178040720
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140386186296528('string', u' state-${similar/review_state}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            econtext['item_wf_state_class'] = __value

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<a')

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386178039952
                            __default_140386178039952 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution u'${url}' (72:41)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fae34457750> -> __attr_href
                            __token = 4459
                            __token = 4461
                            try:
                                __zt_tmp = __attrs_140386178040720
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href = _static_140386186296528('path', u'url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_href = __attr_href
                            if (__attr_href is None):
                                pass
                            else:
                                if (__attr_href is _DEFAULT_MARKER):
                                    __attr_href = None
                                else:
                                    __tt = type(__attr_href)
                                    if ((__tt is int) or (__tt is float) or (__tt is long)):
                                        __attr_href = unicode(__attr_href)
                                    else:
                                        if (__tt is str):
                                            __attr_href = decode(__attr_href)
                                        else:
                                            if (__tt is not unicode):
                                                try:
                                                    __attr_href = __attr_href.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__attr_href)
                                                    __attr_href = (unicode(__attr_href) if (__attr_href is __converted) else __converted)
                                                else:
                                                    __attr_href = __attr_href()
                            if (__attr_href is not None):
                                __append((u' href="%s"' % __attr_href))

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386178040848
                            __default_140386178040848 = _DEFAULT_MARKER

                            # <Substitution u"python:'contenttype-' + normalizeString(result_type) + item_wf_state_class" (74:57)> -> __attr_class
                            __token = 4631
                            try:
                                __zt_tmp = __attrs_140386178040720
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_140386186296528('python', u"'contenttype-' + normalizeString(result_type) + item_wf_state_class", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((u' class="%s"' % __attr_class))
                            __append(u'>')

                            # <Interpolation value=<Substitution u'${similar/pretty_title_or_id}' (74:133)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fae34460510> -> __content_140386296014144
                            __token = 4707
                            __token = 4709
                            try:
                                __zt_tmp = __attrs_140386178040720
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __content_140386296014144 = _static_140386186296528('path', u'similar/pretty_title_or_id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            __content_140386296014144 = __quote(__content_140386296014144, '\x00', '&#0;', None, None)
                            __content_140386296014144 = __content_140386296014144
                            if (__content_140386296014144 is None):
                                pass
                            else:
                                if (__content_140386296014144 is None):
                                    __content_140386296014144 = None
                                else:
                                    __tt = type(__content_140386296014144)
                                    if ((__tt is int) or (__tt is float) or (__tt is long)):
                                        __content_140386296014144 = unicode(__content_140386296014144)
                                    else:
                                        if (__tt is str):
                                            __content_140386296014144 = decode(__content_140386296014144)
                                        else:
                                            if (__tt is not unicode):
                                                try:
                                                    __content_140386296014144 = __content_140386296014144.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__content_140386296014144)
                                                    __content_140386296014144 = (unicode(__content_140386296014144) if (__content_140386296014144 is __converted) else __converted)
                                                else:
                                                    __content_140386296014144 = __content_140386296014144()
                            if (__content_140386296014144 is not None):
                                __append(__content_140386296014144)
                            __append(u'</a>')
                            if (__backup_item_wf_state_class_140386136243920 is __marker):
                                del econtext['item_wf_state_class']
                            else:
                                econtext['item_wf_state_class'] = __backup_item_wf_state_class_140386136243920
                            __append(u'\n                                ')

                            # <Static value=<_ast.Dict object at 0x7fae34460450> name=None at 7fae34460c50> -> __attrs_140386178043088
                            __attrs_140386178043088 = _static_140386178040912

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span class="discreet">')

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386178041872
                            __default_140386178041872 = _DEFAULT_MARKER

                            # <Value u"python:plone_view.cropText(similar.Description or '', desc_length)" (75:51)> -> __cache_140386178041552
                            __token = 4792
                            try:
                                __zt_tmp = __attrs_140386178043088
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140386178041552 = _static_140386186296528('python', u"plone_view.cropText(similar.Description or '', desc_length)", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                            # <BinOp left=<Value u"python:plone_view.cropText(similar.Description or '', desc_length)" (75:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae34460750> -> __condition
                            __expression = __cache_140386178041552

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u' Description ')
                            else:
                                __content = __cache_140386178041552
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</span>\n                            </li>')
                            if (__backup_url_140386136736400 is __marker):
                                del econtext['url']
                            else:
                                econtext['url'] = __backup_url_140386136736400
                            if (__backup_result_type_140386135632720 is __marker):
                                del econtext['result_type']
                            else:
                                econtext['result_type'] = __backup_result_type_140386135632720
                            if (__backup_result_url_140386136767568 is __marker):
                                del econtext['result_url']
                            else:
                                econtext['result_url'] = __backup_result_url_140386136767568
                            __append(u'\n                        ')
                            ____index_140386175274064 -= 1
                            if (____index_140386175274064 > 0):
                                __append('')
                        if (__backup_similar_140386135632976 is __marker):
                            del econtext['similar']
                        else:
                            econtext['similar'] = __backup_similar_140386135632976
                        __append(u'\n\n                        </ul>\n                        </nav>\n\n                    ')
                    if (__backup_normalizeString_140386176017872 is __marker):
                        del econtext['normalizeString']
                    else:
                        econtext['normalizeString'] = __backup_normalizeString_140386176017872
                    if (__backup_desc_length_140386135466064 is __marker):
                        del econtext['desc_length']
                    else:
                        econtext['desc_length'] = __backup_desc_length_140386135466064
                    if (__backup_use_view_action_140386135650064 is __marker):
                        del econtext['use_view_action']
                    else:
                        econtext['use_view_action'] = __backup_use_view_action_140386135650064
                    if (__backup_registry_140386135649808 is __marker):
                        del econtext['registry']
                    else:
                        econtext['registry'] = __backup_registry_140386135649808
                    if (__backup_plone_view_140386135649680 is __marker):
                        del econtext['plone_view']
                    else:
                        econtext['plone_view'] = __backup_plone_view_140386135649680
                    if (__backup_similar_items_140386135649936 is __marker):
                        del econtext['similar_items']
                    else:
                        econtext['similar_items'] = __backup_similar_items_140386135649936
                    if (__backup_first_parent_140386135649552 is __marker):
                        del econtext['first_parent']
                    else:
                        econtext['first_parent'] = __backup_first_parent_140386135649552
                    __append(u'\n                </div>\n            ')
                    if (__backup_redirection_view_140386173968784 is __marker):
                        del econtext['redirection_view']
                    else:
                        econtext['redirection_view'] = __backup_redirection_view_140386173968784
                    __append(u'\n\n        ')
                __append(u'\n\n        ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386195057616
                __attrs_140386195057616 = _static_140386247937936
                __backup_isManager_140386176017232 = get('isManager', __marker)

                # <Value u'view/is_manager' (89:35)> -> __value
                __token = 5260
                try:
                    __zt_tmp = __attrs_140386195057616
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'view/is_manager', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['isManager'] = __value

                # <Value u"python: err_type != 'NotFound'" (88:41)> -> __condition
                __token = 5193
                try:
                    __zt_tmp = __attrs_140386195057616
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('python', u" err_type != 'NotFound'", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n\n            ')

                    # <Static value=<_ast.Dict object at 0x7fae35a5d4d0> name=None at 7fae35a5df90> -> __attrs_140386175271248
                    __attrs_140386175271248 = _static_140386201097424

                    # <h1 ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<h1 class="documentFirstHeading">')
                    __stream_140386201098320 = []
                    __append_140386201098320 = __stream_140386201098320.append
                    __append_140386201098320(u'\n                We&#8217;re sorry, but there seems to be an error&hellip;\n            ')
                    __msgid_140386201098320 = __re_whitespace(''.join(__stream_140386201098320)).strip()
                    if u'heading_site_error_sorry':
                        __append(translate(u'heading_site_error_sorry', mapping=None, default=__msgid_140386201098320, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</h1>\n\n            ')

                    # <Static value=<_ast.Dict object at 0x7fae34460e10> name=None at 7fae34460d10> -> __attrs_140386178040336
                    __attrs_140386178040336 = _static_140386178043408

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="content-core">\n                ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386127697488
                    __attrs_140386127697488 = _static_140386247937936

                    # <Value u'isManager' (97:36)> -> __condition
                    __token = 5548
                    try:
                        __zt_tmp = __attrs_140386127697488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('path', u'isManager', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div>\n                   ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386127697808
                        __attrs_140386127697808 = _static_140386247937936

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<p>')
                        __stream_140386127696848 = []
                        __append_140386127696848 = __stream_140386127696848.append
                        __append_140386127696848(u'\n                   Here is the full error message:\n                   ')
                        __msgid_140386127696848 = __re_whitespace(''.join(__stream_140386127696848)).strip()
                        if u'description_site_admin_full_error':
                            __append(translate(u'description_site_admin_full_error', mapping=None, default=__msgid_140386127696848, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</p>\n\n                   ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386127699472
                        __attrs_140386127699472 = _static_140386247937936

                        # <pre ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<pre>')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386127695952
                        __default_140386127695952 = _DEFAULT_MARKER

                        # <Value u'err_tb' (102:37)> -> __cache_140386127698320
                        __token = 5747
                        try:
                            __zt_tmp = __attrs_140386127699472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386127698320 = _static_140386186296528('path', u'err_tb', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'err_tb' (102:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae3145d310> -> __condition
                        __expression = __cache_140386127698320

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140386127698320
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</pre>\n                </div>')
                    __append(u'\n\n                ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386127698832
                    __attrs_140386127698832 = _static_140386247937936

                    # <Value u'not:isManager' (105:40)> -> __condition
                    __token = 5821
                    try:
                        __zt_tmp = __attrs_140386127698832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('not', u'isManager', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n                    ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386127696272
                        __attrs_140386127696272 = _static_140386247937936

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<p>')
                        __stream_140386135920720_site_admin = ''
                        __stream_140386127698768 = []
                        __append_140386127698768 = __stream_140386127698768.append
                        __append_140386127698768(u'\n                    If you are certain you have the correct web address but are encountering an error, please\n                    contact the ')
                        __stream_140386135920720_site_admin = []
                        __append_140386135920720_site_admin = __stream_140386135920720_site_admin.append

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386204876880
                        __attrs_140386204876880 = _static_140386247937936

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append_140386135920720_site_admin(u'<span>\n                    ')

                        # <Static value=<_ast.Dict object at 0x7fae35df8490> name=None at 7fae35df8350> -> __attrs_140386204880336
                        __attrs_140386204880336 = _static_140386204877968

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append_140386135920720_site_admin(u'<a')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386204877584
                        __default_140386204877584 = _DEFAULT_MARKER

                        # <Substitution u'string:${context/portal_url}/contact-info' (111:44)> -> __attr_href
                        __token = 6222
                        try:
                            __zt_tmp = __attrs_140386204880336
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140386186296528('string', u'${context/portal_url}/contact-info', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append_140386135920720_site_admin((u' href="%s"' % __attr_href))
                        __append_140386135920720_site_admin(u'>')
                        __stream_140386204877520 = []
                        __append_140386204877520 = __stream_140386204877520.append
                        __append_140386204877520(u'site administration')
                        __msgid_140386204877520 = __re_whitespace(''.join(__stream_140386204877520)).strip()
                        if u'label_site_admin':
                            __append_140386135920720_site_admin(translate(u'label_site_admin', mapping=None, default=__msgid_140386204877520, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append_140386135920720_site_admin(u'</a></span>')
                        __append_140386127698768(u'${site_admin}')
                        __stream_140386135920720_site_admin = ''.join(__stream_140386135920720_site_admin)
                        __append_140386127698768(u'.\n                    ')
                        __msgid_140386127698768 = __re_whitespace(''.join(__stream_140386127698768)).strip()
                        if u'description_site_error_mail_site_admin':
                            __append(translate(u'description_site_error_mail_site_admin', mapping={u'site_admin': __stream_140386135920720_site_admin, }, default=__msgid_140386127698768, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</p>\n                ')
                    __append(u'\n            </div>\n\n        ')
                if (__backup_isManager_140386176017232 is __marker):
                    del econtext['isManager']
                else:
                    econtext['isManager'] = __backup_isManager_140386176017232
                __append(u'\n\n')
                if (__backup_err_log_id_140386179295888 is __marker):
                    del econtext['err_log_id']
                else:
                    econtext['err_log_id'] = __backup_err_log_id_140386179295888
                if (__backup_err_tb_140386173480208 is __marker):
                    del econtext['err_tb']
                else:
                    econtext['err_tb'] = __backup_err_tb_140386173480208
                if (__backup_err_type_140386173878416 is __marker):
                    del econtext['err_type']
                else:
                    econtext['err_type'] = __backup_err_type_140386173878416
            _slots = econtext[u'__slot_main'] = _deque((__fill_main, ))

            # <Value u'context/@@main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_140386177529808
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140386186296528('path', u'context/@@main_template/macros/master', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140386120928704 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140386120928704
            __i18n_domain = __previous_i18n_domain_140386177528720
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }