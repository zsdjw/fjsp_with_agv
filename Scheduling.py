import numpy as np




# 创建三个类 加工机器 工件 以及 AGV小车
class machine:
    def __init__(self):
        self.start=[]
        self.end=[]
        self.last_ot=0   #上个工序的结束时间
        self.jobs = []  # 记录在这个机器上的加工工件
    
    def update(self,s,e): #更新信息
        self.start.append(s)
        self.end.append(e)
        self.last_ot = e


class job:
    def __init__(self):
        self.start=[]
        self.end=[]
        self.last_loc = 0
        self.last_m = 0
        self.last_ot=0  # 上道工序的完工时间
        self.machines = [] #记录该工件在哪些机器上加工过
        
    def update(self,s,e, last_m, last_loc): #更新信息
        self.start.append(s)
        self.end.append(e)
        self.last_m = last_m
        self.last_ot = e
        self.last_loc = last_loc
        self.machines.append(last_m)


class AGV:
    def __init__(self):
        self.start=[]
        self.end=[]
        self.last_m = 0 #agv上道工序所在的机器
        self.last_loc = 0
        self.last_ot = 0 #上个搬运任务的结束时间
        
        
    def update(self,s,e,last_loc): #更新信息
        self.start.append(s)
        self.end.append(e)
        self.last_loc = last_loc
        self.last_ot = e







class Scheduling:
    def __init__(self,J_num,M_num,A_num):
        
        self.J_num = J_num #三个物体的数量
        self.M_num = M_num
        self.A_num = A_num
        
        self.Jobs = []     # 创建类集合
        self.Machines = []
        self.Agvs = []
        
        self.Create_agv()
        self.Create_Job()
        self.Create_machine()
    
    def Create_Job(self):   
        for i in range(self.J_num):
            J = job()
            self.Jobs.append(J)
    
    def Create_machine(self):
        for i in range(self.M_num):
            M = machine()
            self.Machines.append(M)
    
    def Create_agv(self):
        for i in range(self.A_num):
            A = AGV()
            self.Agvs.append(A)
    