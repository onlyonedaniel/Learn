# DataVis
数据可视化
# 数据库
## 1.创建数据库
```sql 
  create database dataVis default charset utf8;
```
## 2.创建用户
```sql 
create USER 'tester'@'%' identified by 'tester';
```
## 3.授权
```sql 
grant privileges on dataVis To 'tester'@'%';
```
## 4.权限刷新
```sql 
flush privileges;
```
## 5.生成数据库迁移文件
```console
  python3 manage.py makemigrations
```
## 6.迁移
```console
  python3 manage.py migrate
```
# 前端启动 dev
```bash
  npm install 
  vue ui
  run dev
```
#后端启动
```bash
  python3 manage.py runserver 127.0.0.1:8081
```
