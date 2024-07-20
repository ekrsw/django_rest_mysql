-- MYSQL_USERに権限を付与
-- 今回はadministratorというユーザを指定
GRANT ALL PRIVILEGES ON *.* TO 'administrator'@'%';
FLUSH PRIVILEGES;