import subprocess
import time
import pandas as pd

# 경로의 K_IP ip주소가 있는 파일을 읽음
df= pd.read_excel("ip_check.xlsx")
print("                 Tracert program")
print()
print("--------------------------------------------------------")
print(df)
print()
print("Press the factory code you want to check: (K5, K4, K3)")

fac_cd=input()
Get_list=list(df["Get"])
Send_list=list(df["Send"])
K_fac_list=list(df["K_factory"])

def checking(i):
    proc = subprocess.Popen(['tracert', Send_list[i]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # subprocess를 통해 받은 데이터
    check = proc.communicate()
    check = str(check[0])
    ch = 0
    for i in Get_list:
        if i in check:
            print("True:  " + i)
            ch = 1
    if ch == 0:
        print("No IP: ", i)
#check K5
if fac_cd=='K5' or fac_cd=='k5':
    print("Check K5")
    for i in range(len(Send_list)):
        if 'K5 -' in K_fac_list[i] or 'k5 -' in K_fac_list[i]:
            print(Send_list[i], K_fac_list[i])
            checking(i)
if 'K5 -' in K_fac_list or 'k5 -' in K_fac_list:
    print("Check the K_factory direction. Nothing found")

#check k4
if fac_cd=='K4'or fac_cd=='k4':
    print("Check K4")
    for i in range(len(Send_list)):
        if 'K4 -' in K_fac_list[i] or 'k4 -' in K_fac_list[i]:
            print(Send_list[i], K_fac_list[i])
            checking(i)
if 'K4 -' in K_fac_list or 'k4 -' in K_fac_list:
    print("Check the K_factory direction. Nothing found")

#check k3
if fac_cd == 'K3' or fac_cd == 'k3':
    print("Check K3")
    for i in range(len(Send_list)):
        if 'K3 -' in K_fac_list[i] or 'k3 -' in K_fac_list[i]:
            print(Send_list[i], K_fac_list[i])
            checking(i)
    if 'K3 -' in K_fac_list or 'k3 -' in K_fac_list:
        print("Check the K_factory direction. Nothing found")
print("Finished, press")
