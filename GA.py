import random
from Scheduling import Scheduling

class GA:
    def __init__(self, job_state, machine_num, agv_num, agv_time):
        # 定义机器数量 工件数量 AGV小车数量 可加工机器集合等初始条件
        self.job_state = job_state  #是一个三维数组 一维表示工件数  二维表示各个工件的工序数 三维表示可加工机器集合    数组中的数字表示加工时长 不能加工为-1
        self.machine_num = machine_num  #机器数量  
        self.agv_num = agv_num          # agv数量
        self.job_num = len(self.job_state)
        self.agv_time = agv_time        #agv在各机器之间的搬运时间
        self.Pm = 0.2                   #交叉变异因子
        self.Pc = 0.9    
        self.Pop_size = 100         #种群大小
        self.iter = 100             # 迭代次数
        
        #工件各工序可选的加工机器
        self.job_machine = [[[k for k in range(len(self.job_state[i][j]))
                              if self.job_state[i][j][k] != -1] for j in range(len(self.job_state[i]))]
                            for i in range(len(self.job_state))]
        
        
        #记录工件的加工工序
        self.job_process_record = [0 for i in range(self.job_num)]
        
        
        
    #生成染色体 机器编码 工序编码 以及 AGV编码
    def RCH(self):
        #生成工序编码
        j_code = []
        m_code = []
        a_code = []
        record = [0 for i in range(len(self.job_state))] #记录工件在编码中出现的次数
        
        for i in range(len(self.job_state)):
            for x in range(len(self.job_state[0])):
                j_code.append(i)
        random.shuffle(j_code) # 打乱顺序 随机编码
        
        #机器编码
        for i in range(len(j_code)):  #j_code[i]是工件 record[j_code[i]]是工件的第几道工序
            m_code.append(random.choice(self.job_machine[j_code[i]][record[j_code[i]]]))
            record[j_code[i]] +=1
            
        #AGV编码
        for i in range(len(j_code)):
            a_code.append(random.randint(0, self.agv_num-1))  #随机从小车选取
            
        return [j_code, m_code, a_code]


    
    #生成初始种群
    def CHS(self):
        pass
    
    #选择
    def Select(self):
        pass
    
    #交叉
    def Crossover(self):
        pass
    
    #变异
    def Mutation(self):
        pass
    
    #解码
    def decode(self, codes):
        
        s = Scheduling(self.job_num, self.machine_num, self.agv_num)
        for i in range(len(code[0])):
            
            job = codes[0][i]
            machine = codes[1][i]
            agv = codes[2][i]
        
            process = self.job_process_record[codes[0][i]] #当前工件的工序
            
            next_machine = machine + 1 #将机器数加一 工件起始位置为0
            
            
            now_machine = s.Jobs[job].last_loc  #next_machine 和 now_machine 用来表示位置 初始位置为0 机器位置是machine+1
            
            if now_machine !=  next_machine:
                # 小车开始搬运时间 = max(小车结束时间 + 小车从结束位置前往工件处的时间， 工件上一工序结束加工时间)
                agv_start_time = max(s.Agvs[agv].last_ot + self.travel_time[s.Agvs[agv].last_loc][s.Jobs[job].last_loc],
                                     s.Jobs[job].last_ot)

                agv_end_time = agv_start_time + self.travel_time[now_machine][next_machine]
                #小车位置更新
                agv_loc = next_machine
                
                s.Agvs[agv].update(agv_start_time, agv_end_time, agv_loc)
                
                # 工件开始加工时间 = max(小车搬运到达机器的时间， 机器加工结束时间)
                job_start_time = max(agv_end_time, s.Machines[machine].last_ot)
    
            else:
                job_start_time = s.Machines[machine].last_ot
                

            job_end_time = job_start_time + self.job_state[job][process][machine]

            machine_start_time = job_start_time
            machine_end_time = job_end_time
            self.job_process_record[job] +=1 #记录工件已知加工工序数 工序+1
                
            #更新 加工机器 工件 信息
            s.Jobs[job].update(job_start_time, job_end_time, machine, next_machine )
            
            s.Machines[machine].update(machine_start_time,machine_end_time)