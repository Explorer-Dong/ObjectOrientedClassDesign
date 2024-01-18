## 1、选题与架构

### 1.1 题目复现

我选的是第一个题目，下面是题目要求：

数据文件：==课程表、学生表、成绩表==等。

模块：课程管理、学生管理、成绩管理等。

模块中的功能：打开、保存、查询、增加、删除、修改等。

### 1.2 设计要求

对于设计要求中的**网站程序**。我的想法是：

课程设计要求中可以使用除了`C++`之外的面向对象的语言进行编程，同时鼓励网站程序，于是我便选择了基于`python`语言的`flask`框架进行网络编程的课程设计的实现

其中涉及到了**继承**与前端页面的**模板**技术，加上**网站程序**，也算是勉强达到了判定**优秀**技术门槛

### 1.3 组织架构

<img src="https://s2.loli.net/2023/09/06/XlPwT4WsYCNiyr1.png" alt="image-20230906223653279" style="zoom:50%;" />

**后端**采用`flask`框架

（1）通过`flask`特有的蓝图，使用动态路由与视图函数绑定，实现了对不同页面的交互逻辑

（2）通过flask集成的`SQLAlchemy`第三方包，利用`pymysql`驱动器，对数据库进行直接的`CRUD`操作而不用写`SQL`语句

前端采用`Jinja2`、`bootstrip5.3.0`和Ajax`技术`

（1）`Jinja2`实现了传统的静态样式文件（`css`、`js`）与页面文件（`html`）与后端的数据进行绑定

（2）通过集成的`bootstrip`对页面进行渲染与排版，增强阅读性

（3）`Ajax`则实现了在页面不刷新的基础上对数据进行实时的删除操作

**数据库**采用传统的`mysql`

（1）数据库服务器使用的是本地的主机服务器

### 1.4 效果展示[^1]

<img src="https://s2.loli.net/2023/09/06/lyqPm3xjBEZcFGU.gif" alt="演示" style="zoom: 50%;" />

## 2、开发环境

### 2.1 开发工具

编辑器：`Visual Studio Code`

数据库管理工具：`DataGrip 2023.2`

流程图设计软件：`Xmind`

文字稿编辑器：`Typora`

### 2.2 第三方依赖版本

（1）前端

```
bootstrip 5.3.0
```

（2）后端

```
Python 3.11.1
Flask 2.3.2
```

（3）数据库

```
MySQL Server 8.0\bin\mysql.exe  Ver 8.0.34 for Win64 on x86_64
```

## 3、软件代码详解

### 3.1 代码组织架构[^2]

![image-20230822233857683](https://s2.loli.net/2023/09/06/wNYbX2DZupcntSr.png)

<img src="https://s2.loli.net/2023/09/06/OUH3PsSD5m1NfgY.png" alt="image-20230906224124121" style="zoom: 67%;" />

<img src="https://s2.loli.net/2023/09/06/aujf5b8i2IcLZ3Q.png" alt="image-20230906224133491" style="zoom: 67%;" />

```
app.py						# 主接口：汇总全局的代码接口并且是项目运行的起始位置
config.py					# 配置文件：配置数据库连接信息
exts.py						# 数据库对象文件：存储数据库对象SQALcharmy()放置循环引用
models.py					# ORM模型映射类文件：存储表结构的python类对象，一张表一个类对象
blueprints/				# 蓝图py软件包
    base_module.py			# 定义蓝图父类，确定增删改查的具体方法
    course.py				# 定义蓝图子类：课程表，绑定相关的动态路由并连接到相关的前端页面
    score.py				# 定义蓝图子类：分数表，绑定相关的动态路由并连接到相关的前端页面
    student.py				# 定义蓝图子类：学生表，绑定相关的动态路由并连接到相关的前端页面
    __pycache__/			# 存储已编译的字节码文件（自动生成）
        base_module.cpython-311.pyc
        course.cpython-311.pyc
        score.cpython-311.pyc
        student.cpython-311.pyc
static/					# 静态文件文件夹
    css/					# css样式表文件夹
        my.css					# 自定义的css样式表
    js/						# js脚本文件夹
        my.js					# 自定义的js文件，主要是通过Ajax实现交互
templates/				# html页面文件夹
    base.html				# 模板页面
    course-add.html			# 课程表增加页
    course-correct.html		# 课程表修改页
    course.html				# 课程表主页（含搜索功能）
    index.html				# 主页
    score-add.html			# 分数表增加页
    score-correct.html		# 分数表修改页
    score.html				# 分数表主页（含搜索功能）
    student-add.html		# 学生表增加页
    student-correct.html	# 学生表修改页
    student.html			# 学生表主页（含搜索功能）
__pycache__/			# 存储已编译的字节码文件（自动生成）
    app.cpython-311.pyc
    config.cpython-311.pyc
    exts.cpython-311.pyc
    models.cpython-311.pyc
```

### 3.2 逐个模块解析

#### 3.2.1 后端

（1）`app.py`：程序主接口

```python
# 导入相关的第三方库和相应的蓝图对象

# 实例化一个flask对象

# 配置这个flask对象

# 将flask绑定数据库对象

# 将flask绑定不同的蓝图

# 主页路由进入逻辑

# 程序运行
```

（2）`config.py`：配置文件

```python
# 主要是配置flask对象连接的mysql驱动器和服务器
```

（3）`exts.py`：存储数据库对象

```python
# 解决循环引用问题而将SQLAlcharmy对象单独存储在这个文件中
```

（4）`models.py`：存储数据库表的`ORM`映射模型

```python
# 一个表一个类

# 课程类ORM表
class Course(db.Model):
    __tablename__ = "course"
    number = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(20))
    college = db.Column(db.String(20))
    teacher = db.Column(db.String(15))

# 分数类ORM表
class Score(db.Model):
    __tablename__ = "score"
    number = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(10), nullable=True)
    chinese = db.Column(db.Integer, nullable=True)
    math = db.Column(db.Integer, nullable=True)
    english = db.Column(db.Integer, nullable=True)

# 学生类ORM表
class Student(db.Model):
    __tablename__ = "student"
    number = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(10))
    age = db.Column(db.Integer)
    college = db.Column(db.String(10))
    major = db.Column(db.String(10))
```

#### 3.2.2 前端

（1）`static/`：自定义的静态文件

```css
/* 自定义高亮类 */
.highlight {
    background-color: yellow;
    font-weight: bold;
}
```



```js
// 通过Ajax请求实现不刷新页面的删除数据的操作
function confirm_delete_student(student_number) {
  if (confirm("确定要删除学号为 " + student_number + " 的学生数据吗？")) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/student-delete/" + student_number, true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.send("confirmed=true");
  }
}
```

（2）`templates/`：存储`html`界面

flask自带的Jinja2页面继承的逻辑就是将每个页面不同的部分用一个`{% block 块名称 %}{% endblock %}`锁住，用于后续界面的自定义编写

以下只展示**主页**和**课程表**前端页面的代码结构，其余的两个表界面逻辑是一致的，只不过后端传递的数据略有不同而已

```html
<!-- 模板 -->
head部分

title部分		<!-- 继承自定义部分 -->
	<title>{% block title %}{% endblock %}</title>

link部分

body部分

header部分
main部分		<!-- 继承自定义部分 -->
    <main style="flex-grow: 1;">
        <div class="container"> {% block main %} {% endblock %} </div>
    </main>

footer部分
script部分
```

```html
<!-- 主页 -->
{% extends 'base.html' %}

{% block title %}首页{% endblock %}

{% block main %}

三个表界面的链接

{% endblock %}
```



```html
<!-- 表主页 + 搜索功能 -->
{% extends 'base.html' %}

{% block title %}课程表{% endblock %}

{% block main %}

搜索表单

表格展示

{% endblock %}
```

```html
<!-- 增加页 -->
{% extends 'base.html' %}

{% block title %}课程表添加页{% endblock %}

{% block main %}

增加数据的表单

{% endblock %}
```

```html
<!-- 修改页 -->
{% extends 'base.html' %}

{% block title %}学生表{% endblock %}

{% block main %}

修改数据的表单

{% endblock %}
```

#### 3.2.3 蓝图

首先需要有一个蓝图的概念：即存储不同模块的视图函数与动态路由，实现界面视图函数的封装化，提高代码的可维护性与可扩展性

由于每一个模块实现的功能都是一致的，因此我们将增删改查的方法统一实现在一个类中

对于每一个模块在继承上述`BaseModule`类对象时，只需要传递传递相关的表单参数即可

```python
# base_module.py

class BaseModule(Blueprint):
    # 初始化：创建一个Blueprint对象
    pass
    
    # 主页面 + 搜索功能方法实现
    
    # 增加数据方法实现
    
    # 删除数据方法实现
    
    # 修改数据方法实现
```

```python
# course.py

class CourseModule(BaseModule):
    # 初始化bp对象
    def __init__(self):
        super().__init__("course", __name__, url_prefix="/")

    # 数据表主页面传递参数
    def course(self):
        return self.search_items(Course, Course.name, "form_course", "course.html")

    # 数据增加页面传递的参数
    def course_add(self):
        return self.add_item(Course, "course-add.html")

    # 数据删除传递的参数
    def course_delete(self, number):
        return self.delete_item(Course, number)

    # 数据修改页传递的参数
    def course_correct(self, number):
        return self.correct_item(Course, "course-correct.html", number)

bp = CourseModule()

# 增加动态路由，并且将这些路由与上述bp对象进行绑定
bp.add_url_rule("/course/", view_func=bp.course, methods=["GET", "POST"])
bp.add_url_rule("/course-add/", view_func=bp.course_add, methods=["GET", "POST"])
bp.add_url_rule("/course-delete/<string:number>", view_func=bp.course_delete, methods=["GET", "POST"])
bp.add_url_rule("/course-correct/<string:number>", view_func=bp.course_correct, methods=["GET", "POST"])
```


## 4、版本迭代信息

### 4.1 web01

实现一个简单的`flask`程序，启动程序后可以通过本地服务器，在浏览器的渲染下看到内容

### 4.2 web02

在数据库中创建好三个表并且在`flask`程序中进行连接与测试

### 4.3 web03

（1）编写三个数据表展示页面的视图函数

（2）采用`flask`特有的`Jinja2`模板写好前端的大致架构

​		（2.1）定义主页的框架为三个链接，链接到三个数据表操作与展示页面

​		（2.2）为三个数据表展示页面写好模板页面`base.html`通过`Jinja2`进行模板继承

### 4.4 web04

（1）前端

​		（1.1）对传递过来的参数进行表格展示和渲染

（2）后端

​		（2.1）写好`ORM`映射模型

​		（2.2）写好三个数据展示路由中的`get`请求，直接对数据库中的数据进行展示（向前端传递数据库中的数据，通过父类`sqlalchemy`的`query`方法实现数据的抓取，通过`flask`独有的`render_template`向前端传递参数进行渲染

### 4.5 web05

（1）前端

​		（1.1）写好表单用来进行`post`请求，向后端传递搜索的关键词

（2）后端

​		（2.1）打好架构：一个数据表格的四个界面

​				（2.1.1）==数据表页==就是展示所有的数据并且提供==**搜索**功能==，（当前版本已实现）

​				（2.1.2）==增加页==

​				（2.1.3）==删除页==

​				（2.1.4）==修改页==

### 4.6 web06

（1）前端

​		（1.1）去掉删除数据的页面展示，直接取代为一个`js`脚本提示

​		（1.2）写好增加数据和修改数据的前端页面，尤其是表单的结构与参数传递

（2）后端

​		（2.1）写好单个数据表的增删改三个动态路由与视图函数

​		（2.2）根据前端表单传递的数据实现相应的功能

​				（2.2.1）增加和修改需要跳转新页面进行用户表单的输入

​				（2.2.2）**删除**直接点击即可，通过`js`的`Ajax`逻辑将布尔值传递给后端从而实现了确认删除则删除，取消删除则不删除

​		（2.3）对数据表页与**增加**页面和**修改**页面进行互连

### 4.7 web07

完成另外两个数据表的增删改查工作

（1）前端

​		（1.1）将数据表页进行重编写，达到展示：搜索、增加、删除、修改的界面布局

​		（1.2）分别增添：修改和增加数据的页面

（2）后端

​		（2.1）实现数据表主页的搜索功能

​		（2.2）增加学生表和课程表的动态路由和视图函数，即删除、增加和修改的视图函数

> 到此，课程表、学生表和成绩表的打开、保存、增删改查功能已经全部实现
>
> 后续：
>
> - 重构后端代码，进行多文件管理便于后期功能的新增
> - 重构前端代码，多用模板继承，便于后期新增功能时减少代码量
> - 增加静态文件进行页面的布局设计与组件的美化

### 4.8 web08

**将后端架构进行重新设计与布局，便于后期进行扩增与维护**

我们引入新的概念：蓝图。用来存储不同模块的动态路由与视图函数

首先回顾一下当初将所有后端代码存入一个py文件的逻辑

1. 实例化一个`flask`对象`app`

2. 连接到数据库的服务器
3. 使用`SQLAlcharm`对这个`flask`对象进行ORM封`装`
4. 定义多个模块的`ORM`类
5. 定义所有模块的所有动态路由与视图函数

接下来我们对代码进行重构

![image-20230814235443813](https://s2.loli.net/2023/09/06/aKoIPvRGEhY8pSA.png)

1. 我们将`flask`对象的配置放入`config.py`中，因为后续可能会扩增出邮箱登录的功能等等需要配置的内容
2. 我们将`ORM`的封装过程放在了`exts.py`中
3. 我们将所有自定义的`ORM`类放在了`models.py`中，后续如果扩增其他的模块，比如奖学金、研究生模块等等，在当前文件进行扩增
4. 我们将每一个模块的视图函数都存放在了蓝图中，所谓蓝图，其实就是一个用来将视图函数引用到主接口`app.py`的接口模块，蓝图中每一个`py`文件就对应了一个模块中的所有的动态路由与视图函数，从而实现了对每一个模块的分块管理与编写

其中除了蓝图这个新的概念之外，其实还隐藏了一个小细节，就是这个`exts.py`文件的存在意义，是为了解决循环引用问题的

- 首先`app.py`需要用到db对象（即被`SQLAlarchm`实例化的`ORM`对象，以下全部简称为`db`）来封装flask`对象`，那么`app.py`需要引用db`这个`对象

- 其次`models.py`需要引用db对象来进行实际模块中对表的实例化（这一点对于循环引用暂时没有影响）
- 最重要的是蓝图`blueprints`中的每一个模块中所写的视图函数都需要用到db对象来操作数据库中的数据

那么我们就不能像一开始的那样将`db`对象封装写在`app.py`中了，而应该独立出去单独作为一个模块来被引用

以下是模块之间引用的可视化

<img src="https://s2.loli.net/2023/09/06/fTiYWDvgePtIFqV.png" alt="image-20230815005643500" style="zoom:50%;" />



如果加`exts.py`文件，像之前一样在`app.py`中进行数据库实例化`flask`对象的话，就会是下面的引用形式

<img src="https://s2.loli.net/2023/09/06/wVDxJ6vTYLFcBms.png" alt="image-20230815005628488" style="zoom:50%;" />

### 4.9 web09

（1）重构前端代码

​		（1.1）引入前端框架`bootstrip5`

​		（1.2）将所有的页面都进行了`Jinja2`模板继承

### 4.10 web10

（1）发现后端`bug`。即重构了前端代码后，对后端的一些表单有影响

​		（1.1）在执行确认删除后，数据并没有被删除，原因是在重构前端的时候在`html`页面删除的脚本文件不适用于所有的“确认删除”，需要每一个模块重写一个“确认删除”

（2）修改了一些前端样式

### 4.11 web11

（1）发现`bug`

​		（1.1）发现前端`bug`，修复了`course`页面的表单名

​		（1.2）发现前端`bug`，修复传递的参数名

​		（1.3）发现前端`bug`，修复学生修正页面的表单名

（2）重构后端代码

​		（2.1）提炼出全新视图函数基类

​		（2.2）为了传递参数的时候进行变量名的统一，将有关课程表`course`的所有的课程编号字段从原来的`course_order`全部改成了`number`，将所有的课程名从`course_name`全部改成了`name`进行统一

### 4.12 web12

（1）前端：增添了前端的一些样式

（2）后端：引入`add_url_rule`概念，对一个视图类的自定义方法赋予动态路由，从而提高了代码的可维护性与可读性。整个项目的类的数量也成功的达到了7个，符合了课设的标准

（3）发现后端`bug`：修改了后端中学生表和分数表中的一些变量名称和表单名称，错误原因是在拷贝的时候没有将相关的变量修改完全

### 4.13 web13

新增表单数据安全检验功能。由于对数据库sql语言不熟悉，加上SQALcharm对数据库的封装很完备了，故不准备在base_module.py中自定义db的语句来实现增删改的功能。转而新增**数据检验**功能，来完备数据库读写的安全性

（1）后端：安全性扩增与整改

> - **输入长度限制：**添加了一个对关键字长度的验证，确保用户输入不会过长，导致数据库查询性能下
>
> - **输入格式验证：**使用正则表达式对关键字格式进行验证，只允许包含字母、数字和中文，以防止恶意输入
>
> - **防止SQL注入攻击：**去除首尾空白字符

​		（1.1）“增”：除了上述三个以外，再扩增一个防止编号为空的逻辑，因为如果编号为空，后期无法删除或者修改，因为删除和修改都是根据编号唯一索引的

​		（1.2）“删”：未做任何改动

​		（1.3）添加相应的抛出异常提示

（2）前端

​		（2.1）对于传进来的异常参数进行动态的展示与渲染

### 4.14 web14

测试发送验证码功能

（1）邮箱服务器：

​		（1.1）在邮箱中开启IMAP/SMTP服务，生成授权码，用于第三方软件（此处就是当前的flask项目）登录邮箱从而发送邮件

（2）后端：

​		（2.1）在exts.py中创建`Mail()`对象

​		（2.2）在app.py中导入上述对象并且绑定在app()对象上从而初始化

​		（2.3）在蓝图软件包中定义一个登录界面的视图函数模块auth.py，并书写一个固定的发送邮件的视图函数sendemail进行测试

### 4.15 web15

（1）后端

​		（1.1）动态发送验证码。根据用户输入的邮箱（表单）进行动态的发送邮件验证码

​		（1.2）存储验证码前导知识。为了对用户输入的验证码与实际的验证码进行比对，需要将生成的验证码进行存储。可取的最好的方式是缓存，但是为了降低技术难度，采取数据库直接存储的方式进行实现。于是我们就需要新增数据库的ORM模型

​		（1.3）引入数据库迁移概念。由于直接在数据库图形管理软件中进行数据库的操作还是很复杂，就引入新的flask概念，即数据库迁移操作：通过已创建的ORM模型直接映射到服务器中已存在的但是是空的数据库中进行添加新表或者修改表的操作。在将flask对象与db数据库对象绑定后，就在终端中进行如下的三个操作即可完成数据库的创建与迁移

​				（1.3.1）flask db init			初始化迁移环境

​				（1.3.2）flask db migrate	生成迁移脚本

​				（1.3.3）flask db upgrade	更新到数据库中

​		（1.4）实现存储验证码

## 5、设计感想

（1）技术选型原因

选择这个主题和实现方法其实是因为我之前在大创设计网站的时候使用的就是`flask`的微`web`框架，尤其是对于数据库的连接与增删改查也是比较熟悉了，就选择了第一个选题并用网站编程来实现

（2）开发战线

整个开发过称一共进行了15个版本的迭代，在我的不完全统计下，大约使用了12天合计35小时

（3）我的想法

**关于面向对象：**虽然语言不是`C++`，但是整个网站对于面向对象的概念及相关的面向对象应用还是比较多的。比如整个项目都是对于一个集成好的`FLask`对象进行的一系列操作；同时对于数据库的操作也是使用类封装的概念，每一个**表**封装成一个类从而进行后续的操作；而对于视图函数的封装，其实是在进行代码整改和重构的时候才使用的，也算是一种后期的迭代优化吧，即将每一个页面封装成一个类，由于三个数据表的页面逻辑都是差不多的，从而提炼出来了一个全新的基类用于三个页面的继承

**关于多文件：**除了曾经王老师在给我们上课的时候以及课后进行巩固时使用到了多文件体系，在平时的代码练习中，比如`OJ`，都不会用到多文件编写，从而导致了缺乏一个整体架构的能力。在完成本课程设计的过程中，也是理解并且熟悉了多文件编写的理念与实操。首先需要经历的是如何将一个完成的模块进行拆分，接着需要知道如何拆分后的文件联系起来，包括相关对象的导入等，最后就是全神贯注的完成每一个模块的代码工作了。这样不但更加清楚了整个项目的**架构**，也提高了整个项目的**可维护性**和**可扩展性**

**关于迭代：**开发前期的迭代主要通过实现功能为主，到了中期就会因为代码量过大以及逻辑变得复杂而不得不多文件编写，这样进行迭代的时候也会更加的方便。其实最好的迭代方式是使用Git，同时同步更新到云服务器GitHub或者Gitee，但是还是不熟悉相关的协同操作指令，只得通过复制文件的方式进行迭代存储。但是最终也是实现了Git本地管理并且上传到了GitHub！

## 6、参考资料

[python](https://docs.python.org/3/)

[Flask](https://dormousehole.readthedocs.io/en/2.1.2/)

[Bootstrip](https://v5.bootcss.com/docs/getting-started/introduction/)

## 7、附录

[^1]: `video_to_gif.py`（将视频转化为gif持续播放）

```python
import moviepy.editor as mpy

# 视频文件的本地路径
content = mpy.VideoFileClip('D:\Huawei Share\Screenshot\课设.mp4')

# 剪辑0分0秒到0分10秒的片段
c1 = content.subclip((0, 3), (0, 15))

# 设置要输出的分辨率（可以根据需要进行调整）
target_resolution = (1920, 1080)  # 设置为最高清晰度

# 调整分辨率
c1 = c1.resize(target_resolution)

# 将片段的播放速度设置为一倍速
c1 = c1.speedx(1.0)

# 将片段保存为 GIF 图到 python 的默认路径，设置帧率为 24 帧/秒
c1.write_gif("E:\A_web_design\ClassDesine\demo.gif", fps=10)
```

[^2]: `层级信息.py`（展示整个文件夹的体系）

```python
import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

startpath = 'E:\A_web_design\ClassDesine\web12'
list_files(startpath)
```



