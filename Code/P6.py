import random
import pygame
import sys
import time
import math
import socket
import threading
import webbrowser

#Thread Start Variables
stop_all = threading.Event()

#Pygame Start Variables
pygame.init()
pygame.font.init()
width = 1000
height = 700
size = (width, height)
icon = pygame.image.load("Images/UNm.png")
icon = pygame.transform.scale_by(icon, 2)
pygame.display.set_icon(icon)
pygame.display.set_caption("UNO")

#Screen Surfaces
screen = pygame.display.set_mode(size)
alpha_surface = pygame.Surface((size), pygame.SRCALPHA)
text_cuadrant_surface = pygame.Surface((250,300), pygame.SRCALPHA)

#Fonts
font_win_defeat = pygame.font.SysFont('Arial', 98)
font_reason_win_defeat =  pygame.font.SysFont('Arial', 24)
title_size = 140
font_title = pygame.font.SysFont('Arial', title_size)
font_button = pygame.font.SysFont("Arial", 80)
font_button2 = pygame.font.SysFont("Arial", 70)
font_button3 = pygame.font.SysFont("Arial", 115)
font_button4 = pygame.font.SysFont("Arial", 50)
font_button5 = pygame.font.SysFont("Arial", 85)
font_button6 = pygame.font.SysFont("Arial", 50)
font_button7 = pygame.font.SysFont("Arial", 35)
font_button8 = pygame.font.SysFont("Arial", 45)
font_button9 = pygame.font.SysFont("Arial", 55)
font_chat = pygame.font.SysFont("Arial", 16)
font_chat2 = pygame.font.SysFont("Arial", 22)

#Pre Renders
uno_rect_text = font_button9.render("UNO", True, (0,0,255))
background__main_menu_image = pygame.image.load("Images/background_title_screen.png")
background_image = pygame.image.load("Images/Background_play.png")

card_image_bot = pygame.image.load("Images/UN.png")
card_image_resiced_bot = pygame.transform.scale(card_image_bot, (50,75))

card_images = {"0R":pygame.image.load("Images/0R.png"),"0B":pygame.image.load("Images/0B.png"),"0Y":pygame.image.load("Images/0Y.png"),"0G":pygame.image.load("Images/0G.png"),
			   "1R":pygame.image.load("Images/1R.png"),"1B":pygame.image.load("Images/1B.png"),"1Y":pygame.image.load("Images/1Y.png"),"1G":pygame.image.load("Images/1G.png"),
			   "2R":pygame.image.load("Images/2R.png"),"2B":pygame.image.load("Images/2B.png"),"2Y":pygame.image.load("Images/2Y.png"),"2G":pygame.image.load("Images/2G.png"),
			   "3R":pygame.image.load("Images/3R.png"),"3B":pygame.image.load("Images/3B.png"),"3Y":pygame.image.load("Images/3Y.png"),"3G":pygame.image.load("Images/3G.png"),
			   "4R":pygame.image.load("Images/4R.png"),"4B":pygame.image.load("Images/4B.png"),"4Y":pygame.image.load("Images/4Y.png"),"4G":pygame.image.load("Images/4G.png"),
			   "5R":pygame.image.load("Images/5R.png"),"5B":pygame.image.load("Images/5B.png"),"5Y":pygame.image.load("Images/5Y.png"),"5G":pygame.image.load("Images/5G.png"),
			   "6R":pygame.image.load("Images/6R.png"),"6B":pygame.image.load("Images/6B.png"),"6Y":pygame.image.load("Images/6Y.png"),"6G":pygame.image.load("Images/6G.png"),
			   "7R":pygame.image.load("Images/7R.png"),"7B":pygame.image.load("Images/7B.png"),"7Y":pygame.image.load("Images/7Y.png"),"7G":pygame.image.load("Images/7G.png"),
			   "8R":pygame.image.load("Images/8R.png"),"8B":pygame.image.load("Images/8B.png"),"8Y":pygame.image.load("Images/8Y.png"),"8G":pygame.image.load("Images/8G.png"),
			   "9R":pygame.image.load("Images/9R.png"),"9B":pygame.image.load("Images/9B.png"),"9Y":pygame.image.load("Images/9Y.png"),"9G":pygame.image.load("Images/9G.png"),
			   "+2R":pygame.image.load("Images/+2R.png"),"+2B":pygame.image.load("Images/+2B.png"),"+2Y":pygame.image.load("Images/+2Y.png"),"+2G":pygame.image.load("Images/+2G.png"),
			   "FR":pygame.image.load("Images/FR.png"),"FB":pygame.image.load("Images/FB.png"),"FY":pygame.image.load("Images/FY.png"),"FG":pygame.image.load("Images/FG.png"),
			   "XR":pygame.image.load("Images/XR.png"),"XB":pygame.image.load("Images/XB.png"),"XY":pygame.image.load("Images/XY.png"),"XG":pygame.image.load("Images/XG.png"),
			   "RR":pygame.image.load("Images/RR.png"),"BB":pygame.image.load("Images/BB.png"),"YY":pygame.image.load("Images/YY.png"),"GG":pygame.image.load("Images/GG.png"),
			   "WW":pygame.image.load("Images/WW.png"),"+4W":pygame.image.load("Images/+4W.png"),"UnBut":pygame.image.load("Images/uno_button.png"),"RulBut":pygame.image.load("Images/Rules.png"),
      		   "GitBut":pygame.image.load("Images/github.png"),"P1IMG":pygame.image.load("Images/Player1.png"),"P2IMG":pygame.image.load("Images/Player2.png"),
			   "P3IMG":pygame.image.load("Images/Player3.png"),"P4IMG":pygame.image.load("Images/Player4.png")}

#Lists
#Title Colors
title_colors = [(0,0,255)]*20+[(0,8,247),(0,16,239),(0,24,231),(0,32,223),(0,40,215),(0,48,207),(0,56,199),(0,64,191),(0,72,183),(0,80,175),(0,88,167),(0,96,159),(0,104,151),(0,112,143),(0,120,135),(0,128,127),(0,136,119),(0,144,111),(0,152,103),(0,160,95),(0,168,87),(0,176,79),(0,184,71),(0,192,63),(0,200,55),(0,208,47),(0,216,39),(0,224,31),(0,232,23),(0,240,15),(0,248,7),(0,255,0)]+[(0,255,0)]*40+[(16,255,0),(32,255,0),(48,255,0),(64,255,0),(80,255,0),(96,255,0),(112,255,0),(128,255,0),(144,255,0),(160,255,0),(176,255,0),(192,255,0),(208,255,0),(224,255,0),(240,255,0),(255,255,0)]+[(255,255,0)]*40+[(255,248,0),(255,240,0),(255,232,0),(255,224,0),(255,216,0),(255,208,0),(255,200,0),(255,192,0),(255,184,0),(255,176,0),(255,168,0),(255,160,0),(255,152,0),(255,144,0),(255,136,0),(255,128,0),(255,120,0),(255,112,0),(255,104,0),(255,96,0),(255,88,0),(255,80,0),(255,72,0),(255,64,0),(255,56,0),(255,48,0),(255,40,0),(255,32,0),(255,24,0),(255,16,0),(255,8,0),(255,0,0)]+[(255,0,0)]*40+[(255,0,0),(248,0,7),(240,0,15),(232,0,23),(224,0,31),(216,0,39),(208,0,47),(200,0,55),(192,0,63),(184,0,71),(176,0,79),(168,0,87),(160,0,95),(152,0,103),(144,0,111),(136,0,119),(128,0,127),(120,0,135),(112,0,143),(104,0,151),(96,0,159),(88,0,167),(80,0,175),(72,0,183),(64,0,191),(56,0,199),(48,0,207),(40,0,215),(32,0,223),(24,0,231),(16,0,239),(8,0,247),(0,0,255)]+[(0,0,255)]*20
#Rule Text
rules_text = [
    "SINGLE PLAYER RULES:",
    "- Block and Reverse cards return the turn to the one who played it.",
    "- When you have only one card, an 'UNO' button appears floating ",
    "  on the screen.Click it fast, or you will receive 2 more cards.",
    "",
    "LOCAL MULTIPLAYER RULES:",
    "- If there are only 2 players, Block and Reverse cards work", 
    "  like in Single Player.",
    "- In games with more than 2 players, Block skips the next", 
    "  player's turn and Reverse changes the direction of turns.",
    "- When a player has only one card, the 'UNO' button appears", 
    "  as in Single Player.",
	"- The ball on top of each deck represents the Player depending",
	"  on how many points does the ball have."
    "",
    "ONLINE MULTIPLAYER RULES:",
    "- To join a session, enter the host's IP, port, and password", 
    "  the host can see this at the left of the host waiting screen.",
	"  In the join menu LAN is for the same device(have 2 games in the",
	"  same device) and WAN is for remote connection. If the remote",
 	"  connection is in the same wifi then is as simple as just put ip,", 
	"  port, and password. But if the host is in another wifi that wifi", 
 	"  needs to have port forwading with the port being used.(At the end", 
  	"  I explain how to set up port forwading)",
    "- Card rules are the same as Local Multiplayer.",
    "- The 'UNO' button is always visible next to the center card.",
    "- If no one has UNO, players clicking it will receive 2 cards.",
    "- If a player with one card clicks 'UNO' before anyone else,",
    "  no cards are added to others and this player is safe for the turn.", 
    "- False 'UNO' clicks add 2 cards without passing the turn.",
    "- There is a chat box: press Enter to activate it,", 
    "  type your message, and Enter to send.",
    "  Press Enter with an empty message to close the chat box."
    "",
    "KEYS",
    "- To move through the menu click the button to go to select it",
    "  and press the key ESCAPE to go back and if you are in a game",
    "  ESCAPE will open a menu to quit",
    "- In a game you have 2 options place a card or pick one to advance",
    "  your turn, if you wanna play a card click a card to play, and click",
    "  the central card, in case you want to pick one, just click the big deck",
    "  at the left of the central card",
    "- Choosing color, when you play a wild card for circles at the left of the",
    "  screen will appear click the circle of the color you want to pick",
    "- Write, in any part that requires you to write something just write it",
    "  no indicator will appear",
	"",
	"PORTFORWARDING",
	"- Port forwarding lets others connect to your game online.",
	"- You need your local IP and access to your router settings.",
	"",
	"- To get your local IP on Windows, open CMD and type: ipconfig",
	"  then look for the IPv4 Address (example: 192.168.1.15).",
	"",
	"- Open your browser and enter your router gateway.",
	"  Usually it is something like 192.168.1.1 or 192.168.0.1.",
	"  Log in with the username and password from your router",
	"  (often written on the router label or given by your provider).",
	"",
	"- In your router settings look for NAT, Port Forwarding,",
	"  Advanced Settings, or Firewall. The name can vary.",
	"  Add the port your game uses, choose TCP, UDP, or BOTH.",
	"  Then select the device using the IPv4 you found earlier.",
	"  Save the changes when finished.",
	"",
	"- Now, to allow others to join, you need your Public IP.",
	"  Search on Google: what is my ip and copy the number shown.",
	"  This is the IP your friends will use to connect.",
	"",
	"- Share your Public IP, the Port you opened, and the Server",
	"  password if the game has one. Players can now connect",
	"  even if they are using different Wi-Fi networks.",
	"",
	"- If it does not work, your provider may be blocking ports",
	"  with something called CGNAT. If so, call your provider",
	"  and ask them to disable CGNAT or enable port forwarding."
    
]

#Tricky Init Variables
player_amount_checker = 1
y_checker = 111
BOT_checker = True
def Start_Variables():
	"""
	If You Are Reading This, Im Sorry for this WarCrime of a Code, I Just Wanna Finish
	If You Are Getting Sick Of Seing This def, I Do Recommend That You Stop Watching
	& Rewieing This Mounstrousity Of A Script.
	"""
	global player1_deck, player2_deck, player3_deck, player4_deck, bot_deck
	global start_cart_item, card_to_display_cords, cards_player_hitmox_cords
	global number_cards_list, turns, CHAT_SAVE, CHAT_PROCESS_SAVE, CHAT_REMOVED_SAVE
	global player_amount, y, y3, Game, turn, player, BOT, main_player, special, move
	global blue_in_bot, green_in_bot, yellow_in_bot, red_in_bot, dpal
	global direction_right, actual_player_amount, Main_Loop, double_check_pa
	global player1_card_amount, bot_card_amount, card_direction_player, keys
	global x2, y2, card_selected, selection, new_card, turn_go, pause_bool
	global chosing_color_cooldown, z, b, safe, safe_bot, Victory, Defeat
	global pa, n, v, Reason, p1, p2, p3, p4, Host, Client, played
	global total_data, slot1, slot2, slot3, slot4, one_use_activation
	global REQUIRED_KEYWORD, msg, conn1, conn2, conn3, conn4, pa10
	global client_game, click, q1, one_use_ip_get, client, x_back
	global remove_or_not, color, y_background_main_menu_image
	global message_send1, message_send2, message_send3, message_send4, message_send
	global cards_to_pick_for_next_player, direction_bool, chat_string
	global message_being_made, message_for_chat, message_treshold
	global line1_rect, line2_rect, line3_rect, can_put_text, line_to_write
	global line1_messages, line2_messages, send_message, getting_port
	global turn_already_updated, line1, line2, line3, csy, x_for_reserve
	global deck1, deck2, deck3, deck4, valid, mini, move_past
	global csx, remine, remine1, chat_message_to_send, move2, wait_circle
	global rot_cir_pos, started
	global mazoA, mazoA_backUp, mazoB, mazoB_backUp, turn_go, scroll_y
	global mazoC, mazoD, BOT_checker, forceturn, random_inteval_cards
	global text_box, send_chat, win, conections, uno_played, card_image_resiced_bot

	#PreLoad
	card_image_resiced_bot = pygame.transform.scale(card_image_bot, (50,75))
	
	#Decks
	#112 Cards
	mazoA_backUp = ["0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:', "0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:',"0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:',"0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:',"0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:', "0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:',"0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:',"0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:' , "+2:", "+2:", "+2:", "+2:", "+2:", "+2:", "+2:", "+2:", "F:", "F:", "F:", "F:", "F:", "F:", "F:", "F:", "X:", "X:", "X:", "X:", "X:", "X:", "X:", "X:", "+4:", "+4:", "+4:", "+4:", "W:", "W:", "W:", "W:"]
	mazoA = ["0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:', "0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:',"0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:',"0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:',"0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:', "0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:',"0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:',"0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:', "+2:", "+2:", "+2:", "+2:", "+2:", "+2:", "+2:", "+2:", "F:", "F:", "F:", "F:", "F:", "F:", "F:", "F:", "X:", "X:", "X:", "X:", "X:", "X:", "X:", "X:", "+4:", "+4:", "+4:", "+4:", "W:", "W:", "W:", "W:"]
	mazoB_backUp = ["R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G","R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "R", "R", "B", "B", "Y", "Y", "G", "G", "R", "R", "B", "B", "Y", "Y", "G", "G", "R", "R", "B", "B", "Y", "Y", "G", "G", "W", "W", "W", "W", "W", "W", "W", "W"]
	mazoB = ["R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G","R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "R", "R", "B", "B", "Y", "Y", "G", "G", "R", "R", "B", "B", "Y", "Y", "G", "G", "R", "R", "B", "B", "Y", "Y", "G", "G", "W", "W", "W", "W", "W", "W", "W", "W"]

	#Start Cards
	mazoC = ["0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:', "0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:',"0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:',"0:", "1:", "2:", "3:", '4:', '5:', '6:', '7:', '8:', '9:']
	mazoD = ["R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G"]

 
	#Players Decks
	player1_deck = []
	player2_deck = []
	player3_deck = []
	player4_deck = []
	bot_deck = []
 
	deck1 = []
	deck2 = []
	deck3 = []
	deck4 = []

	#Random Necesairy Lists
	start_cart_item = []

	card_to_display_cords = []

	cards_player_hitmox_cords = []

	number_cards_list = []	

	turns = []	

	CHAT_SAVE = []

	CHAT_PROCESS_SAVE = []

	CHAT_REMOVED_SAVE = []

	random_inteval_cards = []

	dpal = [6,7]

	#Starting Variables
	player_amount = 1
	y = 111 #112 - 1
	y3 = 111
	Game = True
	turn = 1
	player = 1
	BOT = False
	main_player = 1
	special = False
	move = "Duck"
	blue_in_bot, green_in_bot, yellow_in_bot, red_in_bot = 0, 0, 0, 0
	direction_right = True
	actual_player_amount = 2
	Main_Loop = True
	player1_card_amount =  0
	bot_card_amount = 0
	card_direction_player = 1
	keys = pygame.key.get_pressed()
	x2, y2 = None, None
	card_selected = None
	selection = False
	new_card = True
	turn_go = True
	chosing_color_cooldown = False
	z = True
	b = 7
	safe = False
	safe_bot = False
	Victory = False
	Defeat = False
	pa = 2
	opa = pa
	pa10 = pa
	n = False
	v = False
	Reason = " "
	p1 = p2 = p3 = p4 = False
	Host = False
	Client = False
	played = False
	total_data = ""
	slot1, slot2, slot3, slot4 = (0,255,0), (255,0,0), (255,0,0), (255,0,0)
	one_use_activation = True
	REQUIRED_KEYWORD = "UNO"
	msg = "UNO"
	conn1, conn2, conn3, conn4 = None, None, None, None
	client_game = True
	click = True
	click2 = True
	q1 = False
	one_use_ip_get = True
	client = None
	x_back = None
	remove_or_not = True
	color = random.randint(0, len(title_colors) - 1)
	y_background_main_menu_image = random.randrange(0, 1400, 2)
	message_send1 = message_send2 = message_send3 = message_send4 = "Duck"
	message_send = "DUCK"
	cards_to_pick_for_next_player = 0
	direction_bool = "T"
	chat_string = ""
	message_being_made = ""
	message_for_chat = ""
	message_treshold = 15
	line1_rect = pygame.Rect((30,40, 300,25))
	line2_rect = pygame.Rect((30,70, 300,25))
	line3_rect = pygame.Rect((30,100, 300,25))
	can_put_text = True
	line_to_write = True
	line1_messages = ""
	line2_messages = ""
	send_message = False
	getting_port = True
	turn_already_updated = False
	line1 = ""
	line2 = ""
	line3 = ""
	csy = 0
	x_for_reserve = None
	csx = 0
	remine = ""
	remine1 = ""
	text_box = False
	player_assigned = 1
	send_chat = False
	win = False
	conections = False
	uno_played = False
	chat_message_to_send = ""
	valid = True
	forceturn = 0
	mini = False
	turn_go = False
	move_past = "DUCK"
	move2 = "duck"
	rot_cir_pos = 0
	wait_circle = False
	scroll_y = 0
	double_check_pa = False
	card_images["P1IMG"] = pygame.image.load("Images/Player1.png")
	card_images["P2IMG"] = pygame.image.load("Images/Player2.png")
	card_images["P3IMG"] = pygame.image.load("Images/Player3.png")
	card_images["P4IMG"] = pygame.image.load("Images/Player4.png")
	started = False
	pause_bool = False
Start_Variables()

#DEFs
#Get Local Ipv4 & Check Port
def get_local_ipv4():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.error as e:
        return f"Error getting local IP: {e}"
	
def is_port_in_use(host, port, timeout=0.5):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return False   # Port is open (connection succeeded)
    except (ConnectionRefusedError, TimeoutError, OSError):
        return True      # Port is closed, filtered, or unreachable

	
#Client Receive
def receive(q):
	global msg, client, data
	global client_game, Client, Host, HOSTIP, PORTIP
	data = None

	if q == 1:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.connect((HOSTIP, PORTIP))
		client.sendall(msg.encode())
		print("[Client Receive Thread Started]")
		received_data_from_first_msg = client.recv(1024).decode()
		if received_data_from_first_msg == "Nice Try Buddy":
			return False
		elif received_data_from_first_msg == "Server Full":
			return "Server Full"
		elif received_data_from_first_msg == "Game Already Started":
			return "Game Already Started"
		else:
			return True
	if q == 2:
		client.setblocking(False)
		try:
			time.sleep(0.1)
			data = client.recv(1024)
			if data:
				return data.decode()
			if msg:
				client.sendall(msg.encode())
				msg = None
				
		except KeyboardInterrupt:
			client.close()
		except:
			return None
   
def Send(data_to_server):
	global client
	client.sendall(data_to_server.encode())
 
def Send_Message():
    global send_message, message_send, player_assigned
    while True: 
        time.sleep(0.05)
        if send_message == True:
            msg_to_send = message_send
            if not msg_to_send:
                send_message = False
                continue
            Send(f"{player_assigned};{msg_to_send}")
            send_message = False

	
threading.Thread(target=Send_Message, daemon=True).start()

#Server Setup
MAX_CLIENTS = 4
clients = {}  
available_slots = list(range(1, MAX_CLIENTS + 1))  # slots 1 to 4

lock = threading.Lock()  #to avoid race conditions


def handle_client(conn, addr, slot_number):
	global deck1, deck2, deck3, deck4, move_data, cards_data, player_data, total_data,  turn
	global slot1, slot2, slot3, slot4, available_slots, REQUIRED_KEYWORD
	global conn1, conn2, conn3, conn4
	global chat_message, direction_bool, cards_to_pick
	global p1, p2, p3, p4

	try:
		first_msg = conn.recv(1024).decode().strip()
		if first_msg != REQUIRED_KEYWORD and slot_number != 1:
			print(f"[REJECTED] {addr} wrong keyword: {first_msg}")
			conn.sendall(b"Nice Try Buddy")
			conn.close()
			return None	
		else:
			conn.sendall(b"Well Done")
  
		if slot_number == 2:
			conn2 = conn
		elif slot_number == 3:
			conn3 = conn
		elif slot_number == 4:
			conn4 = conn
     
		print(f"[CONNECTED] Player {slot_number}")
		if 1 not in available_slots:
			slot1 = (0,255,0)
		if 2 not in available_slots:
			slot2 = (0,255,0)
			p2 = True
		if 3 not in available_slots:
			slot3 = (0,255,0)
			p3 = True
		if 4 not in available_slots:
			slot4 = (0,255,0)
			p4 = True

		while not stop_all.is_set():
			data = conn.recv(1024)
			if data and ";" not in data.decode().strip(" ") and "&" not in data.decode().strip(" ") and "`" not in data.decode().strip(" "):
				try:
					total_data = data.decode().strip(" ")
					cut2 = total_data.index("/")
					player_data = total_data[:cut2]
					total_data = total_data.replace((player_data + "/"), ' ')
					cut = total_data.index("|") 
					cards_data = total_data[:cut]
					cut3 = total_data.index("*")
					cut4 = total_data.index("]")
					remove_maybe = total_data[cut4:]
					remove_maybe = list(remove_maybe.replace("]", ""))
					remove_maybe = "".join(remove_maybe)

					cut5 = total_data.index("[")
					direction_bool = total_data[cut5:total_data.index(")")]
					direction_bool = list(direction_bool.replace('[', ""))
					direction_bool = "".join(direction_bool)
					
					cut6 = total_data.index(")")
					cards_to_pick = total_data[cut6:total_data.index("(")]
					cards_to_pick = list(cards_to_pick.replace(')', ""))
					cards_to_pick = "".join(cards_to_pick)
					
					cut7 = total_data.index("(")
					chat_message = total_data[cut7:]
					chat_message = list(chat_message.replace("(", ""))
					chat_message = "".join(chat_message)

					try:
						cut8 = total_data.index("<")
						players_cards_amounts = total_data[cut8:]
						total_data = total_data.replace(players_cards_amounts, "")
						deck1_amount = players_cards_amounts.split("<")
						players_cards_amounts = players_cards_amounts.replace("<", "")
						players_cards_amounts_rest = players_cards_amounts.split(">")
						deck2_amount = players_cards_amounts_rest[1]
						deck3_amount = players_cards_amounts_rest[2]
						deck4_amount = players_cards_amounts_rest[3]
					except:
						pass
					
					turn = total_data[cut3:total_data.index("]")]
					turn = turn.replace("*", "")
					turn = int(turn)
					move_data = total_data[cut:total_data.index("*")]
					move_data = move_data.replace("|", "")
					if slot_number == 1:
						deck1 = cards_data.split("'")
						deck1.remove(' ')
					elif slot_number == 2:
						deck2 = cards_data.split("'")
						deck2.remove(' ')
					elif slot_number == 3:
						deck3 = cards_data.split("'")
						deck3.remove(' ')
					elif slot_number == 4:
						deck4 = cards_data.split("'")
						deck4.remove(' ')
				except Exception as e:
					print("Invalid Data Format")
					print(e, total_data)
					total_data = None
					
			else:
				pass
			if ";" in data.decode().strip(" ") or "&" in data.decode().strip(" ") or "`" in data.decode().strip(" "):
				total_data = data.decode().strip(" ")
	except Exception as e:
		print(f"[ERROR] {e}")
	finally:
		with lock:
			print(f"[DISCONNECTED] Player {slot_number}")
			clients.pop(slot_number, None)
			available_slots.append(slot_number)  #free the slot
			available_slots.sort()  #keep them ordered lowest -> highest

			if slot_number == 2:
				slot2 = (255,0,0)
				p2 = False
				conn2 = None
			if slot_number == 3:
				slot3 = (255,0,0)
				p3 = False
				conn3 = None
			if slot_number == 4:
				slot4 = (255,0,0)
				p4 = False
				conn4 = None
		conn.close()


def start_server(port, host="0.0.0.0"):
	global one_use_ip_get, conn1
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((host, port))
	server.listen()
	print(f"Server listening on {host}:{port}")

	while not stop_all.is_set():
		conn, addr = server.accept()
		if one_use_ip_get == True:
			conn1 = conn
			one_use_ip_get = False
		with lock:
			if len(clients) >= MAX_CLIENTS or not available_slots:
				conn.sendall(b"Server Full")
				print(f"[REJECTED] Connection from {addr} (Server full)")
				conn.close()
				continue

			elif started == True:
				conn.sendall(b"Game Already Started")
				print(f"[REJECTED] Connection from {addr} (Game Already Started)")
				conn.close()
				continue

            #assign the lowest available slot
			slot_number = available_slots.pop(0)

        #Start thread for new client
		threading.Thread(
            target=handle_client,
            args=(conn, addr, slot_number),
            daemon=True
		).start()

def start_server_thread():
    server_thread = threading.Thread(
        target=start_server,
        args=(PORTIP, "0.0.0.0"),
        daemon=True
    )
    server_thread.start()
    

#Menus
	#Pause Host
def Pause_Host():
	while True:
		time.sleep(0.05)
		screen.blit(font_button.render("Are You Sure You", True, (0,0,0)), (width/2 - font_button.render("Are You Sure You", True, (255,255,255)).get_width()/2 + 3 + 10, 102))
		screen.blit(font_button.render("Are You Sure You", True, (255,255,255)), (width/2 - font_button.render("Are You Sure You", True, (255,255,255)).get_width()/2 + 10, 100))
		screen.blit(font_button.render("Want Stop Hosting?", True, (0,0,0)), (width/2 - font_button.render("Want Stop Hosting?", True, (255,255,255)).get_width()/2 + 3 + 10, 182))
		screen.blit(font_button.render("Want Stop Hosting?", True, (255,255,255)), (width/2 - font_button.render("Want Stop Hosting?", True, (255,255,255)).get_width()/2 + 10, 180))
  
		main_menu_button = pygame.draw.rect(screen, (255,255,255), (375,270,250,100), 10, 16)
		screen.blit(font_button2.render("Yes", True, (0,0,0)), (width/2 - font_button2.render("Yes", True, (255,255,255)).get_width()/2 + 3, 277))
		screen.blit(font_button2.render("Yes", True, (255,255,255)), (width/2 - font_button2.render("Yes", True, (255,255,255)).get_width()/2, 274))

		resume_button = pygame.draw.rect(screen, (255,255,255), (375,390,250,100), 10, 16)
		screen.blit(font_button2.render("No", True, (0,0,0)), (width/2 - font_button2.render("No", True, (255,255,255)).get_width()/2 + 3, 403))
		screen.blit(font_button2.render("No", True, (255,255,255)), (width/2 - font_button2.render("No", True, (255,255,255)).get_width()/2, 400))
  
		pos_mouse = pygame.mouse.get_pos()
		mouse_cursor = pygame.draw.rect(alpha_surface, (0,0,0,0), (pos_mouse[0],pos_mouse[1], 10,10))
  
		pygame.display.flip()
  
		if mouse_cursor.colliderect(resume_button) and pygame.mouse.get_pressed()[0]:
			return

		if mouse_cursor.colliderect(main_menu_button) and pygame.mouse.get_pressed()[0]:
			return False
     
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					return
			if event.type == pygame.QUIT:
				return "exit"
	#Pause
def Pause_Menu():
	global color, pause_bool
	pause_bool = True
	while True:
		time.sleep(0.07)
  
		color += 1
		if color >= len(title_colors) - 1:
			color = 0
   
		screen.blit(font_button.render("Pause Menu", True, (title_colors[color])), (width/2 - font_button.render("Pause Menu", True, (255,255,255)).get_size()[0]/2, 100))
  
		resume_button = pygame.draw.rect(screen, (title_colors[color]), (375,250, 250,100), 10, 16)
		screen.blit(font_button2.render("Resume", True, (title_colors[color])), (width/2 - font_button2.render("Resume", True, (255,255,255)).get_size()[0]/2,254))
		main_menu_button = pygame.draw.rect(screen, (title_colors[color]), (375,370, 250,100), 10, 16)
		screen.blit(font_button9.render("Quit Game", True, (title_colors[color])), (width/2 - font_button9.render("Quit Game", True, (255,255,255)).get_size()[0]/2,380))
		quit_button = pygame.draw.rect(screen, (title_colors[color]), (375,490, 250,100), 10, 16)
		screen.blit(font_button2.render("QUIT", True, (title_colors[color])), (width/2 - font_button2.render("QUIT", True, (255,255,255)).get_size()[0]/2,496))
  
		pos_mouse = pygame.mouse.get_pos()
		mouse_cursor = pygame.draw.rect(alpha_surface, (0,0,0,0), (pos_mouse[0],pos_mouse[1], 10,10))
  
		pygame.display.flip()
  
		if mouse_cursor.colliderect(resume_button) and pygame.mouse.get_pressed()[0]:
			pause_bool = False
			return

		if mouse_cursor.colliderect(main_menu_button) and pygame.mouse.get_pressed()[0]:
			pause_bool = False
			return False

		if mouse_cursor.colliderect(quit_button) and pygame.mouse.get_pressed()[0]:
			pause_bool = False
			return "exit"
     
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					return
			if event.type == pygame.QUIT:
				pause_bool = False
				return "exit"
	#Rules
def draw_text(scroll_offset, color):
	global scroll_y
	line_height = 45
	title_surface = font_title.render("How to Play", True, (title_colors[color]))
	screen.blit(title_surface, (width//2 - title_surface.get_width()//2, 10 + scroll_offset))

    # Dibujar texto desplazable
	y = 180 + scroll_offset
	for line in rules_text:
		shadow = font_button7.render(line, True, (0,0,0))
		text_surface = font_button7.render(line, True, (255,255,255))

		screen.blit(shadow, (62, y + 2))
		screen.blit(text_surface, (60, y))
		y += line_height
        
	#Main Menu
def Main_Menu():
	global Main_Loop, Game, player_amount, mazoA, mazoA3, mazoA_backUp, mazoB, mazoB3, mazoB_backUp
	global title_size, color, y_background_main_menu_image, scroll_y, started
	global pa, BOT, Who_Playing, n, y, y3, v, slot1, slot2, slot3, slot4
	global Host, Client, one_use_activation, player_amount_checker, y_checker
	global click, q1, receiver_client, HOSTIP, PORTIP, msg, REQUIRED_KEYWORD
	global BOT_checker, conections, rot_cir_pos, one_use_ip_get

	title_size_increase = True
	MM = True
	click = True  
	color_slowness = 0
	conections = True
	rt = False
	line_height = 45
	max_scroll = -(len(rules_text) * line_height - 450)

	while MM:
		time.sleep(0.02)
		pos_mouse = pygame.mouse.get_pos()
		mouse_cursor = pygame.draw.rect(alpha_surface, (0,0,0,0), (pos_mouse[0], pos_mouse[1], 10, 10))

		#Draw Main Menu
		#Background
		screen.blit(background__main_menu_image, (0, y_background_main_menu_image))
		screen.blit(background__main_menu_image, (0, y_background_main_menu_image - background__main_menu_image.get_height()))
		y_background_main_menu_image += 5
		if y_background_main_menu_image >= background__main_menu_image.get_height():
			y_background_main_menu_image = 0
			
		font_title = pygame.font.SysFont('Arial', title_size)

		#Buttons With Text
		play_button_text = font_button.render("START", True, (title_colors[color]))
		quit_button_text = font_button.render("QUIT", True, (title_colors[color]))
		title_text = font_title.render("UNO", True, (title_colors[color]))
		
		play_button = pygame.draw.rect(screen, (title_colors[color]), (375,350, 250,100),10, 10)
		screen.blit(play_button_text, (392, 350))
		quit_button = pygame.draw.rect(screen, (title_colors[color]), (375,465, 250,100),10, 10)
		screen.blit(quit_button_text, (420, 470))
		screen.blit(title_text, (width/2 - title_text.get_size()[0]/2, 100))
		
		if title_size < 120:
			title_size_increase = True
		if title_size > 160:
			title_size_increase = False
		if title_size_increase == True:
			title_size += 2
		if title_size_increase == False:
			title_size -= 2
			
		if color_slowness == 1:
			color += color_slowness
		else:
			color_slowness += 0.2
			
		color = int(color)
		if color >= len(title_colors):
			color = 0
   
		#Github
		github_button = rules_button = pygame.draw.rect(alpha_surface, (0,0,0), (20,625, 50,50))
		screen.blit(card_images["GitBut"], (20,625))
		if mouse_cursor.colliderect(github_button) and pygame.mouse.get_pressed()[0] and click == True:
			click = False
			webbrowser.open("https://github.com/Winsulf")
		#Rules
		rules_button = pygame.draw.rect(alpha_surface, (0,0,0), (20,565, 50,50))
		screen.blit(card_images["RulBut"], (20,565))
		if mouse_cursor.colliderect(rules_button) and pygame.mouse.get_pressed()[0]:
			rt = True
		while rt == True:
			time.sleep(0.02)
			screen.blit(background__main_menu_image, (0, y_background_main_menu_image))
			screen.blit(background__main_menu_image, (0, y_background_main_menu_image - background__main_menu_image.get_height()))
			y_background_main_menu_image += 5
			if y_background_main_menu_image >= background__main_menu_image.get_height():
				y_background_main_menu_image = 0
    
			if color_slowness == 1:
				color += color_slowness
			else:
				color_slowness += 0.2
			
			color = int(color)
			if color >= len(title_colors):
				color = 0
    
			draw_text(scroll_y, color)
			pygame.display.flip()
   
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						rt = False
				if event.type == pygame.MOUSEWHEEL:
					scroll_y += event.y * 20
				elif event.type == pygame.QUIT:
					Main_Loop = False
					Game = False
					MM = False
					return False
			scroll_y = max(max_scroll, min(scroll_y, 0))
		
		pygame.display.flip()

	   
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONUP:
				click = True
			elif event.type == pygame.QUIT:
				Main_Loop = False
				Game = False
				MM = False
				return False
  
		#Botones principales
		if mouse_cursor.colliderect(play_button):
			if pygame.mouse.get_pressed()[0] and click:
				click = False
				m = True

				while m:
					time.sleep(0.02)
					#Background
					screen.blit(background__main_menu_image, (0, y_background_main_menu_image))
					screen.blit(background__main_menu_image, (0, y_background_main_menu_image - background__main_menu_image.get_height()))
					y_background_main_menu_image += 5
					if y_background_main_menu_image >= background__main_menu_image.get_height():
						y_background_main_menu_image = 0
						
					#Changing Color
					if color_slowness == 1:
						color += color_slowness
					else:
						color_slowness += 0.2
					
					color = int(color)
					if color >= len(title_colors):
						color = 0
					
					pos_mouse = pygame.mouse.get_pos()
					mouse_cursor = pygame.draw.rect(alpha_surface, (0,0,0,0), (pos_mouse[0], pos_mouse[1], 10, 10))

					single_player = pygame.draw.rect(screen, (title_colors[color]), (100,100, 350,200), 15, 15)
					single_player_text2 = font_button2.render("Player", True, (title_colors[color]))
					single_player_text1 = font_button.render("Single", True, (title_colors[color]))
					screen.blit(single_player_text1, (100 + 350 / 4,115))
					screen.blit(single_player_text2, (100 + 10 + 350 / 4,180))
					
					local_multiplayer = pygame.draw.rect(screen, (title_colors[color - 20]), (550,100, 350,200), 15, 15)
					local_multiplayer_text2 = font_button2.render("MultiPlayer", True, (title_colors[color - 20]))
					local_multiplayer_text1 = font_button.render("Local", True, (title_colors[color - 20]))
					screen.blit(local_multiplayer_text1, (550 + 350 / 4,115))
					screen.blit(local_multiplayer_text2, (550 + 350 / 10,180))
					
					multiplayer = pygame.draw.rect(screen, (title_colors[color - 40]), (325,330, 350,200), 15, 15)
					multiplayer_text2 = font_button2.render("Multiplayer", True, (title_colors[color - 40]))
					multiplayer_text1 = font_button.render("Online", True, (title_colors[color - 40]))
					screen.blit(multiplayer_text1, (width/2 - multiplayer_text1.get_size()[0]/2,345))
					screen.blit(multiplayer_text2, (325 + 350 / 10,410))
					
					pygame.display.flip()

				   
					for event in pygame.event.get():
						if event.type == pygame.MOUSEBUTTONUP:
							click = True
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_ESCAPE:
								m = False
						elif event.type == pygame.QUIT:
							Main_Loop = False
							Game = False
							MM = False
							m = False
							n = False
							v = False
							return False

					#Single Player
					if mouse_cursor.colliderect(single_player):
						if pygame.mouse.get_pressed()[0] and click:
							click = False
							MM = False
							BOT = True
							player_amount = 1
							m = False
							pa = 2

					#Local Multiplayer
					if mouse_cursor.colliderect(local_multiplayer):
						if pygame.mouse.get_pressed()[0] and click:
							click = False
							n = True
							m = False  
						   
							while n:
								time.sleep(0.02)
								#Background
								screen.blit(background__main_menu_image, (0, y_background_main_menu_image))
								screen.blit(background__main_menu_image, (0, y_background_main_menu_image - background__main_menu_image.get_height()))
								y_background_main_menu_image += 5
								if y_background_main_menu_image >= background__main_menu_image.get_height():
									y_background_main_menu_image = 0
									
								#Changing Color
								if color_slowness == 1:
									color += color_slowness
								else:
									color_slowness += 0.2
									
								color = int(color)
								if color >= len(title_colors):
									color = 0
								
								pos_mouse = pygame.mouse.get_pos()
								mouse_cursor = pygame.draw.rect(alpha_surface, (255,0,0,0), (pos_mouse[0], pos_mouse[1], 10, 10))

								v2 = pygame.draw.rect(screen, (title_colors[color - 60]), (325,200, 350,100), 15, 15)
								v2_text = font_button.render("2 Players", True, (title_colors[color - 60]))
								screen.blit(v2_text, (325 + 350 / 9, 200))
								v3 = pygame.draw.rect(screen, (title_colors[color - 80]), (325,310, 350,100), 15, 15)
								v3_text = font_button.render("3 Players", True, (title_colors[color - 80]))
								screen.blit(v3_text, (325 + 350 / 9, 310))
								v4 = pygame.draw.rect(screen, (title_colors[color - 100]), (325,420, 350,100), 15, 15)
								v4_text = font_button.render("4 Players", True, (title_colors[color - 100]))
								screen.blit(v4_text, (325 + 350 / 9, 420))
								pygame.display.flip()

								for event in pygame.event.get():
									if event.type == pygame.MOUSEBUTTONUP:
										click = True
									if event.type == pygame.KEYDOWN:
										if event.key == pygame.K_ESCAPE:
											m = True	
											n = False
									elif event.type == pygame.QUIT:
										Main_Loop = False
										Game = False
										MM = False
										n = False
										return False

								if mouse_cursor.colliderect(v2):
									if pygame.mouse.get_pressed()[0] and click:
										y_checker = 111
										player_amount_checker = 2
										click = False
										BOT = False
										player_amount = 2
										MM = False
										pa = 2
										n = False
										Game = True
										Main_Loop = True

								if mouse_cursor.colliderect(v3):
									if pygame.mouse.get_pressed()[0] and click:
										y_checker = 111
										player_amount_checker = 3
										click = False
										BOT = False
										player_amount = 3
										y = 111
										y3 = 111
										MM = False
										pa = 3
										n = False
										Game = True
										Main_Loop = True

								if mouse_cursor.colliderect(v4):
									if pygame.mouse.get_pressed()[0] and click:
										y_checker = 111
										player_amount_checker = 4
										click = False
										BOT = False
										player_amount = 4
										y = 111
										y3 = 111
										MM = False
										pa = 4
										n = False
										Game = True
										Main_Loop = True

					#Multiplayer
					if mouse_cursor.colliderect(multiplayer):
						if pygame.mouse.get_pressed()[0] and click:
							click = False
							v = True
							m = False
							safe_lock = True

						while v:
							time.sleep(0.02)
							#Background
							screen.blit(background__main_menu_image, (0, y_background_main_menu_image))
							screen.blit(background__main_menu_image, (0, y_background_main_menu_image - background__main_menu_image.get_height()))
							y_background_main_menu_image += 5
							if y_background_main_menu_image >= background__main_menu_image.get_height():
								y_background_main_menu_image = 0
								
							#Changing Color
							if color_slowness == 1:
								color += color_slowness
							else:
								color_slowness += 0.2
         
							color = int(color)
							if color >= len(title_colors):
								color = 0
									
							pos_mouse = pygame.mouse.get_pos()
							mouse_cursor = pygame.draw.rect(alpha_surface, (255,0,0,0), (pos_mouse[0], pos_mouse[1], 10,10))

							host_rec = pygame.draw.rect(screen, (title_colors[color]), (75,200, 350,200), 20, 15)
							host_text = font_button3.render("HOST", True, (title_colors[color]))
							screen.blit(host_text, (115, 225))
							join_rec = pygame.draw.rect(screen, (title_colors[color]), (575,200, 350,200), 20, 15)
							join_text = font_button3.render("JOIN", True, (title_colors[color]))
							screen.blit(join_text, (635,225))
							pygame.display.flip()

							for event in pygame.event.get():
								if event.type == pygame.MOUSEBUTTONUP:
									click = True
								if event.type == pygame.KEYDOWN:
									if event.key == pygame.K_ESCAPE and safe_lock == True:
										m = True	
										v = False
								if event.type == pygame.KEYUP:
									if event.key == pygame.K_ESCAPE:
										safe_lock = True
								elif event.type == pygame.QUIT:
									Main_Loop = False
									Game = False
									MM = False
									v = False
									n = False
									Host = False
									Client = False
									return False 

							if mouse_cursor.colliderect(host_rec):
								if pygame.mouse.get_pressed()[0] and click:
									click = False
									#Get IPv4 & Port
									HOSTIP = get_local_ipv4()
									port_being_made = ""
									check_port = False
									getting_port = True
									checker = "Duck"
									get_password = False
									password_being_made = ""
									q1c = True
									while getting_port == True:
										time.sleep(0.02)
										pygame.display.flip()
										screen.blit(background__main_menu_image, (0, y_background_main_menu_image))
										screen.blit(background__main_menu_image, (0, y_background_main_menu_image - background__main_menu_image.get_height()))
										y_background_main_menu_image += 5
										if y_background_main_menu_image >= background__main_menu_image.get_height():
											y_background_main_menu_image = 0
										if color_slowness == 1:
											color += color_slowness
										else:
											color_slowness += 0.2
										color = int(color)
										if color >= len(title_colors):
											color = 0

										if port_being_made and int(port_being_made) > 65535:
											port_being_made = 65535
										if get_password == False:
											port_get_text = font_button3.render("Select A Port To Host", True, title_colors[color])
											screen.blit(port_get_text, (width/2 - port_get_text.get_size()[0]/2, 100))
											screen.blit(font_button4.render("1-65535", True, (title_colors[color])), (width/2 - font_button4.render("1-65535", True, (title_colors[color])).get_size()[0]/2, 210))
											screen.blit((font_button.render(f"{port_being_made}", True, (255,255,255))), (width/2 - font_button.render(f"{port_being_made}", True, (255,255,255)).get_size()[0]/2, 275))

										if check_port == True:
											if is_port_in_use(HOSTIP, int(port_being_made)) == True:
												PORTIP = int(port_being_made)
												get_password = True
												check_port = False
											else:
												check_port = False
												checker = port_being_made
										
										if checker == port_being_made:
											screen.blit(font_button2.render("That Port Is Already In Use", True, (title_colors[color])), (width/2 - font_button2.render("That Port Is Already In Use", True, (title_colors[color])).get_size()[0]/2, 400))
											pygame.display.flip()

										if get_password == True:
											port_get_text = font_button5.render("Put A Password To The Server", True, title_colors[color])
											screen.blit(port_get_text, (width/2 - port_get_text.get_size()[0]/2, 100))
											screen.blit(font_button4.render("Or Press Enter To Make It Public", True, (title_colors[color])), (width/2 - font_button4.render("Or Press Enter To Make It Public", True, (title_colors[color])).get_size()[0]/2, 200))
											screen.blit((font_button.render(f"{password_being_made}", True, (255,255,255))), (width/2 - font_button.render(f"{password_being_made}", True, (255,255,255)).get_size()[0]/2, 265))
											pygame.display.flip()

											
										for event in pygame.event.get():
											if event.type == pygame.KEYDOWN:
												if event.key == pygame.K_ESCAPE and q1 == False:
													q1c = False
													v = True
													getting_port = False	
													q1 = False
													safe_lock = False
											if event.type == pygame.KEYDOWN and get_password == False:
												if event.unicode.isdigit() and len(str(port_being_made)) < 5:
													port_being_made += event.unicode
												if event.key == pygame.K_BACKSPACE:
													port_being_made = str(port_being_made)[:-1]
												if event.key == pygame.K_RETURN and len(port_being_made):
													if int(port_being_made) >= 0 and int(port_being_made) < 65535:
														check_port = True

											if event.type == pygame.KEYDOWN and get_password == True:
												if event.key == pygame.K_BACKSPACE:
													password_being_made = str(password_being_made)[:-1]
												if event.unicode.isalnum() and len(str(password_being_made)) < 10:
													password_being_made += event.unicode
												if event.key == pygame.K_RETURN and len(password_being_made) > 0:
													REQUIRED_KEYWORD = password_being_made
													getting_port = False
												if event.key == pygame.K_RETURN:
													getting_port = False
														
											if event.type == pygame.QUIT:
												getting_port = False
												Main_Loop = False
												Game = False
												MM = False
												v = False
												n = False
												q1 = False
												Host = False
												Client = False
												return False

									try:
										if HOSTIP and PORTIP:
											if q1c == True:
												q1 = True
											else:
												q1 = False
									except:
										q1 = False
          
									while q1:
										time.sleep(0.02)
										pos_mouse = pygame.mouse.get_pos()
										mouse_cursor = pygame.draw.rect(alpha_surface, (255,0,0,0), (pos_mouse[0], pos_mouse[1], 10,10))
										screen.blit(background__main_menu_image, (0, y_background_main_menu_image))
										screen.blit(background__main_menu_image, (0, y_background_main_menu_image - background__main_menu_image.get_height()))
										y_background_main_menu_image += 5
										if y_background_main_menu_image >= background__main_menu_image.get_height():
											y_background_main_menu_image = 0
										if color_slowness == 1:
											color += color_slowness
										else:
											color_slowness += 0.2
										color = int(color)
										if color >= len(title_colors):
											color = 0

										pygame.draw.rect(screen, (slot1), (350,20, 300,100), 12, 16)  
										screen.blit(font_button2.render("Player 1", True, (slot1)), (width/2 - font_button2.render("Player 1", True, (slot1)).get_size()[0]/2, 25))
										pygame.draw.rect(screen, (slot2), (350,140, 300,100), 12, 16)
										screen.blit(font_button2.render("Player 2", True, (slot2)), (width/2 - font_button2.render("Player 2", True, (slot2)).get_size()[0]/2, 145))
										pygame.draw.rect(screen, (slot3), (350,260, 300,100), 12, 16)  
										screen.blit(font_button2.render("Player 3", True, (slot3)), (width/2 - font_button2.render("Player 3", True, (slot3)).get_size()[0]/2, 265))
										pygame.draw.rect(screen, (slot4), (350,380, 300,100), 12, 16) 
										screen.blit(font_button2.render("Player 4", True, (slot4)), (width/2 - font_button2.render("Player 4", True, (slot4)).get_size()[0]/2, 385))

										screen.blit(font_button6.render("Hosting Ip", True, (title_colors[color])), (font_button6.render("Hosting Port", True, (title_colors[color])).get_size()[0]/2 + 50 - font_button6.render("Hosting Ip", True, (title_colors[color])).get_size()[0]/2,50)) 
										screen.blit(font_button7.render(f"{HOSTIP}", True, (255,255,255)), (font_button6.render("Hosting Ip", True, (title_colors[color])).get_size()[0]/2 + font_button6.render("Hosting Port", True, (title_colors[color])).get_size()[0]/2 + 50 - font_button6.render("Hosting Ip", True, (title_colors[color])).get_size()[0]/2 - font_button7.render(f"{HOSTIP}", True, (255,255,255)).get_size()[0]/2, 100))

										screen.blit(font_button6.render("Hosting Port", True, (title_colors[color])), (50,200)) 
										screen.blit(font_button7.render(f"{PORTIP}", True, (255,255,255)), (font_button6.render("Hosting Port", True, (title_colors[color])).get_size()[0]/2 + 50 - font_button7.render(f"{PORTIP}", True, (255,255,255)).get_size()[0]/2, 250))

										screen.blit(font_button6.render("Password", True, (title_colors[color])), ((font_button6.render("Hosting Port", True, (title_colors[color])).get_size()[0]/2 + 50 - font_button6.render("Password", True, (title_colors[color])).get_size()[0]/2 ,350)))
										screen.blit(font_button7.render(f"{REQUIRED_KEYWORD}", True, (255,255,255)), (font_button6.render("Password", True, (title_colors[color])).get_size()[0]/2 + font_button6.render("Hosting Port", True, (title_colors[color])).get_size()[0]/2 + 50 - font_button6.render("Password", True, (title_colors[color])).get_size()[0]/2 - font_button7.render(f"{REQUIRED_KEYWORD}", True, (255,255,255)).get_size()[0]/2, 400))
										

										if one_use_activation:
											#Client Start Receive Thread
											one_use_ip_get = True
											stop_all.clear() 
											receiver_client = threading.Thread(target=receive, args=(1,), daemon=True)
											receiver_client.start()
											start_server_thread()
											Host = True
											Client = True
											one_use_activation = False

										if len(available_slots) < 3:
											start_button = pygame.draw.rect(screen, (240,240,0), (350,520, 300,100),15,16)
											screen.blit(font_button2.render("Start", True, (240,240,0)), (width/2 - font_button2.render("Start", True, (240,240,0)).get_size()[0]/2, 525))
											if mouse_cursor.colliderect(start_button):
												if pygame.mouse.get_pressed()[0]:
													started = True
													q1 = False
													MM = False
													v = False
													n = False
													BOT = False
													y = 111
													y3 = 111
													Game = False
													Main_Loop = False

										pygame.display.flip()

										for event in pygame.event.get():
											if event.type == pygame.MOUSEBUTTONUP:
												click = True
											if event.type == pygame.KEYDOWN:
												if event.key == pygame.K_ESCAPE:
													pause_check = Pause_Host()
													if pause_check == False:
														quit_all()
														return
													if pause_check == "exit":
														quit_all()
														return False
											elif event.type == pygame.QUIT:
												Main_Loop = False
												Game = False
												MM = False
												v = False
												n = False
												q1 = False
												Host = False
												Client = False
												return False

							if mouse_cursor.colliderect(join_rec):
								if pygame.mouse.get_pressed()[0] and click:
									getting_ip_and_port = True
									next = False
									get_port_for_join = False
									check_port_to_join = False
									port_being_made = ""
									checker_failed_for_port_joining = "DUCK"
									password_check = False
									password_being_made = ""
									checking_password_check = False
									check_check_port_to_join = False
									password_checked = "DUCK"
									next2 = False
									ip_being_made = ""
									ip_ready = False
									GG = True
									while getting_ip_and_port == True:
										time.sleep(0.02)
										pygame.display.flip()
										pos_mouse = pygame.mouse.get_pos()
										mouse_cursor = pygame.draw.rect(alpha_surface, (255,0,0,0), (pos_mouse[0], pos_mouse[1], 10,10))
										screen.blit(background__main_menu_image, (0, y_background_main_menu_image))
										screen.blit(background__main_menu_image, (0, y_background_main_menu_image - background__main_menu_image.get_height()))
										y_background_main_menu_image += 5
										if y_background_main_menu_image >= background__main_menu_image.get_height():
											y_background_main_menu_image = 0
										if color_slowness == 1:
											color += color_slowness
										else:
											color_slowness += 0.2
										color = int(color)
										if color >= len(title_colors):
											color = 0

										if port_being_made and int(port_being_made) > 65535:
											port_being_made = 65535
										if next != True and next2 != True and GG == True:
											auto_ip = pygame.draw.rect(screen, (title_colors[color]), (400,250, 200,100), 15,16)
											screen.blit(font_button.render("LAN", True, (title_colors[color])), (width/2 - font_button.render("LAN", True, (title_colors[color])).get_size()[0]/2, 255))
											set_ip = pygame.draw.rect(screen, (title_colors[color]), (400,400, 200,100), 15, 16)
											screen.blit(font_button.render("WAN", True, (title_colors[color])), (width/2 - font_button.render("WAN", True, (title_colors[color])).get_size()[0]/2, 405))
											if click == True and pygame.mouse.get_pressed()[0] and mouse_cursor.colliderect(auto_ip):
												next = True
											if click == True and pygame.mouse.get_pressed()[0] and mouse_cursor.colliderect(set_ip):
												next2 = True
            
										if next2 == True:
											screen.blit(font_button3.render("Put Server IP", True, (title_colors[color])), (width/2 - font_button3.render("Put Servers IP", True, (title_colors[color])).get_size()[0]/2, 100))
											screen.blit(font_button5.render(f"{ip_being_made}", True, (255,255,255)), (width/2 - font_button5.render(f"{ip_being_made}", True, (255,255,255)).get_size()[0]/2, 275))

										if next == True:
											HOSTIP = get_local_ipv4()
											get_port_for_join = True
           
										if check_port_to_join == True:
											if is_port_in_use(HOSTIP, int(port_being_made)) == False:
												password_check = True
												check_port_to_join = False
												check_check_port_to_join = True
											else:
												checker_failed_for_port_joining = port_being_made
												check_check_port_to_join = False
												check_port_to_join = False
									
										if get_port_for_join == True and check_check_port_to_join == False:
											screen.blit(font_button3.render("Enter A Port To Join", True, title_colors[color]), (width/2 - font_button3.render("Enter A Port To Join", True, title_colors[color]).get_size()[0]/2, 100))
											screen.blit(font_button4.render("1-65535", True, title_colors[color]), (width/2 - font_button4.render("1-65536", True, title_colors[color]).get_size()[0]/2, 210))
											screen.blit((font_button.render(f"{port_being_made}", True, (255,255,255))), (width/2 - font_button.render(f"{port_being_made}", True, (255,255,255)).get_size()[0]/2, 275))
           
										if str(checker_failed_for_port_joining) == str(port_being_made):
											screen.blit(font_button2.render("Theres Nobody Hosting In That Port", True, (title_colors[color])), (width/2 - font_button2.render("Theres Nobody Hosting In That Port", True, (title_colors[color])).get_size()[0]/2, 400))
											pygame.display.flip()
           
										if password_check == True:
											screen.blit(font_button3.render("Enter The Password", True, (title_colors[color])), (width/2 - font_button3.render("Enter The Password", True, (title_colors[color])).get_size()[0]/2, 100))
											screen.blit(font_button4.render('If There Is Non Just Put "UNO"', True, (title_colors[color])), (width/2 - font_button4.render("If There Is Non Just Press Enter", True, (title_colors[color])).get_size()[0]/2, 210))
											screen.blit(font_button.render(f"{password_being_made}", True, (255,255,255)), (width/2 - font_button.render(f"{password_being_made}", True, (255,255,255)).get_size()[0]/2, 275))
           
										if checking_password_check == True:
											msg = password_being_made
											PORTIP = int(port_being_made)
											msg_received_from_first_msg = receive(1)
											if msg_received_from_first_msg == True:
												getting_ip_and_port = False
												checking_password_check = False
											elif msg_received_from_first_msg == "Server Full":
												password_checked = "Server Full"
												checking_password_check = False
											elif msg_received_from_first_msg == "Game Already Started":
												password_checked = "Game Already Started"
												checking_password_check = False
											else:
												checking_password_check = False
												password_checked = password_being_made
            
										if password_checked == password_being_made:
											screen.blit(font_button2.render("Wrong Password", True, (title_colors[color])),(width/2 - font_button2.render("Wrong Password", True, (title_colors[color])).get_size()[0]/2, 500))
											pygame.display.flip()
										elif password_checked == "Server Full":
											screen.blit(font_button2.render("Server Is Full", True, (title_colors[color])),(width/2 - font_button2.render("Server Is Full", True, (title_colors[color])).get_size()[0]/2, 500))
											pygame.display.flip()
										elif password_checked == "Game Already Started":
											screen.blit(font_button2.render("Game Already Started", True, (title_colors[color])),(width/2 - font_button2.render("Game Already Started", True, (title_colors[color])).get_size()[0]/2, 500))
											pygame.display.flip()
           
										for event in pygame.event.get():
											if event.type == pygame.KEYDOWN:
												if event.key == pygame.K_ESCAPE:
													v = True
													getting_ip_and_port = False
													one_use_activation = False
												else:
													one_use_activation = True
											if event.type == pygame.KEYDOWN and password_check == False and next2 == False:
												if event.unicode.isdigit() and len(str(port_being_made)) < 5:
													port_being_made += event.unicode
												if event.key == pygame.K_BACKSPACE:
													port_being_made = str(port_being_made)[:-1]
												if event.key == pygame.K_RETURN and len(port_being_made):
													if int(port_being_made) < 65535 and int(port_being_made) > 0 and len(port_being_made) > 0:
														check_port_to_join = True

											if event.type == pygame.KEYDOWN and password_check == True and next2 == False:
												if event.key == pygame.K_BACKSPACE:
													password_being_made = str(password_being_made)[:-1]
												if event.unicode.isalnum() and len(str(password_being_made)) < 10:
													password_being_made += event.unicode
												if event.key == pygame.K_RETURN and len(password_being_made) > 0:
													checking_password_check = True

											if event.type == pygame.KEYDOWN and next2 == True:
												if event.key == pygame.K_BACKSPACE:
													ip_being_made = str(ip_being_made)[:-1]
												if (event.unicode.isdigit() or event.unicode == ".") and len(str(ip_being_made)) < 15:
													ip_being_made += event.unicode
												if event.key == pygame.K_RETURN and len(str(ip_being_made)) > 6:
													HOSTIP = ip_being_made
													get_port_for_join = True
													next2 = False
													GG = False
													
														
											if event.type == pygame.QUIT:
												getting_ip_and_port = False
												one_use_activation = False
												return False
									
									if one_use_activation == True:
										Host = False
										Client = True
										one_use_activation = False
										click = False
										Main_Loop = False
										Game = False
										MM = False
										v = False
										n = False
										q1 = False
										BOT = False
	

		# Quit Button
		if mouse_cursor.colliderect(quit_button):
			if pygame.mouse.get_pressed()[0] and click:
				click = False
				MM = False
				Game = False
				Main_Loop = False
				return False
    
	if Client == True or Host == True:
		return "OG"
	else:
		BOT_checker = BOT
		return "LG"
    
#Circle
def Circle(r):
	global x_circle, y_circle
	if r == 20:
		cx = 400
		cy = 300
		theta = [i / 100 * 2 * math.pi for i in range(101)]  # Generate angles from 0 to 2*pi
		x_circle = [r * math.cos(t) + cx for t in theta]
		y_circle = [r * math.sin(t) + cy for t in theta]
	else:
		cx2 = 500
		cy2 = 350
		theta2 = [i / 100 * 2 * math.pi for i in range(101)]  
		x_circle2 = [r * math.cos(t) + cx2 for t in theta2]
		y_circle2 = [r * math.sin(t) + cy2 for t in theta2]
		return x_circle2, y_circle2
Circle(20)
xc, yc = Circle(120)
#Start Cards
def Start_Cards():
	global BOT, card_down, y, player_amount, start_cart, deck1, deck_bot, deck2, view_deck_bot, deck3, deck4, pa
	global mazoA, mazoB, mazoC, mazoD
	start_cart5 = random.randint(0,39)
	cart_start_moveA = mazoC.pop(start_cart5)
	cart_start_moveB = mazoD.pop(start_cart5)
	y -= 1
	start_cart_item.append(cart_start_moveA)
	start_cart_item.append(cart_start_moveB)
	start_cart_deck1 = " ".join(start_cart_item)
	start_cart = start_cart_deck1.replace(": ", "")
	card_down = start_cart

	if player_amount >= 1:
		for i in range(b):
			cart_to_move = random.randint(1,y) - 1
			cart_being_movedA = mazoA.pop(cart_to_move)
			cart_being_movedB = mazoB.pop(cart_to_move)
			y -= 1
			player1_deck.append(cart_being_movedA)
			player1_deck.append(cart_being_movedB)
		
		view_deck1_1 = " ".join(player1_deck)
		view_deck1 = view_deck1_1.replace(": ", "")
		deck1 = view_deck1.split(" ")
		if BOT == False:
			if player_amount >= 2:
				for i in range(b):
					cart_to_move = random.randint(1,y) - 1
					cart_being_movedA = mazoA.pop(cart_to_move)
					cart_being_movedB = mazoB.pop(cart_to_move)
					y -= 1
					player2_deck.append(cart_being_movedA)
					player2_deck.append(cart_being_movedB)
		
				view_deck1_2 = " ".join(player2_deck)
				view_deck2 = view_deck1_2.replace(": ", "")
				deck2 = view_deck2.split(" ")
			else:
				deck2 = []
			if player_amount >= 3:
				for i in range(b):
					cart_to_move = random.randint(1,y) - 1
					cart_being_movedA = mazoA.pop(cart_to_move)
					cart_being_movedB = mazoB.pop(cart_to_move)
					y -= 1
					player3_deck.append(cart_being_movedA)
					player3_deck.append(cart_being_movedB)
		
				view_deck1_3 = " ".join(player3_deck)
				view_deck3 = view_deck1_3.replace(": ", "")
				deck3 = view_deck3.split(" ")
			else:
				deck3 = []
			if player_amount >= 4:
				for i in range(b):
					cart_to_move = random.randint(1,y) - 1
					cart_being_movedA = mazoA.pop(cart_to_move)
					cart_being_movedB = mazoB.pop(cart_to_move)
					y -= 1
					player4_deck.append(cart_being_movedA)
					player4_deck.append(cart_being_movedB)
		
				view_deck1_4 = " ".join(player4_deck)
				view_deck4 = view_deck1_4.replace(": ", "")
				deck4 = view_deck4.split(" ")
			else:
				deck4 = []
		turns.append(deck1)

	if BOT == True:
		deck2 = []
		deck3 = []
		deck4 = []
		for i in range(b):
			cart_to_move = random.randint(1,y) - 1
			cart_being_movedA = mazoA.pop(cart_to_move)
			cart_being_movedB = mazoB.pop(cart_to_move)
			y -= 1
			bot_deck.append(cart_being_movedA)
			bot_deck.append(cart_being_movedB)
		
		view_deck_bot_1 = " ".join(bot_deck)
		view_deck_bot = view_deck_bot_1.replace(": ", "")
		deck_bot = view_deck_bot.split(" ")
		turns.append(deck_bot)	

#BOT IA
def BOT_IA():
	global card_down, turn, deck_bot, new_card, player, safe_bot, bot_deck
	card_to_take_bot = False
	new_card = True
	for i in (deck_bot):
		card_down_check = list(card_down)
		if len(card_down_check) > 2:
			card_down_check_fix = card_down_check[0] + card_down_check[1]
			card_down_check.remove(card_down_check[1])
			card_down_check[0] = card_down_check_fix
		bot_card_parts = list(i)
		if len(bot_card_parts) > 2:
			bot_card_part_fix = bot_card_parts[0] + bot_card_parts[1]
			bot_card_parts.remove(bot_card_parts[1])
			bot_card_parts[0] = bot_card_part_fix
		if card_down_check[0] == bot_card_parts[0] or card_down_check[1] == bot_card_parts[1] or card_down_check[0] == "O":
			#Use Skips
			if f"F{bot_card_parts[1]}" == "".join(bot_card_parts):
				card_down = f"F{bot_card_parts[1]}"
				Create_Visual_Card(deck1)
				pygame.display.flip()
				time.sleep(0.4)
				deck_bot.remove(card_down)
				continue
			if f"X{bot_card_parts[1]}" == "".join(bot_card_parts):
				card_down = f"X{bot_card_parts[1]}"
				Create_Visual_Card(deck1)
				pygame.display.flip()
				time.sleep(0.4)
				deck_bot.remove(card_down)
				continue
			#Use + Cards(No Wild)
			if "+2" in bot_card_parts and new_card == True:
				card_down == f"+2{bot_card_parts[1]}"
				player = 1
				Pick_Card(deck1)
				Pick_Card(deck1)
				pygame.display.flip()
				time.sleep(0.5)
				new_card = False
			card_down = i
			deck_bot.remove(i)
			try:
				bot_deck.remove(f"{bot_card_parts[0]}:")
				bot_deck.remove(f"{bot_card_parts[1]}")
			except:
				pass
			card_to_take_bot = False
			safe_bot = False
			if direction_right == True:
				turn += 1
			elif direction_right == False:
				turn -= 1
			else:
				print("Error 405 Direction")
			new_card = True
			break
		else:	
			card_to_take_bot = True

	#Save Himself With WildCards
	if "WW" in bot_deck:
		if random.randint(1,10) != 5:
			card_to_take_bot = False
			card_down = "WW"
			Create_Visual_Card(deck1)
			pygame.display.flip()
			time.sleep(0.5)
			Color_Chosing("bot")
			bot_deck.remove("WW")
			player =  1

			
	if "+4W" in bot_deck:
		if random.randint(1,10) != 5:
			card_to_take_bot = False
			card_down = "+4W"
			Create_Visual_Card(deck1)
			player = 1
			Pick_Card(deck1)#deck1 because is it giving it to the player
			Pick_Card(deck1)
			Pick_Card(deck1)
			Pick_Card(deck1)		
			pygame.display.flip()
			time.sleep(0.5)	
			Color_Chosing("bot")
			bot_deck.remove("+4W")
			
	
	#Bot Takes Card
	if card_to_take_bot:
		if card_to_take_bot == True:
			Pick_Card(deck_bot)
			safe_bot = False
			if direction_right == True:
				turn += 1
			elif direction_right == False:
				turn -= 1
			else:
				print("Error 405 Direction")
	
	card_to_take_bot = False


def Create_Opponents_Cards(cards_bot_hitmox_cords, deck_bot, card_bot_x, card_bot_y, z):#1-3 players
	global random_inteval_cards
	card_botx2 = card_bot_x
	x10 = 1
	trashold_bot = 3
	broke_2 = False
	broke2_2 = False
	card_direction_bot = 1
	cards_bot_hitmox_cords = []
	for i in range(int(deck_bot)):
		card_rect_bot = pygame.draw.rect(alpha_surface, (0,0,0,0), (card_bot_x,card_bot_y, 50,75))
		cards_bot_hitmox_cords.append(card_bot_x)
		cards_bot_hitmox_cords.append(card_bot_y)
		if z == True:
			if card_direction_bot == 1:
				card_bot_x += 45 * x10 
				card_direction_bot = 2
			elif card_direction_bot == 2:
				card_bot_x -= 45 * x10 
				card_direction_bot = 1
		if z == False:
			if card_direction_bot == 1:
				card_bot_x += 30 * x10 
				card_direction_bot = 2
			elif card_direction_bot == 2:
				card_bot_x -= 30 * x10 
				card_direction_bot = 1
		x10 += 1
		if x10 > 9:
			if broke2_2 == False:
				broke_2 = False
				broke2_2 = True

		if x10 > 7 or x10 > 9:
			if broke_2 == False:
				card_bot_y += 40
				card_bot_x = card_botx2
				x10 = 1
				trashold_bot = 3
				broke_2 = True
				card_direction_bot = 1

		if x10 > trashold_bot:
			card_bot_y -= 3
			trashold_bot += 2
		screen.blit(card_image_resiced_bot, card_rect_bot)

def Create_Visual_Card(Who_Playing):
	global player1_card_amount, bot_card_amount, deck_bot, number_cards_list, card_down_rec, grab_card_rec
	global card_direction_player, cards_player_hitmox_cords, card_image_resiced_bot, mini
	global deck1_amount, deck2_amount, deck3_amount, deck4_amount, player_assigned, pa, dpal
	#Inicial Def Variables
	x = 1
	x10 = 1
	card_player_x = 450
	card_player_y = 350
	card_bot_x = 475
	card_bot_y = 50
	trashold = 3
	trashold_bot = 3
	broke = False
	broke2 = False
	broke_2 = False
	broke2_2 = False
	card_direction_player = 1
	card_direction_bot = 1
	cards_player_hitmox_cords = []
	cards_bot_hitmox_cords = []
	number_cards_list = []

	#Player Deck
	if len(Who_Playing) != 0:
		for  i in Who_Playing:
			number_cards_list.append(i)
			card_rect = pygame.draw.rect(alpha_surface, (0,0,0,0), (card_player_x,card_player_y, 100,150))
			cards_player_hitmox_cords.append(card_player_x)
			cards_player_hitmox_cords.append(card_player_y)
			if card_direction_player == 1:
				card_player_x += 90 * x 
				card_direction_player = 2
			elif card_direction_player == 2:
				card_player_x -= 90 * x 
				card_direction_player = 1
			x += 1
			if x > 11:
				if broke2 == False:
					broke = False
					broke2 = True

			if x > 9 or x > 11:
				if broke == False:
					card_player_y += 75
					card_player_x = 450
					x = 1
					trashold = 3
					broke = True
					card_direction_player = 1

			if x > trashold:
				card_player_y += 5
				trashold += 2
			try:
				card_image = card_images[f"{i}"]
				screen.blit(card_image, card_rect)
			except:
				pass
	

	
	#Opononent Cards
	if BOT == True:
		for i in deck_bot:
			card_rect_bot = pygame.draw.rect(alpha_surface, (0,0,0,0), (card_bot_x,card_bot_y, 50,75))
			cards_bot_hitmox_cords.append(card_bot_x)
			cards_bot_hitmox_cords.append(card_bot_y)
			if card_direction_bot == 1:
				card_bot_x += 45 * x10 
				card_direction_bot = 2
			elif card_direction_bot == 2:
				card_bot_x -= 45 * x10 
				card_direction_bot = 1
			x10 += 1
			if x10 > 9:
				if broke2_2 == False:
					broke_2 = False
					broke2_2 = True

			if x10 > 7 or x10 > 9:
				if broke_2 == False:
					card_bot_y += 40
					card_bot_x = 475
					x10 = 1
					trashold_bot = 3
					broke_2 = True
					card_direction_bot = 1

			if x10 > trashold_bot:
				card_bot_y -= 5
				trashold_bot += 2
			screen.blit(card_image_resiced_bot, card_rect_bot)

	#Oponents Decks
	if BOT != True:
		if player_assigned != 1:
			if opa == 2:
				if player_assigned == 2:
					Create_Opponents_Cards(cards_bot_hitmox_cords, deck1_amount, 475, 50, True)
					screen.blit(card_images["P1IMG"], (480,5))
			if opa == 3:
				if player_assigned == 3:
					Create_Opponents_Cards(cards_bot_hitmox_cords, deck1_amount, 255, 50, True)
					screen.blit(card_images["P1IMG"], (260,5))
				if player_assigned == 2:
					Create_Opponents_Cards(cards_bot_hitmox_cords, deck1_amount, 255, 50, True)
					screen.blit(card_images["P1IMG"], (260,5))
			if opa == 4:
				card_image_resiced_bot = pygame.transform.scale(card_image_bot, (34,50))
				if player_assigned == 2:
					Create_Opponents_Cards(cards_bot_hitmox_cords, deck1_amount, 800, 50, False)
					screen.blit(card_images["P1IMG"], (798,5))
				if player_assigned == 3:
					Create_Opponents_Cards(cards_bot_hitmox_cords, deck1_amount, 500, 50, False)
					screen.blit(card_images["P1IMG"], (498,5))
				if player_assigned == 4:
					Create_Opponents_Cards(cards_bot_hitmox_cords, deck1_amount, 200, 50, False)
					screen.blit(card_images["P1IMG"], (198,5))

		if player_assigned != 2 and opa >= 2:
			if opa == 2:
				if player_assigned == 1:
					Create_Opponents_Cards(cards_bot_hitmox_cords, deck2_amount, 475, 50, True)
					screen.blit(card_images["P2IMG"], (480,5))
			if opa == 3:
				if player_assigned == 3:
					Create_Opponents_Cards(cards_bot_hitmox_cords, deck2_amount, 695, 50, True)
					screen.blit(card_images["P2IMG"], (700,5))
				if player_assigned == 1:
					Create_Opponents_Cards(cards_bot_hitmox_cords, deck2_amount, 255, 50, True)
					screen.blit(card_images["P2IMG"], (260,5))
			if opa == 4:
				card_image_resiced_bot = pygame.transform.scale(card_image_bot, (34,50))
				if player_assigned == 1:
					Create_Opponents_Cards(cards_bot_hitmox_cords, deck2_amount, 200, 50, False)
					screen.blit(card_images["P2IMG"], (198,5))
				if player_assigned == 3:
					Create_Opponents_Cards(cards_bot_hitmox_cords, deck2_amount, 800, 50, False)
					screen.blit(card_images["P2IMG"], (798,5))
				if player_assigned == 4:
					Create_Opponents_Cards(cards_bot_hitmox_cords, deck2_amount, 500, 50, False)
					screen.blit(card_images["P2IMG"], (498,5))

		if player_assigned != 3 and opa >= 3:
			if opa == 3:
				if player_assigned == 1 or player_assigned == 2:
					Create_Opponents_Cards(cards_bot_hitmox_cords, deck3_amount, 695, 50, True)
					screen.blit(card_images["P3IMG"], (700,5))
			if opa == 4:
				card_image_resiced_bot = pygame.transform.scale(card_image_bot, (34,50))
				if player_assigned == 1:
					Create_Opponents_Cards(cards_bot_hitmox_cords, deck3_amount, 500, 50, False)
					screen.blit(card_images["P3IMG"], (498,5))
				if player_assigned == 2:
					Create_Opponents_Cards(cards_bot_hitmox_cords, deck3_amount, 200, 50, False)
					screen.blit(card_images["P3IMG"], (198,5))
				if player_assigned == 4:
					Create_Opponents_Cards(cards_bot_hitmox_cords, deck3_amount, 800, 50, False)
					screen.blit(card_images["P3IMG"], (798,5))

		if player_assigned != 4 and opa >= 4:
			card_image_resiced_bot = pygame.transform.scale(card_image_bot, (34,50))
			if player_assigned == 1:
				Create_Opponents_Cards(cards_bot_hitmox_cords, deck4_amount, 800, 50, False)
				screen.blit(card_images["P4IMG"], (798,5))
			if player_assigned == 2:
				Create_Opponents_Cards(cards_bot_hitmox_cords, deck4_amount, 500, 50, False)
				screen.blit(card_images["P4IMG"], (498,5))
			if player_assigned == 3:
				Create_Opponents_Cards(cards_bot_hitmox_cords, deck4_amount, 200, 50, False)
				screen.blit(card_images["P4IMG"], (198,5))

	#Card Down
	card_down_rec = pygame.draw.rect(alpha_surface, (255,0,0,0), (425,200, 150,100))
	card_image = card_images[f"{card_down}"]
	card_down_image = pygame.transform.rotate(card_image,90)
	screen.blit(card_down_image, card_down_rec)

	#Grab Card
	grab_card_rec = pygame.draw.rect(screen, (255,0,0), (585,175, 100,150))
	


def Cursor(cards_player_hitmox_cords):
	global x2, y2, card_selected, selection, mouse_cursor, z, Who_Playing
	x = 0
	pos_mouse = pygame.mouse.get_pos()
	mouse_cursor = pygame.draw.rect(alpha_surface, (255,0,0,0), (pos_mouse[0],pos_mouse[1], 10,10))
	for i in range(int(len(cards_player_hitmox_cords) / 2)):
			

			hitbox = pygame.draw.rect(alpha_surface,(0,0,0,0), (cards_player_hitmox_cords[x],cards_player_hitmox_cords[x + 1], 100,150))
			if mouse_cursor.colliderect(hitbox):
				if pygame.mouse.get_pressed()[0]:
					z = True
					x2 = cards_player_hitmox_cords[x]
					y2 = cards_player_hitmox_cords[x + 1]
					card_selected = number_cards_list[i]
					selection = True
			x += 2

	try:		
		if x2 and y2 and z == True:
			Create_Visual_Card(Who_Playing)
			card_rect = pygame.draw.rect(alpha_surface, (0,0,0,0), (x2,y2, 100,150))
			card_image = card_images[f"{card_selected}"]
			screen.blit(card_image, card_rect)
			pygame.draw.rect(screen, (255,215,215), (x2,y2, 100,150), 12, 5)		
	except:
		pass

#Pick Card
def Pick_Card(D):
	global y ,player, view_deck_bot, view_deck1
	cart_to_move = random.randint(1,y) - 1
	cart_being_movedA = mazoA.pop(cart_to_move)
	cart_being_movedB = mazoB.pop(cart_to_move)
	y -= 1
	cart_picker_moved = cart_being_movedA + cart_being_movedB
	cart_picker_moved = cart_picker_moved.replace(":", "")

	D.append(cart_picker_moved)
	view_deck1_1 = " ".join(D)
	view_deck1 = view_deck1_1.replace(": ", "")	
	
#Changing Color Special
def Color_Chosing(p):
		global direction_right, turn, move, card_down, special, Main_Loop, Game, player
		global blue_in_bot, green_in_bot, yellow_in_bot, red_in_bot, chosing_color_cooldown,card_down
		global Client, Host
		if p == 1:
			choice = False
			special = True

			rec_blu = pygame.draw.rect(screen, (0,0,200), (50,100, 100,100), 0, 100)
			rec_gre = pygame.draw.rect(screen, (0,255,0), (50,225, 100,100), 0, 100)
			rec_yel = pygame.draw.rect(screen, (255,255,0), (50,350, 100,100), 0, 100)
			rec_red = pygame.draw.rect(screen, (255,0,0), (50,475, 100,100), 0, 100)
			pygame.display.update()
			while choice != True:
				time.sleep(0.05)
				mouse_pos = pygame.mouse.get_pos()
				mouse = pygame.draw.rect(alpha_surface, (255,0,0,0), (mouse_pos[0],mouse_pos[1], 25, 25))
				pygame.display.flip()

				if mouse.colliderect(rec_blu):
					if pygame.mouse.get_pressed()[0]:
						card_down = "BB"
						choice = True
				elif mouse.colliderect(rec_gre):
					if pygame.mouse.get_pressed()[0]:
						card_down = "GG"
						choice = True
				elif mouse.colliderect(rec_yel):
					if pygame.mouse.get_pressed()[0]:
						card_down = "YY"
						choice = True
				elif mouse.colliderect(rec_red):
					if pygame.mouse.get_pressed()[0]:
						card_down = "RR"
						choice = True

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						Main_Loop = False
						Game = False
						choice = True
						Host = False
						Client = False
						return False
					
			
		if p == "bot":
			for i in deck_bot:
				cards_bot = list(i)
				if len(cards_bot) > 2:
					cards_bot_fix = cards_bot[0] + cards_bot[1]
					cards_bot.remove(cards_bot[1])
					cards_bot[0] = cards_bot_fix	
				if cards_bot[1] == "B":
					blue_in_bot += 1
				elif cards_bot[1] == "G":
					green_in_bot += 1
				elif cards_bot[1] == "Y":
					yellow_in_bot += 1
				elif cards_bot[1] == "R":
					red_in_bot += 1
	
			percent_for_blue = blue_in_bot/(blue_in_bot + green_in_bot + yellow_in_bot + red_in_bot)
			percent_for_green = green_in_bot/(blue_in_bot + green_in_bot + yellow_in_bot + red_in_bot)
			percent_for_yellow = yellow_in_bot/(blue_in_bot + green_in_bot + yellow_in_bot + red_in_bot)
			percent_for_red = red_in_bot/(blue_in_bot + green_in_bot + yellow_in_bot + red_in_bot)
			
			weights_for_chosing_bot_color = [percent_for_blue, percent_for_green, percent_for_yellow, percent_for_red]
			colors_for_bot_to_choice = ["BB", "GG", "YY", "RR"]

			chosen_color_bot = random.choices(colors_for_bot_to_choice, weights=weights_for_chosing_bot_color, k=1)[0]
			card_down = chosen_color_bot 
			pygame.display.flip()
			time.sleep(0.5)

	#Uno
def UNO(p):
	global Main_Loop, Game, screen, safe, uno_played, pa, valid
	global Client, Host, deck1_amount, deck2_amount, deck3_amount, deck4_amount, l
	available_time = random.randint(2,6)
	available_time /= 10
	at = 0.0
	r = random.randrange(200,300,20)
	cx = 500
	cy = 350
	m = 1
	n = 1
	theta = [i / 100 * 2 * math.pi for i in range(101)]  # Generate angles from 0 to 2*pi
	xu = [r * math.cos(t) + cx for t in theta]
	yu = [r * math.sin(t) + cy for t in theta]
	v = random.randrange(0,100,5)
	while p == 1 and safe == False:
		m += n
		if m + v >= 100:
			v = 0
		if m > len(xu) - n:
			m = 0
			
		
		time.sleep(0.03)
		at += 0.01

		screen.blit(background_image, (0,0))
		uno_rec = pygame.draw.rect(alpha_surface, (0,0,0,0), (xu[v + m],yu[v + m], 100,100))
		screen.blit(card_images["UnBut"],( xu[v + m],yu[v + m]))
		

		pos_mouse = pygame.mouse.get_pos()
		mouse_cursor = pygame.draw.rect(alpha_surface, (0,0,0,0), (pos_mouse[0],pos_mouse[1], 10,10))
		pygame.display.flip()

		if mouse_cursor.colliderect(uno_rec):
			if pygame.mouse.get_pressed()[0]:
				return True

		if at > available_time:
			return False
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Main_Loop = False
				Game = False
				p = 0
				return "exit"
	
	if p == 2:
		random_bot_uno_chance = random.randint(0,100)
		if random_bot_uno_chance < 70:
			return True
		else:
			return False
		
	if p == 3:
		action = False
		msg = ""
		mouse_pos = pygame.mouse.get_pos()
		mouse_cursor = pygame.draw.rect(alpha_surface, (0,0,0,0), (mouse_pos[0],mouse_pos[1], 10,10))

		uno_rect = pygame.draw.rect(alpha_surface, (0,0,0), (300,220, 100,100))
		screen.blit(card_images["UnBut"],(300,220))
		if mouse_cursor.colliderect(uno_rect) and pygame.mouse.get_pressed()[0] and valid == True:
			deck1_amount = int(deck1_amount)
			deck2_amount = int(deck2_amount)
			deck3_amount = int(deck3_amount)
			deck4_amount = int(deck4_amount)
			if deck1_amount == 1:
				if player_assigned != 1 and valid == True:
					deck1_amount += 2
					msg = "`1"
					Send(msg)
					action = True
				else:
					uno_played = True
					action = False
			if deck2_amount == 1:
				if player_assigned != 2 and valid == True:
					deck2_amount += 2
					msg = "`2"
					Send(msg)
					action = True
				else:
					uno_played = True
					action = False
			if deck3_amount == 1:
				if player_assigned != 3 and valid == True:
					deck3_amount += 2
					msg = "`3"
					Send(msg)
					action = True
				else:
					uno_played = True
					action = False
			if deck4_amount == 1:
				if player_assigned != 4 and valid == True:
					deck4_amount += 2
					msg = "`4"
					Send(msg)
					action = True
				else:
					uno_played = True
					action = False

			if action == True:
				valid = False
			else:
				valid = True
     
			if pa == 2:
				if deck1_amount != 1 and deck2_amount != 1 and valid == True:
					Pick_Card(l)
					Pick_Card(l)
					valid = False
			if pa == 3:
				if deck1_amount != 1 and deck2_amount != 1 and deck3_amount != 1 and valid == True:
					Pick_Card(l)
					Pick_Card(l)
					valid = False
			if pa == 4:
				if deck1_amount != 1 and deck2_amount != 1 and deck3_amount != 1 and deck4_amount != 1 and valid == True:
					Pick_Card(l)
					Pick_Card(l)
					valid = False


	
#Player/s Control/s
def Control_Player(Who_Playing):
	global new_card, z, turn, chosing_color_cooldown, move, card_down
	global start_cart, special, turn_go, BOT, selection, move_past, move2
	global player, direction_right, forceturn, pa10, click2, safe
	try:
		list(move)
	except:
		move = "drock"
	if BOT == False:
		move_past = "dracula"
	Cursor(cards_player_hitmox_cords)
	Create_Visual_Card(Who_Playing)
	turn_go = False
	if selection == True:
		if card_down_rec.colliderect(mouse_cursor) and pygame.mouse.get_pressed()[0]:
			move = card_selected
			selection = False
			move2 = "dock"
	if grab_card_rec.colliderect(mouse_cursor) and pygame.mouse.get_pressed()[0] and click2 == True:
		click2 = False
		Pick_Card(Who_Playing)
		Create_Visual_Card(Who_Playing)
		pygame.display.flip()
		new_card = False
		z = False
		TURN(1)
		if BOT == True:
			turn = player = 2
		player = turn
		time.sleep(0.1)
	if True:#move != move_past or move2 == "DUCK":
		card_placed = list(move)
		card_down_check = list(card_down)
		if len(card_placed) > 2:
			card_placed_fix = card_placed[0] + card_placed[1]
			card_placed.remove(card_placed[1])
			card_placed[0] = card_placed_fix
		if len(card_down_check) > 2:
			card_down_check_fix = card_down_check[0] + card_down_check[1]
			card_down_check.remove(card_down_check[1])
			card_down_check[0] = card_down_check_fix
		if move in Who_Playing:
			if card_placed[0] == card_down_check[0] or card_placed[1] == card_down_check[1] or card_placed[1] == "W" or special == True and turn_go == False:
				card_down = move
				Who_Playing.remove(move)
				new_card = True
				turn_go = True
				if "+2" in card_placed and BOT == True and new_card == True:
					Pick_Card(deck_bot)
					Pick_Card(deck_bot)
				if "+2" in card_placed and BOT == False and new_card == True:
					turn2 = turn
					if direction_right == True:
						turn2 += 1
					elif direction_right == False:
						turn2 -= 1
					else:
						print("Error 405 Direction")
					if turn2 > pa:
						turn2 = 1
					if turn2 < 1:
						turn2 = pa
					if turn2 == 1 and p1 == False:
						if direction_right == True:
							turn2 = 2
						if direction_right == False:
							turn2 = 4
					if turn2 == 2 and p2 == False:
						if direction_right == True:
							turn2 = 3
						if direction_right == False:
							turn2 = 1
					if turn2 == 3 and p3 == False:
						if direction_right == True:
							turn2 = 4
						if direction_right == False:
							turn2 = 2
					if turn2 == 4 and p4 == False:
						if direction_right == True:
							turn2 = 1
						if direction_right == False:
							turn2 = 3
					player2 = turn2
					for i in range(2):
						if BOT == True:
							if player2 == 2:
								Pick_Card(deck_bot)
								new_card = False		
						else:
							if turn2 == 1:
								f = deck1
							if turn2 == 2:
								f = deck2
							if turn2 == 3:
								f = deck3
							if turn2 == 4:
								f = deck4
							try:
								Pick_Card(f)
							except:
								pass

				if "+4" in card_placed and new_card == True and BOT == True:
					Pick_Card(deck_bot)
					Pick_Card(deck_bot)
					Pick_Card(deck_bot)
					Pick_Card(deck_bot)
				if "+4" in card_placed and new_card == True and BOT == False:
					turn2 = turn
					if direction_right == True:
						turn2 += 1
					elif direction_right == False:
						turn2 -= 1
					else:
						print("Error 405 Direction")
					if turn2 > pa:
						turn2 = 1
					if turn2 < 1:
						turn2 = pa
					if turn2 == 1 and p1 == False:
						if direction_right == True:
							turn2 = 2
						if direction_right == False:
							turn2 = 4
					if turn2 == 2 and p2 == False:
						if direction_right == True:
							turn2 = 3
						if direction_right == False:
							turn2 = 1
					if turn2 == 3 and p3 == False:
						if direction_right == True:
							turn2 = 4
						if direction_right == False:
							turn2 = 2
					if turn2 == 4 and p4 == False:
						if direction_right == True:
							turn2 = 1
						if direction_right == False:
							turn2 = 3
					player2 = turn2
					for i in range(4):
						if BOT == True:
							if player2 == 2:
								Pick_Card(deck_bot)		
						else:
							if turn2 == 1:
								f = deck1
							if turn2 == 2:
								f = deck2
							if turn2 == 3:
								f = deck3
							if turn2 == 4:
								f = deck4
							try:
								Pick_Card(f)
							except:
								pass
				if "W" in card_placed and new_card == True:
					if Color_Chosing(1) == False:
						return False
					new_card = False
					move = ""
				if "F" in card_placed and BOT == True: 
					forceturn = 1
				if "F" in card_placed and BOT == False:
					if pa10 == 2:
						if Who_Playing == deck1:
							forceturn = 1
						if Who_Playing == deck2:
							forceturn = 2
						if Who_Playing == deck3:
							forceturn = 3
						if Who_Playing == deck4:
							forceturn = 4
					else:
						if direction_right == True:
							direction_right = False
						elif direction_right == False:
							direction_right = True
					new_card = False
				if "X" in card_placed and BOT == True:
					forceturn = 1
				if "X" in card_placed and BOT == False:
					if pa10 == 2:
						if Who_Playing == deck1:
							forceturn = 1
						if Who_Playing == deck2:
							forceturn = 2
						if Who_Playing == deck3:
							forceturn = 3
						if Who_Playing == deck4:
							forceturn = 4
					else:
						TURN(1)
					new_card = False
				view_deck1_1 = " ".join(Who_Playing)
				view_deck1 = view_deck1_1.replace(": ", "")
				chosing_color_cooldown = False
				special = False
				z = False
				if BOT == True:
					move_past = move
					move = ""
					if turn_go == True:
						if direction_right == True:
							turn += 1
						elif direction_right == False:
							turn -= 1
						else:
							print("Error 405 Direction")
				else:
					TURN(1)
					move_past = move
					move = ""
					time.sleep(0.05)
				card_placed = ["D", "U", "C", "K"]
				move2 = "DUCK"

#Server In Game
def TURN(q):
	global turn, player, pa, direction_right, player_assigned, player_data, safe
	safe = False
	if q == 1:
		try:
			pa2 = opa
		except:
			pa2 = pa
		if direction_right == True:
			turn += 1
		elif direction_right == False:
			turn -= 1
		else:
			print("Error 405 Direction")
   
		if turn > pa2:
			turn = 1
		if turn < 1:
			turn = pa2
  
	if q == 2:
		w = player_assigned
		if direction_right == True:
			w -= 1
		elif direction_right == False:
			w += 1
		else:
			print("Error 405 Direction")
   
		if w > pa:
			w = 1
		if w < 1:
			w = pa
		return w
	
	if q == 3:
		turn2 = int(player_data)

		if turn2 > pa:
			turn2 = 1
		if turn2 < 1:
			turn2 = pa
		w = turn2

		if direction_right == True:
			w += 1
		elif direction_right == False:
			w -= 1
		else: 
			print("Error 405 Direction")

		if w > pa:
			w = 1
		if w < 1:
			w = pa
		
		return w
 
#Host Loop
def HOST():
	global pa, player_amount, Client, turn, p2, p3, p4, opa
	global deck1, deck2, deck3, deck4, card_down, start_cart, total_data
	global message_send1, message_send2, message_send3, message_send4
	global cards_to_pick_for_next_player, direction_bool, double_check_pa
	if Host == True:
		Client = True
		if slot1 == (0,255,0):
			player_amount = 1
			pa = 1
			opa = 1
		if slot2 == (0,255,0):
			player_amount = 2
			pa = 2
			opa = 2
		if slot3 == (0,255,0):
			player_amount = 3
			pa = 3
			opa = 3
		if slot4 == (0,255,0):
			player_amount = 4
			pa = 4
			opa = 4
	
		Start_Cards()
 
		if deck1:
			conn1.sendall("1/".encode() + (",".join(deck1)).encode() + "|".encode() + card_down.encode() + "*".encode() + str(turn).encode() + "]Y".encode() + f"[{direction_bool}".encode() + f"){cards_to_pick_for_next_player}".encode() + f"({pa}?{pa}#{available_slots}".encode() + f"<{len(deck1)}>{len(deck2)}>{len(deck3)}>{len(deck4)}>".encode())
			time.sleep(0.1)
		if deck2:
			conn2.sendall("2/".encode() + (",".join(deck2)).encode() + "|".encode() + card_down.encode() + "*".encode() + str(turn).encode() + "]Y".encode() + f"[{direction_bool}".encode() + f"){cards_to_pick_for_next_player}".encode() + f"({pa}?{pa}#{available_slots}".encode() + f"<{len(deck1)}>{len(deck2)}>{len(deck3)}>{len(deck4)}>".encode())
			time.sleep(0.1)
		if deck3:
			conn3.sendall("3/".encode() + (",".join(deck3)).encode() + "|".encode() + card_down.encode() + "*".encode() + str(turn).encode() + "]Y".encode() + f"[{direction_bool}".encode() + f"){cards_to_pick_for_next_player}".encode() + f"({pa}?{pa}#{available_slots}".encode() + f"<{len(deck1)}>{len(deck2)}>{len(deck3)}>{len(deck4)}>".encode())
			time.sleep(0.1)
		if deck4:
			conn4.sendall("4/".encode() + (",".join(deck4)).encode() + "|".encode() + card_down.encode() + "*".encode() + str(turn).encode() + "]Y".encode() + f"[{direction_bool}".encode() + f"){cards_to_pick_for_next_player}".encode() + f"({pa}?{pa}#{available_slots}".encode() + f"<{len(deck1)}>{len(deck2)}>{len(deck3)}>{len(deck4)}>".encode())
			time.sleep(0.1)

	def Multiplayer_Move(deck, q):
			global move_data, card_down, played, turn, player, total_data
			global deck1, deck2, deck3, deck4, available_slots, double_check_pa
			global cards_to_pick_for_next_player, direction_bool, chat_message, message_send
			played = False
			
			if total_data and ";" not in total_data and "&" not in total_data and "`" not in total_data: 
				try:
					if remove_or_not == True:		
						deck = deck.remove(move_data)
						remove_or_not = False
					total_data = None
				except:
					pass
				finally:
					card_down = move_data
					played = True
					next_turn = TURN(3)
     
					if conn1:
						if turn == 1:
							cards_to_pick_for_next_player1 = cards_to_pick
						else:
							cards_to_pick_for_next_player1 = 0
						conn1.sendall("1/".encode() + (",".join(deck1)).encode() + "|".encode() + card_down.encode() + "*".encode() + str(turn).encode() + "]Y".encode() + f"[{direction_bool}".encode() + f"){cards_to_pick_for_next_player1}".encode() + f"({pa}?{opa}#{available_slots}".encode() + f"<{len(deck1)}>{len(deck2)}>{len(deck3)}>{len(deck4)}>".encode())
					if conn2:
						if turn == 2:
							cards_to_pick_for_next_player2 = cards_to_pick
						else:
							cards_to_pick_for_next_player2 = 0
						conn2.sendall("2/".encode() + (",".join(deck2)).encode() + "|".encode() + card_down.encode() + "*".encode() + str(turn).encode() + "]Y".encode() + f"[{direction_bool}".encode() + f"){cards_to_pick_for_next_player2}".encode() + f"({pa}?{opa}#{available_slots}".encode() + f"<{len(deck1)}>{len(deck2)}>{len(deck3)}>{len(deck4)}>".encode())
					if conn3:
						if turn == 3:
							cards_to_pick_for_next_player3 = cards_to_pick
						else:
							cards_to_pick_for_next_player3 = 0
						conn3.sendall("3/".encode() + (",".join(deck3)).encode() + "|".encode() + card_down.encode() + "*".encode() + str(turn).encode() + "]Y".encode() + f"[{direction_bool}".encode() + f"){cards_to_pick_for_next_player3}".encode() + f"({pa}?{opa}#{available_slots}".encode() + f"<{len(deck1)}>{len(deck2)}>{len(deck3)}>{len(deck4)}>".encode())
					if conn4:
						if turn == 4:
							cards_to_pick_for_next_player4 = cards_to_pick
						else:
							cards_to_pick_for_next_player4 = 0
						conn4.sendall("4/".encode() + (",".join(deck4)).encode() + "|".encode() + card_down.encode() + "*".encode() + str(turn).encode() + "]Y".encode() + f"[{direction_bool}".encode() + f"){cards_to_pick_for_next_player4}".encode() + f"({pa}?{opa}#{available_slots}".encode() + f"<{len(deck1)}>{len(deck2)}>{len(deck3)}>{len(deck4)}>".encode())
						
					total_data = None
     
			if total_data and ";" in total_data and "&" not in total_data and "`" not in total_data:
				if conn1:
					conn1.sendall(total_data.encode())
				if conn2:
					conn2.sendall(total_data.encode())
				if conn3:
					conn3.sendall(total_data.encode())
				if conn4:
					conn4.sendall(total_data.encode())
				total_data = None

			elif total_data and "&" in total_data and "`" not in total_data:
				if conn1:
					conn1.sendall(total_data.encode())
				if conn2:
					conn2.sendall(total_data.encode())
				if conn3:
					conn3.sendall(total_data.encode())
				if conn4:
					conn4.sendall(total_data.encode())
				total_data = None
			
			elif total_data and "`" in total_data:
				if conn1:
					conn1.sendall(total_data.encode())
				if conn2:
					conn2.sendall(total_data.encode())
				if conn3:
					conn3.sendall(total_data.encode())
				if conn4:
					conn4.sendall(total_data.encode())
				total_data = None


	while Host == True and not stop_all.is_set():
		time.sleep(0.2)
	
		current_player_disconnected = False
		if turn == 2 and 2 in available_slots:
			current_player_disconnected = True
			p2 = False
		elif turn == 3 and 3 in available_slots:
			current_player_disconnected = True
			p3 = False
		elif turn == 4 and 4 in available_slots:
			current_player_disconnected = True
			p4 = False
		else:
			current_player_disconnected = False

		if 4 in available_slots:
			p4 = False
		
		if current_player_disconnected:
			double_check_pa = True
			TURN(1)
   
		if double_check_pa == True:
			pa = 1
			if p2 == True:
				pa += 1
			if p3 == True:
				pa += 1
			if p4 == True:
				pa += 1
			
		print(available_slots)
		try:
			if total_data:
				if TURN(2) == 1:
					if Multiplayer_Move(deck1, 1) == "Not Valid Move":
						conn1.sendall(b"Not Valid Move")
						total_data = None
				elif TURN(2) == 2:
					if Multiplayer_Move(deck2, 2) == "Not Valid Move":
						conn2.sendall(b"Not Valid Move")
						total_data = None
				elif TURN(2) == 3:
					if Multiplayer_Move(deck3, 3) == "Not Valid Move":
						conn3.sendall(b"Not Valid Move")
						total_data = None
				elif TURN(2) == 4:
					if Multiplayer_Move(deck4, 4) == "Not Valid Move":
						conn4.sendall(b"Not Valid Move")
						total_data = None
			total_data = None
		except Exception as e:
			pass
     

def CHAT():
	global text_box, send_chat, chat_message_to_send, line1, line2, line3, player_assigned, x_for_reserve
	while Client == True:
		time.sleep(0.1)
		if text_box == True:
			line1 = ""
			line2 = ""
			line3 = ""
			for i in list(chat_message_to_send):
				if font_chat.render(f"{line1 + "m"}", True, (255,255,255)).get_size()[0] < text_cuadrant_surface.get_size()[0] - 10:
					line1 += i
				elif font_chat.render(f"{line2 + "m"}", True, (255,255,255)).get_size()[0] < text_cuadrant_surface.get_size()[0] - 10:
					line2 += i
				elif font_chat.render(f"{line3 + "m"}", True, (255,255,255)).get_size()[0] < text_cuadrant_surface.get_size()[0] - 10:
					line3 += i	

		if send_chat == True and len(chat_message_to_send.strip(" ")) > 0 :
			send_chat = False
			Send(f'{player_assigned};{chat_message_to_send}')	
			chat_message_to_send = ""

#Waiting Circle
def Circle_Wait_Thread():#YES THIS IS A THREAD JUST FOR A ****** WAITING CIRCLE
	global xc, yc, wait_circle, Client
	color = 0
	color_slowness = 0
	xyc = 0
	while Client == True and Host != True:
		while wait_circle == True and Client == True and pause_bool == False:
			time.sleep(0.02)
			if color_slowness == 1:
				color += color_slowness
			else:
				color_slowness += 0.2
			
			color = int(color)
			if color >= len(title_colors):
				color = 0
			try:
				screen.blit(background_image, (0,0))
				pygame.draw.circle(screen, (title_colors[color]), (xc[int(xyc)], yc[int(xyc)]), 5)
				xyc += 1
				if xyc > 100:
					xyc = 0
				screen.blit(font_button.render("Waiting For Host To Start", True, (title_colors[color - 40])), (width/2 - font_button.render("Waiting For Host To Start", True, (255,255,255)).get_size()[0]/2, 120))
				pygame.display.flip()
			except:
				pass

def Online_Game():
	global Host, Client, player_assigned, pa
	global deck1, deck2, deck3, deck4, opa
	global deck1_amount, deck2_amount, deck3_amount, deck4_amount
	global card_down, turn, direction_right, direction_bool
	global screen, background_image, rot_cir_pos
	global text_cuadrant_surface, font_chat
	global CHAT_SAVE, CHAT_PROCESS_SAVE, x_for_reserve
	global line1, line2, line3, valid, available_slots
	global x_for_reserve, client_game, wait_circle
	global cards_to_pick_for_next_player, message_send
	global selection, z, move, card_selected, dpal
	global mouse_cursor, card_down_rec, grab_card_rec
	global cards_player_hitmox_cords, xc, yc
	global Who_Playing, slot3, text_box, send_chat
	global win, l, uno_played, chat_message_to_send
	if Host == True:
		threading.Thread(target=HOST, daemon=True).start()
     
	if Client == True:
		threading.Thread(target=CHAT, daemon=True).start()
		threading.Thread(target=Circle_Wait_Thread, daemon=True).start()

	lost = False
	text_box = False
	l = None
	if l == None:
		wait_circle = True
	opa = pa
	while Client == True:
		xx = False
		x = None
		chat_message_to_send = ""
		send_chat = False
		while not x:
			time.sleep(0.05)
			x = receive(2)
			try:
				len(l)
				try:
					screen.blit(background_image, (0,0))
					Create_Visual_Card(l)
					UNO(3)
				except:
					pass
			except:
				pass

			if Host == True:
				if opa == 2 and 2 in available_slots and Host == True or opa == 3 and 2 in available_slots and 3 in available_slots and Host == True or opa == 4 and 2 in available_slots and 3 in available_slots and 4 in available_slots:
					klp = True
					while klp == True:
						time.sleep(0.1)
						screen.blit(font_win_defeat.render("All Players Disconected", True, (255,255,255)), (width/2 - font_win_defeat.render("All Players Disconected", True, (255,255,255)).get_size()[0]/2, 150))
						x = None
						l = None
						Client = False
						Host = False
						main_menu_rect = pygame.draw.rect(screen, (255,255,255), (width/2 - 125, 325, 250,80),10, 11)
						quit_rect = pygame.draw.rect(screen, (255,255,255), (width/2 - 125, 425, 250,80),10, 11)

						screen.blit(font_button4.render("Main Menu", True, (255,255,255)), (width/2 - font_button4.render("Main Menu", True, (255,255,255)).get_size()[0]/2, 330))
						screen.blit(font_button2.render("QUIT", True, (255,255,255)), (width/2 - font_button2.render("QUIT", True, (255,255,255)).get_size()[0]/2, 425))

						mouse_pos = pygame.mouse.get_pos()
						mouse_cursor = pygame.draw.rect(alpha_surface, (0,0,0,0), (mouse_pos[0],mouse_pos[1], 10,10))

						if pygame.mouse.get_pressed()[0]:
							if mouse_cursor.colliderect(main_menu_rect):
								klp = False
								quit_all()
								return
							if mouse_cursor.colliderect(quit_rect):
								klp = False
								return False

						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								klp = False
								return False

						pygame.display.flip()
    
    
			if pa > 2:
				pygame.draw.circle(screen, (255,255,255), (x_circle[rot_cir_pos] + 535, y_circle[rot_cir_pos] - 260), 4)
				if direction_right == True:
					rot_cir_pos += 2
				elif direction_right == False:
					rot_cir_pos -= 2
				if rot_cir_pos > 100:
					rot_cir_pos = 0
				if rot_cir_pos < 0:
					rot_cir_pos = 100
			
			if text_box == True:
				pygame.draw.rect(text_cuadrant_surface, (128,128,128,160), (text_cuadrant_surface.get_rect()))
				screen.blit(text_cuadrant_surface, (720,30))
				pygame.draw.line(screen, (0,0,0), (720,245), (970, 245), 3)
				pygame.draw.line(screen, (0,0,0), (720,330), (970, 330), 3)
				pygame.draw.line(screen, (0,0,0), (720,245), (720, 330), 3)
				pygame.draw.line(screen, (0,0,0), (970,245), (970, 330), 3)
				screen.blit(font_chat.render(f"{line1}", True, (255,255,255)), (730,250))
				screen.blit(font_chat.render(f"{line2}", True, (255,255,255)), (730,270))
				screen.blit(font_chat.render(f"{line3}", True, (255,255,255)), (730,290))
				csbsy = 35
				i3 = ""
				csx = 0 
				for i in CHAT_SAVE:
					CHAT_SAVE.remove(i)
					i2 = str(i[:i.index(";") + 1])
					if i2 == "1;":
						i3 = "Player 1: "
					if i2 == "2;":
						i3 = "Player 2: "
					if i2 == "3;":
						i3 = "Player 3: "
					if i2 == "4;":
						i3 = "Player 4: "
					i = i.replace(f"{i2}", "")
					i = i3 + i
					csx += 1
					CHAT_PROCESS_SAVE.append(i)
				for i in range(len(CHAT_PROCESS_SAVE)):
					if csbsy + 20 > 225:
						CHAT_PROCESS_SAVE.remove(CHAT_PROCESS_SAVE[0])
					line4 = ""
					line5 = ""
					line6 = ""
					line7 = ""
					try:
						for u in list(CHAT_PROCESS_SAVE[i]):
							if font_chat.render(f"{line4 + "m"}", True, (255,255,255)).get_size()[0] < text_cuadrant_surface.get_size()[0] - 10:
								line4 += u
							elif font_chat.render(f"{line5 + "m"}", True, (255,255,255)).get_size()[0] < text_cuadrant_surface.get_size()[0] - 10:
								line5 += u
							elif font_chat.render(f"{line6 + "m"}", True, (255,255,255)).get_size()[0] < text_cuadrant_surface.get_size()[0] - 10:
								line6 += u
							elif font_chat.render(f"{line7 + "m"}", True, (255,255,255)).get_size()[0] < text_cuadrant_surface.get_size()[0] - 10:
								line7 += u
					except:
						pass
						
					if len(line4) > 0:
						screen.blit(font_chat.render(f"{line4}", True, (255,255,255)), (730, csbsy))
					if len(line5) > 0:
						csbsy += 20
						screen.blit(font_chat.render(f"{line5}", True, (255,255,255)), (730, csbsy))
					if len(line6) > 0:
						csbsy += 20
						screen.blit(font_chat.render(f"{line6}", True, (255,255,255)), (730, csbsy))
					if len(line7) > 0:
						csbsy += 20
						screen.blit(font_chat.render(f"{line7}", True, (255,255,255)), (730, csbsy))
					if len(line4) > 0:
						csbsy += 20	

			if wait_circle == False:
				pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE and text_box == True and font_chat.render(f"{line3 + "m"}", True, (255,255,255)).get_size()[0] < text_cuadrant_surface.get_size()[0] - 10:
						chat_message_to_send += " "
					if event.unicode.isalnum() and text_box == True and font_chat.render(f"{line3 + "m"}", True, (255,255,255)).get_size()[0] < text_cuadrant_surface.get_size()[0] - 10 and event.key != pygame.K_SEMICOLON:
						chat_message_to_send += event.unicode
					if event.key == pygame.K_RETURN and text_box == False:
						text_box = True
					elif event.key == pygame.K_RETURN and text_box == True and len(chat_message_to_send) == 0:
						text_box = False
						screen.blit(background_image, (0,0))
						try:
							Create_Visual_Card(l)
						except:
							pass
						pygame.display.flip()
					if event.key == pygame.K_RETURN and text_box == True and len(chat_message_to_send) > 0:
						send_chat = True
						CHAT_SAVE.append(f"{player_assigned};{chat_message_to_send}")
					if event.key == pygame.K_BACKSPACE:
						chat_message_to_send = chat_message_to_send[:-1]
      
					if event.key == pygame.K_ESCAPE:
						pause_check = Pause_Menu()
						if pause_check == False:
							quit_all()
							return
						if pause_check == "exit":
							return False
	
				if event.type == pygame.QUIT:
					client_game = False
					Host = False
					xx = True
					return False
			if xx == True:
				break

		if xx == True:
			client_game = False
			Client = False
			Host = False
	
		client_game = True
		print("x=",x)
		#Forcefixing when win and uno message send at the same time
		if x and "`" in x and "&" in x:
			x = x.replace("`", "")

		if x and "`" in x and ']' not in x and "&" not in x and ";" not in x:
			checking_uno_player = list(x)
			checking_uno_player = [x for x in checking_uno_player if x != "`"]
			for i in range(len(checking_uno_player)):
				checking_uno_player[i-1] = int(checking_uno_player[i-1])
			if player_assigned in checking_uno_player and uno_played == False:
				Pick_Card(l)
				Pick_Card(l)
				if direction_right == True:
					direction_bool = "T"
				elif direction_right == False:
					direction_bool = "F"
				else:
					print("ERROR SENDING DIRECTION DATA")
				msg = f"{player_assigned}/'{"'".join(l)}|{card_down}*{turn}]N[{direction_bool}){cards_to_pick_for_next_player}({message_send}?{opa}"
				Send(msg)
				screen.blit(background_image, (0,0))
				try:
					Create_Visual_Card(l)
				except:
					pass
		
		if "&" in x and ']' not in x and "`" not in x and ";" not in x:
			winning_player = x[x.index("&"):]
			winning_player = winning_player.replace("&", "")
			while True:
				time.sleep(0.1)
				if winning_player != "0":
					screen.blit(font_win_defeat.render(f"Player {winning_player} Wins", True, (255,255,255)), (width/2 - font_win_defeat.render(f"Player {winning_player} Wins", True, (255,255,255)).get_size()[0]/2, 150))
					winning_player_int = int(winning_player)
					if winning_player_int == 1:
						deck1_amount = 0
					if winning_player_int == 2:
						deck2_amount = 0
					if winning_player_int == 3:
						deck3_amount = 0
					if winning_player_int == 4:
						deck4_amount = 0
				else:
					screen.blit(font_win_defeat.render("Host Disconected", True, (255,255,255)), (width/2 - font_win_defeat.render("Host Disconected", True, (255,255,255)).get_size()[0]/2, 150))
					x = None
					l = None
					Client = False
				main_menu_rect = pygame.draw.rect(screen, (255,255,255), (width/2 - 125, 325, 250,80),10, 11)
				quit_rect = pygame.draw.rect(screen, (255,255,255), (width/2 - 125, 425, 250,80),10, 11)
  
				screen.blit(font_button4.render("Main Menu", True, (255,255,255)), (width/2 - font_button4.render("Main Menu", True, (255,255,255)).get_size()[0]/2, 330))
				screen.blit(font_button2.render("QUIT", True, (255,255,255)), (width/2 - font_button2.render("QUIT", True, (255,255,255)).get_size()[0]/2, 425))

				mouse_pos = pygame.mouse.get_pos()
				mouse_cursor = pygame.draw.rect(alpha_surface, (0,0,0,0), (mouse_pos[0],mouse_pos[1], 10,10))

				if pygame.mouse.get_pressed()[0]:
					if mouse_cursor.colliderect(main_menu_rect):
						quit_all()
						return
					if mouse_cursor.colliderect(quit_rect):
						return False

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						return False
	
				pygame.display.flip()
 
		if x and ";" in x:
			if str(player_assigned) not in x:
				CHAT_SAVE.append(x)
			x = None
  
		if x and ";" not in x and "&" not in x and "`" not in x:
			valid = True
			cut = x.index("/")
			player_assigned = int(x[:cut])
			x = x.replace(f"{player_assigned}/", "")
			cut2 = x.index("|")
			cut3 = x.index("*")
			cut4 = x.index("]")
			remove_maybe = x[cut4:x.index("[")]

			remove_maybe = list(remove_maybe.replace("]", ""))
			remove_maybe = "".join(remove_maybe)
			x = x.replace(f"]{remove_maybe}", "")

			cut5 = x.index("[")
			direction_bool = x[cut5:x.index(")")]
			direction_bool = list(direction_bool.replace('[', ""))
			direction_bool = "".join(direction_bool)

			cut6 = x.index(")")
			cards_to_pick = x[cut6:x.index("(")]
			cards_to_pick = list(cards_to_pick.replace(')', ""))
			cards_to_pick = int("".join(cards_to_pick))

			cut7 = x.index("(")
			try:
				pa = x[cut7:x.index("<")]
			except:
				pa = x[cut7:]
			pal = list(pa.replace("(", "").replace("?", ""))
			dpal = pa[pa.index("#"):]
			pa = int(pal[0])
			opa = int(pal[1])

			if '1' in dpal:
				card_images["P1IMG"] = pygame.image.load("Images/Player1D.png")
			else:
				card_images["P1IMG"] = pygame.image.load("Images/Player1.png")

			if '2' in dpal:
				card_images["P2IMG"] = pygame.image.load("Images/Player2D.png")
			else:
				card_images["P2IMG"] = pygame.image.load("Images/Player2.png")

			if '3' in dpal:
				card_images["P3IMG"] = pygame.image.load("Images/Player3D.png")
			else:
				card_images["P3IMG"] = pygame.image.load("Images/Player3.png")

			if '4' in dpal:
				card_images["P4IMG"] = pygame.image.load("Images/Player4D.png")
			else:
				card_images["P4IMG"] = pygame.image.load("Images/Player4.png")

			try:
				cut8 = x.index("<")
				players_cards_amounts = x[cut8:]
				x = x.replace(players_cards_amounts, "")
				players_cards_amounts = players_cards_amounts.replace("<", "")
				players_cards_amounts_rest = players_cards_amounts.split(">")
				deck1_amount = players_cards_amounts_rest[0].replace("<", "")
				deck2_amount = players_cards_amounts_rest[1]
				deck3_amount = players_cards_amounts_rest[2]
				deck4_amount = players_cards_amounts_rest[3]
			except:
				pass
  
			turn = int((x[cut3:x.index("[")].replace("*", "")))
			card_down = x[cut2:x.index("*")]
			card_down = card_down.replace("|", "")

			if player_assigned == 1:
				deck1 = x[:cut2]
				deck1 = deck1.split(",")
				l = deck1
				wait_circle = False	
				Who_Playing = deck1
			elif player_assigned == 2:
				deck2 = x[:cut2]
				deck2 = deck2.split(",")
				l = deck2
				wait_circle = False	
				Who_Playing = deck2
			elif player_assigned == 3:
				deck3 = x[:cut2]
				deck3 = deck3.split(",")
				l = deck3
				wait_circle = False	
				Who_Playing = deck3
			elif player_assigned == 4:
				deck4 = x[:cut2]
				deck4 = deck4.split(",")
				l = deck4
				wait_circle = False	
				Who_Playing = deck4

			if direction_bool == "T":
				direction_right = True
			elif direction_bool == "F":
				direction_right = False
			else:
				print("ERROR IN GETTING DIRECTION DATA")

			if cards_to_pick > 0 and len(l) != 0:
				for i in range(cards_to_pick):
					Pick_Card(l)
				cards_to_pick = 0
				msg = f"{player_assigned}/'{"'".join(l)}|{card_down}*{turn}]N[{direction_bool}){cards_to_pick}({message_send}?{opa}"
				Send(msg)

			x = None

			countq = 0
			while client_game == True:
				screen.blit(background_image, (0,0))
				if pa > 2:
					pygame.draw.circle(screen, (255,255,0), (x_circle[rot_cir_pos] + 535, y_circle[rot_cir_pos] - 260), 4)
					if direction_right == True:
						rot_cir_pos += 3
					elif direction_right == False:
						rot_cir_pos -= 3
					if rot_cir_pos > 100:
						rot_cir_pos = 0
					if rot_cir_pos < 0:
						rot_cir_pos = 100
				#Chat
				if selection != True:
					x_for_reserve = receive(2)
				if x_for_reserve and ";" in x_for_reserve and ']' not in x_for_reserve:
					if str(player_assigned) not in x_for_reserve:
						CHAT_SAVE.append(x_for_reserve)
					x_for_reserve = None
				if x_for_reserve and "`" in x_for_reserve and ']' not in x_for_reserve:
					checking_uno_player = list(x_for_reserve)
					checking_uno_player = [x_for_reserve for x_for_reserve in checking_uno_player if x_for_reserve != "`"]
					for i in range(len(checking_uno_player)):
						checking_uno_player[i-1] = int(checking_uno_player[i-1])
					if player_assigned in checking_uno_player and uno_played == False:
						Pick_Card(l)
						Pick_Card(l)
						if direction_right == True:
							direction_bool = "T"
						elif direction_right == False:
							direction_bool = "F"
						else:
							print("ERROR SENDING DIRECTION DATA")
						msg = f"{player_assigned}/'{"'".join(l)}|{card_down}*{turn}]N[{direction_bool}){cards_to_pick_for_next_player}({message_send}?{opa}"
						Send(msg)
						screen.blit(background_image, (0,0))
						try:
							Create_Visual_Card(l)
						except:
							pass
					x_for_reserve = None
       
				while x_for_reserve and "&0" in x_for_reserve:
					time.sleep(0.1)
					screen.blit(font_win_defeat.render("Host Disconected", True, (255,255,255)), (width/2 - font_win_defeat.render("Host Disconected", True, (255,255,255)).get_size()[0]/2, 150))
					x = None
					l = None
					Client = False
					main_menu_rect = pygame.draw.rect(screen, (255,255,255), (width/2 - 125, 325, 250,80),10, 11)
					quit_rect = pygame.draw.rect(screen, (255,255,255), (width/2 - 125, 425, 250,80),10, 11)
  
					screen.blit(font_button4.render("Main Menu", True, (255,255,255)), (width/2 - font_button4.render("Main Menu", True, (255,255,255)).get_size()[0]/2, 330))
					screen.blit(font_button2.render("QUIT", True, (255,255,255)), (width/2 - font_button2.render("QUIT", True, (255,255,255)).get_size()[0]/2, 425))

					mouse_pos = pygame.mouse.get_pos()
					mouse_cursor = pygame.draw.rect(alpha_surface, (0,0,0,0), (mouse_pos[0],mouse_pos[1], 10,10))

					if pygame.mouse.get_pressed()[0]:
						if mouse_cursor.colliderect(main_menu_rect):
							quit_all()
							x_for_reserve = None
							return
						if mouse_cursor.colliderect(quit_rect):
							x_for_reserve = None
							return False

					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							x_for_reserve = None
							return False
	
					pygame.display.flip()
					

				#Playing Logic
				if direction_right == True:
					direction_bool = "T"
				elif direction_right == False:
					direction_bool = "F"
				else:
					print("ERROR SENDING DIRECTION DATA")

				if turn == player_assigned:
					if lost == True:
						TURN(1)
						msg = f"{player_assigned}/'{"'".join(l)}|{card_down}*{turn}]N[{direction_bool}){cards_to_pick_for_next_player}({message_send}?{opa}"
						Send(msg)
					Create_Visual_Card(l)
					Cursor(cards_player_hitmox_cords)
					UNO(3)
					if grab_card_rec.colliderect(mouse_cursor):
						if pygame.mouse.get_pressed()[0]:
							Pick_Card(l) 
							TURN(1)
							cards_to_pick_for_next_player = 0
							if not message_send:
								message_send = " "
							msg = f"{player_assigned}/'{"'".join(l)}|{card_down}*{turn}]N[{direction_bool}){cards_to_pick}({message_send}?{opa}"
							Send(msg)
							client_game = False
							uno_played = False
							z = False
					if selection == True:
						countq += 1
						if countq % 20 == 0:
							x_for_reserve = receive(2)
						if mouse_cursor.colliderect(card_down_rec):
							if pygame.mouse.get_pressed()[0]:
								move = card_selected
								card_placed = list(move)
								card_down_check = list(card_down)
								if len(card_placed) > 2:
									card_placed_fix = card_placed[0] + card_placed[1]
									card_placed.remove(card_placed[1])
									card_placed[0] = card_placed_fix
								if len(card_down_check) > 2:
									card_down_check_fix = card_down_check[0] + card_down_check[1]
									card_down_check.remove(card_down_check[1])
									card_down_check[0] = card_down_check_fix
								if move in Who_Playing:
									if card_placed[0] == card_down_check[0] or card_placed[1] == card_down_check[1] or "W" in list(card_placed):
										card_down = move
										l.remove(move)
										if len(l) == 0:
											win = True
											msg = f"&{player_assigned}"
											Send(msg)
											client_game = False
											break
										if len(l) > 25:
											lost = True

										if "W" in list(move):
											if Color_Chosing(1) == False:
												return False

										if "X" in list(move):
											TURN(1)
											msg = f"{player_assigned}/'{"'".join(l)}|{card_down}*{turn}]Y[{direction_bool}){cards_to_pick}({message_send}"

										if "F" in list(move):
											if pa > 2:
												if direction_bool == "T":
													direction_bool ="F"
												elif direction_bool == "F":
													direction_bool = "T"
											else:
												TURN(1)
												msg = f"{player_assigned}/'{"'".join(l)}|{card_down}*{turn}]Y[{direction_bool}){cards_to_pick}({message_send}"

										if direction_bool == "T":
											direction_right = True
										elif direction_bool == "F":
											direction_right = False
	

										if not message_send:
											message_send = " "

										if "+" in list(move):
											cards_to_pick = int((list(move)[1]))
										else:
											cards_to_pick = 0
	
										TURN(1)
										msg = f"{player_assigned}/'{"'".join(l)}|{card_down}*{turn}]Y[{direction_bool}){cards_to_pick}({message_send}?{opa}"
										if msg:
											try:
												Send(msg)
												client_game = False
											except:
												x_for_reserve = "&0"
										z = False
										uno_played = False

				else:
					Create_Visual_Card(l)
					UNO(3)
					client_game = False
     
				#CHAT
				if text_box == True:
					try:
						screen.blit(background_image, (0,0))
						Create_Visual_Card(l)
						if turn == player_assigned:
							Cursor(cards_player_hitmox_cords)
						UNO(3)
						if pa > 2:
							pygame.draw.circle(screen, (255,255,0), (x_circle[rot_cir_pos] + 535, y_circle[rot_cir_pos] - 260), 4)
							if direction_right == True:
								rot_cir_pos += 3
							elif direction_right == False:
								rot_cir_pos -= 3
							if rot_cir_pos > 100:
								rot_cir_pos = 0
							if rot_cir_pos < 0:
								rot_cir_pos = 100
					except:
						pass
					pygame.draw.rect(text_cuadrant_surface, (128,128,128,160), (text_cuadrant_surface.get_rect()))
					screen.blit(text_cuadrant_surface, (720,30))
					pygame.draw.line(screen, (0,0,0), (720,245), (970, 245), 3)
					pygame.draw.line(screen, (0,0,0), (720,330), (970, 330), 3)
					pygame.draw.line(screen, (0,0,0), (720,245), (720, 330), 3)
					pygame.draw.line(screen, (0,0,0), (970,245), (970, 330), 3)
					screen.blit(font_chat.render(f"{line1}", True, (255,255,255)), (730,250))
					screen.blit(font_chat.render(f"{line2}", True, (255,255,255)), (730,270))
					screen.blit(font_chat.render(f"{line3}", True, (255,255,255)), (730,290))
					csbsy = 35
					i3 = ""
					csx = 0 
					for i in CHAT_SAVE:
						CHAT_SAVE.remove(i)
						i2 = str(i[:i.index(";") + 1])
						if i2 == "1;":
							i3 = "Player 1: "
						if i2 == "2;":
							i3 = "Player 2: "
						if i2 == "3;":
							i3 = "Player 3: "
						if i2 == "4;":
							i3 = "Player 4: "
						i = i.replace(f"{i2}", "")
						i = i3 + i
						csx += 1
						CHAT_PROCESS_SAVE.append(i)
					for i in range(len(CHAT_PROCESS_SAVE)):
						if csbsy + 20 > 225:
							CHAT_PROCESS_SAVE.remove(CHAT_PROCESS_SAVE[0])
						line4 = ""
						line5 = ""
						line6 = ""
						line7 = ""
						try:
							for u in list(CHAT_PROCESS_SAVE[i]):
								if font_chat.render(f"{line4 + "m"}", True, (255,255,255)).get_size()[0] < text_cuadrant_surface.get_size()[0] - 10:
									line4 += u
								elif font_chat.render(f"{line5 + "m"}", True, (255,255,255)).get_size()[0] < text_cuadrant_surface.get_size()[0] - 10:
									line5 += u
								elif font_chat.render(f"{line6 + "m"}", True, (255,255,255)).get_size()[0] < text_cuadrant_surface.get_size()[0] - 10:
									line6 += u
								elif font_chat.render(f"{line7 + "m"}", True, (255,255,255)).get_size()[0] < text_cuadrant_surface.get_size()[0] - 10:
									line7 += u
						except:
							print(Exception)

						if len(line4) > 0:
							screen.blit(font_chat.render(f"{line4}", True, (255,255,255)), (730, csbsy))
						if len(line5) > 0:
							csbsy += 20
							screen.blit(font_chat.render(f"{line5}", True, (255,255,255)), (730, csbsy))
						if len(line6) > 0:
							csbsy += 20
							screen.blit(font_chat.render(f"{line6}", True, (255,255,255)), (730, csbsy))
						if len(line7) > 0:
							csbsy += 20
							screen.blit(font_chat.render(f"{line7}", True, (255,255,255)), (730, csbsy))
						if len(line4) > 0:
							csbsy += 20	

				pygame.display.flip()
				time.sleep(0.05)
    
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_SPACE and text_box == True and font_chat.render(f"{line3 + "m"}", True, (255,255,255)).get_size()[0] < text_cuadrant_surface.get_size()[0] - 10:
							chat_message_to_send += " "
						if event.unicode.isalnum() and text_box == True and font_chat.render(f"{line3 + "m"}", True, (255,255,255)).get_size()[0] < text_cuadrant_surface.get_size()[0] - 10 and event.key != pygame.K_SEMICOLON:
							chat_message_to_send += event.unicode
						if event.key == pygame.K_RETURN and text_box == False:
							text_box = True
						elif event.key == pygame.K_RETURN and text_box == True and len(chat_message_to_send) == 0:
							text_box = False
						if event.key == pygame.K_RETURN and text_box == True and len(chat_message_to_send) > 0:
							send_chat = True
							CHAT_SAVE.append(f"{player_assigned};{chat_message_to_send}")
						if event.key == pygame.K_BACKSPACE:
							chat_message_to_send = chat_message_to_send[:-1]

						if event.key == pygame.K_ESCAPE:
							pause_check = Pause_Menu()
							if pause_check == False:
								quit_all()
								return
							if pause_check == "exit":
								return False

					if event.type == pygame.QUIT:
						client_game = False
						Host = False
						return False
		x = None
		print("x reseted, new x=",x)

				
			
#QUIT Threads 
def quit_all():
	global stop_all, conn1, conn2, conn3, conn4, Host, turn, player_assigned, Client
	print("[QUIT] Closing Threads")
	stop_all.set()
 
	try:
		if Client == True:
			msg = f"{player_assigned}/'{"'".join(l)}|{card_down}*{turn}]N[{direction_bool}){cards_to_pick_for_next_player}({message_send}"
			Send(msg)
			if player_assigned == turn:
				TURN(1)
				msg = f"{player_assigned}/'{"'".join(l)}|{card_down}*{turn}]N[{direction_bool}){cards_to_pick_for_next_player}({message_send}"
				Send(msg)
			Client = False
	except:
		pass
   
	try:
		print("[QUIT] Host Closing - Notifying Clients")
		disconnect_message = b"&0"
        
		for c in [conn1, conn2, conn3, conn4]:
			try:
				if c:
					c.sendall(disconnect_message)
					print(f"[QUIT] Sent disconnect message to client")
			except Exception as e:
				print(f"[QUIT] Error sending disconnect message: {e}")
    
		time.sleep(0.2)
	except:
		print("[QUIT ERROR]", Exception)

	# cerrar conexiones
	for c in [conn1, conn2, conn3, conn4]:
		try:
			if c:
				c.close()
		except:
			pass
	conn1 = conn2 = conn3 = conn4 = conn = None
	print("[QUIT] Server & Connections Closed")
   

#Main Loop
def Local_Game():
	global Main_Loop, Game, Host, screen, background_image
	global deck1, deck2, deck3, deck4, deck_bot
	global BOT, player_amount, player, turn, pa, pa10
	global mazoA, mazoB, mazoA_backUp, mazoB_backUp, y, y3
	global card_down, start_cart, move, direction_right
	global safe, safe_bot, Victory, Defeat, Reason
	global p1, p2, p3, p4, turn_go, opa, click2
	global Who_Playing, forceturn, rot_cir_pos
	global deck1_amount, deck2_amount, deck3_amount, deck4_amount, player_assigned
	if Main_Loop == True and Host == False:
		screen.blit(background_image, (0,0))
		pygame.display.flip()

		Start_Cards()
		Who_Playing = deck1

		if player_amount == 2:
			p1 = p2 = True
		if player_amount == 3:
			p1 = p2 = p3 = True
		if player_amount == 4:
			p1 = p2 = p3 = p4 = True

	#Start Actual Game Loop
		while Game == True:
			opa = pa
			if BOT != True:
				player_text = font_win_defeat.render(f"{player}", True, (255,255,255))
				screen.blit(player_text, (0,0))
				if BOT != True:
					player_assigned = turn
					if pa >= 1:
						deck1_amount = len(deck1)
					if pa >= 2:
						deck2_amount = len(deck2)
					if pa >= 3:
						deck3_amount = len(deck3)
					if pa >= 4:
						deck4_amount = len(deck4)
		#Game Over
		#Winning Sinlge Player Conditions 
			if BOT == True:
				if len(deck1) > 25:
					Defeat = True
					Reason = " Too Much Cards "
					Main_Loop = False
					break
				if len(deck1) <= 0:
					Victory = True
					Main_Loop = False
					break
				if len(deck_bot) > 25:
					Victory = True
					Main_Loop = False
					break
				if len(deck_bot) <= 0:
					Defeat = True
					Main_Loop = False
					Reason = " Your Opponent Won "
					break

		#Winning Local Multiplayer Conditions
			else:

				if len(deck1) <= 0:
					Victory = True
					Main_Loop = False
					Reason = ' Player 1 Wins '
					break
				if len(deck1) > 25:
					p1 = False
					card_images["P1IMG"] = pygame.image.load("Images/Player1D.png")
					if player_amount == 2:
						Victory = True
						Main_Loop = False
						Reason = ' Player 2 Wins \n Player 1 Had To Much Cards '
						break
				if player_amount >= 2:
					if len(deck2) <= 0:
						Victory = True
						Main_Loop = False
						Reason = ' Player 2 Wins '
						break
					if len(deck2) > 25:
						p2 = False
						card_images["P2IMG"] = pygame.image.load("Images/Player2D.png")
						if player_amount == 2:
							Victory = True
							Reason = " Player 1 Wins \n Player 2 Had To Much Cards "
							Main_Loop = False
							break
				if player_amount >= 3:
					if len(deck3) <= 0:
						Victory = True
						Main_Loop = False
						Reason = ' Player 3 Wins '
						break
					if len(deck3) > 25:
						p3 = False
						card_images["P3IMG"] = pygame.image.load("Images/Player3D.png")
				if player_amount >= 4:
					if len(deck4) <= 0:
						Victory = True
						Main_Loop = False
						Reason = ' Player 4 Wins '
						break
					if len(deck4) > 25:
						p4 = False
						card_images["P4IMG"] = pygame.image.load("Images/Player4D.png")

				pa10 = 4
				if p1 == False:
					pa10 -= 1
				if p2 == False:
					pa10 -= 1
				if p3 == False:
					pa10 -= 1
				if p4 == False:
					pa10 -= 1
				if player == 1 and p1 == False or player == 2 and p2 == False or player == 3 and p3 == False or player == 4 and p4 == False:
					TURN(1)
					player = turn
			
				if player_amount == 3:
					if p1 == False and p2 == False:
						Victory = True
						Reason = " Player 3 Wins \n Rest Players Have Too Much Cards "
						Game = False
						Main_Loop = False
					if p2 == False and p3 == False:
						Victory = True
						Reason = " Player 1 Wins \n Rest Players Have Too Much Cards "
						Game = False
						Main_Loop = False
					if p1 == False and p3 == False:
						Victory = True
						Reason = " Player 2 Wins \n Rest Players Have Too Much Cards "
						Game = False
						Main_Loop = False
				if player_amount == 4:
					if p1 == False and p2 == False and p3 == False:
						Victory = True
						Reason = " Player 4 Wins \n Other Players Have Too Much Cards "
						Game = False
						Main_Loop = False
					if p2 == False and p3 == False and p4 == False:
						Victory = True
						Reason = " Player 1 Wins \n Other Players Have Too Much Cards "
						Game = False
						Main_Loop = False
					if p3 == False and p4 == False and p1 == False:
						Victory = True
						Reason = " Player 2 Wins \n Other Players Have Too Much Cards "
						Game = False
						Main_Loop = False
					if p1 == False and p2 == False and p4 == False:
						Victory = True
						Reason = " Player 3 Wins \n Other Players Have Too Much Cards "
						Game = False
						Main_Loop = False
			
		#Cursor Functions & Draw Cards
			#if BOT != True:
			Create_Visual_Card(Who_Playing)
			if player_amount > 2:
				pygame.draw.circle(screen, (255,255,255), (x_circle[rot_cir_pos] + 535, y_circle[rot_cir_pos] - 260), 4)
				if direction_right == True:
					rot_cir_pos += 3
				elif direction_right == False:
					rot_cir_pos -= 3
				if rot_cir_pos > 100:
					rot_cir_pos = 0
				if rot_cir_pos < 0:
					rot_cir_pos = 100
			Cursor(cards_player_hitmox_cords)
			pygame.display.flip()
			time.sleep(0.05)
		#Reshufell Deck
			if y < 8:
				mazoA = mazoA_backUp.copy()
				mazoB = mazoB_backUp.copy()
				y = y3
				print("\n Deck Has Been Reshufelled \n ")

		#Fixing Special Cards
			down_card_parts = list(card_down)
			if len(down_card_parts) > 2:
				down_card_part_fix = down_card_parts[0] + down_card_parts[1]
				down_card_parts.remove(down_card_parts[1])
				down_card_parts[0] = down_card_part_fix
				card_down = "".join(down_card_parts)

		#Special Cards
			player = turn
			if BOT == True:
				if turn > 2:
					turn = 1
				elif turn < 1:
					turn = 2

			if forceturn != 0:
				turn = forceturn
				player = turn
				forceturn = 0

	#Player 
			if BOT == True:
				if player == 1:
					if Control_Player(deck1) == False:
						return False
				if player == 2:
					time.sleep(0.5)
					BOT_IA()
			else:
				if turn == 1:
					if Control_Player(deck1) == False:
						return False
					Who_Playing = deck1

				elif turn == 2:
					if Control_Player(deck2) == False:
						return False
					Who_Playing = deck2

				elif turn == 3:
					if Control_Player(deck3) == False:
						return False
					Who_Playing = deck3

				elif turn == 4:
					if Control_Player(deck4) == False:
						return False
					Who_Playing = deck4
				
	#Players UNO
			if BOT == False:
				if len(deck1) == 1 and safe == False and turn == 1:
					uno_checker = UNO(1)
					if uno_checker == True:
						safe = True
					if uno_checker == False:
						safe = True
						Pick_Card(deck1)
						Pick_Card(deck1)
					if uno_checker == "exit":
						return False

				if len(deck2) == 1 and safe == False and turn == 2:
					uno_checker = UNO(1)
					if uno_checker == True:
						safe = True
					if uno_checker == False:
						safe = True
						Pick_Card(deck2)
						Pick_Card(deck2)
					if uno_checker == "exit":
						return False

				if len(deck3) == 1 and safe == False and turn == 3:
					uno_checker = UNO(1)
					if uno_checker == True:
						safe = True
					if uno_checker == False:
						safe = True
						Pick_Card(deck3)
						Pick_Card(deck3)
					if uno_checker == "exit":
						return False
				
				if len(deck4) == 1 and safe == False and turn == 4:
					uno_checker = UNO(1)
					if uno_checker == True:
						safe = True
					if uno_checker == False:
						safe = True
						Pick_Card(deck4)
						Pick_Card(deck4)
					if uno_checker == "exit":
						return False
				
			if BOT == True:
				if len(deck1) == 1 and safe == False:
					uno_checker = UNO(1)
					if uno_checker == True:
						safe = True
					if uno_checker == False:
						safe = True
						Pick_Card(deck1)
						Pick_Card(deck1)
					if uno_checker == "exit":
						return False
					
				if len(deck_bot) == 1 and safe_bot == False:
					uno_checker = UNO(2)
					if uno_checker == True:
						safe_bot = True
					if uno_checker == False:
						safe_bot = True
						if direction_right == True:
							turn += 1
						elif direction_right == False:
							turn -= 1
						else:
							print("Error 405 Direction")
						if turn > 2:
							turn = 1
						if turn < 1:
							turn = 2
						player = turn
						Pick_Card(deck_bot)
						Pick_Card(deck_bot)

		#Pygame
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Main_Loop = False
					Game = False
					return False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pause_option = Pause_Menu()
						if pause_option == "exit":
							return False
						if pause_option == False:
							return
				if event.type == pygame.MOUSEBUTTONUP:
					click2 = True
			screen.blit(background_image, (0,0))

	if Victory == True:
		color = random.randint(5,(len(title_colors) - 5))
	while Victory  == True:
		time.sleep(0.1)
		color += 1
		if color > len(title_colors) - 1:
			color = 0
		Create_Visual_Card(Who_Playing)
		victort_text = font_win_defeat.render("VICTORY", True, (title_colors[color]))
		screen.blit(victort_text, ((width // 2) - 98 -78, 150))
		if Reason:
			reason_defeat = font_reason_win_defeat.render(f"{Reason}", False, (title_colors[color]))
			rec_to_center_reason_defeat = reason_defeat.get_rect()
			rec_to_center_reason_defeat.center = (width // 2, 275)
			screen.blit(reason_defeat, rec_to_center_reason_defeat)

		play_again_rect = pygame.draw.rect(screen, (title_colors[color]), (width/2 - 125, 325, 250,80),10, 11)
		main_menu_rect = pygame.draw.rect(screen, (title_colors[color]), (width/2 - 125, 425, 250,80),10, 11)
		quit_rect = pygame.draw.rect(screen, (title_colors[color]), (width/2 - 125, 525, 250,80),10, 11)
  
		screen.blit(font_button4.render("Play Again", True, (title_colors[color])), (width/2 - font_button4.render("Play Again", True, (255,255,255)).get_size()[0]/2, 330))
		screen.blit(font_button4.render("Main Menu", True, (title_colors[color])), (width/2 - font_button4.render("Main Menu", True, (255,255,255)).get_size()[0]/2, 430))
		screen.blit(font_button2.render("QUIT", True, (title_colors[color])), (width/2 - font_button2.render("QUIT", True, (255,255,255)).get_size()[0]/2, 525))
	
		mouse_pos = pygame.mouse.get_pos()
		mouse_cursor = pygame.draw.rect(alpha_surface, (0,0,0,0), (mouse_pos[0],mouse_pos[1], 10,10))
	
		if pygame.mouse.get_pressed()[0]:
			if mouse_cursor.colliderect(play_again_rect):
				return "play_again"
			if mouse_cursor.colliderect(main_menu_rect):
				return
			if mouse_cursor.colliderect(quit_rect):
				return False
  
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Victory = False
				return False

	if Defeat == True:
		color = random.randint(5,(len(title_colors) - 5))
	while Defeat == True:
		time.sleep(0.1)
		color += 1
		if color > len(title_colors) - 1:
			color = 0
		Create_Visual_Card(deck1)
		defeat_text = font_win_defeat.render("DEFEAT", True, (title_colors[color]))
		screen.blit(defeat_text, (340, 150))
		if Reason:
			reason_defeat = font_reason_win_defeat.render(f"{Reason}", False, (title_colors[color]))
			rec_to_center_reason_defeat = reason_defeat.get_rect()
			rec_to_center_reason_defeat.center = (width // 2, 275)
			screen.blit(reason_defeat, rec_to_center_reason_defeat)
   
		play_again_rect = pygame.draw.rect(screen, (title_colors[color]), (width/2 - 125, 325, 250,80),10, 11)
		main_menu_rect = pygame.draw.rect(screen, (title_colors[color]), (width/2 - 125, 425, 250,80),10, 11)
		quit_rect = pygame.draw.rect(screen, (title_colors[color]), (width/2 - 125, 525, 250,80),10, 11)
  
		screen.blit(font_button4.render("Play Again", True, (title_colors[color])), (width/2 - font_button4.render("Play Again", True, (255,255,255)).get_size()[0]/2, 330))
		screen.blit(font_button4.render("Main Menu", True, (title_colors[color])), (width/2 - font_button4.render("Main Menu", True, (255,255,255)).get_size()[0]/2, 430))
		screen.blit(font_button2.render("QUIT", True, (title_colors[color])), (width/2 - font_button2.render("QUIT", True, (255,255,255)).get_size()[0]/2, 525))
	
		mouse_pos = pygame.mouse.get_pos()
		mouse_cursor = pygame.draw.rect(alpha_surface, (0,0,0,0), (mouse_pos[0],mouse_pos[1], 10,10))
	
		if pygame.mouse.get_pressed()[0]:
			if mouse_cursor.colliderect(play_again_rect):
				return "play_again"
			if mouse_cursor.colliderect(main_menu_rect):
				return
			if mouse_cursor.colliderect(quit_rect):
				return False
   
		pygame.display.flip()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Defeat = False
				return False
    
	return True
    
def main():
	global BOT_checker, BOT, player_amount_checker, player_amount, y, y_checker, y3
	global mazoA, mazoB, pa
	run = True
	menu_check = "Duck"
	print("[Start]")
	while run == True:
		Start_Variables()
		player_amount = player_amount_checker
		y = y_checker
		y3 = y_checker
		pa = player_amount_checker

		if menu_check != "LGF":
			menu_check = Main_Menu()

		if menu_check == "LG" or menu_check == "LGF":#Local Game
			if BOT_checker == False:
				BOT = False
			if BOT_checker == True:
				BOT = True
			menu_check = "Duck"
			local_check = Local_Game()
			if local_check == False:
				run = False
			if local_check == "play_again":
				menu_check = "LGF"
    
		elif menu_check == "OG":#Online Game
			online_check = Online_Game()
			if online_check == False:
				run = False
		elif menu_check == False:
			run = False
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
   
main()

  
quit_all()
pygame.quit() 
sys.exit() 
