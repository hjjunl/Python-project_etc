import subprocess
import pandas as pd

# 경로의 K_IP ip주소가 있는 파일을 읽음
df= pd.read_excel("ip_check.xlsx")
print("why")
Send_list=list(df["Send"])
Get_list=list(df["Get"])
K_fac_list=list(df["K_factory"])
Check_list = []

for i in range(len(Send_list)):
    proc = subprocess.Popen(['tracert', Get_list[i]], stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    # subprocess를 통해 받은 데이터
    check = proc.communicate()
    check = str(check[0])
    ch = 0
    for i in Send_list:
        if i in check:
            Check_list.append("True")
            ch = 1
    if ch == 0:
        Check_list.append("False")
arr=[]
df['Check']=Check_list
for i in range(len(df['Check'])):
    if 'False' in df['Check'][i]:
        arr.append(i)

df2=df.loc[arr,:]

print(df2)
# print(df)
