#coding=utf8
from board import Board
from nbaApi import NbaApi
import time
import locale
locale.setlocale(locale.LC_ALL, '')
api = NbaApi()
fresh_time = 10  #10s刷新一下

games = api.getGames()
last_updated = time.time()
status = "menu"

board = Board()
menus = []
board.draw_menu(games)
while(True):
    key = board.screen.getch()
    if key == ord('q'):
        board.exit()
        break
    if key == ord('s'):
        status = "menu"
        games = api.getGames()
        board.draw_menu(games)
    elif status == 'menu':
        t = time.time()
        if t - last_updated > fresh_time or key == ord("r"):
            games = api.getGames()
            board.draw_menu(games)
            last_updated = time.time()
        for idx in range(1,len(games)+1):
            if key == ord(str(idx)):
                status = 'live'
                msgs = api.getMessage(games[idx-1]['pb_url'])
                board.init_match(games[idx-1])
                board.update(msgs)
                last_updated = time.time()
                break
    elif status == 'live':
        t = time.time()
        if t - last_updated > fresh_time or key == ord("r"):
            msgs = api.getMessage(games[idx-1]['pb_url'])
            board.init_match(games[idx-1])
            board.update(msgs)
            last_updated = time.time()
