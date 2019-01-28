### Django内置的字段类型，字段名采用驼峰命名法
| 类型 | 说明 |
| ------ | :------|
| AutoField | 一个自动增加的整数类型字段，通常不需要自己设置Django会添加一个id字段，从1开始计数 </font> |
| BigAutoField | 64位整数类型自增字段，数字范围更大 |
| BigIntegerField | 64位整数字段(非自增字段) |
| BinaryField | 二进制数据类型，使用受限，一般很少用 |
| BooleanField | 布尔类型，默认值为None，如果要接收null值，请使用NullBooleanField |
| CharField | 字符串类型，必须接收一个max_length参数，表示字符串长度不能超过该值 |
| CommaSeparatedIntegerField | 逗号分隔的整数类型，必须接收一个max_length参数，常用于表示较大的金额数目 |
| DateField | class DateField(auto_now=False, auto_now_add=False, **options)日期类型。一个Python中的datetime.date的实例。<br>在HTML中表现为TextInput标签。在admin后台中，Django会帮你自动添加一个JS的日历表和一个“Today”快捷方式，以及附加的日期合法性验证。<br>两个重要参数：（参数互斥，不能共存） auto_now:每当对象被保存时将字段设为当前日期，常用于保存最后修改时间。<br>auto_now_add：每当对象被创建时，设为当前日期，常用于保存创建日期(注意，它是不可修改的)。<br>设置上面两个参数就相当于给field添加了editable=False和blank=True属性。<br>如果想具有修改属性，请用default参数。例子：pub_time = models.DateField(auto_now_add=True)，自动添加发布时间。|
| DateTimeField | 日期时间类型，Python的datetime.datetime的实例，与DateField相比就是多了小时、分和秒的显示，其他的功能、参数、用法、默认值都一样 |
| DecimalField | 固定精度的十进制小数 相当于Python的Decimal实例，必须提供两个指定的参数！参数max_digits：最大的位数，必须大于或等于小数点位数 。decimal_places：小数点位数，精度。 当localize=False时，它在HTML表现为NumberInput标签，否则是text类型。例子：储存最大不超过999，带有2位小数位精度的数，定义如下：models.DecimalField(..., max_digits=5, decimal_places=2)。|
| DurationField | 持续时间类型，存储一定期间的时间长度，类似Python中的timedelta。在不同的数据库实现中有不同的表示方法，常用于时间之间的加减运算，但是在PostgreSQL等数据库之间有兼容性问题 |
| EmailField | 邮箱类型，默认max_length最大长度254，，可以使用Django内置的EmaiValidator进行邮箱地址合法性验证 | 
| FileField | ``` class FileField(upload_to=None,max_length=100,**options)```上传文件类型，|
| FilePathField | 文件路径类型 |
| FloatField | 浮点数类型 |
| ImageField | 图像类型 |
| IntegerField | 整数类型，最常用的字段之一 |
| GenericIPAddressField | class GenericIPAddressField(protocol='both', unpack_ipv4=False, **options)[source],IPV4或者IPV6地址，字符串形式，例如192.0.2.30或者2a02:42fe::4在HTML中表现为TextInput标签。参数protocol默认值为‘both’，可选‘IPv4’或者‘IPv6’，表示你的IP地址类型。 |
| NullBooleanField | 类似布尔字段，只不过额外允许NULL作为选项之一 | 
| PositiveIntegerField | 正整数字段
| PositiveSmallIntegerField | 较小的正整数字段 |
| SlugField |  slug是一个新闻行业的术语。一个slug就是一个某种东西的简短标签，包含字母、数字、下划线或者连接线，通常用于URLs中。可以设置max_length参数，默认为50。|
| SmallIntegerField | 小整数 |
| TextField | 大量的文本内容 |
| TimeField | 时间字段，Python中的datetime.time的实例，只作用于小时、分和秒 |
| URLField | 一个用于保存URL地址的字符串类型，默认最大长度为200 |
| UUIDField | 用于保存通用唯一识别码 | 

### 自己关联自己的的外键
##### 1.多对一的关系，通常被称为外键。
class ForeignKey(to,on_delete,**options)[source],外键需要两个位置参数，一个是关联的模型，一个是on_delete选项 <font color="#ff0000">外键要设置在定义多的一方</font>
如果要创建一个递归的外键，也就是自己关联自己的的外键，使用下面的方法：
关联对象改为```'self'``` 如下<br/>
```models.ForeignKey('self', on_delete=models.CASCADE)```