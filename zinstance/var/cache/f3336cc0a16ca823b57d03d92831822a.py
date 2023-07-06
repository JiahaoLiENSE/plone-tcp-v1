# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.discussion-3.4.7-py2.7.egg/plone/app/discussion/browser/comments.pt'

__tokens = {46: (u'view/can_reply', 1, 46), 104: (u' view/is_discussion_allowe', 2, 42), 183: (u'd view/anonymous_discussion_allow', 3, 50), 261: (u'ed view/edit_comment_allo', 4, 41), 336: (u'wed view/delete_own_comment_all', 5, 45), 398: (u'Anon view/is_anon', 6, 25), 449: (u'eview view/can_', 7, 27), 496: (u'eplies python:view.get_replies(can', 8, 24), 566: (u'replies python:view.has_replies(ca', 9, 27), 643: (u'terImage view/show_commen', 10, 33), 699: (u'   errors options/state/getErro', 11, 20), 760: (u'     wtool context/@@plone_too', 12, 18), 825: (u' auth_token context/@@authenticator/t', 13, 22), 902: (u'python:isDiscussionAllowed or has_replies', 14, 26), 1025: (u'python:isAnon and not isAnonymousDiscussionAllowed', 18, 24), 1115: (u'view/login_action', 19, 37), 1554: (u'has_replies', 30, 24), 1449: (u"python: showCommenterImage and 'discussion showCommenterImage' or 'discussion'", 29, 31), 1611: (u'replies', 31, 43), 1690: (u'reply_dict/comment', 34, 35), 1749: (u' reply/getI', 35, 39), 1796: (u'h reply_dict/depth|python', 36, 33), 1857: (u"th python: depth > 10 and '10' or de", 37, 32), 1939: (u'url python:view.get_commenter_home_url(username=reply.author_usern', 38, 41), 2051: (u'link python:author_home_url and not i', 39, 40), 2131: (u't_url python:view.get_commenter_portrait(reply.author_use', 40, 36), 2231: (u"_state python:wtool.getInfoFor(reply, 'review_state', ", 41, 35), 2323: (u'canEdit python:view.can_edi', 42, 29), 2390: (u'anDelete python:view.can_dele', 43, 30), 2460: (u"olorclass python:lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else '", 44, 30), 2795: (u"python:canReview or review_state == 'published'", 47, 32), 2614: (u"python:'comment replyTreeLevel{depth} {state}'.format(depth= depth, state=colorclass(review_state))", 45, 39), 2750: (u' comment_i', 46, 35), 2903: (u'showCommenterImage', 49, 57), 2970: (u'has_author_link', 50, 46), 3039: (u'author_home_url', 51, 52), 3291: (u'portrait_url', 56, 50), 3354: (u' reply/author_nam', 57, 49), 3606: (u'not: has_author_link', 63, 40), 3673: (u'portrait_url', 64, 45), 3731: (u' reply/author_nam', 65, 44), 3931: (u'has_author_link', 71, 42), 4055: (u'author_home_url', 73, 48), 3988: (u'reply/author_name', 72, 40), 4187: (u'not: has_author_link', 76, 45), 4252: (u'reply/author_name', 77, 43), 4319: (u'not: reply/author_name', 78, 45), 4617: (u'python:view.format_time(reply.modification_date)', 83, 38), 4858: (u'reply/getText', 90, 49), 5156: (u'python:not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)', 97, 45), 5294: (u'string:${reply/absolute_url}/@@delete-own-comment', 98, 53), 5396: (u" python:view.can_delete_own(reply) and 'display: inline' or 'display: none", 99, 51), 5520: (u'd string:delete-${comment_i', 100, 47), 6147: (u'python:canDelete', 112, 45), 6218: (u'string:${reply/absolute_url}/@@moderate-delete-comment', 113, 53), 6322: (u' string:delete-${comment_id', 114, 48), 6768: (u'python:isEditCommentAllowed and canEdit', 123, 49), 7066: (u'auth_token', 127, 44), 7128: (u'string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', 128, 50), 7499: (u'not: auth_token', 134, 47), 7571: (u'string:${reply/absolute_url}/@@edit-comment', 135, 55), 7666: (u' string:edit-${comment_id', 136, 50), 8392: (u'canReview', 152, 45), 8452: (u'reply_dict/actions|nothing', 153, 49), 8632: (u' action/i', 155, 50), 8533: (u'string:${reply/absolute_url}/@@transmit-comment', 154, 53), 8691: (u'd string:${action/id}-${comment_i', 156, 47), 8823: (u'action/id', 157, 94), 9064: (u'action/title', 161, 57), 9384: (u'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', 170, 39), 9665: (u'python: has_replies and not isDiscussionAllowed', 178, 28), 9918: (u'python:has_replies and (isAnon and not isAnonymousDiscussionAllowed)', 187, 24), 10026: (u'view/login_action', 188, 37), 10355: (u'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', 197, 54), 10581: (u'view/comment_transform_message', 202, 28), 10780: (u'view/form/render', 207, 40)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140235428417936 = {u'type': u'submit', u'name': u'form.button.DeleteComment', u'value': u'Delete', u'class': u'destructive', }
_static_140235373419728 = {u'action': u'', u'class': u'commentactionsform', u'id': u'string:edit-${comment_id}', u'name': u'edit', u'method': u'get', }
_static_140235451441296 = {u'src': u'defaultUser.png', u'alt': u'', u'class': u'defaultuserimg', u'height': u'32', }
_static_140235428377104 = {u'type': u'hidden', u'name': u'workflow_action', u'value': u'action/id', }
_static_140235428378704 = {u'type': u'submit', u'name': u'form.button.TransmitComment', u'value': u'action/title', u'class': u'context', }
_static_140235374093200 = {u'class': u'commentActions', }
_static_140235427393296 = {u'id': u'commenting', u'class': u'reply', }
_static_140235427390224 = {u'type': u'submit', u'class': u'standalone loginbutton', u'value': u'Log in to add comments', }
_static_140235426046928 = {u'type': u'submit', u'name': u'form.button.DeleteComment', u'value': u'Delete', u'class': u'destructive', }
_static_140235374162704 = {u'class': u'commentImage', }
_static_140235424481808 = {u'class': u'reply', }
_static_140235428419280 = {u'action': u'', u'class': u'commentactionsform', u'id': u'string:delete-${comment_id}', u'name': u'delete', u'method': u'post', }
_static_140235373418960 = {u'action': u'', u'class': u'commentactionsform', u'id': u'string:${action/id}-${comment_id}', u'name': u'', u'method': u'get', }
_static_140235451443280 = {u'class': u'documentByLine', }
_static_140235373783632 = {u'class': u'commentBody', }
_static_140235423520592 = {u'class': u'context reply-to-comment-button hide allowMultiSubmit', }
_static_140235385277904 = {u'src': u'defaultUser.png', u'alt': u'', u'class': u'defaultuserimg', u'height': u'32', }
_static_140235373782032 = {u'class': u'commentDate', }
_static_140235423520272 = {u'href': u'string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', u'class': u'pat-plone-modal context commentactionsform', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235431285712 = {u'href': u'', }
_static_140235424466256 = {u'style': u"python:view.can_delete_own(reply) and 'display: inline' or 'display: none'", u'name': u'delete', u'id': u'string:delete-${comment_id}', u'method': u'post', u'action': u'', u'class': u'commentactionsform', }
_static_140235373351504 = {u'type': u'submit', u'class': u'standalone loginbutton', u'value': u'Log in to add comments', }
_static_140235489934800 = {}
_static_140235385245776 = {u'href': u'', }
_static_140235435449424 = __compile_zt_expr
_static_140235431390352 = {u'class': u'comment', u'id': u'comment_id', }
_static_140235385296976 = {u'class': u'discussion', }
_static_140235431259280 = {u'class': u'reply', }
_static_140235427392080 = {u'action': u'view/login_action', }
_static_140235385297808 = {u'action': u'view/login_action', }
_static_140235431388688 = {u'class': u'discreet', }
_static_140235357539600 = {u'type': u'submit', u'name': u'form.button.EditComment', u'value': u'Edit', u'class': u'context', }

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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235368755792
            __attrs_140235368755792 = _static_140235489934800
            __backup_userHasReplyPermission_140235432291600 = get('userHasReplyPermission', __marker)

            # <Value u'view/can_reply' (1:46)> -> __value
            __token = 46
            try:
                __zt_tmp = __attrs_140235368755792
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/can_reply', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['userHasReplyPermission'] = __value
            __backup_isDiscussionAllowed_140235431277968 = get('isDiscussionAllowed', __marker)

            # <Value u'view/is_discussion_allowed' (2:42)> -> __value
            __token = 104
            try:
                __zt_tmp = __attrs_140235368755792
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/is_discussion_allowed', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['isDiscussionAllowed'] = __value
            __backup_isAnonymousDiscussionAllowed_140235426070672 = get('isAnonymousDiscussionAllowed', __marker)

            # <Value u'view/anonymous_discussion_allowed' (3:50)> -> __value
            __token = 183
            try:
                __zt_tmp = __attrs_140235368755792
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/anonymous_discussion_allowed', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['isAnonymousDiscussionAllowed'] = __value
            __backup_isEditCommentAllowed_140235373358608 = get('isEditCommentAllowed', __marker)

            # <Value u'view/edit_comment_allowed' (4:41)> -> __value
            __token = 261
            try:
                __zt_tmp = __attrs_140235368755792
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/edit_comment_allowed', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['isEditCommentAllowed'] = __value
            __backup_isDeleteOwnCommentAllowed_140235431277136 = get('isDeleteOwnCommentAllowed', __marker)

            # <Value u'view/delete_own_comment_allowed' (5:45)> -> __value
            __token = 336
            try:
                __zt_tmp = __attrs_140235368755792
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/delete_own_comment_allowed', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['isDeleteOwnCommentAllowed'] = __value
            __backup_isAnon_140235431277392 = get('isAnon', __marker)

            # <Value u'view/is_anonymous' (6:25)> -> __value
            __token = 398
            try:
                __zt_tmp = __attrs_140235368755792
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/is_anonymous', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['isAnon'] = __value
            __backup_canReview_140235431280528 = get('canReview', __marker)

            # <Value u'view/can_review' (7:27)> -> __value
            __token = 449
            try:
                __zt_tmp = __attrs_140235368755792
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/can_review', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['canReview'] = __value
            __backup_replies_140235368759184 = get('replies', __marker)

            # <Value u'python:view.get_replies(canReview)' (8:24)> -> __value
            __token = 496
            try:
                __zt_tmp = __attrs_140235368755792
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u'view.get_replies(canReview)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['replies'] = __value
            __backup_has_replies_140235431278096 = get('has_replies', __marker)

            # <Value u'python:view.has_replies(canReview)' (9:27)> -> __value
            __token = 566
            try:
                __zt_tmp = __attrs_140235368755792
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u'view.has_replies(canReview)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['has_replies'] = __value
            __backup_showCommenterImage_140235451444368 = get('showCommenterImage', __marker)

            # <Value u'view/show_commenter_image' (10:33)> -> __value
            __token = 643
            try:
                __zt_tmp = __attrs_140235368755792
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/show_commenter_image', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['showCommenterImage'] = __value
            __backup_errors_140235431258256 = get('errors', __marker)

            # <Value u'options/state/getErrors|nothing' (11:20)> -> __value
            __token = 699
            try:
                __zt_tmp = __attrs_140235368755792
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'options/state/getErrors|nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['errors'] = __value
            __backup_wtool_140235373356752 = get('wtool', __marker)

            # <Value u'context/@@plone_tools/workflow' (12:18)> -> __value
            __token = 760
            try:
                __zt_tmp = __attrs_140235368755792
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'context/@@plone_tools/workflow', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['wtool'] = __value
            __backup_auth_token_140235426088336 = get('auth_token', __marker)

            # <Value u'context/@@authenticator/token|nothing' (13:22)> -> __value
            __token = 825
            try:
                __zt_tmp = __attrs_140235368755792
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'context/@@authenticator/token|nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['auth_token'] = __value

            # <Value u'python:isDiscussionAllowed or has_replies' (14:26)> -> __condition
            __token = 902
            try:
                __zt_tmp = __attrs_140235368755792
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('python', u'isDiscussionAllowed or has_replies', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140235431256208 = __i18n_domain
                __i18n_domain = u'plone'
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1b10ac90> name=None at 7f8b1b10a9d0> -> __attrs_140235426102480
                __attrs_140235426102480 = _static_140235431259280

                # <Value u'python:isAnon and not isAnonymousDiscussionAllowed' (18:24)> -> __condition
                __token = 1025
                try:
                    __zt_tmp = __attrs_140235426102480
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('python', u'isAnon and not isAnonymousDiscussionAllowed', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="reply">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b18535b90> name=None at 7f8b18535810> -> __attrs_140235431279632
                    __attrs_140235431279632 = _static_140235385297808

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<form')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235451401360
                    __default_140235451401360 = _DEFAULT_MARKER

                    # <Substitution u'view/login_action' (19:37)> -> __attr_action
                    __token = 1115
                    try:
                        __zt_tmp = __attrs_140235431279632
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_140235435449424('path', u'view/login_action', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((u' action="%s"' % __attr_action))
                    __append(u'>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8b179d1250> name=None at 7f8b17a93f10> -> __attrs_140235373351632
                    __attrs_140235373351632 = _static_140235373351504

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input class="standalone loginbutton" type="submit"')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373351888
                    __default_140235373351888 = _DEFAULT_MARKER

                    # <Translate msgid=u'label_login_to_add_comments' node=<_ast.Str object at 0x7f8b179d1990> at 7f8b179d1190> -> __attr_value
                    __attr_value = u'Log in to add comments'
                    __attr_value = translate(u'label_login_to_add_comments', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u' />\n        </form>\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b18535850> name=None at 7f8b1b10f990> -> __attrs_140235373351760
                __attrs_140235373351760 = _static_140235385296976

                # <Value u'has_replies' (30:24)> -> __condition
                __token = 1554
                try:
                    __zt_tmp = __attrs_140235373351760
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'has_replies', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373351696
                    __default_140235373351696 = _DEFAULT_MARKER

                    # <Substitution u"python: showCommenterImage and 'discussion showCommenterImage' or 'discussion'" (29:31)> -> __attr_class
                    __token = 1449
                    try:
                        __zt_tmp = __attrs_140235373351760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140235435449424('python', u" showCommenterImage and 'discussion showCommenterImage' or 'discussion'", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', u'discussion', _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235431389520
                    __attrs_140235431389520 = _static_140235489934800
                    __backup_reply_dict_140235424467024 = get('reply_dict', __marker)

                    # <Value u'replies' (31:43)> -> __iterator
                    __token = 1611
                    try:
                        __zt_tmp = __attrs_140235431389520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140235435449424('path', u'replies', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    (__iterator, ____index_140235431389008, ) = getitem('repeat')(u'reply_dict', __iterator)
                    econtext['reply_dict'] = None
                    for __item in __iterator:
                        econtext['reply_dict'] = __item
                        __append(u'\n\n            ')

                        # <Static value=<_ast.Dict object at 0x7f8b1b12ac90> name=None at 7f8b1b12a2d0> -> __attrs_140235431387472
                        __attrs_140235431387472 = _static_140235431390352
                        __backup_reply_140235432289808 = get('reply', __marker)

                        # <Value u'reply_dict/comment' (34:35)> -> __value
                        __token = 1690
                        try:
                            __zt_tmp = __attrs_140235431387472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140235435449424('path', u'reply_dict/comment', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        econtext['reply'] = __value
                        __backup_comment_id_140235368754768 = get('comment_id', __marker)

                        # <Value u'reply/getId' (35:39)> -> __value
                        __token = 1749
                        try:
                            __zt_tmp = __attrs_140235431387472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140235435449424('path', u'reply/getId', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        econtext['comment_id'] = __value
                        __backup_depth_140235374113296 = get('depth', __marker)

                        # <Value u'reply_dict/depth|python:0' (36:33)> -> __value
                        __token = 1796
                        try:
                            __zt_tmp = __attrs_140235431387472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140235435449424('path', u'reply_dict/depth|python:0', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        econtext['depth'] = __value
                        __backup_depth_140235374162576 = get('depth', __marker)

                        # <Value u"python: depth > 10 and '10' or depth" (37:32)> -> __value
                        __token = 1857
                        try:
                            __zt_tmp = __attrs_140235431387472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140235435449424('python', u" depth > 10 and '10' or depth", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        econtext['depth'] = __value
                        __backup_author_home_url_140235377023568 = get('author_home_url', __marker)

                        # <Value u'python:view.get_commenter_home_url(username=reply.author_username)' (38:41)> -> __value
                        __token = 1939
                        try:
                            __zt_tmp = __attrs_140235431387472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140235435449424('python', u'view.get_commenter_home_url(username=reply.author_username)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        econtext['author_home_url'] = __value
                        __backup_has_author_link_140235385327504 = get('has_author_link', __marker)

                        # <Value u'python:author_home_url and not isAnon' (39:40)> -> __value
                        __token = 2051
                        try:
                            __zt_tmp = __attrs_140235431387472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140235435449424('python', u'author_home_url and not isAnon', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        econtext['has_author_link'] = __value
                        __backup_portrait_url_140235424465808 = get('portrait_url', __marker)

                        # <Value u'python:view.get_commenter_portrait(reply.author_username)' (40:36)> -> __value
                        __token = 2131
                        try:
                            __zt_tmp = __attrs_140235431387472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140235435449424('python', u'view.get_commenter_portrait(reply.author_username)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        econtext['portrait_url'] = __value
                        __backup_review_state_140235426069712 = get('review_state', __marker)

                        # <Value u"python:wtool.getInfoFor(reply, 'review_state', 'none')" (41:35)> -> __value
                        __token = 2231
                        try:
                            __zt_tmp = __attrs_140235431387472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140235435449424('python', u"wtool.getInfoFor(reply, 'review_state', 'none')", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        econtext['review_state'] = __value
                        __backup_canEdit_140235431256848 = get('canEdit', __marker)

                        # <Value u'python:view.can_edit(reply)' (42:29)> -> __value
                        __token = 2323
                        try:
                            __zt_tmp = __attrs_140235431387472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140235435449424('python', u'view.can_edit(reply)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        econtext['canEdit'] = __value
                        __backup_canDelete_140235431388752 = get('canDelete', __marker)

                        # <Value u'python:view.can_delete(reply)' (43:30)> -> __value
                        __token = 2390
                        try:
                            __zt_tmp = __attrs_140235431387472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140235435449424('python', u'view.can_delete(reply)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        econtext['canDelete'] = __value
                        __backup_colorclass_140235431388176 = get('colorclass', __marker)

                        # <Value u"python:lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else 'state-'+x)" (44:30)> -> __value
                        __token = 2460
                        try:
                            __zt_tmp = __attrs_140235431387472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140235435449424('python', u"lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else 'state-'+x)", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        econtext['colorclass'] = __value

                        # <Value u"python:canReview or review_state == 'published'" (47:32)> -> __condition
                        __token = 2795
                        try:
                            __zt_tmp = __attrs_140235431387472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140235435449424('python', u"canReview or review_state == 'published'", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div')

                            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431389904
                            __default_140235431389904 = _DEFAULT_MARKER

                            # <Substitution u"python:'comment replyTreeLevel{depth} {state}'.format(depth= depth, state=colorclass(review_state))" (45:39)> -> __attr_class
                            __token = 2614
                            try:
                                __zt_tmp = __attrs_140235431387472
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_140235435449424('python', u"'comment replyTreeLevel{depth} {state}'.format(depth= depth, state=colorclass(review_state))", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', u'comment', _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((u' class="%s"' % __attr_class))

                            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431387344
                            __default_140235431387344 = _DEFAULT_MARKER

                            # <Substitution u'comment_id' (46:35)> -> __attr_id
                            __token = 2750
                            try:
                                __zt_tmp = __attrs_140235431387472
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_id = _static_140235435449424('path', u'comment_id', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_id is not None):
                                __append((u' id="%s"' % __attr_id))
                            __append(u'>\n\n                ')

                            # <Static value=<_ast.Dict object at 0x7f8b17a97310> name=None at 7f8b17a97450> -> __attrs_140235374165776
                            __attrs_140235374165776 = _static_140235374162704

                            # <Value u'showCommenterImage' (49:57)> -> __condition
                            __token = 2903
                            try:
                                __zt_tmp = __attrs_140235374165776
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140235435449424('path', u'showCommenterImage', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<div class="commentImage">\n                    ')

                                # <Static value=<_ast.Dict object at 0x7f8b18529050> name=None at 7f8b18529410> -> __attrs_140235385247248
                                __attrs_140235385247248 = _static_140235385245776

                                # <Value u'has_author_link' (50:46)> -> __condition
                                __token = 2970
                                try:
                                    __zt_tmp = __attrs_140235385247248
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140235435449424('path', u'has_author_link', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                if __condition:

                                    # <a ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<a')

                                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385245904
                                    __default_140235385245904 = _DEFAULT_MARKER

                                    # <Substitution u'author_home_url' (51:52)> -> __attr_href
                                    __token = 3039
                                    try:
                                        __zt_tmp = __attrs_140235385247248
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_href = _static_140235435449424('path', u'author_home_url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                    __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                                    if (__attr_href is not None):
                                        __append((u' href="%s"' % __attr_href))
                                    __append(u'>\n                         ')

                                    # <Static value=<_ast.Dict object at 0x7f8b1c44a090> name=None at 7f8b1c44a510> -> __attrs_140235385277584
                                    __attrs_140235385277584 = _static_140235451441296

                                    # <img ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<img')

                                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235451444816
                                    __default_140235451444816 = _DEFAULT_MARKER

                                    # <Substitution u'portrait_url' (56:50)> -> __attr_src
                                    __token = 3291
                                    try:
                                        __zt_tmp = __attrs_140235385277584
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_src = _static_140235435449424('path', u'portrait_url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                    __attr_src = __quote(__attr_src, '"', '&quot;', u'defaultUser.png', _DEFAULT_MARKER)
                                    if (__attr_src is not None):
                                        __append((u' src="%s"' % __attr_src))

                                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235451441872
                                    __default_140235451441872 = _DEFAULT_MARKER

                                    # <Substitution u'reply/author_name' (57:49)> -> __attr_alt
                                    __token = 3354
                                    try:
                                        __zt_tmp = __attrs_140235385277584
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_alt = _static_140235435449424('path', u'reply/author_name', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                    __attr_alt = __quote(__attr_alt, '"', '&quot;', u'', _DEFAULT_MARKER)
                                    if (__attr_alt is not None):
                                        __append((u' alt="%s"' % __attr_alt))
                                    __append(u' class="defaultuserimg" height="32" />\n                    </a>')
                                __append(u'\n                    ')

                                # <Static value=<_ast.Dict object at 0x7f8b18530dd0> name=None at 7f8b1c44ab90> -> __attrs_140235385277136
                                __attrs_140235385277136 = _static_140235385277904

                                # <Value u'not: has_author_link' (63:40)> -> __condition
                                __token = 3606
                                try:
                                    __zt_tmp = __attrs_140235385277136
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140235435449424('not', u' has_author_link', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                if __condition:

                                    # <img ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<img')

                                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385277456
                                    __default_140235385277456 = _DEFAULT_MARKER

                                    # <Substitution u'portrait_url' (64:45)> -> __attr_src
                                    __token = 3673
                                    try:
                                        __zt_tmp = __attrs_140235385277136
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_src = _static_140235435449424('path', u'portrait_url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                    __attr_src = __quote(__attr_src, '"', '&quot;', u'defaultUser.png', _DEFAULT_MARKER)
                                    if (__attr_src is not None):
                                        __append((u' src="%s"' % __attr_src))

                                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385278416
                                    __default_140235385278416 = _DEFAULT_MARKER

                                    # <Substitution u'reply/author_name' (65:44)> -> __attr_alt
                                    __token = 3731
                                    try:
                                        __zt_tmp = __attrs_140235385277136
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_alt = _static_140235435449424('path', u'reply/author_name', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                    __attr_alt = __quote(__attr_alt, '"', '&quot;', u'', _DEFAULT_MARKER)
                                    if (__attr_alt is not None):
                                        __append((u' alt="%s"' % __attr_alt))
                                    __append(u' class="defaultuserimg" height="32" />')
                                __append(u'\n                </div>')
                            __append(u'\n\n                ')

                            # <Static value=<_ast.Dict object at 0x7f8b1c44a850> name=None at 7f8b17a978d0> -> __attrs_140235385275792
                            __attrs_140235385275792 = _static_140235451443280

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="documentByLine">\n                    ')

                            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235431287888
                            __attrs_140235431287888 = _static_140235489934800
                            __append(u'\n                        ')

                            # <Static value=<_ast.Dict object at 0x7f8b1b1113d0> name=None at 7f8b1b111790> -> __attrs_140235431287376
                            __attrs_140235431287376 = _static_140235431285712

                            # <Value u'has_author_link' (71:42)> -> __condition
                            __token = 3931
                            try:
                                __zt_tmp = __attrs_140235431287376
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140235435449424('path', u'has_author_link', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                            if __condition:

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<a')

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431285200
                                __default_140235431285200 = _DEFAULT_MARKER

                                # <Substitution u'author_home_url' (73:48)> -> __attr_href
                                __token = 4055
                                try:
                                    __zt_tmp = __attrs_140235431287376
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_140235435449424('path', u'author_home_url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((u' href="%s"' % __attr_href))
                                __append(u'>')

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431288016
                                __default_140235431288016 = _DEFAULT_MARKER

                                # <Value u'reply/author_name' (72:40)> -> __cache_140235431286224
                                __token = 3988
                                try:
                                    __zt_tmp = __attrs_140235431287376
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140235431286224 = _static_140235435449424('path', u'reply/author_name', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                                # <BinOp left=<Value u'reply/author_name' (72:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1b111b10> -> __condition
                                __expression = __cache_140235431286224

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(u'\n                            Poster Name\n                        ')
                                else:
                                    __content = __cache_140235431286224
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</a>')
                            __append(u'\n                        ')

                            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373783056
                            __attrs_140235373783056 = _static_140235489934800

                            # <Value u'not: has_author_link' (76:45)> -> __condition
                            __token = 4187
                            try:
                                __zt_tmp = __attrs_140235373783056
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140235435449424('not', u' has_author_link', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                            if __condition:

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431285584
                                __default_140235431285584 = _DEFAULT_MARKER

                                # <Value u'reply/author_name' (77:43)> -> __cache_140235431285776
                                __token = 4252
                                try:
                                    __zt_tmp = __attrs_140235373783056
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140235431285776 = _static_140235435449424('path', u'reply/author_name', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                                # <BinOp left=<Value u'reply/author_name' (77:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1b111a10> -> __condition
                                __expression = __cache_140235431285776

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:

                                    # <span ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<span />')
                                else:
                                    __content = __cache_140235431285776
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                            __append(u'\n                        ')

                            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373782480
                            __attrs_140235373782480 = _static_140235489934800

                            # <Value u'not: reply/author_name' (78:45)> -> __condition
                            __token = 4319
                            try:
                                __zt_tmp = __attrs_140235373782480
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140235435449424('not', u' reply/author_name', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span>')
                                __stream_140235373781648 = []
                                __append_140235373781648 = __stream_140235373781648.append
                                __append_140235373781648(u'Anonymous')
                                __msgid_140235373781648 = __re_whitespace(''.join(__stream_140235373781648)).strip()
                                if u'label_anonymous':
                                    __append(translate(u'label_anonymous', mapping=None, default=__msgid_140235373781648, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                                __append(u'</span>')
                            __append(u'\n                    \n                    ')

                            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373782288
                            __attrs_140235373782288 = _static_140235489934800
                            __stream_140235431285328 = []
                            __append_140235431285328 = __stream_140235431285328.append
                            __append_140235431285328(u'says:')
                            __msgid_140235431285328 = __re_whitespace(''.join(__stream_140235431285328)).strip()
                            if u'label_says':
                                __append(translate(u'label_says', mapping=None, default=__msgid_140235431285328, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'\n                    ')

                            # <Static value=<_ast.Dict object at 0x7f8b17a3a410> name=None at 7f8b17a3ad90> -> __attrs_140235373784080
                            __attrs_140235373784080 = _static_140235373782032

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="commentDate">')

                            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373781776
                            __default_140235373781776 = _DEFAULT_MARKER

                            # <Value u'python:view.format_time(reply.modification_date)' (83:38)> -> __cache_140235431288400
                            __token = 4617
                            try:
                                __zt_tmp = __attrs_140235373784080
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140235431288400 = _static_140235435449424('python', u'view.format_time(reply.modification_date)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                            # <BinOp left=<Value u'python:view.format_time(reply.modification_date)' (83:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17a3a610> -> __condition
                            __expression = __cache_140235431288400

                            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u'\n                         8/23/2001 12:40:44 PM\n                    ')
                            else:
                                __content = __cache_140235431288400
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</div>\n                </div>\n\n                ')

                            # <Static value=<_ast.Dict object at 0x7f8b17a3aa50> name=None at 7f8b185302d0> -> __attrs_140235374092368
                            __attrs_140235374092368 = _static_140235373783632

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="commentBody">\n\n                    ')

                            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374096080
                            __attrs_140235374096080 = _static_140235489934800

                            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235374093648
                            __default_140235374093648 = _DEFAULT_MARKER

                            # <Value u'reply/getText' (90:49)> -> __cache_140235374093776
                            __token = 4858
                            try:
                                __zt_tmp = __attrs_140235374096080
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140235374093776 = _static_140235435449424('path', u'reply/getText', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                            # <BinOp left=<Value u'reply/getText' (90:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17a86950> -> __condition
                            __expression = __cache_140235374093776

                            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span />')
                            else:
                                __content = __cache_140235374093776
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'\n\n                    ')

                            # <Static value=<_ast.Dict object at 0x7f8b17a86390> name=None at 7f8b17a864d0> -> __attrs_140235374095056
                            __attrs_140235374095056 = _static_140235374093200

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="commentActions">\n                        ')

                            # <Static value=<_ast.Dict object at 0x7f8b1aa90550> name=None at 7f8b1aa90f10> -> __attrs_140235424467472
                            __attrs_140235424467472 = _static_140235424466256

                            # <Value u'python:not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)' (97:45)> -> __condition
                            __token = 5156
                            try:
                                __zt_tmp = __attrs_140235424467472
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140235435449424('python', u'not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                            if __condition:

                                # <form ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<form name="delete"')

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235424467152
                                __default_140235424467152 = _DEFAULT_MARKER

                                # <Substitution u'string:${reply/absolute_url}/@@delete-own-comment' (98:53)> -> __attr_action
                                __token = 5294
                                try:
                                    __zt_tmp = __attrs_140235424467472
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_action = _static_140235435449424('string', u'${reply/absolute_url}/@@delete-own-comment', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                __attr_action = __quote(__attr_action, '"', '&quot;', u'', _DEFAULT_MARKER)
                                if (__attr_action is not None):
                                    __append((u' action="%s"' % __attr_action))
                                __append(u' method="post" class="commentactionsform"')

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235424466704
                                __default_140235424466704 = _DEFAULT_MARKER

                                # <Substitution u"python:view.can_delete_own(reply) and 'display: inline' or 'display: none'" (99:51)> -> __attr_style
                                __token = 5396
                                try:
                                    __zt_tmp = __attrs_140235424467472
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_style = _static_140235435449424('python', u"view.can_delete_own(reply) and 'display: inline' or 'display: none'", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_style is not None):
                                    __append((u' style="%s"' % __attr_style))

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235424467216
                                __default_140235424467216 = _DEFAULT_MARKER

                                # <Substitution u'string:delete-${comment_id}' (100:47)> -> __attr_id
                                __token = 5520
                                try:
                                    __zt_tmp = __attrs_140235424467472
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_id = _static_140235435449424('string', u'delete-${comment_id}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_id is not None):
                                    __append((u' id="%s"' % __attr_id))
                                __append(u'>\n                            ')

                                # <Static value=<_ast.Dict object at 0x7f8b1ae55190> name=None at 7f8b1ae55f10> -> __attrs_140235428418320
                                __attrs_140235428418320 = _static_140235428417936

                                # <input ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<input name="form.button.DeleteComment" class="destructive" type="submit"')

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235428420112
                                __default_140235428420112 = _DEFAULT_MARKER

                                # <Translate msgid=u'label_delete' node=<_ast.Str object at 0x7f8b1ae55d10> at 7f8b1ae55350> -> __attr_value
                                __attr_value = u'Delete'
                                __attr_value = translate(u'label_delete', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                if (__attr_value is not None):
                                    __append((u' value="%s"' % __attr_value))
                                __append(u' />\n                        </form>')
                            __append(u'\n                        ')

                            # <Static value=<_ast.Dict object at 0x7f8b1ae556d0> name=None at 7f8b1ae55690> -> __attrs_140235426049424
                            __attrs_140235426049424 = _static_140235428419280

                            # <Value u'python:canDelete' (112:45)> -> __condition
                            __token = 6147
                            try:
                                __zt_tmp = __attrs_140235426049424
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140235435449424('python', u'canDelete', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                            if __condition:

                                # <form ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<form name="delete"')

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235426047696
                                __default_140235426047696 = _DEFAULT_MARKER

                                # <Substitution u'string:${reply/absolute_url}/@@moderate-delete-comment' (113:53)> -> __attr_action
                                __token = 6218
                                try:
                                    __zt_tmp = __attrs_140235426049424
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_action = _static_140235435449424('string', u'${reply/absolute_url}/@@moderate-delete-comment', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                __attr_action = __quote(__attr_action, '"', '&quot;', u'', _DEFAULT_MARKER)
                                if (__attr_action is not None):
                                    __append((u' action="%s"' % __attr_action))
                                __append(u' method="post" class="commentactionsform"')

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235426047568
                                __default_140235426047568 = _DEFAULT_MARKER

                                # <Substitution u'string:delete-${comment_id}' (114:48)> -> __attr_id
                                __token = 6322
                                try:
                                    __zt_tmp = __attrs_140235426049424
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_id = _static_140235435449424('string', u'delete-${comment_id}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_id is not None):
                                    __append((u' id="%s"' % __attr_id))
                                __append(u'>\n                            ')

                                # <Static value=<_ast.Dict object at 0x7f8b1ac123d0> name=None at 7f8b1ac12490> -> __attrs_140235423520784
                                __attrs_140235423520784 = _static_140235426046928

                                # <input ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<input name="form.button.DeleteComment" class="destructive" type="submit"')

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235423519888
                                __default_140235423519888 = _DEFAULT_MARKER

                                # <Translate msgid=u'label_delete' node=<_ast.Str object at 0x7f8b1a9a9e50> at 7f8b1a9a95d0> -> __attr_value
                                __attr_value = u'Delete'
                                __attr_value = translate(u'label_delete', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                if (__attr_value is not None):
                                    __append((u' value="%s"' % __attr_value))
                                __append(u' />\n                        </form>')
                            __append(u'\n\n                        ')

                            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235423521104
                            __attrs_140235423521104 = _static_140235489934800

                            # <Value u'python:isEditCommentAllowed and canEdit' (123:49)> -> __condition
                            __token = 6768
                            try:
                                __zt_tmp = __attrs_140235423521104
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140235435449424('python', u'isEditCommentAllowed and canEdit', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                            if __condition:
                                __append(u"\n                          <!-- plone 5 will have auth_token available\n                               so we'll use modal pattern -->\n                          ")

                                # <Static value=<_ast.Dict object at 0x7f8b1a9a9610> name=None at 7f8b1a9a9cd0> -> __attrs_140235373417168
                                __attrs_140235373417168 = _static_140235423520272

                                # <Value u'auth_token' (127:44)> -> __condition
                                __token = 7066
                                try:
                                    __zt_tmp = __attrs_140235373417168
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140235435449424('path', u'auth_token', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                if __condition:

                                    # <a ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<a class="pat-plone-modal context commentactionsform"')

                                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373417808
                                    __default_140235373417808 = _DEFAULT_MARKER

                                    # <Substitution u'string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}' (128:50)> -> __attr_href
                                    __token = 7128
                                    try:
                                        __zt_tmp = __attrs_140235373417168
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_href = _static_140235435449424('string', u'${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_href is not None):
                                        __append((u' href="%s"' % __attr_href))
                                    __append(u'>')
                                    __stream_140235423519312 = []
                                    __append_140235423519312 = __stream_140235423519312.append
                                    __append_140235423519312(u'Edit')
                                    __msgid_140235423519312 = __re_whitespace(''.join(__stream_140235423519312)).strip()
                                    if u'Edit':
                                        __append(translate(u'Edit', mapping=None, default=__msgid_140235423519312, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                                    __append(u'</a>')
                                __append(u'\n                          ')

                                # <Static value=<_ast.Dict object at 0x7f8b179e1cd0> name=None at 7f8b179e15d0> -> __attrs_140235357536592
                                __attrs_140235357536592 = _static_140235373419728

                                # <Value u'not: auth_token' (134:47)> -> __condition
                                __token = 7499
                                try:
                                    __zt_tmp = __attrs_140235357536592
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140235435449424('not', u' auth_token', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                if __condition:

                                    # <form ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<form name="edit"')

                                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373417296
                                    __default_140235373417296 = _DEFAULT_MARKER

                                    # <Substitution u'string:${reply/absolute_url}/@@edit-comment' (135:55)> -> __attr_action
                                    __token = 7571
                                    try:
                                        __zt_tmp = __attrs_140235357536592
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_action = _static_140235435449424('string', u'${reply/absolute_url}/@@edit-comment', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                    __attr_action = __quote(__attr_action, '"', '&quot;', u'', _DEFAULT_MARKER)
                                    if (__attr_action is not None):
                                        __append((u' action="%s"' % __attr_action))
                                    __append(u' method="get" class="commentactionsform"')

                                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373417552
                                    __default_140235373417552 = _DEFAULT_MARKER

                                    # <Substitution u'string:edit-${comment_id}' (136:50)> -> __attr_id
                                    __token = 7666
                                    try:
                                        __zt_tmp = __attrs_140235357536592
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_140235435449424('string', u'edit-${comment_id}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((u' id="%s"' % __attr_id))
                                    __append(u'>\n                              ')

                                    # <Static value=<_ast.Dict object at 0x7f8b16abcd10> name=None at 7f8b16abcd90> -> __attrs_140235357539920
                                    __attrs_140235357539920 = _static_140235357539600

                                    # <input ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<input name="form.button.EditComment" class="context" type="submit"')

                                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235357539344
                                    __default_140235357539344 = _DEFAULT_MARKER

                                    # <Translate msgid=u'label_edit' node=<_ast.Str object at 0x7f8b16abc250> at 7f8b16abc750> -> __attr_value
                                    __attr_value = u'Edit'
                                    __attr_value = translate(u'label_edit', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                    if (__attr_value is not None):
                                        __append((u' value="%s"' % __attr_value))
                                    __append(u' />\n                          </form>')
                                __append(u'\n                        ')
                            __append(u"\n\n\n                        <!-- Workflow actions (e.g. 'publish') -->\n                        ")

                            # <Static value=<_ast.Dict object at 0x7f8b179e19d0> name=None at 7f8b179e1fd0> -> __attrs_140235451428368
                            __attrs_140235451428368 = _static_140235373418960

                            # <Value u'canReview' (152:45)> -> __condition
                            __token = 8392
                            try:
                                __zt_tmp = __attrs_140235451428368
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140235435449424('path', u'canReview', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                            if __condition:
                                __backup_action_140235385246288 = get('action', __marker)

                                # <Value u'reply_dict/actions|nothing' (153:49)> -> __iterator
                                __token = 8452
                                try:
                                    __zt_tmp = __attrs_140235451428368
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __iterator = _static_140235435449424('path', u'reply_dict/actions|nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                (__iterator, ____index_140235428379408, ) = getitem('repeat')(u'action', __iterator)
                                econtext['action'] = None
                                for __item in __iterator:
                                    econtext['action'] = __item

                                    # <form ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<form')

                                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235451425296
                                    __default_140235451425296 = _DEFAULT_MARKER

                                    # <Substitution u'action/id' (155:50)> -> __attr_name
                                    __token = 8632
                                    try:
                                        __zt_tmp = __attrs_140235451428368
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_name = _static_140235435449424('path', u'action/id', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                    __attr_name = __quote(__attr_name, '"', '&quot;', u'', _DEFAULT_MARKER)
                                    if (__attr_name is not None):
                                        __append((u' name="%s"' % __attr_name))

                                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235451426320
                                    __default_140235451426320 = _DEFAULT_MARKER

                                    # <Substitution u'string:${reply/absolute_url}/@@transmit-comment' (154:53)> -> __attr_action
                                    __token = 8533
                                    try:
                                        __zt_tmp = __attrs_140235451428368
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_action = _static_140235435449424('string', u'${reply/absolute_url}/@@transmit-comment', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                    __attr_action = __quote(__attr_action, '"', '&quot;', u'', _DEFAULT_MARKER)
                                    if (__attr_action is not None):
                                        __append((u' action="%s"' % __attr_action))
                                    __append(u' method="get" class="commentactionsform"')

                                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235451427472
                                    __default_140235451427472 = _DEFAULT_MARKER

                                    # <Substitution u'string:${action/id}-${comment_id}' (156:47)> -> __attr_id
                                    __token = 8691
                                    try:
                                        __zt_tmp = __attrs_140235451428368
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_140235435449424('string', u'${action/id}-${comment_id}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((u' id="%s"' % __attr_id))
                                    __append(u'>\n                            ')

                                    # <Static value=<_ast.Dict object at 0x7f8b1ae4b210> name=None at 7f8b1ae4b290> -> __attrs_140235428380240
                                    __attrs_140235428380240 = _static_140235428377104

                                    # <input ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<input type="hidden" name="workflow_action"')

                                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235428380368
                                    __default_140235428380368 = _DEFAULT_MARKER

                                    # <Substitution u'action/id' (157:94)> -> __attr_value
                                    __token = 8823
                                    try:
                                        __zt_tmp = __attrs_140235428380240
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_value = _static_140235435449424('path', u'action/id', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_value is not None):
                                        __append((u' value="%s"' % __attr_value))
                                    __append(u' />\n                            ')

                                    # <Static value=<_ast.Dict object at 0x7f8b1ae4b850> name=None at 7f8b1ae4bdd0> -> __attrs_140235424484880
                                    __attrs_140235424484880 = _static_140235428378704

                                    # <input ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<input name="form.button.TransmitComment" class="context" type="submit"')

                                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235424482960
                                    __default_140235424482960 = _DEFAULT_MARKER

                                    # <Translate msgid=None node=<Substitution u'action/title' (161:57)> at 7f8b1aa94d10> -> __attr_value

                                    # <Substitution u'action/title' (161:57)> -> __attr_value
                                    __token = 9064
                                    try:
                                        __zt_tmp = __attrs_140235424484880
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_value = _static_140235435449424('path', u'action/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                                    __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                    if (__attr_value is not None):
                                        __append((u' value="%s"' % __attr_value))
                                    __append(u' />\n                        </form>')
                                    ____index_140235428379408 -= 1
                                    if (____index_140235428379408 > 0):
                                        __append('\n                        ')
                                if (__backup_action_140235385246288 is __marker):
                                    del econtext['action']
                                else:
                                    econtext['action'] = __backup_action_140235385246288
                            __append(u'\n                    </div>\n\n\n                </div>\n                ')

                            # <Static value=<_ast.Dict object at 0x7f8b1a9a9750> name=None at 7f8b17a86d10> -> __attrs_140235424482192
                            __attrs_140235424482192 = _static_140235423520592

                            # <Value u'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)' (170:39)> -> __condition
                            __token = 9384
                            try:
                                __zt_tmp = __attrs_140235424482192
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140235435449424('python', u'isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                            if __condition:

                                # <button ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<button class="context reply-to-comment-button hide allowMultiSubmit">')
                                __stream_140235374094800 = []
                                __append_140235374094800 = __stream_140235374094800.append
                                __append_140235374094800(u'\n                    Reply\n                ')
                                __msgid_140235374094800 = __re_whitespace(''.join(__stream_140235374094800)).strip()
                                if u'label_reply':
                                    __append(translate(u'label_reply', mapping=None, default=__msgid_140235374094800, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                                __append(u'</button>')
                            __append(u'\n            </div>')
                        if (__backup_colorclass_140235431388176 is __marker):
                            del econtext['colorclass']
                        else:
                            econtext['colorclass'] = __backup_colorclass_140235431388176
                        if (__backup_canDelete_140235431388752 is __marker):
                            del econtext['canDelete']
                        else:
                            econtext['canDelete'] = __backup_canDelete_140235431388752
                        if (__backup_canEdit_140235431256848 is __marker):
                            del econtext['canEdit']
                        else:
                            econtext['canEdit'] = __backup_canEdit_140235431256848
                        if (__backup_review_state_140235426069712 is __marker):
                            del econtext['review_state']
                        else:
                            econtext['review_state'] = __backup_review_state_140235426069712
                        if (__backup_portrait_url_140235424465808 is __marker):
                            del econtext['portrait_url']
                        else:
                            econtext['portrait_url'] = __backup_portrait_url_140235424465808
                        if (__backup_has_author_link_140235385327504 is __marker):
                            del econtext['has_author_link']
                        else:
                            econtext['has_author_link'] = __backup_has_author_link_140235385327504
                        if (__backup_author_home_url_140235377023568 is __marker):
                            del econtext['author_home_url']
                        else:
                            econtext['author_home_url'] = __backup_author_home_url_140235377023568
                        if (__backup_depth_140235374162576 is __marker):
                            del econtext['depth']
                        else:
                            econtext['depth'] = __backup_depth_140235374162576
                        if (__backup_depth_140235374113296 is __marker):
                            del econtext['depth']
                        else:
                            econtext['depth'] = __backup_depth_140235374113296
                        if (__backup_comment_id_140235368754768 is __marker):
                            del econtext['comment_id']
                        else:
                            econtext['comment_id'] = __backup_comment_id_140235368754768
                        if (__backup_reply_140235432289808 is __marker):
                            del econtext['reply']
                        else:
                            econtext['reply'] = __backup_reply_140235432289808
                        __append(u'\n\n        ')
                        ____index_140235431389008 -= 1
                        if (____index_140235431389008 > 0):
                            __append('')
                    if (__backup_reply_dict_140235424467024 is __marker):
                        del econtext['reply_dict']
                    else:
                        econtext['reply_dict'] = __backup_reply_dict_140235424467024
                    __append(u'\n\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1b12a610> name=None at 7f8b1b12afd0> -> __attrs_140235424484432
                    __attrs_140235424484432 = _static_140235431388688

                    # <Value u'python: has_replies and not isDiscussionAllowed' (178:28)> -> __condition
                    __token = 9665
                    try:
                        __zt_tmp = __attrs_140235424484432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('python', u' has_replies and not isDiscussionAllowed', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="discreet">')
                        __stream_140235431388048 = []
                        __append_140235431388048 = __stream_140235431388048.append
                        __append_140235431388048(u'\n            Commenting has been disabled.\n        ')
                        __msgid_140235431388048 = __re_whitespace(''.join(__stream_140235431388048)).strip()
                        if u'label_commenting_disabled':
                            __append(translate(u'label_commenting_disabled', mapping=None, default=__msgid_140235431388048, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</div>')
                    __append(u'\n\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1aa94210> name=None at 7f8b1b10b1d0> -> __attrs_140235424483920
                __attrs_140235424483920 = _static_140235424481808

                # <Value u'python:has_replies and (isAnon and not isAnonymousDiscussionAllowed)' (187:24)> -> __condition
                __token = 9918
                try:
                    __zt_tmp = __attrs_140235424483920
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('python', u'has_replies and (isAnon and not isAnonymousDiscussionAllowed)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="reply">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1ad5aa50> name=None at 7f8b1ad5ac50> -> __attrs_140235427392528
                    __attrs_140235427392528 = _static_140235427392080

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<form')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235427393488
                    __default_140235427393488 = _DEFAULT_MARKER

                    # <Substitution u'view/login_action' (188:37)> -> __attr_action
                    __token = 10026
                    try:
                        __zt_tmp = __attrs_140235427392528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_140235435449424('path', u'view/login_action', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((u' action="%s"' % __attr_action))
                    __append(u'>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8b1ad5a310> name=None at 7f8b1ad5a850> -> __attrs_140235428391120
                    __attrs_140235428391120 = _static_140235427390224

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input class="standalone loginbutton" type="submit"')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235428389008
                    __default_140235428389008 = _DEFAULT_MARKER

                    # <Translate msgid=u'label_login_to_add_comments' node=<_ast.Str object at 0x7f8b1ae4ecd0> at 7f8b1ae4e210> -> __attr_value
                    __attr_value = u'Log in to add comments'
                    __attr_value = translate(u'label_login_to_add_comments', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u' />\n        </form>\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1ad5af10> name=None at 7f8b1ad5a590> -> __attrs_140235428390544
                __attrs_140235428390544 = _static_140235427393296

                # <Value u'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)' (197:54)> -> __condition
                __token = 10355
                try:
                    __zt_tmp = __attrs_140235428390544
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('python', u'isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="commenting" class="reply">\n\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235428392464
                    __attrs_140235428392464 = _static_140235489934800

                    # <fieldset ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<fieldset>\n\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235368751504
                    __attrs_140235368751504 = _static_140235489934800

                    # <legend ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<legend>')
                    __stream_140235368752976 = []
                    __append_140235368752976 = __stream_140235368752976.append
                    __append_140235368752976(u'Add comment')
                    __msgid_140235368752976 = __re_whitespace(''.join(__stream_140235368752976)).strip()
                    if u'label_add_comment':
                        __append(translate(u'label_add_comment', mapping=None, default=__msgid_140235368752976, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</legend>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235368751888
                    __attrs_140235368751888 = _static_140235489934800

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p>')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235368754192
                    __default_140235368754192 = _DEFAULT_MARKER

                    # <Value u'view/comment_transform_message' (202:28)> -> __cache_140235368751824
                    __token = 10581
                    try:
                        __zt_tmp = __attrs_140235368751888
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235368751824 = _static_140235435449424('path', u'view/comment_transform_message', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'view/comment_transform_message' (202:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1756e6d0> -> __condition
                    __expression = __cache_140235368751824

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n                You can add a comment by filling out the form below. Plain text\n                formatting.\n            ')
                    else:
                        __content = __cache_140235368751824
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</p>\n\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235424614672
                    __attrs_140235424614672 = _static_140235489934800

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235424613072
                    __default_140235424613072 = _DEFAULT_MARKER

                    # <Value u'view/form/render' (207:40)> -> __cache_140235368753488
                    __token = 10780
                    try:
                        __zt_tmp = __attrs_140235424614672
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235368753488 = _static_140235435449424('path', u'view/form/render', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'view/form/render' (207:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1756ee10> -> __condition
                    __expression = __cache_140235368753488

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div />')
                    else:
                        __content = __cache_140235368753488
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n\n        </fieldset>\n    </div>')
                __append(u'\n\n')
                __i18n_domain = __previous_i18n_domain_140235431256208
            if (__backup_auth_token_140235426088336 is __marker):
                del econtext['auth_token']
            else:
                econtext['auth_token'] = __backup_auth_token_140235426088336
            if (__backup_wtool_140235373356752 is __marker):
                del econtext['wtool']
            else:
                econtext['wtool'] = __backup_wtool_140235373356752
            if (__backup_errors_140235431258256 is __marker):
                del econtext['errors']
            else:
                econtext['errors'] = __backup_errors_140235431258256
            if (__backup_showCommenterImage_140235451444368 is __marker):
                del econtext['showCommenterImage']
            else:
                econtext['showCommenterImage'] = __backup_showCommenterImage_140235451444368
            if (__backup_has_replies_140235431278096 is __marker):
                del econtext['has_replies']
            else:
                econtext['has_replies'] = __backup_has_replies_140235431278096
            if (__backup_replies_140235368759184 is __marker):
                del econtext['replies']
            else:
                econtext['replies'] = __backup_replies_140235368759184
            if (__backup_canReview_140235431280528 is __marker):
                del econtext['canReview']
            else:
                econtext['canReview'] = __backup_canReview_140235431280528
            if (__backup_isAnon_140235431277392 is __marker):
                del econtext['isAnon']
            else:
                econtext['isAnon'] = __backup_isAnon_140235431277392
            if (__backup_isDeleteOwnCommentAllowed_140235431277136 is __marker):
                del econtext['isDeleteOwnCommentAllowed']
            else:
                econtext['isDeleteOwnCommentAllowed'] = __backup_isDeleteOwnCommentAllowed_140235431277136
            if (__backup_isEditCommentAllowed_140235373358608 is __marker):
                del econtext['isEditCommentAllowed']
            else:
                econtext['isEditCommentAllowed'] = __backup_isEditCommentAllowed_140235373358608
            if (__backup_isAnonymousDiscussionAllowed_140235426070672 is __marker):
                del econtext['isAnonymousDiscussionAllowed']
            else:
                econtext['isAnonymousDiscussionAllowed'] = __backup_isAnonymousDiscussionAllowed_140235426070672
            if (__backup_isDiscussionAllowed_140235431277968 is __marker):
                del econtext['isDiscussionAllowed']
            else:
                econtext['isDiscussionAllowed'] = __backup_isDiscussionAllowed_140235431277968
            if (__backup_userHasReplyPermission_140235432291600 is __marker):
                del econtext['userHasReplyPermission']
            else:
                econtext['userHasReplyPermission'] = __backup_userHasReplyPermission_140235432291600
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }