# plone-tcp-v1

### 我的plone源代码地址：https://github.com/JiahaoLiENSE/plone-tcp-v1.git

### 安装新插件官网：https://training.plone.org/mastering-plone-5/eggs1.html

#### 注：我新的包是命名为plone.tcp, 而在这里步骤写的是my.tcpaddon，是根据官网步骤上的名字来命名

### 在以下这个路径创建文件：
`cd plone/zinstance/src/my.tcpaddon/src/my/tcpaddon/`
### 创建文件夹 content，在里面创建 content.py：
`mkdir content`, `nano content.py`
### 往content.py里面添加：
```python
from plone.dexterity.content import Item
from zope.interface import implementer
from plone.supermodel import model

class IMyTCPContent(model.Schema):
    # Define fields for your content type here
    tcp_data = schema.Text(title="TCP Data")

@implementer(IMyTCPContent)
class MyTCPContent(Item):
    pass
```
### 接下来在 `my.tcpaddon/src/my/tcpaddon/` 里更新 `configure.zcml`:
```xml
<?xml version="1.0"?>
<configure xmlns="http://namespaces.zope.org/zope"
           xmlns:browser="http://namespaces.zope.org/browser"
           i18n_domain="my.tcpaddon">

  <include package="plone.app.dexterity" file="meta.zcml" />

  <browser:page
      for="my.tcpaddon.content.IMyTCPContent"
      name="tcp-form"
      template="templates/tcp_form.pt"
      permission="zope2.View"
      />

</configure>
```

### 创建 `templates`文件夹 和它的文件 `tcp_form.pt`, 位置：`my.tcpaddon/src/my/tcpaddon/`:
```html
<metal:use-macro
  metal:macro="plone"
  define-macro="main">

  <form action="tcp-form" method="POST">
    <tal:block tal:repeat="field view/fields">
      <tal:block tal:condition="not field.widget.ignoreRequest(view)"
                 tal:content="field/missing_value"
                 tal:define="name field/getName;
                             value view/request/fields/name;
                             widget field.widget;
                             required field.required;
                             error view/error_for(field)"
                 tal:define="hidden_string widget is widget_hidden and
                                     'hidden' or ''"
                 tal:attributes="name name;
                                 id field/id;
                                 class string:field string:${hidden_string};
                                 required required;
                                 value python:value or widget/multiSelected;
                                 autofocus widget/isFocus;
                                 maxlength widget/maxLength;
                                 tabindex widget/tabindex;
                                 size widget/size;
                                 checked widget/checked;
                                 type widget/inputType;
                                 disabled field/readonly;
                                 autofocus string:${widget/mode} is 'widget' and
                                           field/autofocus_allowed or
                                           string:False;
                                 tal:attributes-1 string:pattern python:widget/getPattern;
                                 tal:attributes-2 string:title widget/title;
                                 tal:attributes-3 string:description widget/description">

        <tal:div tal:condition="field.widget.mode is 'hidden'"
                 class="hidden">
          <input tal:attributes="name name;
                                 value python:value;
                                 type 'hidden'">
        </tal:div>

        <tal:div tal:condition="hidden_string is not 'hidden'"
                 tal:attributes="class widget_class widget/getCSSClass;
                                 id field/id">
          <label tal:attributes="for field/id;
                                 class widget_class widget/getCSSClass">
            ${field.title}
          </label>
          <div tal:replace="structure widget" />
        </tal:div>

        <tal:block tal:condition="error"
                   tal:repeat="msg error">
          <div tal:attributes="class string:message_type error/type"
               tal:content="msg"></div>
        </tal:block>

      </tal:block>
      <input type="submit" value="Submit">
    </form>

</metal:use-macro>
```

### 更新 `setup.py`, 位置：`plone/zinstance/src/my.tcpaddon/setup.py`:
```python
install_requires=[
    'setuptools',
    'plone.dexterity',
    'plone.app.dexterity',
    'plone.supermodel',
],
```

### 更新 `plone/zinstance/src/my.tcpaddon/__init__.py` 来注册content:
```python
# Import your content type class
from my.tcpaddon.content import MyTCPContent

def initialize(context):
    # Register your content type with Plone
    from plone.dexterity import ftidata
    ftidata.register()
    context.registerClass(
        MyTCPContent,
        constructors=(MyTCPContent,),
        permission='my.tcpaddon: Add My TCP Content',
        )
```

### 来写TCP UI view，首先创建 `tcpview.py`, 位置：`plone/zinstance/src/my.tcpaddon/src/my/tcpaddon/`
```python
from Products.Five.browser import BrowserView
from my.tcpaddon.content import IMyTCPContent
from zope.interface import implements

class TCPView(BrowserView):
    implements(ITCPView)

    def __call__(self):
        if self.request.method == 'POST':
            data = self.request.form.get('tcp_data')
            self.send_tcp_request(data)
            return 'TCP request sent'

        return self.index()

    def send_tcp_request(self, data):
        import socket

        host = '主机服务器ip地址'
        port = '端口'

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client_socket.connect((host, port))
            client_socket.sendall(data.encode())
            response = client_socket.recv(1024)
            # Process the response or save it if needed

        finally:
            client_socket.close()
```

### 再回过头更新 `configure.zcml`, 位置：`plone/zinstance/src/my.tcpaddon/src/my/tcpaddon/configure.zcml`:
```xml
<?xml version="1.0"?>
<configure xmlns="http://namespaces.zope.org/zope"
           xmlns:browser="http://namespaces.zope.org/browser"
           i18n_domain="my.tcpaddon">

  <include package="plone.app.dexterity" file="meta.zcml" />

  <browser:page
      for="my.tcpaddon.content.IMyTCPContent"
      name="tcp-form"
      template="templates/tcp_form.pt"
      permission="zope2.View"
      />

  <browser:page
      for="my.tcpaddon.content.IMyTCPContent"
      name="tcp-form"
      class="my.tcpaddon.tcpview.TCPView"
      permission="zope2.View"
      />

</configure>
```

### 添加到 `buildout.cfg`, 位置：`plone/zinstance/`:
```cfg
[buildout]
eggs =
    my.tcpaddon
zcml =
    my.tcpaddon
```

### build
```shell
$ ./bin/buildout
```
