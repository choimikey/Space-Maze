import time

print('''
*******************************************************************************
 __________________    ______
|__________________||||      |
`----------------.-````--.---'
                 `-.___   `---.___
                   `---`----------\           ___
                         |         \   ___.--'---`----.___
                         |---.___.--`-'  ' . '  .. ` ` "  `----.___
                         >    __[===================================
                         |---'  `-----.___ `` " " " '' ___.-----'
 ________________.------.|___.----./      `---.___.---'
|__________________||||      | '' /
`------------------````------'-- /
                        `-.____.'

*******************************************************************************
''')

time.sleep(2)
print("Welcome to the Space maze.")
time.sleep(2)
print('''.    .        .      .             . .     .        .          .          .
         .                 .                    .                .
  .          You got lost a long time ago in a galaxy far, far away...   .
     .               .           .               .        .             .
     .      .            .                 .                                .
 .      .         .         .   . :::::+::::...      .          .         .
     .         .      .    ..::.:::+++++:::+++++:+::.    .     .
                        .:.  ..:+:..+|||+..::|+|+||++|:.             .     .
            .   .    :::....:::::::::++||||O||O#OO|OOO|+|:.    .
.      .      .    .:..:..::+||OO#|#|OOO+|O||####OO###O+:+|+               .
                 .:...:+||O####O##||+|OO|||O#####O#O||OO|++||:     .    .
  .             ..::||+++|+++++|+::|+++++O#O|OO|||+++..:OOOOO|+  .         .
     .   .     +++||++:.:++:..+#|. ::::++|+++||++O##O+:.++|||#O+    .
.           . ++++++++...:+:+:.:+: ::..+|OO++O|########|++++||##+            .
  .       .  :::+++|O+||+::++++:::+:::+++::+|+O###########OO|:+OO       .  .
     .       +:+++|OO+|||O:+:::::.. .||O#OOO||O||#@###@######:+|O|  .
 .          ::+:++|+|O+|||++|++|:::+O#######O######O@############O
          . ++++: .+OO###O++++++|OO++|O#@@@####@##################+         .
      .     ::::::::::::::::::::++|O+..+#|O@@@@#@###O|O#O##@#OO####     .
 .        . :. .:.:. .:.:.: +.::::::::  . +#:#@:#@@@#O||O#O@:###:#| .      .
                           `. .:.:.:.:. . :.:.:%::%%%:::::%::::%:::
.      .                                      `.:.:.:.:   :.:.:.:.  .   .
           .                                                                .''')

time.sleep(3.5)

print("Your mission is to survive by finding the right way out. Beware of the space monsters.") 
time.sleep(3.5)

left_or_right = input ("You\'re at a crossroad in space, where do you want to go? Type \"Left\" or \"Right\". \n")
time.sleep(2)
lower_left_or_right = left_or_right.lower()
if lower_left_or_right == "left":
  print(f"You steer the ship left.")
  time.sleep(2)
  print("You have chosen the correct path.")
  time.sleep(2)
  swim_or_wait = input("Along the way your ship breaks down. There is about 5 minutes of emergency oxygen left. \n You called for help but they are 4 minutes and 30 seconds away. There is a space lake in front of you. \n Do you want to swim across it or risk waiting for help? Type \"Swim\" or \"Wait\" \n")
  lower_wait = swim_or_wait.lower()
  if swim_or_wait == "wait":
    time.sleep(1)
    print("You chose to wait and help arrived JUST IN TIME!! You made it through the lake! Success!")
    time.sleep(2)
    which_door = input("You traveled through the space lake and now you have reached 3 doors. \n In the middle of space. You can't leave because there is a strong gravitational pull and the only way out is to pick a door. \n Pink, Green, or White. Which door are you picking? \n")
    lower_which_door = which_door.lower()
    if lower_which_door == "green":
      time.sleep(1)
      print('''
      
                 .-"-. 
   *     (   +  /     \ . ) 
      )   )     |#    |  (   * 
  .  (      .    \___/         . 
   + .-"-.    *   /^    +  ( 
    /     \  )   (  .-"-.    )  + 
 .  |#    | (    * /     \  (  ) 
     \___/   )  (  |#    |    (  ' 
  *   /^         )  \___/ 
     (    *  '  (     ^\   *  ' 
 .    \     , , , , , ' \       + 
       )    | | | | |    ) . 
   *    . @%@%@%@%@%@%@ (    ) 
   (      {           }  \  (   * 
    ) *   {           }   )    ( 
   (    @%@%@%@%@%@%@%@%@       ) ' 
 +      {               }  *   ( 
        {               }    .    ) 
        {               }        ( 
*      @%@%@%@%@%@%@%@%@%@    +
      
      ''')
      print("You have made it through the end of the Space Maze... Congratulations on living. Here's your special cake. \n Refresh the page and click run to play again.")
    elif lower_which_door == "pink":
      time.sleep(1)
      print('''
      


                       .-'`/
                   .-'`  _/
               .-'`    _/
            .-'       /
         .-'         /
       .'           (
     .'       ,,////)
    .         __,-^/
   .           \()(
   :               \ 
   :             _  \ 
   :            (____\ 
   :              (
   `          )-.__) 
    `              ) 
     `.           ( 
       `.          \  
         `-.        \      
            `-.      \_        
               `'-.    \_
                   `'-.  \_
                       `'-.\

''')
      print("The moon came alive and smiled at you until you died.")
    elif lower_which_door == "white":
      time.sleep(1.5)
      print('''
      
                            . 
                          _,|\ 
                          \__/ 
                           || 
        ___               {_]. 
         \ \               L; ` 
          ) )               | :  ,(),_,_,(), 
        _/_/                | | / /(,,^,,)\ \ 
                            | || | ;`-o-'; | | 
                            |/:) | | '.' | | ( 
                             \ \(   \_-_/   ) | 
                              \ `._--)=(---.: | 
                              |\ '-_|\O/|_-'/\ 
                             | | `\ |/ \| //\ \ 
                             / /   \     /   \ \ 
                            ; |    :\   /:    \/\ 
                            | (   / \\,// \   )\ \ 
                            | |  /  /|'|\  \  | \ \ 
                            | | /  / | | \  \ | |\ \___ 
                            ) :'-_/--|_|--\_-`: ( `-\ 
                           / /  /    / \    \  \ \ 
                          / /  /    /   \    \  \ \ 
                      /\_/ /  /    /     \    \  \ \_/\ 
                      \___'   /   /       \   \   `___/ 
                             /   /         \   \ 
                            /   /           \   \ 
                           /   /             \   \ 
                           /^/                 \^\ 
                          /  /                 \  \ 
                         /  /                   \  \ 
                        /  /                     \  \ 
                       ' ,/                       \, ` 
                      ; /                           \ : 
                     /__/                           \__\  
                    :__/'                           '\__;  
 
 
      
      ''')
      print("Sailor Moon came and saw you as a threat to the universe and destroyed you.")
    else:
      time.sleep(1)
      print ('''
      
                    .?MMMMMMM8$@m-(".-. 
                 (MMMMMMMMMMMMMMe(%e9ODA#%eRwC1%%?!-"; 
                MMMMMMMMMMMMMMMM*%JOMMMMMMMMMMM8M0DC?*%4?". 
              .9MMMMMMMMMMMMMMMwe2#MMMMMMRC41%J#M&DC1D8&wM@*M& 
             'MMMMMMMMMMMMM0@R9eemMMM#0##M9m**i(%???*i(|1#MRD2 
             MMMMMMMMMMM@$449w2C!J%?C%"";"eCw$"|m==||;-`M. 
           .MMMMMMMMMDO*i(((||(ii?*1?*%i"=(?mR  1%?(("%! 
           mM@MM92e!';"i"?ii(ei;""""";";-(??. 
          %MA!!?;"%"="i""mi'-1"""|""=;"""`&( 
          .(4?"(=';;"""*9w|.-||(i%%|;`';;.;' 
           *eJ;`%("((|i99C|.=|C=!1e;"w...... 
           0m*"1|;"!*(&9me'.-1       M .`..R 
           29*"M      -&C(..";       "i .'i% 
           #C!%m      MRD"...J        M.;(|. 
           @81!9     i&&2;...J=       1;!eiM 
          '99*C8     9!"=''`.(%       $A&2"92 
          'w=-(?     M%=`.`.e(        AMM*%!. 
          CM("A     'OJ%.'.!e         #MMO1w% 
          CMA"M.   .MMM%-;'*.         (MMMR0M 
         %MMO!wD4 -MMM@%"|"M.        1MMMM8&DJ 
         8O1DMMM0w"(!%(*1%"M*       .MM%?AOMMM. 
        'R#MMMMMM!24mO91!("=J.      *MMwMMMMMMM 
     =C@M0MM@Ae2MMMMMMMA1%"%J4|    %MMMMMMM0@&M?"                
   (*M@MMR&&&2C#@#R&&&OC("'.&1='***MMMM#A8&AA1(=( 
  ******%(MMMMM@M#OwmJw4A&&i.="2MMM8OwRwCCC1JmD&&$MD                     


      
      ''')
      print("An AT-AT has come out of the thin fabric of spacetime and blew you up.")

  else:
    time.sleep(1)
    print('''
                    ._,.
           "..-..pf.
          -L   ..#'
        .+_L  ."]#
        ,'j' .+.j`                 -'.__..,.,p.
       _~ #..<..0.                 .J-.``..._f.
      .7..#_.. _f.                .....-..,`4'
      ;` ,#j.  T'      ..         ..J....,'.j`
     .` .."^.,-0.,,,,yMMMMM,.    ,-.J...+`.j@
    .'.`...' .yMMMMM0M@^=`""g.. .'..J..".'.jH
    j' .'1`  q'^)@@#"^".`"='BNg_...,]_)'...0-
   .T ...I. j"    .'..+,_.'3#MMM0MggCBf....F.
   j/.+'.{..+       `^~'-^~~""""'"""?'"``'1`
   .... .y.}                  `.._-:`_...jf
   g-.  .Lg'                 ..,..'-....,'.
  .'.   .Y^                  .....',].._f
  ......-f.                 .-,,.,.-:--&`
                            .`...'..`_J`
                            .~......'#'
                            '..,,.,_]`     
                            .L..`..``.     


    
    
    ''')
    print("There was a TIE-Fighter in the lake and shot you to death.")

    


else:
  time.sleep(1)
  print('''
   _______             _______
|@|@|@|@|           |@|@|@|@|
|@|@|@|@|   _____   |@|@|@|@|
|@|@|@|@| /\_T_T_/\ |@|@|@|@|
|@|@|@|@||/\ T T /\||@|@|@|@|
 ~/T~~T~||~\/~T~\/~||~T~~T\~
  \|__|_| \(-(O)-)/ |_|__|/
  _| _|    \\8_8//    |_ |_
|(@)]   /~~[_____]~~\   [(@)|
  ~    (  |       |  )    ~
      [~` ]       [ '~]
      |~~|         |~~|
      |  |         |  |
     _<\/>_       _<\/>_
    /_====_\     /_====_\
    ''')
  print(f"There was a mecha-bot on the {left_or_right} and it shot you with Jericho Missles and you died...")





