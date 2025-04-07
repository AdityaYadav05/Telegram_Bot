import telebot

Token = "6716708858:AAELRrgbPnDJzs05L1lQD8iaqmdnKrMZbk8"

bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,"Welcome to newlight_classes")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,"""/start -> Greetings
    /help ->Tech_learning_simple will give you all command list
    /links ->Tech_learning_simple will give you list of links
    """)
    
@bot.message_handler(commands=['links'])
def links(message): 
	bot.reply_to(message,"""
    /start -> Welcome to the channel
    /help -> This particular message
    /content -> About various Playlists of Simplilearn
	/Business_Communication -> This first video from Business Communication playlist with complete notes 		  
	/HTML -> This first video from HTML playlist with complete notes 
	/CSS -> This first video from CSS playlist with complete notes 
	/JavaScript -> This first video from Javascript playlist with complete notes 
	/React -> This first video from React playlist with complete notes
	/PHP -> This first video from PHP playlist with complete notes 
	/Bootstrap -> This first video from Bootstrap with complete notes 
	/C_language -> The first video from C language playlist with complete notes
	/C_plus_plus -> The first video from C_plus_plus playlist with complete notes
	/DSA_using_C_language -> The first video from DSA_using_C_language playlist with complete notes
    /Python -> The first video from python Playlist with complete notes
    /Numpy_python -> The first video from Numpy_python Playlist with complete notes
    /Java -> The first video from java playlist with complete notes
    /SQL -> The first video from SQL playlist with complete notes
    /Machine_learning -> The first video from Machine_learning playlist with complete notes	
    /DBMS -> The first video from DBMS playlist with complete notes 
    /AI -> The first video from AI playlist with complete notes
    /OS -> The first video from OS playlist with complete notes
    /TOC -> The first video from TOC playlist with complete notes
    /CN -> The first video from CN playlist with complete notes	
	/CompilerDesign_Tutorial -> The first video from CompilerDesign_Tutorial playlist with complete notes
    /Data_Mining -> The first video from Data_Mining playlist with complete notes				   		   
    /contact -> contact information 
	/Email -> mail me for more information 
    """) 
@bot.message_handler(commands=['Business_Communication'])
def Business_Communication(message): 
	bot.reply_to(message,"""
        /Business_Communication -> https://youtube.com/playlist?list=PLnyJK8kcdCduqkQ7rWxHyIic6_nOeUS5W&si=OXMjz0kWPOvWIgsb
    """)
@bot.message_handler(commands=['HTML'])
def HTML(message): 
	bot.reply_to(message,"""
        /HTML -> https://youtu.be/BsDoLVMnmZs?si=sJL7GE8V7S_7Isih
    """)
@bot.message_handler(commands=['CSS'])
def CSS(message): 
	bot.reply_to(message,"""
        /CSS -> https://youtu.be/ESnrn1kAD4E?si=z1RbSai1l8Xrq6WI
    """)
@bot.message_handler(commands=['JavaScript'])
def JavaScript(message): 
	bot.reply_to(message,"""
        /JavaScript -> https://www.youtube.com/watch?v=ER9SspLe4Hg&list=PLu0W_9lII9ahR1blWXxgSlL4y9iQBnLpR
    """)
@bot.message_handler(commands=['React'])
def React(message): 
	bot.reply_to(message,"""
        /React_tutorial_for_beginner -> https://youtu.be/eILUmCJhl64?si=HogtXXlBKK87YxrJ
    """)
@bot.message_handler(commands=['PHP'])
def PHP(message): 
	bot.reply_to(message,"""
        /PHP_tutorial_for_beginner -> https://www.youtube.com/watch?v=z8gIVootnUQ&pp=ygUPcGhwIGZ1bGwgY291cnNl
    """)
@bot.message_handler(commands=['Bootstrap'])
def Bootstrap(message): 
	bot.reply_to(message,"""
        /Bootstrap_Tutorial_for_beginner -> https://youtu.be/QE5oQh63gGE?si=KJrgb_4ZuSefjl2I
    """)
@bot.message_handler(commands=['C_language'])
def C_language(message): 
	bot.reply_to(message,"""
    /C_language_tutorial_for_beginner -> https://youtu.be/irqbmMNs2Bo?si=bNs3Vjw3Wo3tQ30E
    """) 
@bot.message_handler(commands=['C_plus_plus'])
def C_plus_plus(message): 
	bot.reply_to(message,"""
        /C++ -> https://www.youtube.com/watch?v=z9bZufPHFLU&list=PLfqMhTWNBTe0b2nM6JHVCnAkhQRGiZMSJ
    """)
@bot.message_handler(commands=['DSA_using_C_language'])
def DSA_using_C_language(message): 
	bot.reply_to(message,"""
        /DSA_using_C_language -> https://youtube.com/playlist?list=PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi&si=nXz1YiHG6_xPb6J5
    """)
@bot.message_handler(commands=['Python'])
def Python(message): 
	bot.reply_to(message,"""
        /Python_tutorial_for_beginner -> https://youtu.be/ERCMXc8x7mc?si=U47UE_aQ7I0rCd-p
    """)

@bot.message_handler(commands=['Numpy_python'])
def Numpy_python(message): 
	bot.reply_to(message,"""https://www.youtube.com/watch?v=mHucMTU_p04&list=PLMfAHlb5o1xGe4V0ZGWzYKtDkA9ey5g4a
        /Numpy_python_tutorial_for_beginner -> 
    """)
@bot.message_handler(commands=['Java'])
def Java(message): 
	bot.reply_to(message,"""
        /Java_tutorial_for_beginner-> https://www.youtube.com/watch?v=xwga58I1S94&list=PLmRclvVt5DtnqhXTJwd-oqVRwO3bLZCGV
    """)
@bot.message_handler(commands=['SQL'])
def SQL(message): 
	bot.reply_to(message,"""
        /SQL-> https://www.youtube.com/playlist?list=PLsjUcU8CQXGFFAhJI6qTA8owv3z9jBbpd
    """)
@bot.message_handler(commands=['Machine_learning'])
def Machine_Learning(message): 
	bot.reply_to(message,"""
        /Machine_Learning -> https://youtube.com/playlist?list=PLYwpaL_SFmcBhOEPwf5cFwqo5B-cP9G4P&si=SPF3Xd7jl7sTCW-h
    """)
@bot.message_handler(commands=['DBMS'])
def DBMS(message): 
	bot.reply_to(message,"""
        /DBMS-> https://youtube.com/playlist?list=PLG9aCp4uE-s0bu-I8fgDXXhVLO4qVROGy&si=_hCpH5BeDD-cp_iY
    """)
@bot.message_handler(commands=['AI'])
def AI(message): 
	bot.reply_to(message,"""
        /AI -> https://youtube.com/playlist?list=PLV8vIYTIdSnYsdt0Dh9KkD9WFEi7nVgbe&si=8G8jMwImLjECflZb
    """)
@bot.message_handler(commands=['OS'])
def OS(message): 
	bot.reply_to(message,"""
        /OS -> https://youtube.com/playlist?list=PLG9aCp4uE-s17rFjWM8KchGlffXgOzzVP&si=iIRV28m4iN_-wuTt
    """)
@bot.message_handler(commands=['TOC'])
def TOC(message): 
	bot.reply_to(message,"""
        /TOC -> https://youtube.com/playlist?list=PLir19lgiavA26hKnAmVnyXYIshUXUXuDI&si=hiu59JjZYGVGAh6B
    """)
@bot.message_handler(commands=['CN'])
def CN(message): 
	bot.reply_to(message,"""
        /CN -> https://youtube.com/playlist?list=PLir19lgiavA26fn-H2Doxq3KLuszTCGgE&si=rcG4z7QSwS97-Gyo
    """)
@bot.message_handler(commands=['CompilerDesign_Tutorial'])
def CompilerDesign_Tutorial(message): 
	bot.reply_to(message,"""
        /CompilerDesign_Tutorial-> https://youtube.com/playlist?list=PL-JvKqQx2Ate5DWhppx-MUOtGNA4S3spT&si=9KXQ3NZH6jF5Q4kJ
    """)
@bot.message_handler(commands=['Data_Mining'])
def Data_Mining(message): 
	bot.reply_to(message,"""
        /Data_Mining-> https://youtube.com/playlist?list=PLV8vIYTIdSnb4H0JvSTt3PyCNFGGlO78u&si=NvOExNMEL1yt13JR
    """)
@bot.message_handler(commands=['Email'])
def Email(message): 
	bot.reply_to(message,"""
        /Email-> adityayadavvv12@gmail.com
    """)
@bot.message_handler()
def custom(message):
    try:
        msg = eval(message.text.strip())
    except Exception as e:
        msg = "can't be Evaluated...!"
    bot.reply_to(message,msg)

bot.polling()