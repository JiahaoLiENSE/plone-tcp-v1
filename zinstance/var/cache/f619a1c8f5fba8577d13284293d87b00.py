# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.discussion-3.4.7-py2.7.egg/plone/app/discussion/browser/comments.pt'

__tokens = {46: (u'view/can_reply', 1, 46), 104: (u' view/is_discussion_allowe', 2, 42), 183: (u'd view/anonymous_discussion_allow', 3, 50), 261: (u'ed view/edit_comment_allo', 4, 41), 336: (u'wed view/delete_own_comment_all', 5, 45), 398: (u'Anon view/is_anon', 6, 25), 449: (u'eview view/can_', 7, 27), 496: (u'eplies python:view.get_replies(can', 8, 24), 566: (u'replies python:view.has_replies(ca', 9, 27), 643: (u'terImage view/show_commen', 10, 33), 699: (u'   errors options/state/getErro', 11, 20), 760: (u'     wtool context/@@plone_too', 12, 18), 825: (u' auth_token context/@@authenticator/t', 13, 22), 902: (u'python:isDiscussionAllowed or has_replies', 14, 26), 1025: (u'python:isAnon and not isAnonymousDiscussionAllowed', 18, 24), 1115: (u'view/login_action', 19, 37), 1554: (u'has_replies', 30, 24), 1449: (u"python: showCommenterImage and 'discussion showCommenterImage' or 'discussion'", 29, 31), 1611: (u'replies', 31, 43), 1690: (u'reply_dict/comment', 34, 35), 1749: (u' reply/getI', 35, 39), 1796: (u'h reply_dict/depth|python', 36, 33), 1857: (u"th python: depth > 10 and '10' or de", 37, 32), 1939: (u'url python:view.get_commenter_home_url(username=reply.author_usern', 38, 41), 2051: (u'link python:author_home_url and not i', 39, 40), 2131: (u't_url python:view.get_commenter_portrait(reply.author_use', 40, 36), 2231: (u"_state python:wtool.getInfoFor(reply, 'review_state', ", 41, 35), 2323: (u'canEdit python:view.can_edi', 42, 29), 2390: (u'anDelete python:view.can_dele', 43, 30), 2460: (u"olorclass python:lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else '", 44, 30), 2795: (u"python:canReview or review_state == 'published'", 47, 32), 2614: (u"python:'comment replyTreeLevel{depth} {state}'.format(depth= depth, state=colorclass(review_state))", 45, 39), 2750: (u' comment_i', 46, 35), 2903: (u'showCommenterImage', 49, 57), 2970: (u'has_author_link', 50, 46), 3039: (u'author_home_url', 51, 52), 3291: (u'portrait_url', 56, 50), 3354: (u' reply/author_nam', 57, 49), 3606: (u'not: has_author_link', 63, 40), 3673: (u'portrait_url', 64, 45), 3731: (u' reply/author_nam', 65, 44), 3931: (u'has_author_link', 71, 42), 4055: (u'author_home_url', 73, 48), 3988: (u'reply/author_name', 72, 40), 4187: (u'not: has_author_link', 76, 45), 4252: (u'reply/author_name', 77, 43), 4319: (u'not: reply/author_name', 78, 45), 4617: (u'python:view.format_time(reply.modification_date)', 83, 38), 4858: (u'reply/getText', 90, 49), 5156: (u'python:not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)', 97, 45), 5294: (u'string:${reply/absolute_url}/@@delete-own-comment', 98, 53), 5396: (u" python:view.can_delete_own(reply) and 'display: inline' or 'display: none", 99, 51), 5520: (u'd string:delete-${comment_i', 100, 47), 6147: (u'python:canDelete', 112, 45), 6218: (u'string:${reply/absolute_url}/@@moderate-delete-comment', 113, 53), 6322: (u' string:delete-${comment_id', 114, 48), 6768: (u'python:isEditCommentAllowed and canEdit', 123, 49), 7066: (u'auth_token', 127, 44), 7128: (u'string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', 128, 50), 7499: (u'not: auth_token', 134, 47), 7571: (u'string:${reply/absolute_url}/@@edit-comment', 135, 55), 7666: (u' string:edit-${comment_id', 136, 50), 8392: (u'canReview', 152, 45), 8452: (u'reply_dict/actions|nothing', 153, 49), 8632: (u' action/i', 155, 50), 8533: (u'string:${reply/absolute_url}/@@transmit-comment', 154, 53), 8691: (u'd string:${action/id}-${comment_i', 156, 47), 8823: (u'action/id', 157, 94), 9064: (u'action/title', 161, 57), 9384: (u'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', 170, 39), 9665: (u'python: has_replies and not isDiscussionAllowed', 178, 28), 9918: (u'python:has_replies and (isAnon and not isAnonymousDiscussionAllowed)', 187, 24), 10026: (u'view/login_action', 188, 37), 10355: (u'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', 197, 54), 10581: (u'view/comment_transform_message', 202, 28), 10780: (u'view/form/render', 207, 40)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386069387216 = {u'style': u"python:view.can_delete_own(reply) and 'display: inline' or 'display: none'", u'name': u'delete', u'id': u'string:delete-${comment_id}', u'method': u'post', u'action': u'', u'class': u'commentactionsform', }
_static_140386070150736 = {u'src': u'defaultUser.png', u'alt': u'', u'class': u'defaultuserimg', u'height': u'32', }
_static_140386077789136 = {u'src': u'defaultUser.png', u'alt': u'', u'class': u'defaultuserimg', u'height': u'32', }
_static_140386077787280 = {u'class': u'documentByLine', }
_static_140386070449808 = {u'class': u'reply', }
_static_140386072650256 = {u'action': u'', u'class': u'commentactionsform', u'id': u'string:delete-${comment_id}', u'name': u'delete', u'method': u'post', }
_static_140386247937936 = {}
_static_140386070448400 = {u'action': u'view/login_action', }
_static_140386069453712 = {u'class': u'comment', u'id': u'comment_id', }
_static_140386070711184 = {u'type': u'submit', u'name': u'form.button.DeleteComment', u'value': u'Delete', u'class': u'destructive', }
_static_140386069451344 = {u'class': u'discreet', }
_static_140386069340560 = {u'class': u'reply', }
_static_140386069150800 = {u'class': u'commentBody', }
_static_140386069974416 = {u'class': u'discussion', }
_static_140386070447184 = {u'id': u'commenting', u'class': u'reply', }
_static_140386069967248 = {u'action': u'', u'class': u'commentactionsform', u'id': u'string:${action/id}-${comment_id}', u'name': u'', u'method': u'get', }
_static_140386069974672 = {u'action': u'view/login_action', }
_static_140386070880080 = {u'type': u'hidden', u'name': u'workflow_action', u'value': u'action/id', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386078148816 = {u'type': u'submit', u'name': u'form.button.DeleteComment', u'value': u'Delete', u'class': u'destructive', }
_static_140386070112336 = {u'class': u'context reply-to-comment-button hide allowMultiSubmit', }
_static_140386069995472 = {u'href': u'', }
_static_140386069149840 = {u'class': u'commentActions', }
_static_140386070777488 = {u'class': u'commentDate', }
_static_140386069200080 = {u'href': u'', }
_static_140386070111312 = {u'href': u'string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', u'class': u'pat-plone-modal context commentactionsform', }
_static_140386069198736 = {u'class': u'commentImage', }
_static_140386070447760 = {u'type': u'submit', u'class': u'standalone loginbutton', u'value': u'Log in to add comments', }
_static_140386070126864 = {u'type': u'submit', u'name': u'form.button.TransmitComment', u'value': u'action/title', u'class': u'context', }
_static_140386069967888 = {u'action': u'', u'class': u'commentactionsform', u'id': u'string:edit-${comment_id}', u'name': u'edit', u'method': u'get', }
_static_140386069972496 = {u'type': u'submit', u'class': u'standalone loginbutton', u'value': u'Log in to add comments', }
_static_140386069923344 = {u'type': u'submit', u'name': u'form.button.EditComment', u'value': u'Edit', u'class': u'context', }
_static_140386186296528 = __compile_zt_expr

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

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069942672
            __attrs_140386069942672 = _static_140386247937936
            __backup_userHasReplyPermission_140386070486608 = get('userHasReplyPermission', __marker)

            # <Value u'view/can_reply' (1:46)> -> __value
            __token = 46
            try:
                __zt_tmp = __attrs_140386069942672
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/can_reply', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['userHasReplyPermission'] = __value
            __backup_isDiscussionAllowed_140386069973392 = get('isDiscussionAllowed', __marker)

            # <Value u'view/is_discussion_allowed' (2:42)> -> __value
            __token = 104
            try:
                __zt_tmp = __attrs_140386069942672
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/is_discussion_allowed', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['isDiscussionAllowed'] = __value
            __backup_isAnonymousDiscussionAllowed_140386071497232 = get('isAnonymousDiscussionAllowed', __marker)

            # <Value u'view/anonymous_discussion_allowed' (3:50)> -> __value
            __token = 183
            try:
                __zt_tmp = __attrs_140386069942672
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/anonymous_discussion_allowed', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['isAnonymousDiscussionAllowed'] = __value
            __backup_isEditCommentAllowed_140386071806352 = get('isEditCommentAllowed', __marker)

            # <Value u'view/edit_comment_allowed' (4:41)> -> __value
            __token = 261
            try:
                __zt_tmp = __attrs_140386069942672
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/edit_comment_allowed', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['isEditCommentAllowed'] = __value
            __backup_isDeleteOwnCommentAllowed_140386069981584 = get('isDeleteOwnCommentAllowed', __marker)

            # <Value u'view/delete_own_comment_allowed' (5:45)> -> __value
            __token = 336
            try:
                __zt_tmp = __attrs_140386069942672
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/delete_own_comment_allowed', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['isDeleteOwnCommentAllowed'] = __value
            __backup_isAnon_140386070839696 = get('isAnon', __marker)

            # <Value u'view/is_anonymous' (6:25)> -> __value
            __token = 398
            try:
                __zt_tmp = __attrs_140386069942672
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/is_anonymous', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['isAnon'] = __value
            __backup_canReview_140386070483344 = get('canReview', __marker)

            # <Value u'view/can_review' (7:27)> -> __value
            __token = 449
            try:
                __zt_tmp = __attrs_140386069942672
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/can_review', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['canReview'] = __value
            __backup_replies_140386069239760 = get('replies', __marker)

            # <Value u'python:view.get_replies(canReview)' (8:24)> -> __value
            __token = 496
            try:
                __zt_tmp = __attrs_140386069942672
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u'view.get_replies(canReview)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['replies'] = __value
            __backup_has_replies_140386078078864 = get('has_replies', __marker)

            # <Value u'python:view.has_replies(canReview)' (9:27)> -> __value
            __token = 566
            try:
                __zt_tmp = __attrs_140386069942672
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u'view.has_replies(canReview)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['has_replies'] = __value
            __backup_showCommenterImage_140386071167888 = get('showCommenterImage', __marker)

            # <Value u'view/show_commenter_image' (10:33)> -> __value
            __token = 643
            try:
                __zt_tmp = __attrs_140386069942672
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/show_commenter_image', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['showCommenterImage'] = __value
            __backup_errors_140386070487888 = get('errors', __marker)

            # <Value u'options/state/getErrors|nothing' (11:20)> -> __value
            __token = 699
            try:
                __zt_tmp = __attrs_140386069942672
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'options/state/getErrors|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['errors'] = __value
            __backup_wtool_140386070741200 = get('wtool', __marker)

            # <Value u'context/@@plone_tools/workflow' (12:18)> -> __value
            __token = 760
            try:
                __zt_tmp = __attrs_140386069942672
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'context/@@plone_tools/workflow', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['wtool'] = __value
            __backup_auth_token_140386069341520 = get('auth_token', __marker)

            # <Value u'context/@@authenticator/token|nothing' (13:22)> -> __value
            __token = 825
            try:
                __zt_tmp = __attrs_140386069942672
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'context/@@authenticator/token|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['auth_token'] = __value

            # <Value u'python:isDiscussionAllowed or has_replies' (14:26)> -> __condition
            __token = 902
            try:
                __zt_tmp = __attrs_140386069942672
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('python', u'isDiscussionAllowed or has_replies', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140386069340432 = __i18n_domain
                __i18n_domain = u'plone'
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2dcb6190> name=None at 7fae2dcb6150> -> __attrs_140386069973520
                __attrs_140386069973520 = _static_140386069340560

                # <Value u'python:isAnon and not isAnonymousDiscussionAllowed' (18:24)> -> __condition
                __token = 1025
                try:
                    __zt_tmp = __attrs_140386069973520
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('python', u'isAnon and not isAnonymousDiscussionAllowed', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="reply">\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae2dd50e90> name=None at 7fae2dd50bd0> -> __attrs_140386069974480
                    __attrs_140386069974480 = _static_140386069974672

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<form')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069972560
                    __default_140386069972560 = _DEFAULT_MARKER

                    # <Substitution u'view/login_action' (19:37)> -> __attr_action
                    __token = 1115
                    try:
                        __zt_tmp = __attrs_140386069974480
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_140386186296528('path', u'view/login_action', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((u' action="%s"' % __attr_action))
                    __append(u'>\n            ')

                    # <Static value=<_ast.Dict object at 0x7fae2dd50610> name=None at 7fae2dd50290> -> __attrs_140386070659536
                    __attrs_140386070659536 = _static_140386069972496

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input class="standalone loginbutton" type="submit"')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070661392
                    __default_140386070661392 = _DEFAULT_MARKER

                    # <Translate msgid=u'label_login_to_add_comments' node=<_ast.Str object at 0x7fae2ddf8510> at 7fae2ddf8b90> -> __attr_value
                    __attr_value = u'Log in to add comments'
                    __attr_value = translate(u'label_login_to_add_comments', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u' />\n        </form>\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2dd50d90> name=None at 7fae2dd504d0> -> __attrs_140386070662992
                __attrs_140386070662992 = _static_140386069974416

                # <Value u'has_replies' (30:24)> -> __condition
                __token = 1554
                try:
                    __zt_tmp = __attrs_140386070662992
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'has_replies', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070661520
                    __default_140386070661520 = _DEFAULT_MARKER

                    # <Substitution u"python: showCommenterImage and 'discussion showCommenterImage' or 'discussion'" (29:31)> -> __attr_class
                    __token = 1449
                    try:
                        __zt_tmp = __attrs_140386070662992
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140386186296528('python', u" showCommenterImage and 'discussion showCommenterImage' or 'discussion'", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', u'discussion', _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069450832
                    __attrs_140386069450832 = _static_140386247937936
                    __backup_reply_dict_140386078152976 = get('reply_dict', __marker)

                    # <Value u'replies' (31:43)> -> __iterator
                    __token = 1611
                    try:
                        __zt_tmp = __attrs_140386069450832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140386186296528('path', u'replies', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    (__iterator, ____index_140386069453200, ) = getitem('repeat')(u'reply_dict', __iterator)
                    econtext['reply_dict'] = None
                    for __item in __iterator:
                        econtext['reply_dict'] = __item
                        __append(u'\n\n            ')

                        # <Static value=<_ast.Dict object at 0x7fae2dcd1b90> name=None at 7fae2dcd13d0> -> __attrs_140386069453072
                        __attrs_140386069453072 = _static_140386069453712
                        __backup_reply_140386069151248 = get('reply', __marker)

                        # <Value u'reply_dict/comment' (34:35)> -> __value
                        __token = 1690
                        try:
                            __zt_tmp = __attrs_140386069453072
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140386186296528('path', u'reply_dict/comment', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        econtext['reply'] = __value
                        __backup_comment_id_140386071498000 = get('comment_id', __marker)

                        # <Value u'reply/getId' (35:39)> -> __value
                        __token = 1749
                        try:
                            __zt_tmp = __attrs_140386069453072
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140386186296528('path', u'reply/getId', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        econtext['comment_id'] = __value
                        __backup_depth_140386070736016 = get('depth', __marker)

                        # <Value u'reply_dict/depth|python:0' (36:33)> -> __value
                        __token = 1796
                        try:
                            __zt_tmp = __attrs_140386069453072
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140386186296528('path', u'reply_dict/depth|python:0', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        econtext['depth'] = __value
                        __backup_depth_140386069972944 = get('depth', __marker)

                        # <Value u"python: depth > 10 and '10' or depth" (37:32)> -> __value
                        __token = 1857
                        try:
                            __zt_tmp = __attrs_140386069453072
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140386186296528('python', u" depth > 10 and '10' or depth", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        econtext['depth'] = __value
                        __backup_author_home_url_140386069902160 = get('author_home_url', __marker)

                        # <Value u'python:view.get_commenter_home_url(username=reply.author_username)' (38:41)> -> __value
                        __token = 1939
                        try:
                            __zt_tmp = __attrs_140386069453072
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140386186296528('python', u'view.get_commenter_home_url(username=reply.author_username)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        econtext['author_home_url'] = __value
                        __backup_has_author_link_140386069198800 = get('has_author_link', __marker)

                        # <Value u'python:author_home_url and not isAnon' (39:40)> -> __value
                        __token = 2051
                        try:
                            __zt_tmp = __attrs_140386069453072
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140386186296528('python', u'author_home_url and not isAnon', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        econtext['has_author_link'] = __value
                        __backup_portrait_url_140386070741904 = get('portrait_url', __marker)

                        # <Value u'python:view.get_commenter_portrait(reply.author_username)' (40:36)> -> __value
                        __token = 2131
                        try:
                            __zt_tmp = __attrs_140386069453072
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140386186296528('python', u'view.get_commenter_portrait(reply.author_username)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        econtext['portrait_url'] = __value
                        __backup_review_state_140386077788688 = get('review_state', __marker)

                        # <Value u"python:wtool.getInfoFor(reply, 'review_state', 'none')" (41:35)> -> __value
                        __token = 2231
                        try:
                            __zt_tmp = __attrs_140386069453072
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140386186296528('python', u"wtool.getInfoFor(reply, 'review_state', 'none')", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        econtext['review_state'] = __value
                        __backup_canEdit_140386070744208 = get('canEdit', __marker)

                        # <Value u'python:view.can_edit(reply)' (42:29)> -> __value
                        __token = 2323
                        try:
                            __zt_tmp = __attrs_140386069453072
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140386186296528('python', u'view.can_edit(reply)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        econtext['canEdit'] = __value
                        __backup_canDelete_140386070484560 = get('canDelete', __marker)

                        # <Value u'python:view.can_delete(reply)' (43:30)> -> __value
                        __token = 2390
                        try:
                            __zt_tmp = __attrs_140386069453072
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140386186296528('python', u'view.can_delete(reply)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        econtext['canDelete'] = __value
                        __backup_colorclass_140386070742352 = get('colorclass', __marker)

                        # <Value u"python:lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else 'state-'+x)" (44:30)> -> __value
                        __token = 2460
                        try:
                            __zt_tmp = __attrs_140386069453072
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140386186296528('python', u"lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else 'state-'+x)", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        econtext['colorclass'] = __value

                        # <Value u"python:canReview or review_state == 'published'" (47:32)> -> __condition
                        __token = 2795
                        try:
                            __zt_tmp = __attrs_140386069453072
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140386186296528('python', u"canReview or review_state == 'published'", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div')

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069451216
                            __default_140386069451216 = _DEFAULT_MARKER

                            # <Substitution u"python:'comment replyTreeLevel{depth} {state}'.format(depth= depth, state=colorclass(review_state))" (45:39)> -> __attr_class
                            __token = 2614
                            try:
                                __zt_tmp = __attrs_140386069453072
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_140386186296528('python', u"'comment replyTreeLevel{depth} {state}'.format(depth= depth, state=colorclass(review_state))", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', u'comment', _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((u' class="%s"' % __attr_class))

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069452752
                            __default_140386069452752 = _DEFAULT_MARKER

                            # <Substitution u'comment_id' (46:35)> -> __attr_id
                            __token = 2750
                            try:
                                __zt_tmp = __attrs_140386069453072
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_id = _static_140386186296528('path', u'comment_id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_id is not None):
                                __append((u' id="%s"' % __attr_id))
                            __append(u'>\n\n                ')

                            # <Static value=<_ast.Dict object at 0x7fae2dc93790> name=None at 7fae2dc93750> -> __attrs_140386069200592
                            __attrs_140386069200592 = _static_140386069198736

                            # <Value u'showCommenterImage' (49:57)> -> __condition
                            __token = 2903
                            try:
                                __zt_tmp = __attrs_140386069200592
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140386186296528('path', u'showCommenterImage', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<div class="commentImage">\n                    ')

                                # <Static value=<_ast.Dict object at 0x7fae2dc93cd0> name=None at 7fae2dc93f90> -> __attrs_140386071777424
                                __attrs_140386071777424 = _static_140386069200080

                                # <Value u'has_author_link' (50:46)> -> __condition
                                __token = 2970
                                try:
                                    __zt_tmp = __attrs_140386071777424
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140386186296528('path', u'has_author_link', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                if __condition:

                                    # <a ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<a')

                                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071779408
                                    __default_140386071779408 = _DEFAULT_MARKER

                                    # <Substitution u'author_home_url' (51:52)> -> __attr_href
                                    __token = 3039
                                    try:
                                        __zt_tmp = __attrs_140386071777424
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_href = _static_140386186296528('path', u'author_home_url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                    __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                                    if (__attr_href is not None):
                                        __append((u' href="%s"' % __attr_href))
                                    __append(u'>\n                         ')

                                    # <Static value=<_ast.Dict object at 0x7fae2e4c4bd0> name=None at 7fae2e4c4b10> -> __attrs_140386070147984
                                    __attrs_140386070147984 = _static_140386077789136

                                    # <img ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<img')

                                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070148624
                                    __default_140386070148624 = _DEFAULT_MARKER

                                    # <Substitution u'portrait_url' (56:50)> -> __attr_src
                                    __token = 3291
                                    try:
                                        __zt_tmp = __attrs_140386070147984
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_src = _static_140386186296528('path', u'portrait_url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                    __attr_src = __quote(__attr_src, '"', '&quot;', u'defaultUser.png', _DEFAULT_MARKER)
                                    if (__attr_src is not None):
                                        __append((u' src="%s"' % __attr_src))

                                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070150608
                                    __default_140386070150608 = _DEFAULT_MARKER

                                    # <Substitution u'reply/author_name' (57:49)> -> __attr_alt
                                    __token = 3354
                                    try:
                                        __zt_tmp = __attrs_140386070147984
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_alt = _static_140386186296528('path', u'reply/author_name', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                    __attr_alt = __quote(__attr_alt, '"', '&quot;', u'', _DEFAULT_MARKER)
                                    if (__attr_alt is not None):
                                        __append((u' alt="%s"' % __attr_alt))
                                    __append(u' class="defaultuserimg" height="32" />\n                    </a>')
                                __append(u'\n                    ')

                                # <Static value=<_ast.Dict object at 0x7fae2dd7be50> name=None at 7fae2dc93a10> -> __attrs_140386069994064
                                __attrs_140386069994064 = _static_140386070150736

                                # <Value u'not: has_author_link' (63:40)> -> __condition
                                __token = 3606
                                try:
                                    __zt_tmp = __attrs_140386069994064
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140386186296528('not', u' has_author_link', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                if __condition:

                                    # <img ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<img')

                                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070147856
                                    __default_140386070147856 = _DEFAULT_MARKER

                                    # <Substitution u'portrait_url' (64:45)> -> __attr_src
                                    __token = 3673
                                    try:
                                        __zt_tmp = __attrs_140386069994064
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_src = _static_140386186296528('path', u'portrait_url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                    __attr_src = __quote(__attr_src, '"', '&quot;', u'defaultUser.png', _DEFAULT_MARKER)
                                    if (__attr_src is not None):
                                        __append((u' src="%s"' % __attr_src))

                                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070149328
                                    __default_140386070149328 = _DEFAULT_MARKER

                                    # <Substitution u'reply/author_name' (65:44)> -> __attr_alt
                                    __token = 3731
                                    try:
                                        __zt_tmp = __attrs_140386069994064
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_alt = _static_140386186296528('path', u'reply/author_name', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                    __attr_alt = __quote(__attr_alt, '"', '&quot;', u'', _DEFAULT_MARKER)
                                    if (__attr_alt is not None):
                                        __append((u' alt="%s"' % __attr_alt))
                                    __append(u' class="defaultuserimg" height="32" />')
                                __append(u'\n                </div>')
                            __append(u'\n\n                ')

                            # <Static value=<_ast.Dict object at 0x7fae2e4c4490> name=None at 7fae2df09190> -> __attrs_140386069995152
                            __attrs_140386069995152 = _static_140386077787280

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="documentByLine">\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069993744
                            __attrs_140386069993744 = _static_140386247937936
                            __append(u'\n                        ')

                            # <Static value=<_ast.Dict object at 0x7fae2dd55fd0> name=None at 7fae2dd55650> -> __attrs_140386070775120
                            __attrs_140386070775120 = _static_140386069995472

                            # <Value u'has_author_link' (71:42)> -> __condition
                            __token = 3931
                            try:
                                __zt_tmp = __attrs_140386070775120
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140386186296528('path', u'has_author_link', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            if __condition:

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<a')

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070774672
                                __default_140386070774672 = _DEFAULT_MARKER

                                # <Substitution u'author_home_url' (73:48)> -> __attr_href
                                __token = 4055
                                try:
                                    __zt_tmp = __attrs_140386070775120
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_140386186296528('path', u'author_home_url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((u' href="%s"' % __attr_href))
                                __append(u'>')

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069994640
                                __default_140386069994640 = _DEFAULT_MARKER

                                # <Value u'reply/author_name' (72:40)> -> __cache_140386069993424
                                __token = 3988
                                try:
                                    __zt_tmp = __attrs_140386070775120
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140386069993424 = _static_140386186296528('path', u'reply/author_name', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                                # <BinOp left=<Value u'reply/author_name' (72:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dd55f90> -> __condition
                                __expression = __cache_140386069993424

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(u'\n                            Poster Name\n                        ')
                                else:
                                    __content = __cache_140386069993424
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</a>')
                            __append(u'\n                        ')

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070773968
                            __attrs_140386070773968 = _static_140386247937936

                            # <Value u'not: has_author_link' (76:45)> -> __condition
                            __token = 4187
                            try:
                                __zt_tmp = __attrs_140386070773968
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140386186296528('not', u' has_author_link', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            if __condition:

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070775184
                                __default_140386070775184 = _DEFAULT_MARKER

                                # <Value u'reply/author_name' (77:43)> -> __cache_140386070774544
                                __token = 4252
                                try:
                                    __zt_tmp = __attrs_140386070773968
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140386070774544 = _static_140386186296528('path', u'reply/author_name', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                                # <BinOp left=<Value u'reply/author_name' (77:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2de14f50> -> __condition
                                __expression = __cache_140386070774544

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:

                                    # <span ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<span />')
                                else:
                                    __content = __cache_140386070774544
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                            __append(u'\n                        ')

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070774352
                            __attrs_140386070774352 = _static_140386247937936

                            # <Value u'not: reply/author_name' (78:45)> -> __condition
                            __token = 4319
                            try:
                                __zt_tmp = __attrs_140386070774352
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140386186296528('not', u' reply/author_name', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span>')
                                __stream_140386070774096 = []
                                __append_140386070774096 = __stream_140386070774096.append
                                __append_140386070774096(u'Anonymous')
                                __msgid_140386070774096 = __re_whitespace(''.join(__stream_140386070774096)).strip()
                                if u'label_anonymous':
                                    __append(translate(u'label_anonymous', mapping=None, default=__msgid_140386070774096, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                                __append(u'</span>')
                            __append(u'\n                    \n                    ')

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070774800
                            __attrs_140386070774800 = _static_140386247937936
                            __stream_140386069994512 = []
                            __append_140386069994512 = __stream_140386069994512.append
                            __append_140386069994512(u'says:')
                            __msgid_140386069994512 = __re_whitespace(''.join(__stream_140386069994512)).strip()
                            if u'label_says':
                                __append(translate(u'label_says', mapping=None, default=__msgid_140386069994512, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fae2de14e90> name=None at 7fae2de14450> -> __attrs_140386069150416
                            __attrs_140386069150416 = _static_140386070777488

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="commentDate">')

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070777616
                            __default_140386070777616 = _DEFAULT_MARKER

                            # <Value u'python:view.format_time(reply.modification_date)' (83:38)> -> __cache_140386069995088
                            __token = 4617
                            try:
                                __zt_tmp = __attrs_140386069150416
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140386069995088 = _static_140386186296528('python', u'view.format_time(reply.modification_date)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                            # <BinOp left=<Value u'python:view.format_time(reply.modification_date)' (83:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2de14b90> -> __condition
                            __expression = __cache_140386069995088

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u'\n                         8/23/2001 12:40:44 PM\n                    ')
                            else:
                                __content = __cache_140386069995088
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</div>\n                </div>\n\n                ')

                            # <Static value=<_ast.Dict object at 0x7fae2dc87c50> name=None at 7fae2dd55210> -> __attrs_140386069148688
                            __attrs_140386069148688 = _static_140386069150800

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="commentBody">\n\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069151376
                            __attrs_140386069151376 = _static_140386247937936

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069148176
                            __default_140386069148176 = _DEFAULT_MARKER

                            # <Value u'reply/getText' (90:49)> -> __cache_140386069151184
                            __token = 4858
                            try:
                                __zt_tmp = __attrs_140386069151376
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140386069151184 = _static_140386186296528('path', u'reply/getText', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                            # <BinOp left=<Value u'reply/getText' (90:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dc87650> -> __condition
                            __expression = __cache_140386069151184

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span />')
                            else:
                                __content = __cache_140386069151184
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'\n\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fae2dc87890> name=None at 7fae2dc87cd0> -> __attrs_140386069388432
                            __attrs_140386069388432 = _static_140386069149840

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="commentActions">\n                        ')

                            # <Static value=<_ast.Dict object at 0x7fae2dcc17d0> name=None at 7fae2dcc1b50> -> __attrs_140386078147024
                            __attrs_140386078147024 = _static_140386069387216

                            # <Value u'python:not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)' (97:45)> -> __condition
                            __token = 5156
                            try:
                                __zt_tmp = __attrs_140386078147024
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140386186296528('python', u'not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            if __condition:

                                # <form ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<form name="delete"')

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069387600
                                __default_140386069387600 = _DEFAULT_MARKER

                                # <Substitution u'string:${reply/absolute_url}/@@delete-own-comment' (98:53)> -> __attr_action
                                __token = 5294
                                try:
                                    __zt_tmp = __attrs_140386078147024
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_action = _static_140386186296528('string', u'${reply/absolute_url}/@@delete-own-comment', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                __attr_action = __quote(__attr_action, '"', '&quot;', u'', _DEFAULT_MARKER)
                                if (__attr_action is not None):
                                    __append((u' action="%s"' % __attr_action))
                                __append(u' method="post" class="commentactionsform"')

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069386896
                                __default_140386069386896 = _DEFAULT_MARKER

                                # <Substitution u"python:view.can_delete_own(reply) and 'display: inline' or 'display: none'" (99:51)> -> __attr_style
                                __token = 5396
                                try:
                                    __zt_tmp = __attrs_140386078147024
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_style = _static_140386186296528('python', u"view.can_delete_own(reply) and 'display: inline' or 'display: none'", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_style is not None):
                                    __append((u' style="%s"' % __attr_style))

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078146768
                                __default_140386078146768 = _DEFAULT_MARKER

                                # <Substitution u'string:delete-${comment_id}' (100:47)> -> __attr_id
                                __token = 5520
                                try:
                                    __zt_tmp = __attrs_140386078147024
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_id = _static_140386186296528('string', u'delete-${comment_id}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_id is not None):
                                    __append((u' id="%s"' % __attr_id))
                                __append(u'>\n                            ')

                                # <Static value=<_ast.Dict object at 0x7fae2e51c8d0> name=None at 7fae2e51c790> -> __attrs_140386072652944
                                __attrs_140386072652944 = _static_140386078148816

                                # <input ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<input name="form.button.DeleteComment" class="destructive" type="submit"')

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386072651408
                                __default_140386072651408 = _DEFAULT_MARKER

                                # <Translate msgid=u'label_delete' node=<_ast.Str object at 0x7fae2dfde8d0> at 7fae2dfde710> -> __attr_value
                                __attr_value = u'Delete'
                                __attr_value = translate(u'label_delete', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                if (__attr_value is not None):
                                    __append((u' value="%s"' % __attr_value))
                                __append(u' />\n                        </form>')
                            __append(u'\n                        ')

                            # <Static value=<_ast.Dict object at 0x7fae2dfde210> name=None at 7fae2dcc1f10> -> __attrs_140386070709840
                            __attrs_140386070709840 = _static_140386072650256

                            # <Value u'python:canDelete' (112:45)> -> __condition
                            __token = 6147
                            try:
                                __zt_tmp = __attrs_140386070709840
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140386186296528('python', u'canDelete', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            if __condition:

                                # <form ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<form name="delete"')

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386072652240
                                __default_140386072652240 = _DEFAULT_MARKER

                                # <Substitution u'string:${reply/absolute_url}/@@moderate-delete-comment' (113:53)> -> __attr_action
                                __token = 6218
                                try:
                                    __zt_tmp = __attrs_140386070709840
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_action = _static_140386186296528('string', u'${reply/absolute_url}/@@moderate-delete-comment', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                __attr_action = __quote(__attr_action, '"', '&quot;', u'', _DEFAULT_MARKER)
                                if (__attr_action is not None):
                                    __append((u' action="%s"' % __attr_action))
                                __append(u' method="post" class="commentactionsform"')

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070710224
                                __default_140386070710224 = _DEFAULT_MARKER

                                # <Substitution u'string:delete-${comment_id}' (114:48)> -> __attr_id
                                __token = 6322
                                try:
                                    __zt_tmp = __attrs_140386070709840
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_id = _static_140386186296528('string', u'delete-${comment_id}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_id is not None):
                                    __append((u' id="%s"' % __attr_id))
                                __append(u'>\n                            ')

                                # <Static value=<_ast.Dict object at 0x7fae2de04b90> name=None at 7fae2de04550> -> __attrs_140386070110608
                                __attrs_140386070110608 = _static_140386070711184

                                # <input ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<input name="form.button.DeleteComment" class="destructive" type="submit"')

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070111120
                                __default_140386070111120 = _DEFAULT_MARKER

                                # <Translate msgid=u'label_delete' node=<_ast.Str object at 0x7fae2dd72e50> at 7fae2dd72d10> -> __attr_value
                                __attr_value = u'Delete'
                                __attr_value = translate(u'label_delete', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                if (__attr_value is not None):
                                    __append((u' value="%s"' % __attr_value))
                                __append(u' />\n                        </form>')
                            __append(u'\n\n                        ')

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070112272
                            __attrs_140386070112272 = _static_140386247937936

                            # <Value u'python:isEditCommentAllowed and canEdit' (123:49)> -> __condition
                            __token = 6768
                            try:
                                __zt_tmp = __attrs_140386070112272
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140386186296528('python', u'isEditCommentAllowed and canEdit', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            if __condition:
                                __append(u"\n                          <!-- plone 5 will have auth_token available\n                               so we'll use modal pattern -->\n                          ")

                                # <Static value=<_ast.Dict object at 0x7fae2dd72450> name=None at 7fae2dd72290> -> __attrs_140386069967568
                                __attrs_140386069967568 = _static_140386070111312

                                # <Value u'auth_token' (127:44)> -> __condition
                                __token = 7066
                                try:
                                    __zt_tmp = __attrs_140386069967568
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140386186296528('path', u'auth_token', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                if __condition:

                                    # <a ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<a class="pat-plone-modal context commentactionsform"')

                                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069969168
                                    __default_140386069969168 = _DEFAULT_MARKER

                                    # <Substitution u'string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}' (128:50)> -> __attr_href
                                    __token = 7128
                                    try:
                                        __zt_tmp = __attrs_140386069967568
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_href = _static_140386186296528('string', u'${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_href is not None):
                                        __append((u' href="%s"' % __attr_href))
                                    __append(u'>')
                                    __stream_140386070113040 = []
                                    __append_140386070113040 = __stream_140386070113040.append
                                    __append_140386070113040(u'Edit')
                                    __msgid_140386070113040 = __re_whitespace(''.join(__stream_140386070113040)).strip()
                                    if u'Edit':
                                        __append(translate(u'Edit', mapping=None, default=__msgid_140386070113040, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                                    __append(u'</a>')
                                __append(u'\n                          ')

                                # <Static value=<_ast.Dict object at 0x7fae2dd4f410> name=None at 7fae2dd4fbd0> -> __attrs_140386069968912
                                __attrs_140386069968912 = _static_140386069967888

                                # <Value u'not: auth_token' (134:47)> -> __condition
                                __token = 7499
                                try:
                                    __zt_tmp = __attrs_140386069968912
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140386186296528('not', u' auth_token', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                if __condition:

                                    # <form ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<form name="edit"')

                                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069968720
                                    __default_140386069968720 = _DEFAULT_MARKER

                                    # <Substitution u'string:${reply/absolute_url}/@@edit-comment' (135:55)> -> __attr_action
                                    __token = 7571
                                    try:
                                        __zt_tmp = __attrs_140386069968912
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_action = _static_140386186296528('string', u'${reply/absolute_url}/@@edit-comment', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                    __attr_action = __quote(__attr_action, '"', '&quot;', u'', _DEFAULT_MARKER)
                                    if (__attr_action is not None):
                                        __append((u' action="%s"' % __attr_action))
                                    __append(u' method="get" class="commentactionsform"')

                                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069968336
                                    __default_140386069968336 = _DEFAULT_MARKER

                                    # <Substitution u'string:edit-${comment_id}' (136:50)> -> __attr_id
                                    __token = 7666
                                    try:
                                        __zt_tmp = __attrs_140386069968912
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_140386186296528('string', u'edit-${comment_id}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((u' id="%s"' % __attr_id))
                                    __append(u'>\n                              ')

                                    # <Static value=<_ast.Dict object at 0x7fae2dd44610> name=None at 7fae2dd44bd0> -> __attrs_140386069924560
                                    __attrs_140386069924560 = _static_140386069923344

                                    # <input ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<input name="form.button.EditComment" class="context" type="submit"')

                                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069921872
                                    __default_140386069921872 = _DEFAULT_MARKER

                                    # <Translate msgid=u'label_edit' node=<_ast.Str object at 0x7fae2dd44290> at 7fae2dd44210> -> __attr_value
                                    __attr_value = u'Edit'
                                    __attr_value = translate(u'label_edit', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                    if (__attr_value is not None):
                                        __append((u' value="%s"' % __attr_value))
                                    __append(u' />\n                          </form>')
                                __append(u'\n                        ')
                            __append(u"\n\n\n                        <!-- Workflow actions (e.g. 'publish') -->\n                        ")

                            # <Static value=<_ast.Dict object at 0x7fae2dd4f190> name=None at 7fae2dd4fad0> -> __attrs_140386070878224
                            __attrs_140386070878224 = _static_140386069967248

                            # <Value u'canReview' (152:45)> -> __condition
                            __token = 8392
                            try:
                                __zt_tmp = __attrs_140386070878224
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140386186296528('path', u'canReview', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            if __condition:
                                __backup_action_140386071780944 = get('action', __marker)

                                # <Value u'reply_dict/actions|nothing' (153:49)> -> __iterator
                                __token = 8452
                                try:
                                    __zt_tmp = __attrs_140386070878224
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __iterator = _static_140386186296528('path', u'reply_dict/actions|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                (__iterator, ____index_140386070879248, ) = getitem('repeat')(u'action', __iterator)
                                econtext['action'] = None
                                for __item in __iterator:
                                    econtext['action'] = __item

                                    # <form ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<form')

                                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070879056
                                    __default_140386070879056 = _DEFAULT_MARKER

                                    # <Substitution u'action/id' (155:50)> -> __attr_name
                                    __token = 8632
                                    try:
                                        __zt_tmp = __attrs_140386070878224
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_name = _static_140386186296528('path', u'action/id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                    __attr_name = __quote(__attr_name, '"', '&quot;', u'', _DEFAULT_MARKER)
                                    if (__attr_name is not None):
                                        __append((u' name="%s"' % __attr_name))

                                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070878608
                                    __default_140386070878608 = _DEFAULT_MARKER

                                    # <Substitution u'string:${reply/absolute_url}/@@transmit-comment' (154:53)> -> __attr_action
                                    __token = 8533
                                    try:
                                        __zt_tmp = __attrs_140386070878224
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_action = _static_140386186296528('string', u'${reply/absolute_url}/@@transmit-comment', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                    __attr_action = __quote(__attr_action, '"', '&quot;', u'', _DEFAULT_MARKER)
                                    if (__attr_action is not None):
                                        __append((u' action="%s"' % __attr_action))
                                    __append(u' method="get" class="commentactionsform"')

                                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070879760
                                    __default_140386070879760 = _DEFAULT_MARKER

                                    # <Substitution u'string:${action/id}-${comment_id}' (156:47)> -> __attr_id
                                    __token = 8691
                                    try:
                                        __zt_tmp = __attrs_140386070878224
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_140386186296528('string', u'${action/id}-${comment_id}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((u' id="%s"' % __attr_id))
                                    __append(u'>\n                            ')

                                    # <Static value=<_ast.Dict object at 0x7fae2de2df50> name=None at 7fae2de2d5d0> -> __attrs_140386070128144
                                    __attrs_140386070128144 = _static_140386070880080

                                    # <input ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<input type="hidden" name="workflow_action"')

                                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070128464
                                    __default_140386070128464 = _DEFAULT_MARKER

                                    # <Substitution u'action/id' (157:94)> -> __attr_value
                                    __token = 8823
                                    try:
                                        __zt_tmp = __attrs_140386070128144
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_value = _static_140386186296528('path', u'action/id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_value is not None):
                                        __append((u' value="%s"' % __attr_value))
                                    __append(u' />\n                            ')

                                    # <Static value=<_ast.Dict object at 0x7fae2dd76110> name=None at 7fae2dd76890> -> __attrs_140386070129680
                                    __attrs_140386070129680 = _static_140386070126864

                                    # <input ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<input name="form.button.TransmitComment" class="context" type="submit"')

                                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070130640
                                    __default_140386070130640 = _DEFAULT_MARKER

                                    # <Translate msgid=None node=<Substitution u'action/title' (161:57)> at 7fae2dd76d50> -> __attr_value

                                    # <Substitution u'action/title' (161:57)> -> __attr_value
                                    __token = 9064
                                    try:
                                        __zt_tmp = __attrs_140386070129680
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_value = _static_140386186296528('path', u'action/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                                    __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                    if (__attr_value is not None):
                                        __append((u' value="%s"' % __attr_value))
                                    __append(u' />\n                        </form>')
                                    ____index_140386070879248 -= 1
                                    if (____index_140386070879248 > 0):
                                        __append('\n                        ')
                                if (__backup_action_140386071780944 is __marker):
                                    del econtext['action']
                                else:
                                    econtext['action'] = __backup_action_140386071780944
                            __append(u'\n                    </div>\n\n\n                </div>\n                ')

                            # <Static value=<_ast.Dict object at 0x7fae2dd72850> name=None at 7fae2dcc1210> -> __attrs_140386070127376
                            __attrs_140386070127376 = _static_140386070112336

                            # <Value u'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)' (170:39)> -> __condition
                            __token = 9384
                            try:
                                __zt_tmp = __attrs_140386070127376
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140386186296528('python', u'isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            if __condition:

                                # <button ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<button class="context reply-to-comment-button hide allowMultiSubmit">')
                                __stream_140386069149136 = []
                                __append_140386069149136 = __stream_140386069149136.append
                                __append_140386069149136(u'\n                    Reply\n                ')
                                __msgid_140386069149136 = __re_whitespace(''.join(__stream_140386069149136)).strip()
                                if u'label_reply':
                                    __append(translate(u'label_reply', mapping=None, default=__msgid_140386069149136, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                                __append(u'</button>')
                            __append(u'\n            </div>')
                        if (__backup_colorclass_140386070742352 is __marker):
                            del econtext['colorclass']
                        else:
                            econtext['colorclass'] = __backup_colorclass_140386070742352
                        if (__backup_canDelete_140386070484560 is __marker):
                            del econtext['canDelete']
                        else:
                            econtext['canDelete'] = __backup_canDelete_140386070484560
                        if (__backup_canEdit_140386070744208 is __marker):
                            del econtext['canEdit']
                        else:
                            econtext['canEdit'] = __backup_canEdit_140386070744208
                        if (__backup_review_state_140386077788688 is __marker):
                            del econtext['review_state']
                        else:
                            econtext['review_state'] = __backup_review_state_140386077788688
                        if (__backup_portrait_url_140386070741904 is __marker):
                            del econtext['portrait_url']
                        else:
                            econtext['portrait_url'] = __backup_portrait_url_140386070741904
                        if (__backup_has_author_link_140386069198800 is __marker):
                            del econtext['has_author_link']
                        else:
                            econtext['has_author_link'] = __backup_has_author_link_140386069198800
                        if (__backup_author_home_url_140386069902160 is __marker):
                            del econtext['author_home_url']
                        else:
                            econtext['author_home_url'] = __backup_author_home_url_140386069902160
                        if (__backup_depth_140386069972944 is __marker):
                            del econtext['depth']
                        else:
                            econtext['depth'] = __backup_depth_140386069972944
                        if (__backup_depth_140386070736016 is __marker):
                            del econtext['depth']
                        else:
                            econtext['depth'] = __backup_depth_140386070736016
                        if (__backup_comment_id_140386071498000 is __marker):
                            del econtext['comment_id']
                        else:
                            econtext['comment_id'] = __backup_comment_id_140386071498000
                        if (__backup_reply_140386069151248 is __marker):
                            del econtext['reply']
                        else:
                            econtext['reply'] = __backup_reply_140386069151248
                        __append(u'\n\n        ')
                        ____index_140386069453200 -= 1
                        if (____index_140386069453200 > 0):
                            __append('')
                    if (__backup_reply_dict_140386078152976 is __marker):
                        del econtext['reply_dict']
                    else:
                        econtext['reply_dict'] = __backup_reply_dict_140386078152976
                    __append(u'\n\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae2dcd1250> name=None at 7fae2dcd1f10> -> __attrs_140386070128272
                    __attrs_140386070128272 = _static_140386069451344

                    # <Value u'python: has_replies and not isDiscussionAllowed' (178:28)> -> __condition
                    __token = 9665
                    try:
                        __zt_tmp = __attrs_140386070128272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('python', u' has_replies and not isDiscussionAllowed', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="discreet">')
                        __stream_140386069451088 = []
                        __append_140386069451088 = __stream_140386069451088.append
                        __append_140386069451088(u'\n            Commenting has been disabled.\n        ')
                        __msgid_140386069451088 = __re_whitespace(''.join(__stream_140386069451088)).strip()
                        if u'label_commenting_disabled':
                            __append(translate(u'label_commenting_disabled', mapping=None, default=__msgid_140386069451088, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</div>')
                    __append(u'\n\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2ddc4e90> name=None at 7fae2dc93410> -> __attrs_140386070447120
                __attrs_140386070447120 = _static_140386070449808

                # <Value u'python:has_replies and (isAnon and not isAnonymousDiscussionAllowed)' (187:24)> -> __condition
                __token = 9918
                try:
                    __zt_tmp = __attrs_140386070447120
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('python', u'has_replies and (isAnon and not isAnonymousDiscussionAllowed)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="reply">\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae2ddc4910> name=None at 7fae2ddc4710> -> __attrs_140386070446288
                    __attrs_140386070446288 = _static_140386070448400

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<form')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070447504
                    __default_140386070447504 = _DEFAULT_MARKER

                    # <Substitution u'view/login_action' (188:37)> -> __attr_action
                    __token = 10026
                    try:
                        __zt_tmp = __attrs_140386070446288
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_140386186296528('path', u'view/login_action', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((u' action="%s"' % __attr_action))
                    __append(u'>\n            ')

                    # <Static value=<_ast.Dict object at 0x7fae2ddc4690> name=None at 7fae2ddc4a10> -> __attrs_140386070747984
                    __attrs_140386070747984 = _static_140386070447760

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input class="standalone loginbutton" type="submit"')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070748880
                    __default_140386070748880 = _DEFAULT_MARKER

                    # <Translate msgid=u'label_login_to_add_comments' node=<_ast.Str object at 0x7fae2de0d410> at 7fae2de0d850> -> __attr_value
                    __attr_value = u'Log in to add comments'
                    __attr_value = translate(u'label_login_to_add_comments', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u' />\n        </form>\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2ddc4450> name=None at 7fae2ddc4f10> -> __attrs_140386070747408
                __attrs_140386070747408 = _static_140386070447184

                # <Value u'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)' (197:54)> -> __condition
                __token = 10355
                try:
                    __zt_tmp = __attrs_140386070747408
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('python', u'isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="commenting" class="reply">\n\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070747600
                    __attrs_140386070747600 = _static_140386247937936

                    # <fieldset ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<fieldset>\n\n            ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070042000
                    __attrs_140386070042000 = _static_140386247937936

                    # <legend ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<legend>')
                    __stream_140386070748048 = []
                    __append_140386070748048 = __stream_140386070748048.append
                    __append_140386070748048(u'Add comment')
                    __msgid_140386070748048 = __re_whitespace(''.join(__stream_140386070748048)).strip()
                    if u'label_add_comment':
                        __append(translate(u'label_add_comment', mapping=None, default=__msgid_140386070748048, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</legend>\n            ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070041936
                    __attrs_140386070041936 = _static_140386247937936

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p>')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070040720
                    __default_140386070040720 = _DEFAULT_MARKER

                    # <Value u'view/comment_transform_message' (202:28)> -> __cache_140386070044560
                    __token = 10581
                    try:
                        __zt_tmp = __attrs_140386070041936
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386070044560 = _static_140386186296528('path', u'view/comment_transform_message', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'view/comment_transform_message' (202:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dd613d0> -> __condition
                    __expression = __cache_140386070044560

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n                You can add a comment by filling out the form below. Plain text\n                formatting.\n            ')
                    else:
                        __content = __cache_140386070044560
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</p>\n\n            ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070042896
                    __attrs_140386070042896 = _static_140386247937936

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070041488
                    __default_140386070041488 = _DEFAULT_MARKER

                    # <Value u'view/form/render' (207:40)> -> __cache_140386070044240
                    __token = 10780
                    try:
                        __zt_tmp = __attrs_140386070042896
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386070044240 = _static_140386186296528('path', u'view/form/render', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'view/form/render' (207:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dd61c90> -> __condition
                    __expression = __cache_140386070044240

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div />')
                    else:
                        __content = __cache_140386070044240
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n\n        </fieldset>\n    </div>')
                __append(u'\n\n')
                __i18n_domain = __previous_i18n_domain_140386069340432
            if (__backup_auth_token_140386069341520 is __marker):
                del econtext['auth_token']
            else:
                econtext['auth_token'] = __backup_auth_token_140386069341520
            if (__backup_wtool_140386070741200 is __marker):
                del econtext['wtool']
            else:
                econtext['wtool'] = __backup_wtool_140386070741200
            if (__backup_errors_140386070487888 is __marker):
                del econtext['errors']
            else:
                econtext['errors'] = __backup_errors_140386070487888
            if (__backup_showCommenterImage_140386071167888 is __marker):
                del econtext['showCommenterImage']
            else:
                econtext['showCommenterImage'] = __backup_showCommenterImage_140386071167888
            if (__backup_has_replies_140386078078864 is __marker):
                del econtext['has_replies']
            else:
                econtext['has_replies'] = __backup_has_replies_140386078078864
            if (__backup_replies_140386069239760 is __marker):
                del econtext['replies']
            else:
                econtext['replies'] = __backup_replies_140386069239760
            if (__backup_canReview_140386070483344 is __marker):
                del econtext['canReview']
            else:
                econtext['canReview'] = __backup_canReview_140386070483344
            if (__backup_isAnon_140386070839696 is __marker):
                del econtext['isAnon']
            else:
                econtext['isAnon'] = __backup_isAnon_140386070839696
            if (__backup_isDeleteOwnCommentAllowed_140386069981584 is __marker):
                del econtext['isDeleteOwnCommentAllowed']
            else:
                econtext['isDeleteOwnCommentAllowed'] = __backup_isDeleteOwnCommentAllowed_140386069981584
            if (__backup_isEditCommentAllowed_140386071806352 is __marker):
                del econtext['isEditCommentAllowed']
            else:
                econtext['isEditCommentAllowed'] = __backup_isEditCommentAllowed_140386071806352
            if (__backup_isAnonymousDiscussionAllowed_140386071497232 is __marker):
                del econtext['isAnonymousDiscussionAllowed']
            else:
                econtext['isAnonymousDiscussionAllowed'] = __backup_isAnonymousDiscussionAllowed_140386071497232
            if (__backup_isDiscussionAllowed_140386069973392 is __marker):
                del econtext['isDiscussionAllowed']
            else:
                econtext['isDiscussionAllowed'] = __backup_isDiscussionAllowed_140386069973392
            if (__backup_userHasReplyPermission_140386070486608 is __marker):
                del econtext['userHasReplyPermission']
            else:
                econtext['userHasReplyPermission'] = __backup_userHasReplyPermission_140386070486608
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }