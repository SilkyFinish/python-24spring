# 示例框架
def menu():
    print("""
        —————————————————————学生信息管理系统———————————————————————--
        |                                                           |
        |         1 录入学生信息                                     |
        |         2 从文件录入学生信息                                |
        |         3 查找学生信息                                     |
        |         4 删除学生信息                                     |
        |         5 显示所有学生信息                                 |
        |         6 清空所有学生信息                                 |
        |         0 退出系统                                        |
        |                                                           |
        ------------------------------------------------------------
        """)
    


def insert():
    import csv
    a=0
    while a==0:
        with open('data/student_info.csv','r') as f1:
            student_info=csv.reader(f1,delimiter=',')
            std_list=list(student_info)
            Str = input('请输入学生信息，格式如"学号，姓名，性别，语文成绩，数学成绩，英语成绩"：')#英文逗号
            # 处理 Str，比如存储
            info_list=Str.split(',')
            if  len(info_list)!=6:
                print('格式不正确，请重新输入')
                continue
            elif not (info_list[0].isdigit() and info_list[3].isdigit() and info_list[4].isdigit() and info_list[5].isdigit() ):
                print('格式不正确，请重新输入')
                continue
            elif (len(info_list[0])==5 and info_list[0][0]!='0') and (info_list[2]=='男' or info_list[2]=='女') and (int(info_list[3])>=0 and int(info_list[3])<=100 ) and (int(info_list[4])>=0 and int(info_list[4])<=100 ) and (int(info_list[5])>=0 and int(info_list[5])<=100 ):
                b=0
                for row in std_list:
                    if row[0]==info_list[0]:
                        row=info_list
                        b=1
                if b==0:
                    std_list.append(info_list)
                     
                with open('data/student_info.csv','w',newline='') as f2:
                    new_student_info=csv.writer(f2,delimiter=',')
                    new_student_info.writerows(std_list)
            else:
                print('格式不正确，请重新输入')
                continue
            if_continue = input('继续输入（Y/y）?')
            if if_continue.lower() == 'y':
                continue
            else:
                break
    main()



def csv_insert():
    import os
    import csv
    a=0
    while a==0:
        with open('data/student_info.csv','r') as f1:
            student_info=csv.reader(f1,delimiter=',')
            std_list=list(student_info)
            infile=input('请输入文件名')#不用引号，直接打
            c=0
            if not os.path.exists(infile):
                print('文件不存在，请重新输入')
                continue
            else:
                with open(infile,'r') as f1:
                    csv_student_info=csv.reader(f1,delimiter=',')
                    for row in csv_student_info:
                        if len(row)!=6:
                            print('格式不正确，请重新输入')
                            c=1
                            break
                        else:
                            studentID,name,gender,ChineseScore,Mathscore,Englishscore=row
                            if not (studentID.isdigit() and ChineseScore.isdigit() and Mathscore.isdigit() and Englishscore.isdigit() ):
                                print('格式不正确，请重新输入')
                                c=1
                                break
                            elif (len(studentID)==5 and studentID[0]!='0') and (gender=='男' or gender=='女') and (int(ChineseScore)>=0 and int(ChineseScore)<=100 ) and (int(Mathscore)>=0 and int(Mathscore)<=100 ) and (int(Englishscore)>=0 and int(Englishscore)<=100 ):
                                b=0
                                for row_info in std_list:
                                    if row_info[0]==studentID:
                                        row_info=row
                                        b=1
                                if b==0:
                                    std_list.append(row)

                                with open('data/student_info.csv','w',newline='') as f2:
                                    new_student_info=csv.writer(f2,delimiter=',')
                                    new_student_info.writerows(std_list)
                            else:
                                print('格式不正确，请重新输入')
                                c=1
                                break
            if c==1:
                continue
            else:
                print('录入成功')
                break
    main()


    
def search():
    import csv
    compare=['>','>=','==','!=','<','<=']
    member=['in','not']
    a=0
    information=[]
    while a==0:
        with open('data/student_info.csv','r') as f1:
            content=csv.reader(f1,delimiter=',')
            headers=next(content)
            info=input('请输入查询条件')
            info_list=info.split(' ')
            if len(info_list)!=3 and len(info_list)!=4:
                print('格式不正确，请重新输入')
                continue
            elif info_list[1] in compare:
                if info_list[0]=='学号':
                    if_find=False
                    if len(info_list[2])==5 and info_list[2][0]!='0' and info_list[2].isdigit(): 
                        for row in content:
                            info_list[0]=row[0]
                            if eval(' '.join(info_list)):
                                print(row)
                                information.append(row)
                                if_find=True
                        if if_find==False:
                            print('不存在该学生的信息')
                    else:
                        print('格式不正确，请重新输入')
                        continue
                elif info_list[0]=='姓名':
                    if_find=False
                    for row in content:
                        info_list[0]=f'"{row[1]}"'#名字用单引号
                        if eval(' '.join(info_list)):
                            print(row)
                            information.append(row)
                            if_find=True
                    if if_find==False:
                            print('不存在该学生的信息')
                elif info_list[0]=='性别':
                    if_find=False
                    if info_list[2]=="'男'" or info_list[2]=="'女'":#性别用单引号
                        for row in content:
                            info_list[0]=f'"{row[2]}"'
                            if eval(' '.join(info_list)):
                                print(row)
                                information.append(row)
                                if_find=True
                        if if_find==False:
                            print('不存在该学生的信息')
                    else:
                        print('格式不正确，请重新输入')
                        continue
                elif info_list[0]=='语文成绩':
                    if_find=False
                    if info_list[2].isdigit():
                        if int(info_list[2])>=0 and int(info_list[2])<=100:
                            for row in content:
                                info_list[0]=row[3]
                                if eval(' '.join(info_list)):
                                    print(row)
                                    information.append(row)
                                    if_find=True
                            if if_find==False:
                                print('不存在该学生的信息')
                        else:
                            print('格式不正确，请重新输入')
                            continue
                    else:
                        print('格式不正确，请重新输入')
                        continue
                elif info_list[0]=='数学成绩':
                    if_find=False
                    if info_list[2].isdigit():
                        if int(info_list[2])>=0 and int(info_list[2])<=100:
                            for row in content:
                                info_list[0]=row[4]
                                if eval(' '.join(info_list)):
                                    print(row)
                                    information.append(row)
                                    if_find=True
                            if if_find==False:
                                print('不存在该学生的信息')
                        else:
                            print('格式不正确，请重新输入')
                            continue
                    else:
                        print('格式不正确，请重新输入')
                        continue
                elif info_list[0]=='英语成绩':
                    if_find=False
                    if info_list[2].isdigit():
                        if int(info_list[2])>=0 and int(info_list[2])<=100:
                            for row in content:
                                info_list[0]=row[5]
                                if eval(' '.join(info_list)):
                                    print(row)
                                    information.append(row)
                                    if_find=True
                            if if_find==False:
                                print('不存在该学生的信息')
                        else:
                            print('格式不正确，请重新输入')
                            continue
                    else:
                        print('格式不正确，请重新输入')
                        continue
            elif info_list[1] in member:
                if info_list[1]=='in':
                    if_find=False
                    if info_list[2]=='学号':
                        if len(info_list[0])<=5 and info_list[0].isdigit(): 
                            for row in content:
                                if f'{info_list[0]}' in row[0]:
                                    print(row)
                                    information.append(row)
                                    if_find=True
                            if if_find==False:
                                print('不存在该学生的信息')
                        else:
                            print('格式不正确，请重新输入')
                            continue
                    elif info_list[2]=='姓名':
                        for row in content:
                            if f'{info_list[0]}' in row[1]:
                                print(row)
                                information.append(row)
                                if_find=True
                        if if_find==False:
                            print('不存在该学生的信息')
                    else:
                        print('格式不正确，请重新输入')
                        continue
                elif info_list[1]=='not' and info_list[2]=='in':
                    if_find=False
                    if info_list[3]=='学号':
                        if len(info_list[0])<=5 and info_list[0].isdigit(): 
                            for row in content:
                                if f'{info_list[0]}'  not in row[0]:
                                    print(row)
                                    information.append(row)
                                    if_find=True
                            if if_find==False:
                                print('不存在该学生的信息')
                        else:
                            print('格式不正确，请重新输入')
                            continue
                    elif info_list[3]=='姓名':
                        for row in content:
                            if f'{info_list[0]}'  not in row[1]:
                                print(row)
                                information.append(row)
                                if_find=True
                        if if_find==False:
                            print('不存在该学生的信息')
                    else:
                        print('格式不正确，请重新输入')
                        continue
                else:
                    print('格式不正确，请重新输入')
                    continue
            else:
                print('格式不正确，请重新输入')
                continue
            if_continue = input('继续输入（Y/y）?')
            if if_continue.lower() == 'y':
                continue
            else:
                break
    return information



def delete():
    import csv
    a=0
    while a==0:
        info=search()
        print(info)
        with open('data/student_info.csv','r') as f1:
            student_info=csv.reader(f1,delimiter=',')
            std_list=list(student_info)
            if_delete = input('是否删除？（Y/y）?')
            if if_delete.lower() == 'y':
                for item in info:
                    for row in std_list:
                        if row==item:
                            del std_list[std_list.index(row)]
            with open('data/student_info.csv','w',newline='') as f2:
                new_student_info=csv.writer(f2,delimiter=',')
                new_student_info.writerows(std_list)
        if_continue = input('继续删除（Y/y）?')
        if if_continue.lower() == 'y':
            continue
        else:
            break



def display():
    import csv
    with open('data/student_info.csv','r') as f1:
        content=csv.reader(f1,delimiter=',')
        for row in content:
            print(row)



def clear():
    import csv
    if_delete_all = input('是否全部清空（Y/y）?')
    if if_delete_all.lower() == 'y':
        with open('data/student_info.csv','w',newline='') as f2:
            new_student_info=csv.writer(f2,delimiter=',')



def main():
    print("*****欢迎登陆学生信息管理系统*****")
    flag_on = True
    while flag_on:
        menu()  # 显示页面菜单
        a=0
        while a==0:
            option = input("请选择：")  # 选择菜单项 todo:这里需要更多判断，比如只允许输入整数等
            if option.isdigit():
                option=int(option)
                break
            else:
                print('格式不正确，请重新输入')
                continue

        if option == 0:  # 退出选择界面
            print("您已经退出学生信息管理系统！")
            flag_on = False
        elif option == 1:  # 录入学生成绩信息
            insert()
        elif option == 2:  # 从文件录入学生信息
            csv_insert()
        elif option == 3:  # 查询学生成绩信息
            search()
        elif option == 4:  # 删除学生成绩信息
            delete()
        elif option == 5:
            display()
        elif option == 6:
            clear()


if __name__ == "__main__":
    main()