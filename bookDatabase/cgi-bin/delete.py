#! /usr/bin/env python3
# coding: UTF-8
import cgi
import csv
import sqlite3

form = cgi.FieldStorage()
param_str8 = form.getvalue('param8','')


db_path = "cgi-bin/bookdb.db"			# データベースファイル名を指定

con = sqlite3.connect(db_path)	# データベースに接続
con.text_factory = str
con.row_factory = sqlite3.Row	# 属性名で値を取り出せるようにする
cur = con.cursor()					# カーソルを取得

print("Content-type: text/html\n")
print("<html>")
print("  <head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/></head>")

try:
    cur.execute("delete from BOOKLIST where ID = ? ",(param_str8,))
    rows = cur.fetchall() # 検索結果をリストとして取得

except sqlite3.Error as e: # エラー処理 
    print("Error occurred:", e.args[0])

print(param_str8)
print("が削除されました")

con.commit() 
con.close()

print("</html>")
