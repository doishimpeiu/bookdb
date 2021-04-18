#! /usr/bin/env python3
# coding: UTF-8
import cgi
import csv
import sqlite3
form = cgi.FieldStorage() 
param_str2 = form.getvalue('param2','')
param_str3 = form.getvalue('param3','')
param_str4 = form.getvalue('param4','')
param_str5 = form.getvalue('param5','')
param_str6 = form.getvalue('param6','')
param_str7 = form.getvalue('param7','')

db_path = "cgi-bin/bookdb.db"			# データベースファイル名を指定

con = sqlite3.connect(db_path)	# データベースに接続
con.text_factory = str
con.row_factory = sqlite3.Row	# 属性名で値を取り出せるようにする
cur = con.cursor()					# カーソルを取得

print("Content-type: text/html\n")
print("<html>")
print("  <head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/></head>")

#with open('./BookList.csv', 'r') as file: # CSV ファイルをオープン 
  #reader = csv.reader(file)
try:
    cur.execute('insert into BOOKLIST values (?,?,?,?,?,?);', (param_str2,param_str4,param_str3,param_str5,param_str6,param_str7))
    rows = cur.fetchall() # 検索結果をリストとして取得
except sqlite3.Error as e: # エラー処理 
    print("Error occurred:", e.args[0])

print(param_str3)
print("が追加されました")

con.commit() 
con.close()

print("</html>")