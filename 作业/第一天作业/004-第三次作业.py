'''
1. select * from emp
2. select * from emp limit 4
3. select * from emp where id > 24
4. select * from emp where name like 李
5. select * from emp where id > 10 and id <14 or name like 李
6. select * from emp where not id > 24
7. insert into emp values 张国辉，30，18676575678，运维，2007-8-1
8. delete from emp where id > 25
9. update emp set name='sb' where id=24
10.update emp set name='alex' where name like sb
'''

import os

# select * from emp where name like zhang limit 3
# 开始解析,sql四种语句 CURD insert delete update select

def sql_parse(sql):
    '''
    输入sql语句，根据关键字拿到处理的函数，传入sql语句解析
    :param sql:
    :return:
    '''

    func_dict = {
        'insert':insert_sql_parse,
        'delete':delete_sql_parse,
        'update':update_sql_parse,
        'select':select_sql_parse
    }
    #将sql语句以空格为界转化为一个列表
    sql_l = sql.split(' ')
    #获取列表中的第一个值即为字典对应的key，命令可能为大写，全部转化为小写去执行
    sql_order = sql_l[0].lower()
    sql_result = ''
    if sql_order in func_dict:
        sql_result = func_dict[sql_order](sql_l)
    return sql_result


def insert_sql_parse(sql_l):
    '''
    insert语句，定义语法规则字典传入给语句解析函数
    :param sql_l:
    :return:
    '''
    sql_dic = {
        'func': insert_action,
        'insert': [],
        'into': [],
        'values': [],
    }
    return handle_sql_parse(sql_l, sql_dic)

def delete_sql_parse(sql_l):
    '''
    delete语句，定义语法规则字典传入给语句解析函数
    :param sql_l:
    :return:
    '''
    sql_dic = {
        'func': delete_action,
        'delete': [],
        'from': [],
        'where': [],
    }
    return handle_sql_parse(sql_l, sql_dic)

def update_sql_parse(sql_l):
    '''
    update语句，定义语法规则字典传入给语句解析函数
    :param sql_l:
    :return:
    '''
    sql_dic = {
        'func': update_action,
        'update': [],
        'set': [],
        'where': [],
    }
    return handle_sql_parse(sql_l, sql_dic)

def select_sql_parse(sql_l):
    '''
    select语句，定义语法规则字典传入给语句解析函数
    :param sql_l:
    :return:
    '''
    sql_dic = {
        'func':select_action,
        'select': [],
        'from': [],
        'where': [],
        'limit': [],
    }
    return handle_sql_parse(sql_l,sql_dic)

def handle_sql_parse(sql_l,sql_dic):
    '''
    执行sql解析操作，返回sql_dic
    :param sql:
    :param sql_dic:
    :return:
    sql_dic = {
        'func':select_action,
        'select': [],
        'from': [],
        'where': [],
        'limit': [],
    }
    '''
    tag = False
    for item in sql_l:
        #对应的key都转换为小写
        item = item.lower()
        #如果列表中的值和key对应，并且标志位也是true ，就把标志位置反
        if tag and item in sql_dic:
            tag = False
        # 如果列表中的值和key对应，并且标志位也是false ，就把标志位置反，把对用的item赋值给key
        if not tag and item in sql_dic:
            tag = True
            key = item
            continue
        if tag:
            # 标识为true 就把对应的item放到上次循环中对应的key中
            # 根据上一步的item 在字典中取出对应的列表添加元素
            # 以select为例，输入select * from db1.emp where id > 24
            # 返回{'func': <function select_action at 0x10343f598>, 'select': ['*'], 'from': ['db1.emp'], 'where': ['id', '>', '24'], 'limit': []}
            sql_dic[key].append(item)

    if sql_dic.get('where'):
        # 单独处理where,返回之后的字典，就是把where中的比较字符每一个条件处理成了一个数组
        #{'func': < function select_action at 0x102ecf598 >, 'select': ['*'],'from': ['db1.emp'], 'where': [['id', '>', '24']], 'limit': []}
        sql_dic['where'] = sql_where_parse(sql_dic.get('where'))

    return sql_dic

def sql_where_parse(sql_where_l):
    '''
    处理where语句 <class 'list'>: ['id', '>', '10', 'and', 'id', '<14', 'or', 'name', 'like', '李']
    :param sql_where_l:
    :return:
    '''
    result = []
    key = ['and','or','not']
    char = '' #拼接字符显示
    for value in sql_where_l:
        if len(value) == 0:continue
        # 如果是逻辑运算
        if value in key:
            if len(char) != 0:
                char = logic_parse(char)
                result.append(char)
                result.append(value)
                char = '' #每次都清空
        else:
            # 先处理 and or not 这个三个特殊的逻辑运算符，例如上面的例子中，先把id>10作为一个整体放入char中，遍历到and的时候再对char处理
            # 调用logic_parse()函数进行处理，将id>10处理为一个列表['id','>','10']，将列表添加到外围的列表中，同时添加逻辑运算符，清空char
            # 再次运行
            char+=value
    else:
        # 处理最后一个char字符，变为列表
        char = logic_parse(char)
        result.append(char)
    return result


def logic_parse(logic_str):
    '''
    对where中的逻辑运算做处理，返回一个字典，将一个小的条件过滤
    例如 age>10  转换成 ['age','>','10']
    :param login_str:
    :return:
    '''
    key = ['>','<','=']
    result = []
    char = '' #拼接运算符
    flag = False #添加的标识位
    option = '' #记录是否是运算符
    for value in logic_str:
        # age>10，类似于这样的字符串，逐个处理，如果不是运算符，就拼接字符，直到是运算符为止，
        # 将字符添加到数组中，再次判断是否是运算符，拼接运算符，如果不是运算符 就将运算符也添加到数组中，依次循环
        if value in key:
            flag = True
            if len(char) != 0:
                result.append(char)
                char = ''
            option+= value

        if not flag:
            char+=value

        if flag and value not in key:
            flag = False
            result.append(option)
            option = ''
            char+=value
    else:
        result.append(char)

    # 添加对like的解析
    if len(result) == 1:
        # 以like为分割线，转化为数组，
        result = result[0].split('like')
        # 在中间位置添加like
        result.insert(1,'like')

    return result


def sql_action(sql_dic):
    '''
    字典中提取命令 分发给对应的具体指令去执行
    :param sql_dic:
    :return:
    根据传入的字典，调用对用的方法，
    sql_dic = {
        'func':select_action,
        'select': [],
        'from': [],
        'where': [],
        'limit': [],
    }
    '''
    return sql_dic.get('func')(sql_dic)


def select_action(sql_dic):
    '''
    执行select 语句
    :param sql_dic:
    :return:
    '''
    # 解析路径
    if '.' in sql_dic['from'][0]:
        file_path = sql_dic['from'][0].replace('.','/')
    else:
        file_path = sql_dic['from'][0]

    # print(path,table)

    filehandle = open(file_path,'r',encoding='utf-8')
    #分别去解析where limit 还要对比显示文字
    where_resutl = where_action(filehandle,sql_dic['where'])
    filehandle.close()
    # print(where_resutl)
    #添加limit操作
    limit_result = limit_action(where_resutl,sql_dic['limit'])
    #根据搜索添加结果
    search_result = search_action(limit_result,sql_dic['select'])
    return search_result


def delete_action(sql_dic):
    '''
    删除表中的元素，返回删除成功标识
    :param sql_dic:
    :return:
    '''
    # 'func': delete_action,
    # 'delete': [],
    # 'from': [],
    # 'where': [],
    if '.' in sql_dic['from'][0]:
        file_path = sql_dic['from'][0].replace('.','/')
    else:
        file_path = sql_dic['from'][0]
    titles = "id,name,age,phone,dept,enroll_date".split(',')
    # 创建一个临时文件复制指定文件的内容，完成之后，删除源文件，修改临时文件的名称
    with open(file_path,'r',encoding='utf-8') as r_obj,\
            open("%s.txt" %file_path,'w',encoding='utf-8') as w_obj:
        for item in r_obj:
            tem_dic = dict(zip(titles,item.split(',')))
            flag = logic_action(tem_dic,sql_dic['where'])
            if not flag:
                w_obj.write(item)
        w_obj.flush()#立刻从内存刷到硬盘上

    os.remove(file_path)
    os.rename("%s.txt" %file_path,file_path)
    return [['删除成功']]


def update_action(sql_dic):
    '''
    更新对应的数据
    'func': update_action,
        'update': [],
        'set': [],
        'where': [],
    :param sql_dic:
    :return:
    '''
    if '.' in sql_dic['update'][0]:
        file_path = sql_dic['update'][0].replace('.','/')
    else:
        file_path = sql_dic['update'][0]

    set_sql = sql_dic['set'][0].split(',')
    sets = []
    for value in set_sql:
        sets.append(value.split('='))

    titles = "id,name,age,phone,dept,enroll_date".split(',')
    with open(file_path,'r',encoding='utf-8') as r_obj,\
            open('%s.txt' %file_path,'w',encoding='utf-8') as w_obj:
        # 遍历文件内容
        for item in r_obj:
            changeline = []
            # 将每组数据格式化为一个字典
            temp_dic = dict(zip(titles,item.split(',')))
            # 匹配字典中的值是否和where语句中的值相同
            flag = logic_action(temp_dic,sql_dic['where'])
            if flag:
                #在数据库中存在这个数据,拿到数据修改为要设置的值
                for set in sets:
                    k = set[0]
                    v = set[-1].strip("'")
                    temp_dic[k] = v
                for prop in titles:
                    changeline.append(temp_dic[prop])
            # 数组转化为字符串，保存到文件中
            w_obj.write(','.join(changeline))
        w_obj.flush()
    os.remove(file_path)
    os.rename("%s.txt" % file_path, file_path)
    return [['修改成功']]

def insert_action(sql_dic):
    '''
    'func': insert_action,
        'insert': [],
        'into': [],
        'values': [],
    插入新的元素，先要获取最后一行的数据，获取到他的ID，自增长ID
    :param sql_dic:
    :return:
    '''
    if '.' in sql_dic['into'][0]:
        file_path = sql_dic['into'][0].replace('.','/')
    else:
        file_path = sql_dic['into'][0]
    print(file_path)
    titles = "id,name,age,phone,dept,enroll_date".split(',')
    with open(file_path,'ab+') as f_obj:
        # 查询文件的最后一行
        offset = -50
        while True:
            # seek(offset,可选值) 可选值默认为0 从文件开头算 1 从当前位置开始算 2从文件末尾算
            f_obj.seek(offset,2)
            lines = f_obj.readlines()
            if len(lines) > 1:
                last_line = lines[-1]
                break
            offset *= 2
        # 以二进制打开的文件，要对字符串解码
        last_line = last_line.decode(encoding='utf-8')

        #取出最后一行的ID
        temp_dict = dict(zip(titles,last_line.split(',')))
        last_id = int(temp_dict['id'])
        #id加一 添加到数组中
        add_info = sql_dic['values']
        add_info.insert(0,str(last_id+1))
        # 数组转化为字符串
        new_line = ','.join(add_info) + '\n'
        f_obj.write(new_line.encode('utf-8'))
        f_obj.flush()
    return [['添加成功']]


def where_action(filehandler,whele_sql):
    '''
    解析where语句，显示where语句中的执行条件
    :param filehandler:  文件句柄
    :param whele_sql:
    :return:
    '''
    result = []
    titles = 'id,name,age,phone,dept,enroll_data'.split(',')
    if len(whele_sql) != 0:
        for line in filehandler:
            # zip 转化为一个元祖，如果两个队列长度不一致，以短的返回一个元祖
            #tem_dict={'id': '1', 'name': '姬建明', 'age': '25', 'phone': '15201541043', 'dept': '运维', 'enroll_data': '2013-11-01\n'}
            tem_dic = dict(zip(titles,line.split(',')))
            # 处理逻辑运算符中的数据
            logic_res = logic_action(tem_dic,whele_sql)
            # 返回为true的时候，添加数据到列表中
            if logic_res:
                result.append(line.split(','))
    else:
        return filehandler.readlines()

    return result

def logic_action(dic,where_sql):
    '''
    根据字典和sql语句进行匹配,匹配成功返回true  匹配失败返回false
    :param dic:
    :param where_sql:
    :return:
    '''
    # [['id', '>', '10'], 'and', ['id', '<', '14'], 'or', ['name', 'like', '李']]
    result = []
    for item in where_sql:
        # 过滤掉and or not 等逻辑运算符
        if type(item) is list:
            # print(item,dic)
            prop,option,value = item
            # 如果option为= 在后面在拼接一个=
            if option == '=':
                option+='='
            # 判断是否是数字
            if dic[prop].isdigit():
                dic_v = int(dic[prop])
                value = int(value)
            else:
                dic_v = '%s' %dic[prop]

            if option != 'like':
                # 将字符串str当成有效的表达式来求值并返回计算结果
                flag = str(eval("%s%s%s" %(dic_v,option,value)))
            else:
                if value in dic_v:
                    flag = 'True'
                else:
                    flag = 'False'
        # 拼接每一个匹配的值，
        result.append(flag)
        # 添加and进行连接
        result.append('and')
    #删除最后一个and
    result.pop()
    # 计算数组中的表达式的值
    res = eval(' '.join(result))

    # 将result中的bool值进行处理，并计算所有bool值的最后结果
    return res

def limit_action(where_res,limit_l):
    '''
    根据用户输入的limit 返回limit的个数的数组
    :param where_res:
    :param limit_l:
    :return:
    '''
    # 根据传入的limit 做一个切片处理
    if len(limit_l) != 0:
        return where_res[0:int(limit_l[0])]
    else:
        return where_res

def search_action(limit_res,select_l):
    '''
    根据用户的输入，返回特定的数组
    :param limit_res:
    :param select_l:
    :return:
    '''
    result = []
    fileds_l = []
    titles = 'id,name,age,phone,dept,enroll_data'.split(',')
    if select_l[0] == "*":
        fileds_l = titles
        result = limit_res
    else:
        # 循环匹配where和limit语句的执行结果
        for item in limit_res:
            # zip 转化为一个元祖，如果两个队列长度不一致，以短的返回一个元祖
            #{'id': '25', 'name': '张国辉', 'age': '30', 'phone': '18500841678', 'dept': '运维', 'enroll_data': '2007-8-1\n'}
            temp_dict = dict(zip(titles,item))
            condition_l = []

            fileds_l = select_l
            for i in fileds_l:
                condition_l.append(temp_dict[i].strip())
            result.append(condition_l)
    #只返回搜索的字段名
    return (fileds_l,result)


if __name__ == "__main__":
    while True:
        print('''
        支持大小写的SQL语句查询，大写或者小写都可以
        1. select * from db1.emp
        2. select * from db1.emp limit 4
        3. select * from db1.emp where id > 24
        4. select * from db1.emp where name like 李
        5. select * from db1.emp where id > 10 and id <14 or name like 李
        6. select * from db1.emp where not id > 24
        7. insert into db1.emp values 张国辉，30，18676575678，运维，2007-8-1
        8. delete from db1.emp where id > 25
        9. update db1.emp set name='sb' where id=24
        10.update db1.emp set name='alex' where name like sb
        ''')
        sql = input('sql>>:').strip()
        if sql == 'exit' or sql == 'q':
            break
        if len(sql) == 0:continue

        #开始解析sql语句
        sql_dic = sql_parse(sql)
        print(sql_dic)
        # 拿到处理好的sql语句开始查询
        result = sql_action(sql_dic)
        print('*'*30 + '查询结果' + '*'*30)
        for value in result[-1]:
            print(value)
        print('*'*30 + '查询完毕' + '*'*30)
