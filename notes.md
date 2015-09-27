
- django-admin startproject mysite
-  python manage.py startapp polls


python manage.py migrate

python manage.py makemigrations polls

python manage.py sqlmigrate polls 0001

面的章节中深入地对它进行讲解，但是现在，记住这三步来实现模型的变更：

- 修改你的模型（在models.py中）。
- 运行python manage.py makemigrations 来为这些修改创建迁移文件
- 运行python manage.py migrate 以运用这些改变到数据库中。

https://en.wikipedia.org/wiki/Regular_expression

\w	\w	[A-Za-z0-9_]	Alphanumeric characters plus "_"
\W	\W	[^A-Za-z0-9_]	Non-word characters
[:alpha:]			\a	[A-Za-z]	Alphabetic characters
[:blank:]			\s	[ \t]	Space and tab