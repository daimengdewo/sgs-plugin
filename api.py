from time import sleep
from win32com.client import Dispatch
from util import calculate_text
from pprint import pprint
import os,sys

dm = Dispatch('dm.dmsoft')
path = os.getcwd() + '\pic'
dm.setpath(path)
black_pic = 'b1.bmp|b2.bmp|b3.bmp|b4.bmp|b5.bmp|b6.bmp|b7.bmp|b8.bmp|b9.bmp|b10.bmp|b11.bmp|b12.bmp|b13.bmp'
red_pic = 'r1.bmp|r2.bmp|r3.bmp|r4.bmp|r5.bmp|r6.bmp|r7.bmp|r8.bmp|r9.bmp|r10.bmp|r11.bmp|r12.bmp|r13.bmp'

global black_nbr
global red_nbr

def getnbr():
    YJ = dm.FindpicE(0,0,1920,1080,'YJ.bmp','050505',0.9,0)
    if YJ != '-1|-1|-1':
        # pos = str(YJ).split('|')
        QD = dm.FindpicE(0,0,1920,1080,'QD.bmp','050505',0.9,0)
        ZD = dm.FindpicE(0,0,1920,1080,'ZD.bmp','050505',0.9,0)

        if QD != '-1|-1|-1' and ZD != '-1|-1|-1':
            qd = str(QD).split('|')
            zd = str(ZD).split('|')
            qdx = qd[1]
            qdy = qd[2]
            zdx = zd[1]
            zdy = zd[2]
            black_Cards = dm.FindpicEx(qdx,qdy,zdx,zdy,black_pic,'050505',0.6,0)
            black_nbr = str(black_Cards).split('|')
            red_Cards = dm.FindpicEx(qdx,qdy,zdx,zdy,red_pic,'050505',0.6,0)
            red_nbr = str(red_Cards).split('|')
    try:
        if black_nbr[0] or red_nbr[0] != '':
            YJnbr = []
            if black_nbr[0] != '':
                i = 0   
                for b in black_nbr:
                    i += 1
                    data = str(b).split(',')
                    YJnbr.append(int(data[0])+1)
                    if i == len(black_nbr):
                        break
            if red_nbr[0] != '':
                i = 0  
                for r in red_nbr:
                    i += 1
                    data = str(r).split(',')
                    YJnbr.append(int(data[0])+1)
                    if i == len(red_nbr):
                        break
        text = '{}'.format(YJnbr).strip('[]')
        print('#############################################')
        print('\n')
        print('手牌识别结果为：{}'.format(text))
        print('\n')
        print('---------------尝试计算，请稍后---------------')
        result = calculate_text(text)
        print('智能推荐可选组合如下：')
        print('\n')
        result_long = len(result[0][0]) + len(result[0][1])
        for ret in result:
            if len(ret[0])+len(ret[1]) >= result_long:
                # print(result_long)
                # print(len(ret[0])+len(ret[1]))
                pprint(ret)
                print('\n')
        print('#############################################')
        sys.stdout.flush()
        sleep(30)
    except Exception as e:
        i = 1
        # print('ERROR：未找到目标窗口，将在{}秒后重试。'.format(i))
        sleep(i)




