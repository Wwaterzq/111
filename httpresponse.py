import requests

def check_3xx_response(hosts):
    for host in hosts:
        url = f"https://{host}"  # 使用 HTTPS 协议生成 URL
        try:
            response = requests.get(url, allow_redirects=False)
            if response.status_code >= 300 and response.status_code < 400:
                print(f"The URL {url} returned a {response.status_code} response (3xx redirect).")
                print(response.links)
            else:
                print(f"The URL {url} returned a {response.status_code} response.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred for {url}: {e}")

if __name__ == "__main__":
    target_hosts = [
        "aliyun.com"
    ".aliyun.com",
    "2Fclick.aliyun.com",
    "2Fdeveloper.aliyun.com",
    "2Fhelp.aliyun.com",
    "2Fnew-developer.aliyun.com",
    "2Fxz.aliyun.com",
    "ac.aliyun.com",
    "account.aliyun.com",
    "ai.aliyun.com",
    "ailab.aliyun.com",
    "alert.console.aliyun.com",
    "apds.console.aliyun.com",
    "apsara-stack.aliyun.com",
    "arthas.aliyun.com",
    "beian.aliyun.com",
    "bp.aliyun.com",
    "bsn.console.aliyun.com",
    "click.aliyun.com",
    "cn.aliyun.com",
    "code.aliyun.com",
    "cr.console.aliyun.com",
    "data.aliyun.com",
    "datalakeanalytics.console.aliyun.com",
    "developer.aliyun.com",
    "dms.aliyun.com",
    "dns.aliyun.com",
    "edu.aliyun.com",
    "error-center.aliyun.com",
    "event.aliyun.com",
    "exmail.aliyun.com",
    "expressconnect.console.aliyun.com",
    "free.aliyun.com",
    "gc.ditu.aliyun.com",
    "gs.aliyun.com",
    "hdr.console.aliyun.com",
    "help.aliyun.com",
    "home.console.aliyun.com",
    "homenew.console.aliyun.com",
    "intl.aliyun.com",
    "iot.aliyun.com",
    "ip.console.aliyun.com",
    "jianzhan.aliyun.com",
    "jr.aliyun.com",
    "kafka.console.aliyun.com",
    "linkdevelop.aliyun.com",
    "living.aliyun.com",
    "logo.aliyun.com",
    "mail.aliyun.com",
    "mail.sg.aliyun.com",
    "market.aliyun.com",
    "market.console.aliyun.com",
    "maven.aliyun.com",
    "media.aliyun.com",
    "mgw.console.aliyun.com",
    "mirrors.aliyun.com",
    "mns.console.aliyun.com",
    "mse.console.aliyun.com",
    "nas.console.aliyun.com",
    "new-developer.aliyun.com",
    "ntp1.aliyun.com",
    "ntp2.aliyun.com",
    "ntp3.aliyun.com",
    "ntp4.aliyun.com",
    "ntp5.aliyun.com",
    "ntp6.aliyun.com",
    "open.aliyun.com",
    "opt.aliyun.com",
    "order.aliyun.com",
    "oss.console.aliyun.com",
    "partner.aliyun.com",
    "pop.qiye.aliyun.com",
    "promotion.aliyun.com",
    "qiye.aliyun.com",
    "ram.console.aliyun.com",
    "report.aliyun.com",
    "security.aliyun.com",
    "serverless.aliyun.com",
    "service.aliyun.com",
    "servicemesh.console.aliyun.com",
    "signin.aliyun.com",
    "smartag.console.aliyun.com",
    "smtphk.qiye.aliyun.com",
    "spf.qiye.aliyun.com",
    "spf1.dm.aliyun.com",
    "summit.aliyun.com",
    "survey.aliyun.com",
    "talk.aliyun.com",
    "tianchi.aliyun.com",
    "tm.aliyun.com",
    "tongyi.aliyun.com",
    "usercenter.console.aliyun.com",
    "usercenter2.aliyun.com",
    "vision.aliyun.com",
    "vs.console.aliyun.com",
    "wanwang.aliyun.com",
    "workbench.aliyun.com",
    "xianzhi.aliyun.com",
    "xing.aliyun.com",
    "xz.aliyun.com",
    "yqh.aliyun.com",
    "yunxiao.aliyun.com",
    "zhongbao.aliyun.com"
]
    check_3xx_response(target_hosts)

# .aliyun.com
# 2Fclick.aliyun.com
# 2Fdeveloper.aliyun.com
# 2Fhelp.aliyun.com
# 2Fnew-developer.aliyun.com
# 2Fxz.aliyun.com
# ac.aliyun.com
# account.aliyun.com
# ai.aliyun.com
# ailab.aliyun.com
# alert.console.aliyun.com
# apds.console.aliyun.com
# apsara-stack.aliyun.com
# arthas.aliyun.com
# beian.aliyun.com
# bp.aliyun.com
# bsn.console.aliyun.com
# click.aliyun.com
# cn.aliyun.com
# code.aliyun.com
# cr.console.aliyun.com
# data.aliyun.com
# datalakeanalytics.console.aliyun.com
# developer.aliyun.com
# dms.aliyun.com
# dns.aliyun.com
# edu.aliyun.com
# error-center.aliyun.com
# event.aliyun.com
# exmail.aliyun.com
# expressconnect.console.aliyun.com
# free.aliyun.com
# gc.ditu.aliyun.com
# gs.aliyun.com
# hdr.console.aliyun.com
# help.aliyun.com
# home.console.aliyun.com
# homenew.console.aliyun.com
# intl.aliyun.com
# iot.aliyun.com
# ip.console.aliyun.com
# jianzhan.aliyun.com
# jr.aliyun.com
# kafka.console.aliyun.com
# linkdevelop.aliyun.com
# living.aliyun.com
# logo.aliyun.com
# mail.aliyun.com
# mail.sg.aliyun.com
# market.aliyun.com
# market.console.aliyun.com
# maven.aliyun.com
# media.aliyun.com
# mgw.console.aliyun.com
# mirrors.aliyun.com
# mns.console.aliyun.com
# mse.console.aliyun.com
# nas.console.aliyun.com
# new-developer.aliyun.com
# ntp1.aliyun.com
# ntp2.aliyun.com
# ntp3.aliyun.com
# ntp4.aliyun.com
# ntp5.aliyun.com
# ntp6.aliyun.com
# open.aliyun.com
# opt.aliyun.com
# order.aliyun.com
# oss.console.aliyun.com
# partner.aliyun.com
# pop.qiye.aliyun.com
# promotion.aliyun.com
# qiye.aliyun.com
# ram.console.aliyun.com
# report.aliyun.com
# security.aliyun.com
# serverless.aliyun.com
# service.aliyun.com
# servicemesh.console.aliyun.com
# signin.aliyun.com
# smartag.console.aliyun.com
# smtphk.qiye.aliyun.com
# spf.qiye.aliyun.com
# spf1.dm.aliyun.com
# summit.aliyun.com
# survey.aliyun.com
# talk.aliyun.com
# tianchi.aliyun.com
# tm.aliyun.com
# tongyi.aliyun.com
# usercenter.console.aliyun.com
# usercenter2.aliyun.com
# vision.aliyun.com
# vs.console.aliyun.com
# wanwang.aliyun.com
# workbench.aliyun.com
# xianzhi.aliyun.com
# xing.aliyun.com
# xz.aliyun.com
# yqh.aliyun.com
# yunxiao.aliyun.com
# zhongbao.aliyun.com
