#I thought I found a bug of github...
===============================
I've used a time-misconfig machine to push my code and, of course, caused some kind of certification problem.
I didn't aware the time was wrong at that moment.
After the some googling I decided to use the command `export GIT_SSL_NO_VERIFY=1` to compress the error message for remedy.
Soon I found github cannot track my commit correctly which notice me machine's time was misconfigured.
So come to the conclusion, if you set env variety "GIT_SSL_NO_VERIFY=1" and set time as you want, theoretically you can commit anything at anytime.

Why not have some fun with this? :)
