# icp-domains
[![python](https://img.shields.io/badge/python-3.6|3.7|3.8-blue)](https://github.com/1in9e/icp-domains/tree/main/)

输入一个域名，输出ICP备案所有关联域名

### 所用接口
    <1> https://api.vvhan.com/api/icp?url=
    <2> https://hlwicpfwc.miit.gov.cn/icpproject_query/api/icpAbbreviateInfo/queryByCondition

### Usage
python icp_domains.py example.com

例如OPPO.COM
```
(py3env) ➜ python icp_domains.py oppo.com
[*] oppo.com 对应的备案号为粤ICP备08130115号

[*] 查询对象 粤ICP备08130115号 共有 11 个备案域名
[+] 域名具体信息如下：

域名主办方： OPPO广东移动通信有限公司
域名： allawnfs.com
网站名称： OPPO广东移动通信有限公司官方网站
备案许可证号： 粤ICP备08130115号
网站备案号： 粤ICP备08130115号-14
域名类型： 企业
网站前置审批项： 无
是否限制接入： 否
审核通过日期： 2021-08-02 10:46:39

域名主办方： OPPO广东移动通信有限公司
域名： allawntech.com
网站名称： OPPO广东移动通信有限公司官方网站
备案许可证号： 粤ICP备08130115号
网站备案号： 粤ICP备08130115号-12
域名类型： 企业
网站前置审批项： 无
是否限制接入： 否
审核通过日期： 2021-08-06 15:28:13

域名主办方： OPPO广东移动通信有限公司
域名： opdwz.cn
网站名称： OPPO官方网站
备案许可证号： 粤ICP备08130115号
网站备案号： 粤ICP备08130115号-6
域名类型： 企业
网站前置审批项： 无
是否限制接入： 否
审核通过日期： 2021-06-04 17:29:23

域名主办方： OPPO广东移动通信有限公司
域名： coloros.com
网站名称： 软件商店
备案许可证号： 粤ICP备08130115号
网站备案号： 粤ICP备08130115号-9
域名类型： 企业
网站前置审批项： 无
是否限制接入： 否
审核通过日期： 2021-08-02 10:46:06

域名主办方： OPPO广东移动通信有限公司
域名： oppo.cn
网站名称： OPPO广东移动通信有限公司
备案许可证号： 粤ICP备08130115号
网站备案号： 粤ICP备08130115号-3
域名类型： 企业
网站前置审批项： 无
是否限制接入： 否
审核通过日期： 2021-06-04 17:29:23

域名主办方： OPPO广东移动通信有限公司
域名： allawno.com
网站名称： OPPO广东移动通信有限公司官方网站
备案许可证号： 粤ICP备08130115号
网站备案号： 粤ICP备08130115号-13
域名类型： 企业
网站前置审批项： 无
是否限制接入： 否
审核通过日期： 2021-08-02 10:46:32

域名主办方： OPPO广东移动通信有限公司
域名： coloros.net
网站名称： 门户网
备案许可证号： 粤ICP备08130115号
网站备案号： 粤ICP备08130115号-10
域名类型： 企业
网站前置审批项： 无
是否限制接入： 否
审核通过日期： 2021-06-04 17:29:14

域名主办方： OPPO广东移动通信有限公司
域名： oppo.com
网站名称： OPPO官方网站
备案许可证号： 粤ICP备08130115号
网站备案号： 粤ICP备08130115号-1
域名类型： 企业
网站前置审批项： 无
是否限制接入： 否
审核通过日期： 2021-08-02 10:45:58

域名主办方： OPPO广东移动通信有限公司
域名： oppodigital.com.cn
网站名称： oppo蓝光官网
备案许可证号： 粤ICP备08130115号
网站备案号： 粤ICP备08130115号-5
域名类型： 企业
网站前置审批项： 无
是否限制接入： 否
审核通过日期： 2021-09-24 10:37:36

域名主办方： OPPO广东移动通信有限公司
域名： oppodataintel.cn
网站名称： OPPO广东移动通信有限公司
备案许可证号： 粤ICP备08130115号
网站备案号： 粤ICP备08130115号-15
域名类型： 企业
网站前置审批项： 无
是否限制接入： 否
审核通过日期： 2021-06-04 17:29:23

域名主办方： OPPO广东移动通信有限公司
域名： zeku.com
网站名称： OPPO广东移动通信有限公司
备案许可证号： 粤ICP备08130115号
网站备案号： 粤ICP备08130115号-11
域名类型： 企业
网站前置审批项： 无
是否限制接入： 否
审核通过日期： 2021-09-06 17:02:17

[+] +++ oppo.com 域名的icp备案 粤ICP备08130115号 关联域名列表如下:
allawnfs.com
allawntech.com
opdwz.cn
coloros.com
oppo.cn
allawno.com
coloros.net
oppo.com
oppodigital.com.cn
oppodataintel.cn
zeku.com
```
例如toutiao.com
```
(py3env) ➜ python icp_domains.py toutiao.com
...(省略)
[+] +++ toutiao.com 域名的icp备案 京ICP备12025439号 关联域名列表如下:
bytegeckoext.com
searchpstatp.com
xiguashipin.cn
bytefcdn.com
ibdxiguaimg.com
byteactivity15.com
bytecimg.com
bytetraffic.net
ttbyte.net
zijieurl.com
zijieurl.cn
toutiaowap.com
toutiaowap.cn
byteactivity.com
xiguashipin.net
originalstatic.com
toutiaostatic.com
toutiaopage.com
bytedcdn.com
bytegoofy.com
bytegecko.com
bytescm.com
toutiaocdn.com
bytedanceapi.com
bdgslb.com
toutiaoapi.com
zijieapi.com
bytednsdoc.com
zijiecdn.net
zijieimg.com
zijieimg.cn
toutiaocdn.cn
originalvod.com
byteorge.com
byteapi.com
wukongwenda.cn
jstti.com
xiguaapp.com
itoutiaostatic.com
bytetcc.com
jokecommunity.cn
byteactivity13.com
zijieapi.cn
bytemedi.com
toutiaocloud.com
xsgtvacct.com
toutiaolite.com
toutiao.com
toutiao13.com
zjgslb.com
toutiaolite2.com
zjcdn.com
bdxiguavod.com
itoutiaoimg.com
byte-edge.com
bytemastatic.com
toutiaocloud.cn
bytefast.net
toutiao11.com
toutiao12.com
toutiao14.com
toutiao15.com
bdxiguastatic.com
zijietiaodong.com
byteimgc.com
bytevalk.com
baikevod.com
tekkenthree.com
toutiaovod.com
bytetos.com
zijieurl.cn
toutiaowap.com
toutiaowap.cn
byteactivity.com
xiguashipin.net
originalstatic.com
toutiaostatic.com
toutiaopage.com
bytedcdn.com
bytegoofy.com
bytedance.org
ttbyte.cn
zjbyte.com
zjbyte.cn
zijieurl.net
toutiaowap.net
zijiewap.com
bdactivity.com
activitybyte.com
bytecdn.com
bytemaimg.com
pstatp.com
ttwebview.com
byted-edu.com
byteacct.com
bytedns.net
searchtoutiaoimg.com
wukong.com
zijiecdn.com
pacmantwo.com
samasty.com
zilrms.com
ttjisu.com
bytedns2.com
byted-ug.com
bytenewst.com
byteorg.com
searchstatic.com
jokecommunity.net
neihancommunity.com
byteactivity16.com
byteq8u.net
bvfcdn.com
bfcdnrd.com
bytegeckoext.com
searchpstatp.com
xiguashipin.cn
bytefcdn.com
ibdxiguaimg.com
byteactivity15.com
bytecimg.com
bytetraffic.net
ttbyte.net
zijieurl.com
zijieurl.cn
toutiaowap.com
toutiaowap.cn
byteactivity.com
xiguashipin.net
originalstatic.com
bfcdnsc.com
vfcdnrd.com
wtturl.cn
bytedance.com
bytedance.net
bytedance.cn
ttbyte.com
zjbyte.net
zijiewap.cn
zijiewap.net
xiguavideo.cn
cdndns2.com
byte00.com
bytecdn.net
bytemaimg.com
pstatp.com
ttwebview.com
byted-edu.com
byteacct.com
bytedns.net
bytefae.com
livecdnstatic.com
zijiecdn.cn
zijieimg.net
toutiaocdn.net
toutiaolite1.com
tetrisone.com
ixigua.com
originalimg.com
byteactivity12.com
byteorg.com
searchstatic.com
jokecommunity.net
neihancommunity.com
toutiaolite2.com
zjcdn.com
bdxiguavod.com
itoutiaoimg.com
byte-edge.com
bytemastatic.com
bdxigualive.com
byte008.com
byteactivity14.com
toutiaocloud.net
snssdk.com
ibdxiguastatic.com
toutiaoliving.com
byte-gslb.com
byteq5k.com
bytecdntp.com
oortgslb.com
bytegslb.com
byteactivity16.com
byteq8u.net
bvfcdn.com
bfcdnrd.com
```

### Thanks
> 特别说明，备案号查多个备案详情来自于如下项目:
- https://github.com/wongzeon/ICP-Checker

