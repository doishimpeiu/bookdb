#! /usr/bin/env python3
# coding: UTF-8
import cgi
import csv
import sqlite3

form = cgi.FieldStorage()
param_str1 = form.getvalue('param1','')


db_path = "bookdb.db"			# データベースファイル名を指定

con = sqlite3.connect(db_path)	# データベースに接続
con.text_factory = str
con.row_factory = sqlite3.Row	# 属性名で値を取り出せるようにする
cur = con.cursor()					# カーソルを取得

print("Content-type: text/html\n")
print("<html>")
print("  <head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/></head>")

try:
	cur.execute("SELECT ID, TITLE, AUTHOR, PUBLISHER, PRICE, ISBN from BOOKLIST where TITLE like ? or AUTHOR like ?", ('%'+param_str1+'%', '%'+param_str1+'%',))
	rows = cur.fetchall()			# 検索結果をリストとして取得
	if not rows:
		print("そんな本はありません")
	else:
		for row in rows:		# 検索を1つずつ処理
			print("ID = %d" % int(row['ID']))
			print("<br>")
			print("タイトル = %s" % str(row['TITLE']))
			print("<br>")
			print("筆者 = %s" % str(row['AUTHOR']))
			print("<br>")
			print("出版社 = %s" % str(row['PUBLISHER']))
			print("<br>")
			print("値段 = %s" % str(row['PRICE']))
			print("<br>")
			print("ISBN = %s\n" % str(row['ISBN']))
			print("<br>")
			print("<br>")
			
except sqlite3.Error as e:			# エラー処理
	print("</body>Error occurred:</body>", e.args[0])

con.commit()
con.close()

print("<a href=\"../finalReport.html\">戻る")
print("</html>")
