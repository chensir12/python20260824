"""
    该案例演示了愤怒的小鸟
"""
class Birds:
    def __init__(self,name,color,skill_description):
        self.name = name
        self.color = color
        self.skill_description = skill_description
    def fly(self):
        pass
    def call(self):
        pass
    def use_skill(self):
        print(f"{self.name}使用了技能:{self.skill_description}")

class RedBirds(Birds):
    def fly(self):
        print(f"{self.name},{self.color},稳定飞")
    def call(self):
        print("红鸟叫")

class YellowBirds(Birds):
    def fly(self):
        print(f"{self.name},{self.color},快速飞")
    def call(self):
        print("黄鸟叫")

class BlueBirds(Birds):
    def fly(self):
        print(f"{self.name},{self.color},优雅飞")
    def call(self):
        print("蓝鸟叫")

class Obstacle():
    def __init__(self,name,strength = 10):
        self.name = name
        self.strength = strength
    def be_attacked(self,bird):
        print(f"{bird.name}向障碍物{self.name}发起了攻击")
        bird.use_skill()
        if isinstance(bird, RedBirds):
            damage = 40
        elif isinstance(bird, YellowBirds):
            damage = 80
        else:
            damage = 30 * 3
        self.strength -= damage

        if self.strength <= 0:
            print("障碍物已经被摧毁")
        else:
            print(f"障碍物{self.name}还剩:{self.strength}")


o1 = Obstacle("巨石",10000)
rb = RedBirds("红鸟","红色","火焰攻击")
yb = YellowBirds("黄鸟","黄色","沙尘攻击")
bb = BlueBirds("蓝鸟","蓝色","寒冰攻击")
o1.be_attacked(rb)
o1.be_attacked(yb)
o1.be_attacked(bb)


