import os
import csv
import warnings
import re
from PIL import Image



##############################
#                            #
#           KERNEL           #
#                            #
##############################



class Student:
    def __init__(self, file_name, display_name=None, img_file_path=None, color_r=255, color_g=255, color_b=255, star=7, lvl=90, 
                 skl_ex=5, skl_ns=10, skl_ps=10, skl_ss=10, eq_1=9, eq_2=9, eq_3=9, eq_u=0, 
                 pu_hp=0, pu_ak=0, pu_hl=0, aff_1=0, aff_2=0, aff_3=0, aff_4=0, 
                 ex_type='damage', ex_cost=0, ex_pre=0, ex_dur=0, ns_type='buff', ns_cd=0, ns_pre=0, ns_dur=0,
                 note=''):
        self.file_name = file_name
        if display_name==None:
            self.display_name = file_name
        else:
            self.display_name = display_name
        self.img_file_path = img_file_path
        self.color_r = color_r
        self.color_g = color_g
        self.color_b = color_b
        self.star = star
        self.lvl = lvl
        
        self.skl_ex = skl_ex
        self.skl_ns = skl_ns
        self.skl_ps = skl_ps
        self.skl_ss = skl_ss
        
        self.eq_1 = eq_1
        self.eq_2 = eq_2
        self.eq_3 = eq_3
        self.eq_u = eq_u
        
        self.pu_hp = pu_hp
        self.pu_ak = pu_ak
        self.pu_hl = pu_hl
        
        self.aff_1 = aff_1 
        self.aff_2 = aff_2 
        self.aff_3 = aff_3 
        self.aff_4 = aff_4
        
        self.ex_type = ex_type
        self.ex_cost = ex_cost
        self.ex_pre = ex_pre
        self.ex_dur = ex_dur
        self.ns_type = ns_type
        self.ns_cd = ns_cd
        self.ns_pre = ns_pre
        self.ns_dur = ns_dur

        self.note = note

    def __str__(self):
        return (f"Student(file_name={self.file_name}, display_name={self.display_name}, img_file_path={self.img_file_path}, \n"
                f"color=({self.color_r},{self.color_g},{self.color_b}), star={self.star}, lvl={self.lvl}, \n"
                f"skl_ex={self.skl_ex}, skl_ns={self.skl_ns}, skl_ps={self.skl_ps}, skl_ss={self.skl_ss}, "
                f"eq_1={self.eq_1}, eq_2={self.eq_2}, eq_3={self.eq_3}, eq_u={self.eq_u}, \n"
                f"pu_hp={self.pu_hp}, pu_ak={self.pu_ak}, pu_hl={self.pu_hl}, "
                f"aff_1={self.aff_1}, aff_2={self.aff_2}, aff_3={self.aff_3}, aff_4={self.aff_4}, \n"
                f"ex_type={self.ex_type}, ex_cost={self.ex_cost}, ex_pre={self.ex_pre}, ex_dur={self.ex_dur}, ns_type={self.ns_type}, ns_cd={self.ns_cd}, ns_pre={self.ns_pre}, ns_dur={self.ns_dur}, \n"
                f"note={self.note})")


class Student_Skill_Timeline:
    """
    timeline全部按倒计时来计算
    """
    def __init__(self, student:Student):
        self.student = student
        self.ex_timeline = {}
        self.ns_timeline = {}
        self.buff_timeline = []

    def __str__(self):
        return f"Student_Skill_Timeline(student_name={self.student.display_name}, ex_timeline={self.ex_timeline}, ns_timeline={self.ns_timeline}, buff_timeline={self.buff_timeline})"

    def add_ex(self, time, cost=None, target=None, skl_type='', note=''):
        if cost==None or cost=='':
            cost = self.student.ex_cost
        elif type(cost)==float:
            warnings.warn("WARNING: cost should be an integer but get a float", UserWarning)
        elif type(cost)!=int:
            warnings.warn("REJECTED: cost should be an integer, use default cost setting", UserWarning)
            cost = self.student.ex_cost
        if target==None:
            target=self
        elif type(target)!=Student_Skill_Timeline and type(target)!=Enemy:
            warnings.warn("REJECTED: target should be a SST or Enemy, use self as target", UserWarning)
            target=self
        self.ex_timeline[time]=[target, round(time-self.student.ex_pre,3), round(time-self.student.ex_pre-self.student.ex_dur,3), cost, skl_type, note]

    def clear_ex(self):
        self.ex_timeline = {}

    def remove_ex(self, time):
        try:
            self.ex_timeline.pop(time)
        except:
            warnings.warn("NO TARGET: No ex found", UserWarning)
            
    def add_ns(self, time, target=None, skl_type='', note=''):
        if target==None:
            target=self
        elif type(target)!=Student_Skill_Timeline and type(target)!=Enemy:
            warnings.warn("REJECTED: target should be a SST or Enemy, use self as target", UserWarning)
            target=self
        self.ns_timeline[time]=[target, time-self.student.ns_pre, time-self.student.ns_pre-self.student.ns_dur, skl_type, note]

    def clear_ns(self):
        self.ns_timeline = {}

    def remove_ns(self, time):
        try:
            self.ns_timeline.pop(time)
        except:
            warnings.warn("NO TARGET: No ns found", UserWarning)

    def add_buff(self, buff_start_time, buff_end_time, buff_name, buff_source):
        """
        仅作显示用，buff_source为str，并且不会检查除buff_start_time外的输入（buff_start_time需要排序用，因此需要检查）
        """
        if type(buff_start_time)!=int and type(buff_start_time)!=float:
            warnings.warn("REJECTED: buff_start_time should be a float or int", UserWarning)
        else:
            self.buff_timeline.append([buff_start_time, buff_end_time, buff_name, buff_source])

    def clear_buff(self):
        self.buff_timeline = []


class Enemy:
    """
    Enemy类实际包含enemy自身信息和timeline信息
    timeline全部按倒计时来计算
    """
    def __init__(self, file_name, display_name=None):
        self.file_name = file_name
        if display_name==None:
            self.display_name = file_name
        else:
            self.display_name = display_name
        self.buff_timeline = []
        self.event_timeline = []
        self.damage_timeline = []

    def add_event(self, event_start_time, event_end_time, note):
        if type(event_start_time)!=int and type(event_start_time)!=float:
            warnings.warn("REJECTED: event_start_time should be a float or int", UserWarning)
        else:
            self.event_timeline.append([event_start_time, event_end_time, note])
            self.event_timeline.sort(reverse=True)

    def clear_event(self):
        self.event_timeline = []

    def remove_event(self, event_start_time, event_end_time, event_note):
        for event in self.event_timeline:
            if event[0]==event_start_time and event[1]==event_end_time and event[2]==event_note:
                self.event_timeline.remove(event)
                return
        warnings.warn("NO TARGET: No event found", UserWarning)
        

    def add_buff(self, buff_start_time, buff_end_time, buff_name, buff_source):
        """
        仅作显示用，buff_source为str，并且不会检查除buff_start_time外的输入（buff_start_time需要排序用，因此需要检查）
        """
        if type(buff_start_time)!=int and type(buff_start_time)!=float:
            warnings.warn("REJECTED: buff_start_time should be a float or int", UserWarning)
        else:
            self.buff_timeline.append([buff_start_time, buff_end_time, buff_name, buff_source])
            self.buff_timeline.sort(reverse=True)

    def clear_buff(self):
        self.buff_timeline = []

    def add_damage(self, damage_start_time, damage_end_time, damage_source):
        """
        仅作显示用，damage_source为str，并且不会检查除damage_start_time外的输入（damage_start_time需要排序用，因此需要检查）
        """
        if type(damage_start_time)!=int and type(damage_start_time)!=float:
            warnings.warn("REJECTED: damage_start_time should be a float or int", UserWarning)
        else:
            self.damage_timeline.append([damage_start_time, damage_end_time, damage_source])

    def clear_damage(self):
        self.damage_timeline = []

    def __str__(self):
        return (f"Enemy(file_name={self.file_name}, display_name={self.display_name}, buff_timeline={self.buff_timeline}, event_timeline={self.event_timeline}, damage_timeline={self.damage_timeline})")


class Mission:
    """
    timeline全部按倒计时来计算
    """
    def __init__(self, file_name='', mission_time=240, cost_init_delay=2, log=None):
        if log==None:
            self.init_without_log(file_name, mission_time, cost_init_delay)
        else:
            self.init_with_log(log)

    def init_with_log(self, log:dict):
        """
        {
            'file_name': '猫鬼ins',
            'mission_time': 240,
            'cost_init_delay': 2,
            'cost_timeline': {240: 0, 238: 4200},
            'student_list': [
                ['himari_example', '专二轮椅', 6, 90, 5, 7, 10, 10, 9, 9, 4, 0, 0, 0, 0, 20, 0, 0, 0, 3, True, 30, 1, 15.47, 0, 23],
                ['hanoko_swimsuit_example', '满配水花', 7, 90, 5, 10, 10, 10, 9, 9, 9, 0, 0, 25, 0, 50, 20, 0, 0, 2, True, 30, 1.5, 0.67, 0, 20]
            ],
            'enemy': ['kurokage_example', '猫鬼ins'],
            'student_ex': [
                ['专二轮椅', 225, 2, '满配水花', 'buff', ''],
                ['满配水花', 224, 1, '猫鬼ins', 'damage', ''],
                ['满配水花', 220, None, '猫鬼ins', 'damage', ''],
                ['专二轮椅', 211, None, '满配水花', 'buff', ''],
                ['满配水花', 208, None, '猫鬼ins', 'damage', ''],
                ['满配水花', 200, None, '猫鬼ins', 'damage', '']
            ],
            'student_ns': [
                ['专二轮椅', 210, '猫鬼ins', 'buff', ''],
                ['满配水花', 210, '猫鬼ins', 'buff', '']
            ],
            'enemy_event': [
                [180, 180, '转p2'],
                [120, 120, '转p3']
            ]
        }
        """
        # print(log)
        self.log = {}
        self.log['file_name'] = log['file_name']
        self.log['mission_time'] = log['mission_time']
        self.log['cost_init_delay'] = log['cost_init_delay']
        if 'is_udb' in log.keys():
            self.log['is_udb'] = log['is_udb']
        else:
            self.log['is_udb'] = False
        if 'note' in log.keys():
            self.log['note'] = log['note']
        else:
            self.log['note'] = ''
        self.cost_timeline = {}
        self.cost_direct = {}
        if not log['cost_timeline']:
            self.log['cost_timeline'] = []
        elif type(log['cost_timeline'][0])==int or type(log['cost_timeline'][0])==float:
            self.log['cost_timeline'] = [log['cost_timeline']]
            item = log['cost_timeline']
            self.cost_timeline[item[0]] = item[1]
        elif isinstance(log['cost_timeline'][0], list):
            self.log['cost_timeline'] = log['cost_timeline']
            for item in log['cost_timeline']:
                self.cost_timeline[item[0]] = item[1]
        else:
            warnings.warn("Wrong cost_timeline format", UserWarning)
        if not log['cost_direct']:
            self.log['cost_direct'] = []
        elif type(log['cost_direct'][0])==int or type(log['cost_direct'][0])==float:
            self.log['cost_direct'] = [log['cost_direct']]
            item = log['cost_direct']
            self.cost_direct[item[0]] = item[1]
        elif isinstance(log['cost_direct'][0], list):
            self.log['cost_direct'] = log['cost_direct']
            for item in log['cost_direct']:
                self.cost_direct[item[0]] = item[1]
        else:
            warnings.warn("Wrong cost_direct format", UserWarning)
        self.file_name = log['file_name']
        self.mission_time = log['mission_time']
        self.cost_init_delay = log['cost_init_delay']
        self.is_udb = self.log['is_udb']
        self.note = self.log['note']
        self.student_skill_timelines = []
        self.sub_enemies = []    # sub_enemies 对应类似student_skill_timelines的功能
        self.global_ex_timeline = []
        self.global_ex_time_list = []
        self.instance_dict = {}

        self.log['student_list'] = []
        if not log['student_list']:
            pass
        elif type(log['student_list'][0])==str:
            student_info = log['student_list']
            self.add_sst(Student_Skill_Timeline(Student(*student_info)))
        else:
            for student_info in log['student_list']:
                self.add_sst(Student_Skill_Timeline(Student(*student_info)))

        self.set_enemy(Enemy(*log['enemy']))

        self.log['sub_enemy_list'] = []
        if 'sub_enemy_list' not in log.keys():
            pass
        elif not log['sub_enemy_list']:
            pass
        elif type(log['sub_enemy_list'][0])==str:
            sub_enemy_info = log['sub_enemy_list']
            self.add_sub_enemy(Enemy(*sub_enemy_info))
        else:
            for sub_enemy_info in log['sub_enemy_list']:
                self.add_sub_enemy(Enemy(*sub_enemy_info))

        self.log['student_ex'] = []
        self.log['student_ns'] = []
        self.log['enemy_event'] = []

        if not log['student_ex']:
            pass
        elif isinstance(log['student_ex'][0], list):
            for ex in log['student_ex']:
                if ex[0] in self.instance_dict.keys() and ex[1]<=self.mission_time-self.cost_init_delay and ex[3] in self.instance_dict.keys():
                    self.add_student_ex(*ex)
        else:
            ex = log['student_ex']
            if ex[0] in self.instance_dict.keys() and ex[1]<=self.mission_time-self.cost_init_delay and ex[3] in self.instance_dict.keys():
                self.add_student_ex(*ex)
        
        if not log['student_ns']:
            pass
        elif isinstance(log['student_ns'][0], list):
            for ns in log['student_ns']:
                if ns[0] in self.instance_dict.keys() and ns[1]<=self.mission_time-self.cost_init_delay and ns[2] in self.instance_dict.keys():
                    self.add_student_ns(*ns)
        else:
            ns = log['student_ns']
            if ns[0] in self.instance_dict.keys() and ns[1]<=self.mission_time-self.cost_init_delay and ns[2] in self.instance_dict.keys():
                self.add_student_ns(*ns)
        
        if not log['enemy_event']:
            pass
        elif isinstance(log['enemy_event'][0], list):
            for event in log['enemy_event']:
                if event[0]<self.mission_time and event[0]>=event[1]:
                    self.add_enemy_event(*event)
        else:
            event = log['enemy_event']
            if event[0]<self.mission_time and event[0]>=event[1]:
                self.add_enemy_event(*event)
        
        self.refresh_global_ex_timeline()
        self.settle_buff()

    def init_without_log(self, file_name, mission_time=240, cost_init_delay=2, is_udb=False, note=''):
        self.file_name = file_name
        self.mission_time = mission_time
        self.cost_init_delay = cost_init_delay
        self.is_udb = is_udb
        self.note = note
        self.cost_timeline = {mission_time:0, (mission_time-cost_init_delay):4200}
        self.cost_direct = {}
        self.student_skill_timelines = []
        self.global_ex_timeline = []
        self.global_ex_time_list = []
        self.instance_dict = {}
        self.enemy = None
        self.sub_enemies = []    # sub_enemies 对应类似student_skill_timelines的功能
        self.log = {}
        self.log['file_name'] = file_name
        self.log['mission_time'] = mission_time
        self.log['cost_init_delay'] = cost_init_delay
        self.log['cost_timeline'] = [[mission_time,0], [mission_time-cost_init_delay,4200]]
        self.log['cost_direct'] = []
        self.log['is_udb'] = self.is_udb
        self.log['note'] = self.note

    def set_file_name(self, file_name):
        self.file_name = file_name
        self.log['file_name'] = file_name

    def set_mission_time(self, mission_time):
        self.log['mission_time'] = mission_time
        self_log_temp = self.log.copy()
        self.init_with_log(self_log_temp)

    def set_cost_init_delay(self, cost_init_delay):
        self.log['cost_init_delay'] = cost_init_delay
        self_log_temp = self.log.copy()
        self.init_with_log(self_log_temp)
        
    def set_enemy(self, enemy:Enemy):
        self.enemy = enemy
        self.instance_dict[enemy.display_name] = enemy
        self.log['enemy'] = [enemy.file_name, enemy.display_name]

    def change_enemy_name(self, new_enemy_name):
        old_enemy_name = self.enemy.display_name
        self_log_temp = self.log.copy()
        new_student_ex = []
        for ex_info in self_log_temp['student_ex']:
            if ex_info[3]==old_enemy_name:
                ex_info[3] = new_enemy_name
            new_student_ex.append(ex_info)
        self_log_temp['student_ex'] = new_student_ex
        new_student_ns = []
        for ns_info in self_log_temp['student_ns']:
            if ns_info[2]==old_enemy_name:
                ns_info[2] = new_enemy_name
            new_student_ns.append(ns_info)
        self_log_temp['student_ns'] = new_student_ns
        self_log_temp['enemy'] = [new_enemy_name, new_enemy_name]
        self.init_with_log(self_log_temp)

    def add_sst(self, sst:Student_Skill_Timeline):
        display_name = sst.student.display_name
        if display_name in self.instance_dict.keys():
            warnings.warn("REJECTED: Already added to mission", UserWarning)
            return
        self.student_skill_timelines.append(sst)
        self.instance_dict[display_name] = sst
        try:
            self.log['student_list'].append(list(vars(sst.student).values()))
        except:
            self.log['student_list'] = [list(vars(sst.student).values())]

    def clear_sst(self):
        for student in self.log['student_list']:
            display_name = student[1]
            self.instance_dict.pop(display_name)
        self.student_skill_timelines = []
        self.log['student_list'] = []

    def remove_sst(self, display_name):
        self.student_skill_timelines.remove(self.instance_dict[display_name])
        self.instance_dict.pop(display_name)
        temp = []
        for student in self.log['student_list']:
            if student[1]==display_name:
                temp = student
                break
        self.log['student_list'].remove(temp)

    def add_sub_enemy(self, sub_enemy:Enemy):
        display_name = sub_enemy.display_name
        if display_name in self.instance_dict.keys():
            # print(display_name, self.instance_dict.keys())
            warnings.warn("REJECTED: Already added to mission", UserWarning)
            return
        self.sub_enemies.append(sub_enemy)
        self.instance_dict[display_name] = sub_enemy
        try:
            self.log['sub_enemy_list'].append([sub_enemy.file_name,sub_enemy.display_name])
        except:
            self.log['sub_enemy_list'] = [[sub_enemy.file_name,sub_enemy.display_name]]

    def clear_sub_enemy(self):
        for sub_enemy in self.log['sub_enemy_list']:
            display_name = sub_enemy[1]
            self.instance_dict.pop(display_name)
        self.sub_enemies = []
        self.log['sub_enemy_list'] = []

    def remove_sub_enemy(self, display_name):
        self.sub_enemies.remove(self.instance_dict[display_name])
        self.instance_dict.pop(display_name)
        temp = []
        for sub_enemy in self.log['sub_enemy_list']:
            if sub_enemy[1]==display_name:
                temp = sub_enemy
                break
        self.log['sub_enemy_list'].remove(temp)

    def student_reorder_switch(self, source_display_name, target_display_name):
        temp_list = self.log['student_list']
        new_list = []
        first_flag = False
        last_flag = False
        temp_student = None
        temp_index = None
        for i, student in enumerate(self.log['student_list']):
            if (not first_flag) and (student[1]==source_display_name or student[1]==target_display_name):
                first_flag = True
                temp_student = student
                new_list.append(None)
                temp_index = i
            elif first_flag and (student[1]==source_display_name or student[1]==target_display_name):
                last_flag = True
                new_list.append(temp_student)
                new_list[temp_index] = student
            else:
                new_list.append(student)
        if last_flag:
            self.log['student_list'] = new_list
        else:
            warnings.warn("NO TARGET: Cannot find source or(and) target student", UserWarning)
        

                

    def set_cost_timeline(self, time, cost):
        self.cost_timeline[time] = cost
        self.log['cost_timeline'] = []
        for time, cost in self.cost_timeline.items():
            self.log['cost_timeline'].append([time, cost])
        self.log['cost_timeline'].sort(reverse=True)
        
    def unset_cost_timeline(self, time):
        try:
            self.cost_timeline.pop(time)
            self.log['cost_timeline'] = []
            for time, cost in self.cost_timeline.items():
                self.log['cost_timeline'].append([time, cost])
            self.log['cost_timeline'].sort(reverse=True)
        except:
            warnings.warn("NO TARGET: No cost checkpoint found", UserWarning)

    def reset_cost_timeline(self):
        self.cost_timeline = {self.mission_time:0, self.mission_time-self.cost_init_delay:4200}
        self.log['cost_timeline'] = []
        for time, cost in self.cost_timeline.items():
            self.log['cost_timeline'].append([time, cost])
        self.log['cost_timeline'].sort(reverse=True)

    def set_cost_direct(self, time, cost):
        self.cost_direct[time] = cost
        self.log['cost_direct'] = []
        for time, cost in self.cost_direct.items():
            self.log['cost_direct'].append([time, cost])
        self.log['cost_direct'].sort(reverse=True)
        
    def unset_cost_direct(self, time):
        try:
            self.cost_direct.pop(time)
            self.log['cost_direct'] = []
            for time, cost in self.cost_direct.items():
                self.log['cost_direct'].append([time, cost])
            self.log['cost_direct'].sort(reverse=True)
        except:
            warnings.warn("NO TARGET: No cost checkpoint found", UserWarning)

    def reset_cost_direct(self):
        self.cost_direct = {}
        self.log['cost_direct'] = []
        for time, cost in self.cost_direct.items():
            self.log['cost_direct'].append([time, cost])
        self.log['cost_direct'].sort(reverse=True)

    def get_global_ex_timeline(self):
        repeat_flag = False
        for sst in self.student_skill_timelines:
            name = sst.student.display_name
            for time in sst.ex_timeline.keys():
                if time in self.global_ex_time_list:
                    repeat_flag = True
                    break
                ex = sst.ex_timeline[time]
                if type(ex[0])==Student_Skill_Timeline:
                    target_name = ex[0].student.display_name
                elif type(ex[0])==Enemy:
                    target_name = ex[0].display_name
                self.global_ex_time_list.append(time)
                self.global_ex_timeline.append([time, name, target_name, ex[1], ex[2], ex[3], ex[4], ex[5]])
        self.global_ex_timeline.sort(reverse=True)
        self.global_ex_time_list.sort(reverse=True)
        return repeat_flag

    def clear_global_ex_timeline(self):
        self.global_ex_timeline = []
        self.global_ex_time_list = []

    def refresh_global_ex_timeline(self):
        temp_timeline = self.global_ex_timeline
        temp_time_list = self.global_ex_time_list
        self.clear_global_ex_timeline()
        repeat_flag = self.get_global_ex_timeline()
        if repeat_flag:
            self.global_ex_timeline = temp_timeline
            self.global_ex_time_list = temp_time_list
            warnings.warn("REJECTED: multiple ex at the exact same time", UserWarning)
        

    def settle_buff(self):
        """
        为所有sst中的self.buff_timeline添加数据
        """
        for sst in self.student_skill_timelines:
            sst.clear_buff()
        if self.enemy!=None:
            self.enemy.clear_buff()
            self.enemy.clear_damage()
        for sub_enemy in self.sub_enemies:
            sub_enemy.clear_buff()
            sub_enemy.clear_damage()
        for sst in self.student_skill_timelines:
            name = sst.student.display_name
            for time in sst.ex_timeline.keys():
                ex = sst.ex_timeline[time]
                target = ex[0]
                time_start = ex[1]
                time_end = ex[2]
                skl_type = ex[4]
                if skl_type=='buff':
                    buff_name = name+' ex'
                    target.add_buff(time_start, time_end, buff_name, name)
                elif (skl_type=='damage' or skl_type=='伤害') and type(target)==Enemy:
                    damage_name = name+' ex'
                    target.add_damage(time_start, time_end, damage_name)
            for time in sst.ns_timeline.keys():
                ns = sst.ns_timeline[time]
                target = ns[0]
                time_start = ns[1]
                time_end = ns[2]
                skl_type = ns[3]
                if time_start==time_end:
                    continue
                if skl_type=='buff':
                    buff_name = name+' ns'
                    target.add_buff(time_start, time_end, buff_name, name)
                elif (skl_type=='damage' or skl_type=='伤害') and type(target)==Enemy:
                    damage_name = name+' ns'
                    target.add_damage(time_start, time_end, damage_name)
        for sst in self.student_skill_timelines:
            sst.buff_timeline.sort(reverse=True)
        if self.enemy!=None:
            self.enemy.buff_timeline.sort(reverse=True)
        for sub_enemy in self.sub_enemies:
            sub_enemy.buff_timeline.sort(reverse=True)

    def add_enemy_event(self, event_start_time, event_end_time, note):
        self.enemy.add_event(event_start_time, event_end_time, note)
        try:
            self.log['enemy_event'].append([event_start_time, event_end_time, note])
        except:
            self.log['enemy_event'] = [[event_start_time, event_end_time, note]]
        self.log['enemy_event'].sort(reverse=True)

    def clear_enemy_event(self):
        self.enemy.clear_event()
        self.log['enemy_event'] = []

    def remove_enemy_event(self, start_time, end_time, note):
        self.enemy.remove_event(start_time, end_time, note)
        for event in self.log['enemy_event']:
            if event[0]==start_time and event[1]==end_time and event[2]==note:
                self.log['enemy_event'].remove(event)
                return

    def add_student_ex(self, student_display_name, time, cost=None, target=None, skl_type='', note=''):
        if cost=='':
            cost=None
        if time in self.global_ex_time_list:
            warnings.warn("REJECTED: multiple ex at the exact same time", UserWarning)
            return False
        target_instance = self.instance_dict[target]
        self.instance_dict[student_display_name].add_ex(time, cost=cost, target=target_instance, skl_type=skl_type, note=note)
        try:
            self.log['student_ex'].append([student_display_name, time, cost, target, skl_type, note])
        except:
            self.log['student_ex'] = [[student_display_name, time, cost, target, skl_type, note]]
        self.refresh_global_ex_timeline()
        return True

    def remove_student_ex(self, student_display_name, time):
        self.instance_dict[student_display_name].remove_ex(time)
        self.refresh_global_ex_timeline()
        for student_ex_temp in self.log['student_ex']:
            if student_ex_temp[0]==student_display_name and student_ex_temp[1]==time:
                self.log['student_ex'].remove(student_ex_temp)
                return
        warnings.warn("NO TARGET: No ex found", UserWarning)
        
    def clear_global_ex(self):
        for display_name in self.instance_dict:
            if type(self.instance_dict[display_name])==Student_Skill_Timeline:
                self.instance_dict[display_name].clear_ex()
        self.log['student_ex'] = []
        self.refresh_global_ex_timeline()

    def clear_student_ex(self, student_display_name):
        self.instance_dict[student_display_name].clear_ex()
        for student_ex_temp in self.log['student_ex']:
            if student_ex_temp[0]==student_display_name:
                self.log['student_ex'].remove(student_ex_temp)
        self.refresh_global_ex_timeline()

    def add_student_ns(self, student_display_name, time, target=None, skl_type='', note=''):
        target_instance = self.instance_dict[target]
        self.instance_dict[student_display_name].add_ns(time, target=target_instance, skl_type=skl_type, note=note)
        try:
            self.log['student_ns'].append([student_display_name, time, target, skl_type, note])
        except:
            self.log['student_ns'] = [[student_display_name, time, target, skl_type, note]]

    def remove_student_ns(self, student_display_name, time):
        self.instance_dict[student_display_name].remove_ns(time)
        for student_ns_temp in self.log['student_ns']:
            if student_ns_temp[0]==student_display_name and student_ns_temp[1]==time:
                self.log['student_ns'].remove(student_ns_temp)
                return
        warnings.warn("NO TARGET: No ns found", UserWarning)
        
    def clear_global_ns(self):
        for display_name in self.instance_dict:
            if type(self.instance_dict[display_name])==Student_Skill_Timeline:
                self.instance_dict[display_name].clear_ns()
        self.log['student_ns'] = []

    def clear_student_ns(self, student_display_name):
        self.instance_dict[student_display_name].clear_ns()
        for student_ns_temp in self.log['student_ns']:
            if student_ns_temp[0]==student_display_name:
                self.log['student_ns'].remove(student_ns_temp)
    



def save_student_file(student_instance, directory='./student_files/'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    file_path = os.path.join(directory, f"{student_instance.file_name}.csv")
    
    with open(file_path, mode='w', newline='', encoding='gbk') as file:
        writer = csv.writer(file)
        
        # 将Student实例的属性和值写入CSV文件
        writer.writerow(['file_type', 'student_file'])
        for key, value in student_instance.__dict__.items():
            writer.writerow([key, value])

def load_student_file(path):
    attributes = {}
    
    with open(path, mode='r', encoding='gbk') as file:
        reader = csv.reader(file)
        
        # 判断首行中的file_type是否为student_file
        first_row = next(reader)
        if first_row[-1]=='student_file':
            pass
        else:
            print('not student_file')
            return None
        
        # 读取每一行，将属性和值保存到字典中
        for row in reader:
            attribute, value = row
            
            # 尝试将值转换为正确的类型
            if value.isdigit():  # 处理整数
                value = int(value)
            elif value.replace('.', '', 1).isdigit():  # 处理浮点数
                value = float(value)
            elif value.lower() == 'true':  # 处理布尔值
                value = True
            elif value.lower() == 'false':  # 处理布尔值
                value = False
            
            attributes[attribute] = value
    
    # 使用读取的属性创建一个新的Student实例
    return Student(**attributes)

def save_mission_file(mission, directory = './mission_files/'):
    """
    键值对中，键需要为单个元素，值可以为单个元素，一级列表，二级列表
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, f"{mission.file_name}.csv")
    
    with open(file_path, 'w', newline='', encoding='gbk') as csvfile:
        writer = csv.writer(csvfile)
        print(mission.log)     ############################
        writer.writerow(['file_type', 'mission_file'])
        for key, value in mission.log.items():
            if isinstance(value, list):
                if len(value)==0:
                    writer.writerow([key] + value)
                elif all(isinstance(item, list) for item in value):
                    # 处理多维列表，每个子列表单独一行
                    for item in value:
                        writer.writerow([key] + item)
                        key = ''  # 在后续行保持key为空
                else:
                    # 处理一维列表，将它们保存到同一行
                    writer.writerow([key] + value)
            else:
                # 处理非列表元素
                writer.writerow([key, value])

def convert_type(value):
    if value.isdigit():  # 处理整数
        value = int(value)
    elif value.replace('.', '', 1).isdigit():  # 处理浮点数
        value = float(value)
    elif value.lower() == 'true':  # 处理布尔值
        value = True
    elif value.lower() == 'false':  # 处理布尔值
        value = False
    return value

def load_mission_file(file_path):
    my_dict = {}
    
    with open(file_path, 'r', encoding='gbk') as csvfile:
        reader = csv.reader(csvfile)
        first_row = next(reader)
        if first_row[-1]=='mission_file':
            pass
        else:
            print('not mission_file')
            # my_dict[first_row[0]] = first_row[-1]
            return None
        
        current_key = None
        for row in reader:
            if row[0]:  # 新的键
                current_key = row[0]
                converted_values = [convert_type(v) for v in row[1:]]
                if len(converted_values) > 1:
                    my_dict[current_key] = converted_values
                elif len(converted_values)==1:
                    my_dict[current_key] = converted_values[0]
                else:
                    my_dict[current_key] = []
            else:  # 继续上一个键的值
                converted_values = [convert_type(v) for v in row[1:]]
                if isinstance(my_dict[current_key], list) and isinstance(my_dict[current_key][0], list):
                    my_dict[current_key].append(converted_values)
                else:
                    my_dict[current_key] = [my_dict[current_key], converted_values]

    return Mission(log=my_dict)

def second_to_minsec(second, tail=1):
    if second<=0:
        return "0:00.0"
    temp_minute = int((second)/60)
    temp_second = (second)%60
    if tail==1:
        return f"{temp_minute}:{temp_second:04.1f}"
    elif tail==2:
        return f"{temp_minute}:{temp_second:05.2f}"

def is_valid_english_path(path):
    # 定义允许的字符集：大小写字母、数字、空格和合法的特殊字符
    pattern = r'^[A-Za-z0-9!#$%&\'()/\-\@^_~{},.+=\[\]:;\\ ]+$'
    
    # 使用 re.fullmatch 来检查整个路径是否只包含允许的字符
    return bool(re.fullmatch(pattern, path))

def merge_intervals(interval_list):
    if not interval_list:
        return []
    reverse_flag = False
    if interval_list[0][0]>interval_list[0][1]:
        reverse_flag = True
    interval_list = [(min(a,b), max(a,b)) for a,b in interval_list]
    interval_list.sort()
    merged_intervals = [interval_list[0]]

    for current in interval_list[1:]:
        last = merged_intervals[-1]
        if current[0]<=last[1]:
            merged_intervals[-1] = (last[0], max(last[1],current[1]))
        else:
            merged_intervals.append(current)
    if reverse_flag:
        merged_intervals = [(b,a) for a,b in merged_intervals]
    return merged_intervals

# def crop_and_resize_image(image_path, size=(96, 96), crop=True, bg_color=None):
#     """
#     输入图片路径，读取图片，裁切为正方形，缩放为指定大小，归一化，展平为一维列表，返回该列表
#     """
#     if not image_path:    # 防止NoneType输入报错
#         image_path = ''
#     if not os.path.exists(image_path):
#         restored_array = load_hex_array_from_str(get_no_img_texture())
#         img = array_to_image(restored_array)
#         img_resized = img.resize(size=size)
#     else:
#         # 打开图片
#         img = Image.open(image_path)
#         width, height = img.size

#         # 计算正方形的边长
#         square_size = min(width, height)

#         # 计算裁切区域的左上角和右下角的坐标
#         left = (width - square_size) / 2
#         top = (height - square_size) / 2
#         right = (width + square_size) / 2
#         bottom = (height + square_size) / 2

#         # 裁切图片
#         if crop:
#             img_cropped = img.crop((left, top, right, bottom))
#         else:
#             img_cropped = img

#         # 将图片缩放为指定大小 (96*96)
#         img_resized = img_cropped.resize(size)

#     # 检查图像是否是RGB模式，如果不是则转换为RGB
#     # print(img.mode)
#     if img.mode != 'RGBA':
#         img_resized = img_resized.convert('RGB')
    
#     # 若有填充色则进行填充
#     if bg_color and img.mode=='RGBA':
#         bg_color = tuple(int(i) for i in bg_color)
#         background = Image.new('RGB', size, bg_color).convert('RGBA')
#         img_resized = Image.alpha_composite(background, img_resized)

#     # 转换为numpy数组
#     img_array = np.array(img_resized)

#     # 为每个像素增加alpha通道
#     if img.mode != 'RGBA':
#         alpha_channel = np.full((img_array.shape[0], img_array.shape[1], 1), 255)  # 创建一个全255的alpha通道
#         img_with_alpha = np.concatenate((img_array, alpha_channel), axis=2)  # 将alpha通道添加到图像数组中
#     else:
#         img_with_alpha = img_array

#     # 归一化到0-1.0之间 (包括alpha通道)
#     img_with_alpha_normalized = img_with_alpha / 255.0

#     # 展平为一维列表
#     img_flattened = img_with_alpha_normalized.flatten().tolist()

#     return img_flattened


def crop_and_resize_image(image_path, size=(96, 96), crop=True, bg_color=None):
    """
    输入图片路径，读取图片，裁切为正方形，缩放为指定大小，归一化，展平为一维列表，返回该列表
    """
    target_width, target_height = size
    if not image_path:    # 防止NoneType输入报错
        image_path = ''
    if not os.path.exists(image_path):
        restored_array = load_2d_list_from_hex_str(get_no_img_texture())
        img = create_image_from_2d_list(restored_array)
        img_resized = img.resize(size=size)
    else:
        # 打开图片
        img = Image.open(image_path)
        width, height = img.size

        # 计算正方形的边长
        square_size = min(width, height)

        # 计算裁切区域的左上角和右下角的坐标
        left = (width - square_size) / 2
        top = (height - square_size) / 2
        right = (width + square_size) / 2
        bottom = (height + square_size) / 2

        # 裁切图片
        if crop:
            img_cropped = img.crop((left, top, right, bottom))
        else:
            img_cropped = img

        # 将图片缩放为指定大小 (96*96)
        img_resized = img_cropped.resize(size)
    
    # 若有填充色则进行填充
    if bg_color and img.mode=='RGBA':
        bg_color = tuple(int(i) for i in bg_color)
        background = Image.new('RGB', size, bg_color).convert('RGBA')
        img_resized = Image.alpha_composite(background, img_resized)

    # 检查图像是否是RGB模式A，如果不是则转换为RGBA
    # print(img.mode)
    if img.mode != 'RGBA':
        img_resized = img_resized.convert('RGBA')

    img_flattened = []
    # print(f'height={height}, width={width}, img_size={img_resized.size}')
    for y in range(target_height):
        for x in range(target_width):
            r,g,b,a = img_resized.getpixel((x,y))
            img_flattened.extend([r/255,g/255,b/255,a/255])

    return img_flattened

# def image_to_grayscale(image_path, file_path):
#     "读取图片，并以整数数组存储灰度图，自用函数，不会出现在gui代码中"
#     img = Image.open(image_path).convert('L')  # 'L' 模式表示灰度图
#     img_array = np.array(img)  # 将图片转换为numpy数组
#     img_array_normalized = img_array / 16
#     img_flattened = np.resize(img_array_normalized, (1,img_array_normalized.size))
#     print(img_flattened)
#     np.savetxt(file_path, img_flattened, fmt='%d')

# def image_to_grayscale_hex(image_path, file_path):
#     img = Image.open(image_path).convert('L')  # 'L' 模式表示灰度图
#     img_array = np.array(img)  # 将图片转换为numpy数组
#     img_flattened = np.resize(img_array, (1,img_array.size))
#     # 除以16并确保结果是整数
#     scaled_array = (img_flattened // 16).astype(np.uint8)
#     # 将数组中的每个元素转换为16进制字符串，格式化为两位
#     hex_array = np.vectorize(lambda x: format(x, '1X'))(scaled_array)
#     # 保存为txt文件，每个值用空格分隔
#     with open(file_path, 'w') as f:
#         for row in hex_array:
#             f.write(' '.join(row) + '\n')  # 每行的16进制数按空格分开，并换行

# image_path = './no_img.png'
# txt_path = './no_img.txt'
image_size = (50,45)
# image_to_grayscale_hex(image_path, txt_path)

# def load_hex_array_from_txt(file_path):
#     with open(file_path, 'r') as file:
#         hex_data = file.read().split()  # 读取文件并按空格分割每个16进制值
#     int_array = np.array([int(h, 16) for h in hex_data], dtype=np.uint8)  # 将16进制转换为整数
#     int_array.resize(image_size)
#     return int_array*16
# def load_hex_array_from_str(input_str):
#     hex_data = input_str.split()  # 读取文件并按空格分割每个16进制值
#     int_array = np.array([int(h, 16) for h in hex_data], dtype=np.uint8)  # 将16进制转换为整数
#     int_array.resize(image_size)
#     return int_array*16
def load_2d_list_from_hex_str(input_str):
    if ' ' in input_str:
        hex_data = input_str.split()  # 读取文件并按空格分割每个16进制值
    else:
        hex_data = [char for char in input_str]
    map_dict = {'0':0, '1':1*16, '2':2*16, '3':3*16, '4':4*16, '5':5*16, '6':6*16, '7':7*16, '8':8*16, '9':9*16, 'A':10*16, 'B':11*16, 'C':12*16, 'D':13*16, 'E':14*16, 'F':15*16}
    int_list = [map_dict[i] for i in hex_data]
    width, height = image_size
    int_2d_list = [int_list[i*width:(i+1)*width] for i in range(height)]
    return int_2d_list
# def load_array_from_txt(file_path):
#     normalized_array = np.loadtxt(file_path)
#     array = (normalized_array * 1).astype(np.uint8)
#     array.resize(image_size)
#     return array
# def array_to_image(array, output_image_path=None):
#     img = Image.fromarray(array, 'L')  # 'L' 表示灰度图像模式
#     if output_image_path:
#         img.save(output_image_path)  # 如果提供了路径，则保存图片
#     # img.show()  # 显示图片
#     return img
def create_image_from_2d_list(int_2d_list:list, output_image_path=None):
    # print(len(int_2d_list),len(int_2d_list[-1]))
    width, height = image_size
    img = Image.new('L', (width, height))
    for y in range(height):
        for x in range(width):
            # print(x,y)
            img.putpixel((x,y), int_2d_list[y][x])
    if output_image_path:
        img.save(output_image_path)  # 如果提供了路径，则保存图片
    # img.show()  # 显示图片
    return img

# output_image = './no_img_2.png'  # 可选，保存还原图像的路径
# # 从txt中读取数组并还原图片
# restored_array = load_hex_array_from_txt(txt_path)
# array_to_image(restored_array, output_image)


def get_no_img_texture():
    texture = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFB54BFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEA51223EFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE94137C81AFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFD83138DFFD35FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFD83149DFFFFF71BFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFC72149EFFFFFFFC25FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFB6215AFFFFFFFFFFF61BFFFFFFFFFFFFFFFFFFFFFFFFFFFFB5125BFFFFFFFFFFFFFC26FFFFFFFFFFFFFFFFFFFFFFFFFEA5126CFFFFFFFFFFFFFFFF52CFFFFFFFFFFFFFFFFFFFFFFE94137CFFFFFFFFFFFFFFFFFFB16FFFFFFFFFFFFFFFFFFFFD83138DFFFFFFFFFFFFFFFFFFFFF53DFFFFFFFFFFFFFFFFFD83149EFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFFC7214AEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFB6215AFFFFFFFFFFFFFFFFFFFFFFFFFFFB988ADFFFFFFFFFD5226BFFFFFFFFFFFFFFFFFFFFFFFFFFFA41121137EFFFFFFF626CFFFFFFFFFFFFFFFFFEFFFFFFFFFF6137BCC9523CFFFFFF71BFFFFFFFFFFFFFFFFFB36BFFFFFFF616DFFFFFF923CFFFFFC26FFFFFFFD76CFFFFFF632248DFFF916FFB8FFFFFA25FFFFFF52CFFFFFF4233DFFFFD3486321BFE43DFF41CFFFFF71BFFFFFB17FFFFFC2342BFFFF927CBA84CFB18FFFB17FFFFFC26FFFFFF52DFFFFE4223DFFFF539CBCCBFF91BFFFF53DFFFFF44FFFFFFA18FFFFFD77CFFFFD25BBBBBCFF72CFFFFA17FFFFF54EFFFFFF43DFFFFFFFFFFFF828CBBBBCFF81CFFFFE35FFFFF54FFFFFFF918FFFFFFFFFFFF43ACBBBBBFFA0AFFFFFDBCFFFE35FFFFFFFE33EFFFFFFFFFFB26BBBBBBBEFD25FFFFFF40BFFA18FFFFFFFF819FFFFFFFFFF728CBBBBBBDFF62AFFFFF52CFE42DFFFFFFFFD34FFFFFFFFFE34BCBBBBBBBFFD32AFFFFFEFE519FFFFFFFFFF81AFFFFFFFFA26CBBBBBBBBDFFB228DFFFEA417FFFFFFFFFFFD35FFFFFFFF529CBBBBBBBBBEFFC4124653139FFFFFFFFFFFFF71BFFFFFFD35BBBBBBBBBBBBEFFFA643358DFFFFFFFFFFFFFFC25FFFFFF927CBBBBBBBBBCCABFFFFEEEFFFFFFFFFFFFFFFFFF62BFFFFF53ACBBBBBBBCCA7414CFFFFFFFFFFFFFFFFFFFFFFFB26FFFFC25BBBBBBBCCA73237CFFFFFFFFFFFFFFFFFFFFFFFFF52CFFF728CBBBBCBA73238DFFFFFFFFFFFFFFFFFFFFFFFFFFFB17FFE44ACBBCB963249DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF52DFB26BCCB853249EFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA18F729CB85225AFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF44A45A85225BFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF923354226CFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE333237CFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA338DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
    return texture

# restored_array = load_2d_list_from_hex_str(get_no_img_texture())
# img = create_image_from_2d_list(restored_array, './no_img.png')