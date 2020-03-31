MYSQL_HOST ?= mysql

wait-mysql: # ://{user}:{password}@{host}/{database} だと思うけど・・・
	dockerize -wait tcp://$(MYSQL_HOST):3306 -timeout 10s