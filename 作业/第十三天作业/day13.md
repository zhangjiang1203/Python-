上周内容:

	为啥需要线程:
		1. 进程的缺点:
			- 开启进程和关闭进程,资源的开销是非常大的
			- cpu在进程之间进行切换的时候,花费的时间比较长
		
		2. 线程:
			- 开启线程的速度以及开启线程所需要向操作系统申请的资源,非常的少
			
			- 两种开启线程的方式:
				from threading import Thread
				
				def task():
					print('xxxxxxx')
				
				t = Thread(target=task, args=(x,))
				t.start()
				
			- 线程的相关属性:
				t = Thread(target=task, args=(x,))
				t.start()
				t.name : 线程的名称
				t.active_count: 活跃的线程数
				current_thread : 当前的线程实例
			
			- 守护线程:
				守护进程:
					守护的是父进程
				
				守护线程:
					守护的是进程内的所有的非守护线程
					
今日内容:
	1. 协程
		
		a. 什么是协程?
			其实就是一个线程
		
		b. 为啥要使用协程?
			
			进程: 多进程,执行多个任务的时候, 
				缺点:
					- 开启进程和关闭进程,资源的开销是非常大的
					-  cpu在进程之间进行切换的时候,花费的时间比较长, 需要保存任务的执行状态
				
			线程:
				多线程,执行多个任务
				三个线程, 执行三个任务
				
			思考:	
				三个任务,能不能只开一个线程,然后执行三个任务?
				实现一个, 单线程并发的效果 , 就叫协程
				
			协程的作用:
				单线程并发的效果(yield)
				应用程序里边控制cpu进行上下文的切换
				
			程序引入协程的话:
				优点:
					相对于操作系统控制CPU的切换,消耗时间少一些
					
				缺点:
					就必须要去监控程序里面的所有的IO情况,如果不作处理的话, 后面所有的任务都不会执行
			
			什么时候使用协程比较好?
				遇到IO的时候, 单线程下使用协程比较好
				
			
	2. MySQL
		
	     上节回顾:
			
			MySQL的安装:
				bin:
					mysqld : 服务端的执行文件
					mysql  : 客户端连接服务端的工具
			
			
			文件夹 (数据库):
				文件(数据表):
					数据行
					
			数据库的增删改查(crud):
				增:
					create database db1;
					推荐:create database db1 charset utf8;
				删:
					drop database db1;
				
				改:
					先删掉, 在新增
				
				查:
					show databases;
			
			数据表的增删改查:
				增:
					create table user(
						# 列名称 列类型   
						id int unsigned auto_increment primary key,
						name varchar(32) not null default '',
						age int not null default 1
					)charset = utf8
					
					ps :
						主键索引: 这一列的数据不能空, 加速查找
						char(32) :  列的值是固定的
						varchar(32) : 列的值是变长的
						not null: 推荐加上
							#select * from user where name is not null;
							select * from user where name != '';
					
					数值型:
						int 
						tinyint
						smallint
						mediumint
						bigint
					
				删除:
					drop table user;
				更新:
					表名:
						rename table oldtb to newtb;
					
					列类型:
						更改: alter table xxx change name name char(32) not null default '';
						删除: alter table xxx drop name;
						增加: alter table xxx add depertment  vachar(32) not null default ''; 
				
				查:
					show create table xxx;
			
			数据行:
				create table test1 like test;
				增:
					insert into xxx (name, age) values ('xxx', 12);
					insert into xxx (name, age) values ('xxx', 12), ('ssss', 13),('dddd', 14);
					insert into xxx values select * from test;
				
				删:
					delete from xxx;
					delete from xxx where id > 12;
					delete from xxx where name = 'xxxx' and/or id>12;
				
				改:
					update table xxxx set name='xxxx' ;
					update table xxxx set name='xxxx' where 条件
					update table xxxx set name='xxxx',age=23 where 条件
				
				查:
					select * from xxx;
					select name, age from xxxx;
					
					select * from xxx where  id  in (1,2,3,4);
					select * from xxx where  id  not in (1,2,3,4);
					select * from xxx where  id  between 1 and 4;
					
					select * from xxx where id > 10 and id < 20;
					
					通配符(模糊查询):
						% : 代表所有的字符
						_ : 代表一个字符
						select * from xxx where name like "n%" ; # nndsjadjsabjdsbajd
						select * from xxx where name like "%n%" ; # nndsjadjsabjdsbajd
						select * from xxx where name like "n_";  # ns, nb
						
						ps:
							- sphinx
					限制: (********************************)
						
						select * from xxx limit 5; 
					
						select * from xxx limit offset(4), 取几行(5);
						
						每页显示 5 条数据
						page = 1     limit 0,  10
						page = 2     limit 10, 10
						page = 3     limit 20, 10
						.....
						page = n     select * from user where xxx limit (n-1)*5, 5
						
					
					排序: (***********************************)
						
						select * from xxx order by age ;
						select * from xxx order by age asc;
						select * from xxx order by age desc;
						
						select * from xxx order by age desc, id asc;  # 优先按照age降序排列, 如果age有一样的, 就会按照id进行升序排列
					

					分组:(************)
						
						年龄相同的人一共有多少个?
							select count(id), age from test group by age;
							select count(id) as cnt , age from test group by age;
								count()
								max()
								min()
								avg()
								sum()
							select count(id) as cnt , age from test group by age having cnt < 2;
						
							where 和 having的区别:
								- where 和 having都是过滤数据
								- where 是过滤的原生的数据
								- having 是过滤group by 之后的数据, 进行二次筛选 .
								- having和group by配合使用的
						
							select count(id) as cnt , age from test where id>6 group by age having cnt < 2;
					
					where > group by > order by > limit
					
					select count(id) as cnt, age from test where id>6 group by age having cnt < 2 order by age desc  limit 2,5;
					
					存储引擎: (*********)
						
						- MyISAM
							mysql 5.3
							create table user(
								# 列名称 列类型   
								id int unsigned auto_increment primary key,
								name varchar(32) not null default '',
								age int not null default 1
							)charset = utf8 engine = MyISAM
							mysql 5.5 
							create table user(
								# 列名称 列类型   
								id int unsigned auto_increment primary key,
								name varchar(32) not null default '',
								age int not null default 1
							)charset = utf8
							ENGINE=InnoDB
							
						- Innodb
							
						比较:
							- InnoDB支持事务, Myisam不支持事务
							- MyISAM 表锁 , Innodb行锁
						
						- Memory
						
					事务:
						作用:保证一组sql语句完整的执行
					
						例子:
							吴秀波   5000 - 500 = 4500
						断电:	
							小三儿   5000 + 500 = 5500
							
						
						create table user1(
							id int unsigned auto_increment primary key,
							name varchar(32) not null default '', 
							money int not null default 0
						)charset utf8;
						
						insert into user1 (name, money) values('吴秀波', 5000), ('小三儿', 5000);
						
						开启事务:
							start transcation;
						
							update user1 set money = 4500 where id=1;
							update user1 set money = 5500 where id=2;
						
						提交事物:
							commit;
						回滚:
							rollback;
						
						
					外键: (***********************************)
					
						一对多:
							作用:
								- 减少数据的冗余
								- 约束这一列
							
							user:
								id	name	depertment_id
								1	root1	1
								2	root2	2
								3	root3	3
								4	root4	2
								5	root5	3
								6	root6	1
							
							create table user2(
								id int unsigned auto_increment primary key,
								name varchar(32) not null default '', 
								depertment_id int unsigned not null default 1,
								constraint fk_user_dep foreign key user2(`depertment_id`) references depertment (`id`)
							)charset utf8;
							
							insert into user2 (name, depertment_id) values ('alex', 1), ('eagon', 2),('stephen',1),('tank',3),('zekai',2),('lxx',1);
							
							create table depertment(
								id int unsigned auto_increment primary key,
								dep_name varchar(32) not null default ''
							)charset utf8;
							
							insert into depertment (dep_name) values ('公关部'), ('保安部'), ('IT部');
							
							depertment:	
								id	dep_name
								1	公关部
								2	关关部
								3	公公部
						
						一对一:
							user:
								id	name	 
								1	root1	/root1/
								2	root2	/root2/
								3	root3	/../
								4	root4	/../
								5	root5	/../
								6	root6	/../
								
							create table user2(
								id int unsigned auto_increment primary key,
								name varchar(32) not null default '', 	
									
							)charset utf8;	
								
							create table article(
								id int unsigned auto_increment primary key,
								url varchar(32) not null default '', 
								uid int not null default 1,
								constraint fk_user2_article foreign key (`uid`) references user2 (`id`),
								unique(uid)
							)charset utf8;
							
							article :
											FK + 唯一约束
								id  url       uid
								1   /root1/    1
								2   /root2/    2
								3   /root3/    3
								4   /root4/    4
								#5   /xxxxx/    4
								
							联合唯一索引:
								unique(uid, url)
						
						多对多:
							
							user 
								id   name     gender
								1    eagon      male
								2    xxxx       male
								3    stephen    male
								4    凤姐       female
								5    凤妹       female
							
							daterecord:
									  FK    FK
								id    bid   gid 
								 1     1     4
								 2     1     5
								 3     2     4
								 4     2     5
								 5     5     3
								 5     5     1
								 5     5     2
								 #6     1     1
						
							
							
							user 
								id   name
								1     root1
							
							
							create table user(
								id int  auto_increment primary key,
								name varchar(32) not null default ''
							)charset utf8;
							
							create table host(
								id int  auto_increment primary key,
								hostname varchar(32) not null default ''		
							)charset utf8;	
							
							create table user2host(
								id int  auto_increment primary key,
								uid int not null default 1,
								hid int not null default 1,
								constraint fk_user foreign key (`uid`) references user (`id`),
								constraint fk_host foreign key (`hid`) references host (`id`)
							)charset utf8;
							
							insert into user (name) values ('alex'),('stephen'), ('zekai'), ('eagon');
							insert into host (hostname) values ('c1.com'),('c2.com'), ('c3.com'), ('c4.com'), ('c5.com'), ('c6.com');
							
							insert into user2host (uid, hid) values (1,1), (1,2),(1,3),(2,3),(2,4),(3,1),(3,5),(3,6);
							
						连表查询:
							inner join
							
								select user2.name, depertment.dep_name from user2 inner join depertment on user2.depertment_id=depertment.id;
							
							left join:
								select * from user2 
								left join 
								depertment 
								on user2.depertment_id=depertment.id
								left join 
								xxxx
								on 
								左边的表数据全显示
								
							right join:
								select * from user2 right join depertment on user2.depertment_id=depertment.id
								右边的表全显示
								
							实际的工作中:
								- 如果业务是对外的, 成百上千万的用户量, 不建议使用连表
								- 如果业务是对内的, 差不多几百个人访问量, 就可以使用
							
							
					
					python操作MySQL:
						pymysql 
							- conn = pymysql.connect(host='localhost', user='root', password='', database='db1', port=3306, charset='utf8',cursorclass=pymysql.cursors.DictCursor)

							- cursor().execute(sql)
							
							- conn.commit()
					
					
			视图:
				创建视图:
					create view xxx as select name, age from userinfo;
					
					select * from xxx;
				
				删除视图:
					drop view  xxx;
				
				更新的话:
					先删除, 在创建
			
			
			
			
			函数:
				聚合函数:
					group by:
						sum()
						count()
						avg()
						max()
						min()
				
				内置函数:
					禁止在MySQL中去使用函数
					
			触发器:
				
			
			索引: (*****************************)
			
				作用: 加速查找
				
				类型: 
					hash (memory)
					btree (innodb, MyISAM)
				种类:
					主键索引 : 加速查找 + 不能为空 + 自增
					唯一索引 : 加速查找 + 不能重复 + 可以为null
					普通索引 : 加速查找
					联合索引 : 加速查找
				
				
					create table user1(
						id int unsigned auto_increment primary key,
						name varchar(32) not null default '', 
						money int not null default 0,
						index xxx ('name'),
						index xxx ('name', 'money') 
					)charset utf8;
					
					select * from user1  where name = 'xxxx' and money= 'xxxx';
					
					使用联合索引 > 单个索引
				
				
				表里面有索引, 添加数据或者删除数据的时候,效率是很低
				
				慢日志:
				    slow_query_log = OFF  #是否开启慢日志记录
				    long_query_time = 2  # 时间限制，超过此时间就记录
				    show_query_log_file = /usr/slow.log 日志文件
				    注:查看当前的配置信息
				       show variables like '%query%"'
				       修改当前配置信息
				       set global 变量名 = 值
					开启后,会记录超过sql最大执行时间的sql语句 
					
					
					
				    
					
					
				
			
			
			
			
			
			
			
			
			
			
			
			
			
			
				

				
						
						
						
						
						
						
							
							
							
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
					
					
						
						
						
						
						
						
					
					
					
					
					
					
					
					
					
					
					
					
					
					
			
		
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	