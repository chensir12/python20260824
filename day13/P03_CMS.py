import re
import time

from day13.P02_Customer import Customer


class CMS:
  """客户管理系统类"""

  def __init__(self):
    """初始化客户管理系统"""
    self.customer_id_dict = {} # 客户id字典
    self.customer_name_dict = {} # 客户姓名字典

  def display_menu(self):
    """显示菜单"""
    print(
      """
      ----------客户管理系统----------
           1. 添加客户
           2. 删除客户
           3. 修改客户
           4. 查询客户
           5. 显示客户
           6. 退出
      """
    )

  def add_customer_id(self):
    """添加客户id"""
    # 输入客户id，没问题则返回客户id，有问题则返回False
    customer_id = "None"
    for i in range(3):
      if i < 2:
        # 前2次输入，输入错误则重新输入
        customer_id = input("请输入客户id:")
        # 检查客户id是否合法
        if Customer.check_id(customer_id):
          break
        else:
          print("客户id必须为纯数字")
      else:
        # 第3次输入，输入错误则终止添加
        customer_id = input("最后一次机会，请输入客户id:")
        # 检查客户id是否合法
        if Customer.check_id(customer_id):
          break
        else:
          print("终止添加客户")
          return False
    # 检查客户id是否已存在
    if customer_id in self.customer_id_dict:
      # 之前存在则终止添加
      print("客户id已存在，终止添加客户")
      return False
    else:
      # 之前不存在则返回客户id
      return customer_id

  def add_customer_name(self):
    """添加客户姓名"""
    # 输入客户姓名，没问题则返回客户姓名，有问题则返回False
    customer_name = "None"
    for i in range(3):
      if i < 2:
        # 前2次输入，输入错误则重新输入
        customer_name = input("请输入客户姓名:")
        # 检查客户姓名是否合法
        if Customer.check_name(customer_name):
          break
        else:
          print("客户姓名必须为字符")
      else:
        # 第3次输入，输入错误则终止添加
        customer_name = input("最后一次机会，请输入客户姓名:")
        # 检查客户姓名是否合法
        if Customer.check_name(customer_name):
          break
        else:
          print("终止添加客户")
          return False
    return customer_name

  def set_customer_age(self):
    """添加或修改客户年龄"""
    # 输入客户年龄，没问题则返回客户年龄，有问题则返回False
    customer_age = input("请输入客户年龄:")
    # 检查客户年龄是否合法
    if Customer.check_age(customer_age):
      return customer_age
    else:
      print("好吧，暂时不添加年龄也可以")
    return "None"

  def set_customer_phone(self):
    """添加或修改客户电话"""
    # 输入客户电话，没问题则返回客户电话，有问题则返回False
    customer_phone = input("请输入客户电话:")
    # 检查客户电话是否合法
    if Customer.check_phone(customer_phone):
      return customer_phone
    elif re.search(r"^[\d-]+$", customer_phone):
      print("这个电话号码不太常见，但是可以添加")
      return customer_phone
    else:
      print("好吧，暂时不添加电话号码也可以")
    return "None"

  def set_customer_email(self):
    """添加或修改客户邮箱"""
    # 输入客户邮箱，没问题则返回客户邮箱，有问题则返回False
    customer_email = input("请输入客户邮箱:")
    # 检查客户邮箱是否合法
    if Customer.check_email(customer_email):
      print("邮箱似乎合法")
      return customer_email
    else:
      print("好吧，暂时不添加邮箱也可以")
    return "None"

  def add_customer(self):
    """添加客户"""
    # 添加客户id
    if not (customer_id := self.add_customer_id()):
      return
    # 添加客户姓名
    if not (customer_name := self.add_customer_name()):
      return
    # 添加客户年龄
    customer_age = self.set_customer_age()
    # 添加客户电话
    customer_phone = self.set_customer_phone()
    # 添加客户邮箱
    customer_email = self.set_customer_email()
    # 创建客户对象
    customer = Customer(customer_id, customer_name, customer_age, customer_phone, customer_email)
    # 将客户对象添加到客户id字典中
    self.customer_id_dict[customer_id] = customer
    # 将客户对象添加到客户姓名字典中，每个姓名key对应一个字典value
    # 每个字典value包含此姓名的所有客户，字典value的key为客户id，value为客户对象
    customer_inner_dict = self.customer_name_dict.get(customer_name)
    if customer_inner_dict is None:
      self.customer_name_dict[customer_name] = {customer_id: customer}
    else:
      customer_inner_dict[customer_id] = customer
    print(f'添加客户{customer_id}成功')

  def delete_customer(self):
    """删除客户"""
    # 获取输入的客户id
    customer_id = input("请输入要删除的客户id:")
    # 检查客户id是否合法
    if not Customer.check_id(customer_id):
      print("客户id必须为纯数字")
      print("终止删除客户")
      return
    # 检查客户id是否存在
    if customer_id not in self.customer_id_dict:
      print("客户id不存在")
      print("终止删除客户")
      return
    else:
      customer_name = self.customer_id_dict[customer_id].name
    # 将客户id从客户id字典中删除
    del self.customer_id_dict[customer_id]
    # 将客户id从客户姓名字典中删除
    customer_inner_dict = self.customer_name_dict.get(customer_name)
    del customer_inner_dict[customer_id]
    if len(customer_inner_dict)==0:
      del self.customer_name_dict[customer_name]

    print(f'客户{customer_id}删除完毕')

  def update_customer(self):
    """修改客户"""
    # 获取输入的客户id
    customer_id = input("请输入要修改的客户id:")
    # 检查客户id是否合法
    if not Customer.check_id(customer_id):
      print("客户id必须为纯数字")
      print("终止修改客户")
      return
    # 检查客户id是否存在
    if customer_id not in self.customer_id_dict:
      print("客户id不存在")
      print("终止修改客户")
      return
    # 修改客户年龄
    print(f'客户{customer_id}的历史年龄:', self.customer_id_dict[customer_id].age)
    if (customer_age := self.set_customer_age()) != "None":
      self.customer_id_dict[customer_id].age = customer_age
    # 修改客户电话
    print(f'客户{customer_id}的历史电话:', self.customer_id_dict[customer_id].phone)
    if (customer_phone := self.set_customer_phone()) != "None":
      self.customer_id_dict[customer_id].phone = customer_phone
    # 修改客户邮箱
    print(f'客户{customer_id}的历史邮箱:', self.customer_id_dict[customer_id].email)
    if (customer_email := self.set_customer_email()) != "None":
      self.customer_id_dict[customer_id].email = customer_email
    print(f'客户{customer_id}修改完毕')

  def search_customer(self):
    """查询客户"""
    customer_info = input("请输入要查询的客户id或姓名:")
    if Customer.check_id(customer_info):
      # 如果输入的是id
      # 检查客户id是否存在
      if customer_info in self.customer_id_dict:
        print(self.customer_id_dict[customer_info])
      else:
        print("客户id不存在")
    elif Customer.check_name(customer_info):
      # 如果输入的是姓名
      # 检查客户姓名是否存在
      if customer_info in self.customer_name_dict:
        for customer_id in self.customer_name_dict[customer_info]:
          print(self.customer_name_dict[customer_info][customer_id])
      else:
        print("客户姓名不存在")
    else:
      print("输入的好像不是客户id或姓名")

  def display_customer(self):
    """打印所有客户信息"""
    if len(self.customer_id_dict) == 0:
      print("暂无客户信息")
    for i in self.customer_id_dict:
      print(self.customer_id_dict[i])

  def start(self):
    """启动客户管理系统"""
    try:
      while True:
        self.display_menu()
        choice = input("<< ")
        match choice:
          case "1":
            self.add_customer()
          case "2":
            self.delete_customer()
          case "3":
            self.update_customer()
          case "4":
            self.search_customer()
          case "5":
            self.display_customer()
          case "6":
            print(f'{"*"*100}退出客户管理系统')
            break
          case _:
            print(">> ???")
            time.sleep(1)
    except (EOFError, KeyboardInterrupt):
      print(f'{"*"*100}退出客户管理系统')

if __name__ == "__main__":
  cms = CMS()
  cms.start()