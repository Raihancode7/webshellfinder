#coded by Raihan Adi 
# @Ardi
#!/usr/bin/python3
import os, http.client
import colorama
colorama.init()
def banner():
    print('''
\033[95m┌─┐┬ ┬┌─┐┬  ┬  ┌─┐┬┌┐┌┌┬┐┌─┐┬─┐ 
\033[35m└─┐├─┤├┤ │  │  ├┤ ││││ ││├┤ ├┬┘
\033[94m└─┘┴ ┴└─┘┴─┘┴─┘└  ┴┘└┘─┴┘└─┘┴└─ v1.0
             @Raihan
       https://t.me/Raihan073''')
     
def clearing():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
banner()
website = input('\n Enter Domain Website >>> ')
shells = ['/madspot.php','/mini.php','/amd.php','/minishell.php','/images/galeri/img_album/567814IPT.php','/567814IPT.php','/bhi.php','/sh.php','/IPT.php','/kontol.php','/asu.php','/mad.php','/404.php','/anon.php','/cv.php','/anonymous.php','/shell.php','/sh3ll.php','/madspotshell.php','/b374k.php','/c100.php','/indoxploit.php','/hekel.php','/haxor.php','/IndoXploit.php','/priv8.php','/private.php','/cp.php','/cpbrute.php','/themes/404/404.php','/templates/atomic/index.php','/templates/beez5/index.php','/hacked.php','/r57.php','/wso.php','/WSO.php','/wso24.php','/wso26.php','/wso404.php','/sym.php','/symsa2.php','/sym3.php','/whmcs.php','/whmcskiller.php','/cracker.php','/1.php','/2.php','/sql.php','/gaza.php','/database.php','/a.php','/d.php','/dz.php','/cpanel.php','/system.php','/um3r.php','/zone-h.php','/c22.php','/root.php','/r00t.php','/doom.php','/dam.php','/killer.php','/user.php','/wp-content/plugins/disqus-comment-system/disqus.php','/cpn.php','/shelled.php','/uploader.php','/up.php','/xd.php','/d00.php','/h4xor.php','/tmp/mad.php','/tmp/1.php','/wp-content/plugins/akismet/akismet.php','/images/stories/w.php','/w.php','/downloads/dom.php','/templates/ja-helio-farsi/index.php','/wp-admin/m4d.php','/d.php','/ipt.php','/tebas.php','/hack.php','/raw.php','/madspot.php','/mad.php','/404.php','/anon.php','/anonymous.php','/shell.php','/sh3ll.php','/madspotshell.php','/b374k.php','/c100.php','/priv8.php','/private.php','/cp.php','/cpbrute.php','/themes/404/404.php','/templates/atomic/index.php','/templates/beez5/index.php','/hacked.php','/r57.php','/wso.php','/WSO.php','/wso24.php','/wso26.php','/wso404.php','/sym.php','/symsa2.php','/sym3.php','/whmcs.php','/whmcskiller.php','/cracker.php','/1.php','/2.php','/sql.php','/gaza.php','/database.php','/a.php','/d.php','/dz.php','/cpanel.php','/system.php','/um3r.php','/zone-h.php','/c22.php','/root.php','/r00t.php','/doom.php','/dam.php','/killer.php','/user.php','/wp-content/plugins/disqus-comment-system/disqus.php','/cpn.php','/shelled.php','/uploader.php','/up.php','/xd.php','/d00.php','/h4xor.php','/tmp/mad.php','/tmp/1.php','/wp-content/plugins/akismet/akismet.php','/images/stories/w.php','/w.php','/downloads/dom.php','/templates/ja-helio-farsi/index.php','/wp-admin/m4d.php','/d.php']
foundshells = []

for shell in shells:
    situs = website.replace('http://','')
    host = situs + shell
    conn = http.client.HTTPConnection(situs)
    conn.connect()
    request = conn.request('GET',shell)
    response = conn.getresponse()
    if response.status == 200:
        print('\n\n\t\033[36m[+] Shell found\033[94m %s \n' %host)
        foundshells.append(host)
    else:
        print('\033[31m[-] Not Found\033[94m %s ' %host)
fpth = os.getcwd()
fpth2 = fpth + '/found.txt'
fob = open(fpth2,'w')
fob.close()
fob = open(fpth2,'a')
fob.writelines(foundshells)
print('Found shells saved on found.txt')
input('\n Press enter to exit ! ')
exit()
