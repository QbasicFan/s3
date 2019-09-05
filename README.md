### s3
Landing page django mezzanine template with custom and optimized SEO 

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
**********************************
ToDo
nothing more today ....
normal w3.css = 87.4 kb
minifyed w3.css = 9.7 kb
- 88.9 %
**********************

If you like this starter theme, want help with your django projects or want more advanced django templates visit my website. http://www.philserme.com/
