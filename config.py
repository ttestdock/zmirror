# coding=utf-8
# 这是为Google和中文维�?无缝整合)镜像配置的示例配置文�?
#
# 使用方法:
#   1. 复制本文件到 zmirror 根目�?wsgi.py所在目�?, 并重命名�?config.py
#   2. 修改 my_host_name 为你自己的域�?
#
# 各项设置选项的详细介绍请�?config_default.py 中对应的部分
# 本配置文件假定你的服务器本身在墙�?
# 如果服务器本身在墙内(或者在本地环境下测�? 请修改`Proxy Settings`中的设置
#
# 由于google搜索结果经常会出现中文维�? 所以顺便把它也加入�?
# google跟中文维基之间使用了本程序的镜像隔离功能, 可以保证中文维基站的正常使用
#
# 本配置文件试图还原出一个功能完整的google.
#   但是由于程序本身所�? 还是不能[完整]镜像过来整个[google站群]
#   在后续版本会不断增加可用的网�?
#
# 以下google服务完全可用:
#   google网页搜索/学术/图片/新闻/图书/视频(搜索)/财经/APP搜索/翻译/网页快照/...
#   google搜索与中文维基百科无缝结�?
# 以下服务部分可用:
#     gg地图(地图可看, 左边栏显示不正常)/G+(不能登录)
# 以下服务暂不可用(因为目前无法解决登录的问�?:
#     所有需要登录的东西, docs之类�?
#

# Github: https://github.com/aploium/zmirror

# ############## Local Domain Settings ##############
my_host_name = 'myzmirror.herokuapp.com'
my_host_scheme = 'https://'
my_host_port = None  # None表示使用默认端口, 可以设置成非标准端口, 比如 81

# ############## Target Domain Settings ##############
target_domain = 'www.google.com'
target_scheme = 'https://'

# 这里面大部分域名都是通过 `enable_automatic_domains_whitelist` 自动采集�? 我只是把它们复制黏贴到了这里
# 实际镜像一个新的站�? 手动只需要添加很少的几个域名就可以了.
# 自动采集(如果开启的�?会不断告诉你新域�?
external_domains = (
    "csi.gstatic.com",
    "www-onepick-opensocial.googleusercontent.com",
    '-v6exp3-ds.metric.gstatic.com',
    '-v6exp3-v4.metric.gstatic.com',
    '3-edge-chat.facebook.com',
    '30.media.tumblr.com',
    '31.media.tumblr.com',
    '32.media.tumblr.com',
    '33.media.tumblr.com',
    '34.media.tumblr.com',
    '35.media.tumblr.com',
    '36.media.tumblr.com',
    '37.media.tumblr.com',
    '38.media.tumblr.com',
    '39.media.tumblr.com',
    '40.media.tumblr.com',
    '41.media.tumblr.com',
    '42.media.tumblr.com',
    '43.media.tumblr.com',
    '44.media.tumblr.com',
    '45.media.tumblr.com',
    '46.media.tumblr.com',
    '47.media.tumblr.com',
    '48.media.tumblr.com',
    '49.media.tumblr.com',
    '50.media.tumblr.com',
    '65.media.tumblr.com',
    '66.media.tumblr.com',
    '67.media.tumblr.com',
    '90.media.tumblr.com',
    '91.media.tumblr.com',
    '92.media.tumblr.com',
    '93.media.tumblr.com',
    '94.media.tumblr.com',
    '95.media.tumblr.com',
    '96.media.tumblr.com',
    '97.media.tumblr.com',
    '98.media.tumblr.com',
    '99.media.tumblr.com',
    'about.twitter.com',
    'abs-0.twimg.com',
    'abs-1.twimg.com',
    'abs-2.twimg.com',
    'abs.twimg.com',
    'accounts.google.com',
    'accounts.gstatic.com',
    'accounts.youtube.com',
    'admin.brightcove.com',
    'ads.twitter.com',
    'afp.google.com',
    'ajax.googleapis.com',
    'ak.sail-horizon.com',
    'amp.twimg.com',
    'analytics.google.com',
    'analytics.twitter.com',
    'api-read.facebook.com',
    'api.adsymptotic.com',
    'api.facebook.com',
    'api.instagram.com',
    'api.lytics.io',
    'api.tumblr.com',
    'api.twitter.com',
    'apis.google.com',
    'apps.google.com',
    'assets.tumblr.com',
    'b.scorecardresearch.com',
    'bam.nr-data.net',
    'blog.instagram.com',
    'blog.twitter.com',
    'books.google.com',
    'bot.talk.google.com',
    'brand.twitter.com',
    'brightcove01.brightcove.com',
    'business.twitter.com',
    'c.brightcove.com',
    'calendar.google.com',
    'caps.twitter.com',
    'cards-dev.twitter.com',
    'cdn.static-economist.com',
    'chatenabled.mail.google.com',
    'chrome.google.com',
    'ci4.googleusercontent.com',
    'client-channel.google.com',
    'clients1.google.com',
    'clients2.google.com',
    'clients3.google.com',
    'clients4.google.com',
    'clients5.google.com',
    'clients6.google.com',
    'cloud.google.com',
    'code.google.com',
    'connect.facebook.net',
    'consent-st.truste.com',
    'consent.truste.com',
    'contact.talk.google.com',
    'cookiex.ngd.yahoo.com',
    'cs600.wac.alphacdn.net',
    'cse.google.com',
    'csi.gstatic.com',
    'cynicallys.tumblr.com',
    'd21j20wsoewvjq.cloudfront.net',
    'd6tizftlrpuof.cloudfront.net',
    'dc.ads.linkedin.com',
    'dcdevtzxo4bb0.cloudfront.net',
    'debates.economist.com',
    'dev-hangoutssearch-pa-googleapis.sandbox.google.com',
    'dev.twitter.com',
    'developers.google.com',
    'dis.us.criteo.com',
    'dl.google.com',
    'dnn506yrbagrg.cloudfront.net',
    'docs.google.com',
    'donate.twitter.com',
    'drive.google.com',
    'edge.quantserve.com',
    'encrypted-tbn0.gstatic.com',
    'encrypted-tbn1.gstatic.com',
    'encrypted-tbn2.gstatic.com',
    'encrypted-tbn3.gstatic.com',
    'encrypted.google.com',
    'engineering.twitter.com',
    'espresso.economist.com',
    'events.google.com',
    'execed.economist.com',
    'external.xx.fbcdn.net',
    'eydisrupters.films.economist.com',
    'facebook.com',
    'families.google.com',
    'fbcdn-photos-a-a.akamaihd.net',
    'feedburner.google.com',
    'fi.google.com',
    'filetransferenabled.mail.google.com',
    'films.economist.com',
    'fonts.googleapis.com',
    'fonts.gstatic.com',
    'friendconnectchat.google.com',
    'g.twimg.com',
    'g2.twimg.com',
    'get.google.com',
    'gg.google.com',
    'global1.cmdolb.com',
    'global2.cmdolb.com',
    'gmail.com',
    'gmail.google.com',
    'gmat.economist.com',
    'goku.brightcove.com',
    'googlemail.l.google.com',
    'goto.google.com',
    'gp3.googleusercontent.com',
    'gre.economist.com',
    'groupchat.google.com',
    'groups.google.com',
    'hangouts.google.com',
    'hca.twimg.com',
    'help.instagram.com',
    'help.twitter.com',
    'horizon.economist.com',
    'i.po.st',
    'i.ytimg.com',
    'ib.adnxs.com',
    'id.google.com',
    'ie.talkgadget.google.com',
    'if-v6exp3-v4.metric.gstatic.com',
    'images.google.com',
    'imp2.ads.linkedin.com',
    'inbox.google.com',
    'infographics.economist.com',
    'inputtools.google.com',
    'instagramstatic-a.akamaihd.net',
    'investor.google.com',
    'ipv4.google.com',
    'isolated.mail.google.com',
    'jobs.economist.com',
    'js.bizographics.com',
    'l.facebook.com',
    'l.instagram.com',
    'lh1.googleusercontent.com',
    'lh2.googleusercontent.com',
    'lh3.googleusercontent.com',
    'lh4.googleusercontent.com',
    'lh5.googleusercontent.com',
    'lh6.googleusercontent.com',
    'link.brightcove.com',
    'localhost.twitter.com',
    'login.wikimedia.org',
    'ls.srvcs.tumblr.com',
    'm.android.com',
    'm.facebook.com',
    'm.gmail.com',
    'm.google.com',
    'm.googlemail.com',
    'ma-0.twimg.com',
    'ma-1.twimg.com',
    'ma-2.twimg.com',
    'ma.twimg.com',
    'mab.chartbeat.com',
    'mail-settings.google.com',
    'mail.google.com',
    'manifest.googlevideo.com',
    'maps-api-ssl.google.com',
    'maps.google.com',
    'maps.googleapis.com',
    'maps.gstatic.com',
    'marketingsolutions.economist.com',
    'media-llnw.licdn.com',
    'media.economist.com',
    'media.tumblr.com',
    'media.twitter.com',
    'meta.wikimedia.org',
    'metrics.brightcove.com',
    'mobile.twitter.com',
    'mpp.mxptint.net',
    'muvc.google.com',
    'mx.tumblr.com',
    'myaccount.google.com',
    'myphonenumbers-pa.googleapis.com',
    'netdna.bootstrapcdn.com',
    'news.google.com',
    'notifications.google.com',
    'o.twimg.com',
    'onetoday.google.com',
    'p.po.st',
    'partner.googleadservices.com',
    'payments.google.com',
    'pbs.twimg.com',
    'people-pa.clients6.google.com',
    'photos.google.com',
    'pic.twitter.com',
    'picasa.google.com',
    'picasaweb.google.com',
    'ping.chartbeat.net',
    'pixel.facebook.com',
    'pixel.fetchback.com',
    'pixel.quantserve.com',
    'platform.linkedin.com',
    'platform.twitter.com',
    'play.google.com',
    'players.brightcove.net',
    'plus.google.com',
    'plus.googleapis.com',
    'plus.sandbox.google.com',
    'po.st',
    'preprod.hangouts.sandbox.google.com',
    'privacy.google.com',
    'productforums.google.com',
    'profiles.google.com',
    'prom.corp.google.com',
    'public.talk.google.com',
    'publish.twitter.com',
    'px.srvcs.tumblr.com',
    'quickread.twitter.com',
    'radio.economist.com',
    'research.google.com',
    's-v6exp1-ds.metric.gstatic.com',
    's.po.st',
    's.yimg.com',
    's.ytimg.com',
    's3.amazonaws.com',
    'sadmin.brightcove.com',
    'sb.scorecardresearch.com',
    'schemas.google.com',
    'scholar.google.com',
    'scholar.googleusercontent.com',
    'scontent-lax3-1.cdninstagram.com',
    'scontent-sjc2-1.cdninstagram.com',
    'scontent.cdninstagram.com',
    'scontent.xx.fbcdn.net',
    'script.google.com',
    'secure.adnxs.com',
    'secure.assets.tumblr.com',
    'secure.quantserve.com',
    'secure.static.tumblr.com',
    'security.google.com',
    'service.maxymiser.net',
    'shop.economist.com',
    'sites.google.com',
    'sjs.bizographics.com',
    'snap.licdn.com',
    'sp.analytics.yahoo.com',
    'ssl.gstatic.com',
    'sstats.economist.com',
    'staging.talkgadget.google.com',
    'stags.bluekai.com',
    'static.chartbeat.com',
    'static.criteo.net',
    'static.xx.fbcdn.net',
    'staticxx.facebook.com',
    'stats.economist.com',
    'stats.g.doubleclick.net',
    'status.twitter.com',
    'storage.googleapis.com',
    'store.google.com',
    'stun.l.google.com',
    'stun1.l.google.com',
    'stun2.l.google.com',
    'stun3.l.google.com',
    'stun4.l.google.com',
    'subscriptions.economist.com',
    'success.economist.com',
    'support.google.com',
    'support.twitter.com',
    'syndication.twitter.com',
    't.co',
    't.lv.twimg.com',
    't.myvisualiq.net',
    't0.gstatic.com',
    't1.gstatic.com',
    't2.gstatic.com',
    't3.gstatic.com',
    'tags.bkrtx.com',
    'tags.bluekai.com',
    'tags.tiqcdn.com',
    'tailfeather.twimg.com',
    'talkgadget.google.com',
    'tdapi-staging.atla.twitter.com',
    'tdapi-staging.smf1.twitter.com',
    'ton.twimg.com',
    'ton.twitter.com',
    'tools.google.com',
    'translate.google.com',
    'translate.googleusercontent.com',
    'tt.mbww.com',
    'tumblr.co',
    'tumblr.com',
    'tweetdeck-devel.atla.twitter.com',
    'tweetdeck-devel.smf1.twitter.com',
    'tweetdeck.localhost.twitter.com',
    'tweetdeck.twitter.com',
    'twitter.com',
    'uds.ak.o.brightcove.com',
    'upload.facebook.com',
    'upload.twitter.com',
    'upload.wikimedia.org',
    'upload.wikipedia.org',
    'video.google.com',
    'video.twimg.com',
    'vt.tumblr.com',
    'vupload-edge.facebook.com',
    'vupload2.facebook.com',
    'w.usabilla.com',
    'wallet.google.com',
    'webcache.googleusercontent.com',
    'webservices.sub2tech.com',
    'worldif.economist.com',
    'www.facebook.com',
    'www.gmail.com',
    'www.google.com',
    'www.googleapis.com',
    'www.googletagservices.com',
    'www.gstatic.com',
    'www.linkedin.com',
    'www.tumblr.com',
    'www.twitter.com',
    'youtube.googleapis.com',
    'zh-cn.facebook.com',
    'zh.m.wikipedia.org',
    'zh.wikipedia.org',
    'www.blogger.com',
    'www.worldcat.org',
    'static1.worldcat.org',
    'www.instagram.com',
)

# 强制所有Google站点使用HTTPS
force_https_domains = 'ALL'

# 自动动态添加域�?
enable_automatic_domains_whitelist = True
domains_whitelist_auto_add_glob_list = (
    '*.google.com', '*.gstatic.com', '*.google.com.hk', '*.googleapis.com', "*.googleusercontent.com", '*.blogspot.com', '*.tumblr.com', '*.blogger.com', '*.googlevideo.com', '*.oclc.org',)

# ############## Proxy Settings ##############
# 如果你在墙内使用本配置文�? 请指定一个墙外的http代理
is_use_proxy = False
# 代理的格式及SOCKS代理, 请看 http://docs.python-requests.org/en/latest/user/advanced/#proxies
requests_proxies = dict(
    http='http://127.0.0.1:8123',
    https='https://127.0.0.1:8123',
)

# ############## Sites Isolation ##############
enable_individual_sites_isolation = True

# 镜像隔离, 用于支持Google和维基共�?
isolated_domains = {'zh.wikipedia.org', 'zh.m.wikipedia.org'}

# ############## URL Custom Redirect ##############
url_custom_redirect_enable = True
url_custom_redirect_list = {
    # 这是一个方便的设置, 如果你访�?/wiki ,程序会自动重定向到后面这个长长的wiki首页
    '/wiki': '/extdomains/https-zh.wikipedia.org/',
    # 这是gmail
    '/gmail': '/extdomains/mail.google.com/mail/u/0/h/girbaeneuj90/',
}
plain_replace_domain_alias = [
    ('www.youtube.com','youtube.kdwnil.tk'),
    ('m.youtube.com','youtube.kdwnil.tk'),
]

# ############# Additional Functions #############
# 移除google搜索结果页面的url跳转
#   原理是往页面中插入一下面这段js
# js来自: http://userscripts-mirror.org/scripts/review/117942
custom_inject_content = {
    "head_first": [
        {
            "content": r"""<script>
function checksearch(){
   var list = document.getElementById('ires');
   if(list){
       document.removeEventListener('DOMNodeInserted',checksearch,false);
       document.addEventListener('DOMNodeInserted',clear,false)
   }
};

function clear(){
   var i; var items = document.querySelectorAll('a[onmousedown]');
   for(i =0;i<items.length;i++){
       items[i].removeAttribute('onmousedown');
   }
};
document.addEventListener('DOMNodeInserted',checksearch,false)
</script>""",
            "url_regex": r"^www\.google(?:\.[a-z]{2,3}){1,2}",
        },
    ]
}
