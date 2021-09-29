# -*- coding: utf-8 -*-
# 根据域名icp备案号查询同备案号关联域名脚本 by _lin9e <lin9e@qq.com> link: https://github.com/1in9e

"""
【域名 -> ICP -> 关联域名s】
icp查询from https://github.com/wongzeon/ICP-Checker
接口:
    <1> https://api.vvhan.com/api/icp?url=
    <2> https://hlwicpfwc.miit.gov.cn/icpproject_query/api/icpAbbreviateInfo/queryByCondition
    接口<2>存在滑动验证码，利用cv2进行破解
"""

import requests,hashlib,time,base64,cv2,os,sys,json

def main(domain):
    try:
        r = requests.get(url='https://api.vvhan.com/api/icp?url='+str(domain.strip()))
        js = json.loads(r.text)
        icp = js['info']['icp']
        # icp存在两种格式:
        #   A: 浙B2-20080224-1
        #   B: 京ICP证030173号-1
        info = icp if '-' not in icp else icp.split('-')[0] if len(icp.split('-'))==2 else icp.split('-')[0]+'-'+icp.split('-')[1]
    except Exception as e:
        print(e)
        info = ''
    print("[*] {} 对应的备案号为{}".format(domain, icp))
    if info:
        info_data = {
            'pageNum':'',
            'pageSize':'',
            'unitName':info
        }
        #构造AuthKey
        timeStamp = int(round(time.time()*1000))
        authSecret = 'testtest' + str(timeStamp)
        authKey = hashlib.md5(authSecret.encode(encoding='UTF-8')).hexdigest()
        #获取Cookie
        cookie_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.42'
        }
        cookie = requests.utils.dict_from_cookiejar(requests.get('https://beian.miit.gov.cn/',headers=cookie_headers).cookies)['__jsluid_s']
        #请求获取Token
        t_url = 'https://hlwicpfwc.miit.gov.cn/icpproject_query/api/auth'
        t_headers = {
            'Host': 'hlwicpfwc.miit.gov.cn',
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
            'Accept': '*/*',
            'DNT': '1',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46',
            'Origin': 'https://beian.miit.gov.cn',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://beian.miit.gov.cn/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cookie': '__jsluid_s=' + cookie
        }
        data = {
            'authKey': authKey,
            'timeStamp': timeStamp
        }
        t_response = requests.post(t_url,data=data,headers=t_headers)
        try:
            get_token = t_response.json()['params']['bussiness']
        except:
            print('\n'"请求被禁止，请稍后或更换头部与IP后再试，状态码：",t_response.status_code)
        #获取验证图像、UUID
        p_url = 'https://hlwicpfwc.miit.gov.cn/icpproject_query/api/image/getCheckImage'
        p_headers = {
            'Host': 'hlwicpfwc.miit.gov.cn',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
            'Accept': 'application/json, text/plain, */*',
            'DNT': '1',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46',
            'token': get_token,
            'Origin': 'https://beian.miit.gov.cn',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://beian.miit.gov.cn/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cookie': '__jsluid_s=' + cookie
        }
        p_request = requests.post(p_url,data='',headers=p_headers)
        try:
            p_uuid = p_request.json()['params']['uuid']
            big_image = p_request.json()['params']['bigImage']
            small_image = p_request.json()['params']['smallImage']
        except KeyError:
            print("请重试，请求状态码：",p_request.status_code)
        #解码图片，写入并计算图片缺口位置
        with open('bigImage.jpg','wb') as f:
            f.write(base64.b64decode(big_image))
            f.close()
        with open('smallImage.jpg','wb') as f:
            f.write(base64.b64decode(small_image))
            f.close()
        background_image = cv2.imread('bigImage.jpg',cv2.COLOR_GRAY2RGB)
        fill_image = cv2.imread('smallImage.jpg',cv2.COLOR_GRAY2RGB)
        background_image_canny = cv2.Canny(background_image, 100, 200)
        fill_image_canny = cv2.Canny(fill_image, 100, 300)
        position_match = cv2.matchTemplate(background_image, fill_image, cv2.TM_CCOEFF_NORMED)
        min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(position_match)
        position = max_loc
        mouse_length = position[0]+1
        os.remove('bigImage.jpg')
        os.remove('smallImage.jpg')
        #通过拼图验证，获取sign
        check_url = 'https://hlwicpfwc.miit.gov.cn/icpproject_query/api/image/checkImage'
        check_headers = {
            'Host': 'hlwicpfwc.miit.gov.cn',
            'Accept': 'application/json, text/plain, */*',
            'Connection': 'keep-alive',
            'Content-Length': '60',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
            'DNT': '1',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.42',
            'token': get_token,
            'Content-Type': 'application/json',
            'Origin': 'https://beian.miit.gov.cn',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://beian.miit.gov.cn/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cookie': '__jsluid_s=' + cookie
        }
        check_data = {
            'key':p_uuid,
            'value':mouse_length
        }
        check_request = requests.post(check_url,json=check_data,headers=check_headers)
        try:
            sign = check_request.json()['params']
        except Exception:
            print('\n'"请求被禁止，请稍后或更换头部与IP后再试，状态码：",check_request.status_code)
        #获取备案信息
        info_url = 'https://hlwicpfwc.miit.gov.cn/icpproject_query/api/icpAbbreviateInfo/queryByCondition'
        info_headers = {
            'Host': 'hlwicpfwc.miit.gov.cn',
            'Connection': 'keep-alive',
            'Content-Length': '78',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
            'DNT': '1',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.42',
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/plain, */*',
            'uuid': p_uuid,
            'token': get_token,
            'sign': sign,
            'Origin': 'https://beian.miit.gov.cn',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://beian.miit.gov.cn/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cookie': '__jsluid_s=' + cookie
        }
        info_request = requests.post(info_url,json=info_data,headers=info_headers)
        domain_total = info_request.json()['params']['total']
        page_total = info_request.json()['params']['lastPage']
        page_size = info_request.json()['params']['pageSize']
        start_row = info_request.json()['params']['startRow']
        end_row = info_request.json()['params']['endRow']

        print("\n[*] 查询对象",info,"共有",domain_total,"个备案域名")
        print("[+] 域名具体信息如下：")
        domain_list = []
        for i in range(1,page_total+1):
            for k in range(start_row,end_row+1):
                info_base = info_request.json()['params']['list'][k]
                domain_name = info_base['domain']
                domain_list.append(domain_name)
                domain_type = info_base['natureName']
                domain_licence = info_base['mainLicence']
                domain_web_licence = info_base['serviceLicence']
                domain_site_name = info_base['serviceName']
                domain_status = info_base['limitAccess']
                domain_approve_date = info_base['updateRecordTime']
                domain_owner = info_base['unitName']
                try:
                    domain_content_approved = info_base['contentTypeName']
                    if not bool(domain_content_approved):
                        domain_content_approved = "无"
                except KeyError:
                    domain_content_approved = "无"
                print("\n域名主办方：",domain_owner)
                print("域名：",domain_name)
                print("网站名称：",domain_site_name)
                print("备案许可证号：",domain_licence)
                print("网站备案号：",domain_web_licence)
                print("域名类型：",domain_type)
                print("网站前置审批项：",domain_content_approved)
                print("是否限制接入：",domain_status)
                print("审核通过日期：",domain_approve_date)
            info_data_page = {
                'pageNum':i+1,
                'pageSize':'10',
                'unitName':info
            }
            if info_data_page['pageNum'] > page_total:
                # print("查询完毕")
                break
            else:
                info_request = requests.post(info_url,json=info_data_page,headers=info_headers)
                start_row = info_request.json()['params']['startRow']
                end_row = info_request.json()['params']['endRow']
                time.sleep(3)
        print("\n[+] RESULT: {} 域名的icp备案 {} 关联域名列表如下: ".format(domain, icp))
        for i in domain_list:
            print(i)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("---ICP查关联域名--- by _lin9e")
        print("Usage: {} 'domain'".format(sys.argv[0]))
        print("例如: python icp_domains.py oppo.com")
    else:
        main(sys.argv[1])
