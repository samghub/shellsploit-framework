#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

from random import randint
#from colorama import init
#init(autoreset=True)
#http://asciiset.com/figletserver.html
def banner( num1,num2,num3,num4):
	logo =[""" 

  ******** **               **  **          **          **   **  
 **////// /**              /** /** ******  /**         //   /**  
/**       /**       *****  /** /**/**///** /**  ******  ** ******
/*********/******  **///** /** /**/**  /** /** **////**/**///**/ 
////////**/**///**/******* /** /**/******  /**/**   /**/**  /**  
       /**/**  /**/**////  /** /**/**///   /**/**   /**/**  /**  
 ******** /**  /**//****** *** ***/**      ***//****** /**  //** 
////////  //   //  ////// /// /// //      ///  //////  //    //  
""",
"""
 ____  _          _ _           _       _ _   
/ ___|| |__   ___| | |___ _ __ | | ___ (_) |_ 
\___ \| '_ \ / _ \ | / __| '_ \| |/ _ \| | __|
 ___) | | | |  __/ | \__ \ |_) | | (_) | | |_ 
|____/|_| |_|\___|_|_|___/ .__/|_|\___/|_|\__|
                         |_|     
""",
"""
  ____   ___                ___ ___                    ___                       
 6MMMMb\ `MM                `MM `MM                    `MM           68b         
6M'    `  MM                 MM  MM                     MM           Y89   /     
MM        MM  __     ____    MM  MM   ____   __ ____    MM   _____   ___  /M     
YM.       MM 6MMb   6MMMMb   MM  MM  6MMMMb\ `M6MMMMb   MM  6MMMMMb  `MM /MMMMM  
 YMMMMb   MMM9 `Mb 6M'  `Mb  MM  MM MM'    `  MM'  `Mb  MM 6M'   `Mb  MM  MM     
     `Mb  MM'   MM MM    MM  MM  MM YM.       MM    MM  MM MM     MM  MM  MM     
      MM  MM    MM MMMMMMMM  MM  MM  YMMMMb   MM    MM  MM MM     MM  MM  MM     
      MM  MM    MM MM        MM  MM      `Mb  MM    MM  MM MM     MM  MM  MM     
L    ,M9  MM    MM YM    d9  MM  MM L    ,MM  MM.  ,M9  MM YM.   ,M9  MM  YM.  , 
MYMMMM9  _MM_  _MM_ YMMMM9  _MM__MM_MYMMMM9   MMYMMM9  _MM_ YMMMMM9  _MM_  YMMM9 
                                              MM                                 
                                              MM                                 
                                             _MM_          
""",

"""
  >=>>=>                       >=>  >=>           >=>                  >=>   
>=>    >=> >=>                 >=>  >=>           >=>             >>   >=>   
 >=>       >=>        >==>     >=>  >=> >=> >=>   >=>    >=>         >=>>==> 
   >=>     >=>>=>   >>   >=>   >=>  >=> >>   >=>  >=>  >=>  >=>  >=>   >=>   
      >=>  >=>  >=> >>===>>=>  >=>  >=> >>   >=>  >=> >=>    >=> >=>   >=>   
>=>    >=> >>   >=> >>         >=>  >=> >=> >=>   >=>  >=>  >=>  >=>   >=>   
  >=>>=>   >=>  >=>  >====>   >==> >==> >=>      >==>    >=>     >=>    >=>  
                                        >=>                                  
""",
"""
.d8888. db   db d88888b db      db      d8888b. db       .d88b.  d888888b d888888b 
88'  YP 88   88 88'     88      88      88  `8D 88      .8P  Y8.   `88'   `~~88~~' 
`8bo.   88ooo88 88ooooo 88      88      88oodD' 88      88    88    88       88    
  `Y8b. 88~~~88 88~~~~~ 88      88      88~~~   88      88    88    88       88    
db   8D 88   88 88.     88booo. 88booo. 88      88booo. `8b  d8'   .88.      88    
`8888Y' YP   YP Y88888P Y88888P Y88888P 88      Y88888P  `Y88P'  Y888888P    YP                                                                             
""",
"""
 .d8888b.  888               888 888          888          d8b 888    
d88P  Y88b 888               888 888          888          Y8P 888    
Y88b.      888               888 888          888              888    
 "Y888b.   88888b.   .d88b.  888 888 88888b.  888  .d88b.  888 888888 
    "Y88b. 888 "88b d8P  Y8b 888 888 888 "88b 888 d88""88b 888 888    
      "888 888  888 88888888 888 888 888  888 888 888  888 888 888    
Y88b  d88P 888  888 Y8b.     888 888 888 d88P 888 Y88..88P 888 Y88b.  
 "Y8888P"  888  888  "Y8888  888 888 88888P"  888  "Y88P"  888  "Y888 
                                     888                              
                                     888                              
                                     888     
""",
"""
  _____ __ __    ___  _      _      ____   _       ___   ____  ______ 
 / ___/|  T  T  /  _]| T    | T    |    \ | T     /   \ l    j|      T
(   \_ |  l  | /  [_ | |    | |    |  o  )| |    Y     Y |  T |      |
 \__  T|  _  |Y    _]| l___ | l___ |   _/ | l___ |  O  | |  | l_j  l_j
 /  \ ||  |  ||   [_ |     T|     T|  |   |     T|     | |  |   |  |  
 \    ||  |  ||     T|     ||     ||  |   |     |l     ! j  l   |  |  
  \___jl__j__jl_____jl_____jl_____jl__j   l_____j \___/ |____j  l__j  

""",
"""
  _______   __              __   __           __           __   __   
 |   _   | |  |--. .-----. |  | |  | .-----. |  | .-----. |__| |  |_ 
 |   1___| |     | |  -__| |  | |  | |  _  | |  | |  _  | |  | |   _|
 |____   | |__|__| |_____| |__| |__| |   __| |__| |_____| |__| |____|
 |:  1   |                           |__|                            
 |::.. . |                                                           
 `-------'  
""",
"""
 _______ _     _ _______                _____          _____  _____ _______
 |______ |_____| |______ |      |      |_____] |      |     |   |      |   
 ______| |     | |______ |_____ |_____ |       |_____ |_____| __|__    |   

"""

]

 #num1 Shellcode amount
 #num2 Os type amount
 #num3 Encoder amount
 #num4 injector amount


	dlogo = """
       \033[32m=[ Shellsploit v1 -\033[4m \033[1;31m BETA                               \033[0m\033[32m]
\033[32m+ -- --=[ %s shellcode -\033[4m \033[1;31m%s Different OS                       \033[0m\033[32m]
\033[32m+ -- --=[ %s encoders -\033[4m \033[1;31m (Shellcodes/executable files)          \033[0m\033[32m]
\033[32m+ -- --=[ %s injector -\033[4m \033[1;31m (PE,ELF,DLL,RAR,DEB etc...)            \033[0m\033[32m]
\033[32m+ -- --=[ %s backdoors -\033[4m \033[1;31m (ReverseShell)                        \033[0m\033[32m]
\033[32m+ -- --=[ Open Source :\033[4m \033[1;31mhttps://github.com/b3mb4m/Shellsploit  \033[0m\033[32m]
	""" % (num1,num2,num3,num4, "7")
	#Will be add a function(counterloop) for backdoors  ..

	return '\033[1;31m'+logo[randint(0, len(logo)-1)]+'\033[0m'+dlogo




