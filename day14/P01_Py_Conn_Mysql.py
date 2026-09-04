"""
    该案例演示了python操作mysql数据库
"""
"""
cursorclass=pymysql.cursors.DictCursor 是 PyMySQL 连接参数中的一个设置，它的作用是：指定该连接默认使用的游标（Cursor）类型为“字典游标”。
默认游标（pymysql.cursors.Cursor）：执行查询后，fetchone()、fetchall() 返回的是元组（tuple），例如 (1, '张三', '2024-01-01')。
你需要通过索引（如 row[1]）来获取字段值，容易出错且可读性差。
字典游标（DictCursor）：返回的是字典（dict），例如 {'id': 1, 'name': '张三', 'created_at': '2024-01-01'}。
你可以通过字段名（如 row['name']）来取值，代码更清晰、更健壮（不依赖字段顺序）。
"""
import pymysql


# 获取连接
def get_connection():
    try:
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='aaaaaa',
            database='atguigu',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except:
        print("获取连接的时候发生了异常")

# 从数据库表中查询数据
def select_data(conn):
    # 创建游标对象
    my_cursor = conn.cursor()
    # 执行sql语句
    sql = "select * from t_department"
    my_cursor.execute(sql)
    # 获取查询结果
    result = my_cursor.fetchall()
    for row in result:
        print(row)
    my_cursor.close()


def insert_data(conn):
  my_c = conn.cursor()
  sql = "insert into t_department values (10,'test','testtest')"
  my_c.execute(sql)
  # 提交事务
  conn.commit()
  my_c.close()

def delete_data(conn):
  my_c = conn.cursor()
  sql = "delete from t_department where did=10"
  my_c.execute(sql)
  # 提交事务
  conn.commit()
  my_c.close()

def update_data(conn):
  my_c = conn.cursor()
  sql = "update t_department set dname='dev' where did=10"
  my_c.execute(sql)
  # 提交事务
  conn.commit()
  my_c.close()

if __name__ == '__main__':
  conn = get_connection()
  # insert_data(conn)
  # update_data(conn)
  delete_data(conn)
  select_data(conn)
  conn.close()