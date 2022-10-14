#获取html

import requests
import csv
import time
import urllib




page=input("循环次数：")

for p in range(int(page)):
    p=p+16
    with open(f"demo{p}.csv",mode="r",newline="",encoding="utf-8") as demo:
        reader=csv.reader(demo)
        data=[]
        for row in reader:
            param=str(row).replace('[',"").replace(']',"")
            param=param.replace("'","").replace("'","")
            data.append(param)



    count=0
    url2="https://pro.gdstc.gd.gov.cn/egrantweb/proposal/view-prp"
    headers={

                        "Cookie": "initCookieFlag=true; %2Fegrantweb%2Fachievement_registration_apply%2Finquire_listdataGrid%40100088140=zh_title%2Cis_province_project%2Cprj_title%2Csubject_name%2Corg_name%2Cpsn_name%2Cregistration_area%2Cregistration_org_psn_tel%2Cregistration_org_address%2Czh_status%2Creply_result%2Cregistration_no%2Caudit_comment%2Cpublic_information; SESSION=fb7e8df8-731f-4b8d-b50e-06b357a106ba; __root_domain_v=.gd.gov.cn; _qddaz=QD.732463298494606; openstack_cookie_insert=30006528; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; _qdda=5-1.1; _qddab=5-ry6v2s.l90xye5d; winWidth=1294",
                        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',

     }
    session=requests.session()

    for d in data:
        length=len(d)
        d=d[0:length-41]
        d=d.replace("9F", "")
        pre=urllib.parse.unquote(d)+"9xZKvVD3XXc62rzZIrrwM/fWaixZr+Ys="

        param = {
            "posCodeStr": pre,
            "grantCodeStr": "po+kovPJBFr/BGbjM9wGOE4udLCPSfZt",
            "subGrantCodeStr": "po+kovPJBFr/BGbjM9wGOE4udLCPSfZt",
            "ctrCodeStr" : "undefined" ,
            "Action" : "view"
            }

        res=session.get(url2, params=param,headers=headers)
        with open("html//"+str(count)+f"test{p}.html",mode="w",encoding="utf-8") as f:  #操作一个文件，模式是write，写入一个叫first.html的文件，写入的内容是response的内容
            f.write(res.text)
        count+=1
        # time.sleep(5)
    print(count)