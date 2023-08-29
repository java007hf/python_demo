import easygui as ui
import sys

ui.msgbox("hello", image = "a.gif")
yn = ui.ynbox("msg", "title", choices=("a", "b"))
print(yn)

ui.diropenbox(default="*")
ui.fileopenbox(default="*.py", filetypes=["*.txt", "*.py"])


file = open("p31.py")
ui.textbox("content", "title", text=file.read())

try:
	int("adb")
except:
	ui.exceptionbox()


while True:
	choice = ui.choicebox("select a item", "what do you like?", ["game", "drive", "eat"])
	print(choice)

	ui.msgbox("your select is " + str(choice))

	isContinue = ui.ccbox("do you want play again?", "select")
	print(isContinue)

	if isContinue:
		pass
	else:
		break

#ui.egdemo()