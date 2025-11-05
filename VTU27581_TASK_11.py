import tkinter as tk1

from tkinter import message box

det sumbit():

emp-id = entry-id.get()

name=entry-name.get()

dept=entry-dept.get()

contact= entry-contact get()

messagebox showinof (Employee Details", f" ID:{emp-id}

\n mame: {name} in department: {dept}\n contact:{contact}")

def reset():

entry-id delete (o, tk-END)

entry-name. delete (0,4K-END)

entry-dept. delete (0,1K,END)

entry-contact. delete (O+tk. END)

root. tr.TK()

root .title ("Employee registration form")

root.geometry ("400×300")

root.configure (bg= "lightblue")

tk.lablel (root, text = "Employee id:") раск()

entry-id = tk. Entry (root), entry-id.pack()

tk.label (root, text = "Name:") pack()

entry.name=tk. entry(root),entry. name.pack()

tk.label (root, text = "Department:") pack()

entry.dept=tk-entry (root); entry.dept-pack()

tk. label (root, text = "contact number: ") pack()

entry-contact=tk. Entry (root); entry-contact-park()

tk Button (root, text = "submit",
command = sumbit). pack (pady=5)

tk. Button (root, text = "Reset", command=reset)

Pack() root. main loop()
