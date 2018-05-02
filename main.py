from tkinter import *
from tkinter import ttk
from bittrex.bittrex import Bittrex
from firebase import firebase


def login(*args):
	try:
		# value = apikey.get()
		bittrex = Bittrex(apikey.get(), apisecret.get())
		print(bittrex.get_balances())
		# meters.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
	except ValueError:
		pass

if __name__ == '__main__':

	authentication = firebase.FirebaseAuthentication()
	bittrex = None

	root = Tk()
	root.title("Trade Watcher")

	mainframe = ttk.Frame(root, padding="3 3 12 12")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	mainframe.columnconfigure(0, weight=1)
	mainframe.rowconfigure(0, weight=1)

	apikey = StringVar()
	apisecret = StringVar()
	meters = StringVar()

	apikey_entry = ttk.Entry(mainframe, width=7, textvariable=apikey)
	apikey_entry.grid(column=2, row=1, sticky=(W, E))
	apisecret_entry = ttk.Entry(mainframe, width=7, textvariable=apisecret)
	apisecret_entry.grid(column=3, row=1, sticky=(W, E))

	ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
	ttk.Button(mainframe, text="Calculate", command=login).grid(column=3, row=3, sticky=W)

	# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
	# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
	# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

	for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

	apikey_entry.focus()
	root.bind('<Return>', login)

	root.mainloop()