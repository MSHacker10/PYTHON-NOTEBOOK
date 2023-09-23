#!/usr/bin/env python
# coding: utf-8

# In[1]:


phonebook = {}
phonebook["Eesha"] = 938477566
phonebook["Mohsin"] = 938377264
phonebook["Talha"] = 947662781
print(phonebook)


# In[2]:


phonebook = {
    "Alia" : 938477566,
    "Ali" : 938377264,
    "Adil" : 947662781
}
print(phonebook)


# In[3]:


phonebook = {"Rehan" : 938477566,"Ahmad" : 938377264,"Rehman" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))


# In[4]:


phonebook = {
   "Maryam" : 938477566,
   "Hafsa" : 938377264,
   "Nafia" : 947662781
}
del phonebook["Nafia"]
print(phonebook)


# In[5]:


phonebook = {
   "Hassan" : 938477566,
   "Danial" : 938377264,
   "Ihtesham" : 947662781
}
phonebook.pop("Danial")
print(phonebook)


# In[6]:


phonebook = {  
    "Ahsan" : 938477566,
    "Talha" : 938377264,
    "Mohsin" : 947662781
}  

# your code goes here
phonebook["Ahsan"] = 938273443  
del phonebook["Talha"]  

# testing code
if "Ahsan" in phonebook:  
    print("Ahsan is listed in the phonebook.")
    
if "Mohsin" not in phonebook:      
    print("Mohsin is not listed in the phonebook.")  


# In[7]:


# game.py
# import the draw module


def play_game():
    ...

def main():
    result = play_game()
    

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()


# In[8]:


# draw.py

def draw_game():
    ...

def clear_screen(screen):
    ...


# In[9]:


# game.py
# import the draw module


def main():
    result = play_game()
    draw_game(result)


# In[10]:


# game.py
# import the draw module


def main():
    result = play_game()
    draw_game(result)


# In[23]:


# draw.py

def draw_game():
    # when clearing the screen we can use the main screen object initialized in this module
    clear_screen(main_screen)
    ...

def clear_screen(screen):
    ...

class Screen():
    ...

# initialize main_screen as a singleton
main_screen = Screen()


# In[26]:


import urllib
dir(urllib)
['ContentTooShortError', 'FancyURLopener', 'MAXFTPCACHE', 'URLopener', '__all__', '__builtins__', 
'__doc__', '__file__', '__name__', '__package__', '__version__', '_ftperrors', '_get_proxies', 
'_get_proxy_settings', '_have_ssl', '_hexdig', '_hextochr', '_hostprog', '_is_unicode', '_localhost', 
'_noheaders', '_nportprog', '_passwdprog', '_portprog', '_queryprog', '_safe_map', '_safe_quoters', 
'_tagprog', '_thishost', '_typeprog', '_urlopener', '_userprog', '_valueprog', 'addbase', 'addclosehook', 
'addinfo', 'addinfourl', 'always_safe', 'basejoin', 'c', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 
'getproxies_environment', 'getproxies_macosx_sysconf', 'i', 'localhost', 'main', 'noheaders', 'os', 
'pathname2url', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_macosx_sysconf', 'quote', 
'quote_plus', 'reporthook', 'socket', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 
'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'test', 'test1', 
'thishost', 'time', 'toBytes', 'unquote', 'unquote_plus', 'unwrap', 'url2pathname', 'urlcleanup', 'urlencode', 
'urlopen', 'urlretrieve']


# In[28]:


import re

# Your code goes here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))

