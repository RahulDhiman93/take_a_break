import webbrowser
import time
total_break=raw_input("Enter Number of times you need break in a day : ")
start=0
while start<total_break:
		time.sleep(2*60*60)
		webbrowser.open("https://github.com/RahulDhiman93")
		start+=1
