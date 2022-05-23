#!/usr/bin/python
   2 import os
   3 import platform
   4 
   5 turn = 1 # 1 - Player 1 | 2 - Player 2
   6 clean = ('clear','cls')[platform.system() == 'Windows']
   7 p_char = 'X'
   8 c_char = 'O'
   9 table = ['1','2','3',
  10          '4','5','6',
  11          '7','8','9']
  12 
  13 def winner():
  14     global table
  15     for i in ['X','O']:
  16         # horizontal
  17         if table[0] == table[1] == table[2] == i: return i
  18         if table[3] == table[4] == table[5] == i: return i
  19         if table[6] == table[7] == table[8] == i: return i
  20         # vertical
  21         if table[0] == table[3] == table[6] == i: return i
  22         if table[1] == table[4] == table[7] == i: return i
  23         if table[2] == table[5] == table[8] == i: return i
  24         # diagonal
  25         if table[0] == table[4] == table[8] == i: return i
  26         if table[6] == table[4] == table[2] == i: return i
  27     return None
  28 
  29 def view():
  30     global table
  31     
  32     print " %s | %s | %s " % (table[0],table[1],table[2])
  33     print "---+---+---"
  34     print " %s | %s | %s " % (table[3],table[4],table[5])
  35     print "---+---+---"
  36     print " %s | %s | %s " % (table[6],table[7],table[8])
  37 
  38 def move(pos):
  39     global turn
  40     global table
  41     
  42     if not pos: return None
  43     if not 0 < pos < 10: return False
  44     if table[pos-1] in ['X','O']: return False
  45 
  46     table[pos-1] = ('O','X')[turn == 1]
  47     turn = (1,2)[turn == 1]
  48 
  49 while True:
  50     os.system(clean)
  51     view()
  52 
  53     print "Player %s: " % turn,
  54     movement = int(raw_input())
  55     move(movement)
  56 
  57     win = winner()
  58     if not win: continue
  59     if win == p_char:
  60         print "Player 1 Wins!"
  61         raw_input()
  62         exit()
  63     if win == c_char:
  64         print "Player 2 Wins!"
  65         raw_input()
  66         exit()