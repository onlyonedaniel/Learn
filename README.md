# DataVis
数据可视化
#数据库
##1.创建数据库
·
  create database dataVis default charset utf8;
·
##2.创建用户
·
create USER 'tester'@'%' identified by 'tester';
·
##3.授权
·
grant privileges on dataVis To 'tester'@'%';
·
##4.权限刷新
·
flush privileges;
·