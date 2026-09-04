import re


class Customer:
  """客户类"""

  def __init__(self, c_id, name, age="None", phone="None", email="None"):
    """初始化客户信息"""
    self.id = c_id # 客户编号
    self.name = name # 客户姓名
    self.age = age # 客户年龄
    self.phone = phone # 客户电话
    self.email = email # 客户邮箱

  @staticmethod
  def check_id(c_id):
    """检查id格式"""
    # 检查客户id是否为纯数字
    return c_id.isdigit()

  @staticmethod
  def check_name(name):
    """检查name格式"""
    # 检查客户姓名是否为字符
    return name.isalpha()

  @staticmethod
  def check_age(age):
    """检查age格式"""
    # 检查客户年龄是否为整数
    return age.isdigit()

  @staticmethod
  def check_phone(phone):
    """检查phone格式"""
    # 检查客户电话是否合法
    return True if re.match(r"^1[345789]\d{9}$", phone) else False

  @staticmethod
  def check_email(email):
    """检查email格式"""
    # 检查客户邮箱是否合法
    pattern = r"[\w!#$%&'*+-/=?^`{|}~.]+@[\w!#$%&'*+-/=?^`{|}~.]+\.[a-zA-Z]{2,}$"
    return True if re.match(pattern, email) else False

  def __str__(self):
    """打印客户信息"""
    return (f"Id: {self.id:<5}, Name: {self.name:<10}, Age: {self.age:<5}, Phone: {self.phone:<15}"
        f", Email: {self.email:<25}")