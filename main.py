x = """
create table 订单表 ( 订单编号 int primary key, )
"""

y = """
create table 订单表
(
订单编号 int primary key,
)
"""

print(x == y)