pylogo = '''
          .?77777777777777$.            
          777..777777777777$+           
         .77    7777777777$$$           
         .777..77777777$$$$$$           
         ..........:77$$$$$$$           
  .77777777777777777$$$$$$$$$.=======.  
 777777777777777777$$$$$$$$$$.========  
777777777777$$$$$$$$$$$$$$$$ :========+.
77777777777$$$$$$$$$$$$$$+..=========++~
777777777$$..~=====================+++++
77777$$$$.~~==================++++++++: 
 7$$$$$$$.==================++++++++++. 
 .,$$$$$$.================++++++++++~. \\
         .=========~.........           \\
         .=============++++++            {text}
         .==========+++.  .++           
          ,=======++++++,,++,           
          ..=====+++++++++=.            
                .~+=...                 
'''


def py_format(text):
    # Sorry for terrible example
    return pylogo.format(text=text)
