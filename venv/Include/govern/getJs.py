#获取数据源
import  requests

headers = {
   
    "Cookie":"initCookieFlag=true; %2Fegrantweb%2Fachievement_registration_apply%2Finquire_listdataGrid%40100088140=zh_title%2Cis_province_project%2Cprj_title%2Csubject_name%2Corg_name%2Cpsn_name%2Cregistration_area%2Cregistration_org_psn_tel%2Cregistration_org_address%2Czh_status%2Creply_result%2Cregistration_no%2Caudit_comment%2Cpublic_information; SESSION=ad4e35b5-4ba3-46b5-bcd5-9209b25436a1; __root_domain_v=.gd.gov.cn; _qddaz=QD.732463298494606; openstack_cookie_insert=21286086; _qdda=5-1.1; _qddab=5-61c2ie.l8oa9qgt; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; winWidth=1294"
}

page=input("输入page数目：")

for p in range(int(page)):
    p=p+1;
    url="https://pro.gdstc.gd.gov.cn/egrantweb/prpapprove/list-for-view"
    data={
    "_search": "false",
    "nd": "1664530486548",
    "rows": "100",
    "page": f"{p}",
    "sidx": "status,final_conclusion,other_status,old_status,NLSSORT(zj_name,'NLS_SORT = SCHINESE_PINYIN_M') asc,NLSSORT(grant_name,'NLS_SORT = SCHINESE_PINYIN_M') asc,NLSSORT(area_name,'NLS_SORT = SCHINESE_PINYIN_M') asc,NLSSORT(org_name,'NLS_SORT = SCHINESE_PINYIN_M') asc,NLSSORT(psn_name,'NLS_SORT = SCHINESE_PINYIN_M') asc,NLSSORT(zh_title,'NLS_SORT = SCHINESE_PINYIN_M'),prp_no",
    "sord": "asc",
    "searchString": "stat_year:2022[tear]stat_year_name:2022[tear]grant_code_at_code:73[tear]grant_code_at_code:73"
    }
    res=requests.post(url,data=data,headers=headers)
    with open(f"js{p}.html",mode="w",encoding="utf-8") as f:  #操作一个文件，模式是write，写入一个叫first.html的文件，写入的内容是response的内容
        f.write(res.text)