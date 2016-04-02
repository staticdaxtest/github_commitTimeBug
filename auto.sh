git add .
git commit -m 'msg'
git push origin master
expect 'username'
send 'staticdax\r'
expect 'password'
send 't0D4y!1@DE#bsf\r'
expect eof
exit
