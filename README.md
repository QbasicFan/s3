# s3
Simple template 3
Template starter

3 Sections + contact

editable Model


Front => auto slider 

Section1s

Section2s




![alt text](https://github.com/QbasicFan/s3/blob/master/ss3.png)



*****************
Install
*****************

1)

git clone https://github.com/QbasicFan/s3 

2) settings.py

INSTALLED_APPS = (
    "s3",
    
    ...
3) settings.py

 os.path.join(PROJECT_ROOT, "[full path to ]/s3/templates"),

4) urls.py

  url("^$", include("s3.urls")),
  
5)
python manage.py makemigrations s3
python manage.py migrate s3

6) re-runserver


**********************

If you like this starter theme, want help with your django projects or want more advanced django templates visit my website. http://www.philserme.com/
