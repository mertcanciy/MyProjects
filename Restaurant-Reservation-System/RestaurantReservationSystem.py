from tkinter import *
from tkinter import ttk
import dbm
import pickle


class Restaurant:
    def __init__(self, name, table_num, reservation_info):
        self.name = name
        self.table_num = table_num
        self.reservation_info = reservation_info  # dict of rezerved tables. key = table name, value = [customer name, customer number]
        self.dict_table_object = {}  # key = table name, value = Table object.
#calling table objects in the restaurant class, putting tables
    def create_table_object(self):
        self.dict_table_object.clear()
        for i in range(0, self.table_num):
            if str(
                    i + 1) not in self.reservation_info.keys():  # if the table is available, we will create table object with default values.
                self.dict_table_object[str(i + 1)] = Table(str(i + 1))
            else:
                self.dict_table_object[str(i + 1)] = Table(str(i + 1), "N", self.reservation_info[str(i + 1)][0],
                                                           self.reservation_info[str(i + 1)][1])
            self.dict_table_object[str(i + 1)].create_table_widget(
                app.frame_table_list[int(i / 3)])  # to put tables in frame regularly.

    def update_reservation_table(self, table_name, process):
        if process == "add":
            self.reservation_info[table_name] = [self.dict_table_object[table_name].customer_name,
                                             self.dict_table_object[table_name].customer_number]
        else:  # when process is delete.
            del self.reservation_info[table_name]


class Table:
    def __init__(self, name, is_available="Y", customer_name="", customer_number=""):
        self.name = name
        self.is_available = is_available
        self.customer_name = customer_name
        self.customer_number = customer_number
#is_available is Y as default, by changing its value, we decide its color
    def create_table_widget(self, place):
        if self.is_available == "N":
            color = "red"
        else:
            color = "green"
        self.button_table = Button(place, text=self.name, bg=color, command=self.showInfos, width=15, height=4,
                                   relief=GROOVE)
        self.button_table.pack(side=TOP, pady=5)

    def showInfos(self):  # to fill GUI parts.
        app.entry_customer_name.configure(state="normal")
        app.entry_customer_number.configure(state="normal")
        app.label_table_name["text"] = self.name
        app.entry_customer_name.delete(0, END)
        app.entry_customer_name.insert(END, self.customer_name)
        app.entry_customer_number.delete(0, END)
        app.entry_customer_number.insert(END, self.customer_number)
#updates tables' infos
    def update_table_infos(self, available, customer_name, customer_num,
                           color_button):  # to save/update or delete reservation
        self.is_available = available
        self.customer_name = customer_name
        self.customer_number = customer_num
        self.button_table["bg"] = color_button


class GUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.frame_table_list = []  # to put table object in frames.
        self.selected_res = None  # we will use to select restaurant object from Restaurant_obj dictionary.
        self.unitUI()
#creating frames in this function
    def create_frames(self):
        # main frame
        self.frame_restaurant = Frame(root, bg="dark gray")
        self.frame_restaurant.pack(fill=X, padx=40, pady=5)
        self.frame_box_restaurant = Frame(root, bg="dark gray")
        self.frame_box_restaurant.pack(fill=X, padx=40, pady=5)
        self.frame_infos = Frame(root, bg="dark gray")
        self.frame_infos.pack(fill=X)

        # frames in this frame.
        self.frame_table_name = Frame(self.frame_infos, width=150, bg="dark gray")
        self.frame_table_name.pack(side=LEFT, padx=40)

        self.frame_customer_name = Frame(self.frame_infos, width=150, bg="dark gray")
        self.frame_customer_name.pack(side=LEFT, padx=15)

        self.frame_customer_number = Frame(self.frame_infos, width=150, bg="dark gray")
        self.frame_customer_number.pack(side=LEFT, padx=15)

        self.frame_buttons = Frame(self.frame_infos, width=150, bg="dark gray")
        self.frame_buttons.pack(side=LEFT, padx=15)

        self.frame_process_info = Frame(self.frame_infos, width=150, bg="dark gray")
        self.frame_process_info.pack(side=LEFT)

        # another main frame
        self.frame_tables = Frame(root, width=1100, height=250, highlightbackground="black", highlightcolor="black",
                                  highlightthickness=2, bg="dark gray")
        self.frame_tables.pack(fill=X, pady=10, padx=40)
        # frames in this main frame
        self.frame_tab1 = Frame(self.frame_tables, width=125, height=250, bg="dark gray")
        self.frame_tab1.pack(side=LEFT, padx=10, fill=Y)
        self.frame_table_list.append(self.frame_tab1)

        self.frame_tab2 = Frame(self.frame_tables, width=125, height=250, bg="dark gray")
        self.frame_tab2.pack(side=LEFT, padx=10, fill=Y)
        self.frame_table_list.append(self.frame_tab2)

        self.frame_tab3 = Frame(self.frame_tables, width=125, height=250, bg="dark gray")
        self.frame_tab3.pack(side=LEFT, padx=10, fill=Y)
        self.frame_table_list.append(self.frame_tab3)

        self.frame_tab4 = Frame(self.frame_tables, width=125, height=250, bg="dark gray")
        self.frame_tab4.pack(side=LEFT, padx=10, fill=Y)
        self.frame_table_list.append(self.frame_tab4)

        self.frame_tab5 = Frame(self.frame_tables, width=125, height=250, bg="dark gray")
        self.frame_tab5.pack(side=LEFT, padx=10, fill=Y)
        self.frame_table_list.append(self.frame_tab5)

        self.frame_tab6 = Frame(self.frame_tables, width=125, height=250, bg="dark gray")
        self.frame_tab6.pack(side=LEFT, padx=10, fill=Y)
        self.frame_table_list.append(self.frame_tab6)

        self.frame_tab7 = Frame(self.frame_tables, width=125, height=250, bg="dark gray")
        self.frame_tab7.pack(side=LEFT, padx=10, fill=Y)
        self.frame_table_list.append(self.frame_tab7)

        self.frame_tab8 = Frame(self.frame_tables, width=125, height=250, bg="dark gray")
        self.frame_tab8.pack(side=LEFT, padx=10, fill=Y)
        self.frame_table_list.append(self.frame_tab8)

    def fill_frames(self):
        self.label_res_name = Label(self.frame_restaurant, text="Restaurant Name:", bg="dark gray").pack(side=LEFT)
        self.entry_res_name = Entry(self.frame_restaurant)
        self.entry_res_name.pack(side=LEFT, padx=20)
        self.label_num_table = Label(self.frame_restaurant, text="Number of Tables:", bg="dark gray").pack(side=LEFT)
        self.entry_num_table = Entry(self.frame_restaurant)
        self.entry_num_table.pack(side=LEFT, padx=20)
        self.button_create_res = Button(self.frame_restaurant, text="Create New Restaurant", bg="white",
                                        command=self.create_restaurant)
        self.button_create_res.pack(side=LEFT, padx=20)

        self.label_res_choice = Label(self.frame_box_restaurant, text="Restaurant:", bg="dark gray").pack(side=LEFT)
        self.box_res = ttk.Combobox(self.frame_box_restaurant, state="readonly")
        self.box_res.pack(side=LEFT, padx=20)
        self.box_res.set("Not Selected")
        self.box_res.bind("<<ComboboxSelected>>", self.bind_combobox)
        self.button_del_res = Button(self.frame_box_restaurant, text="Delete", bg="white", command=self.delete_restaurant)
        self.button_del_res.pack(side=LEFT)
        self.button_del_res_sure = Button(self.frame_box_restaurant, text="Click Again to Delete", bg="white",
                                          command=self.sure_delete_restaurant)

        self.label_table = Label(self.frame_table_name, text="Table:  ", bg="dark gray").pack(side=LEFT)
        self.label_table_name = Label(self.frame_table_name, text="[Not Selected]", bg="dark gray")
        self.label_table_name.pack(side=LEFT)

        self.label_customer_name = Label(self.frame_customer_name, text="Customer Name: ", bg="dark gray").pack(
            side=LEFT)
        self.entry_customer_name = Entry(self.frame_customer_name, state="disabled")
        self.entry_customer_name.pack(side=LEFT)

        self.label_customer_number = Label(self.frame_customer_number, text="Customer Number: ", bg="dark gray").pack(
            side=LEFT)
        self.entry_customer_number = Entry(self.frame_customer_number, state="disabled")
        self.entry_customer_number.pack(side=LEFT)

        self.button_save = Button(self.frame_buttons, text="Save/Update Reservation", bg="white", fg="black",
                                  command=self.save_update_reservation)
        self.button_save.pack(padx=5, side=LEFT)

        self.button_delete = Button(self.frame_buttons, text="Delete Reservation", bg="white", fg="black",
                                    command=self.delete_reservation)
        self.button_delete.pack(padx=5, side=LEFT)
#warning labels' functions are here
    def change_warnText_reservation(self, text, color):
        self.label_info_reservation = Label(self.frame_process_info, text=text, bg=color, fg="white", font=("arial", 12))
        self.label_info_reservation.pack(side=LEFT)
        self.label_info_reservation.after(2000, self.label_info_reservation.destroy)

    def change_warnText_restaurant(self, text, color):
        self.label_info_res = Label(self.frame_restaurant, text=text, bg=color, font=("arial", 12), fg="white")
        self.label_info_res.pack(side=LEFT)
        self.label_info_res.after(2000, self.label_info_res.destroy)

    def change_warnText_del_restaurant(self, text, color):
        self.label_combobox_select = Label(self.frame_box_restaurant, fg="white", font=("arial", 12), bg=color,
                                           text=text)
        self.label_combobox_select.pack(side=LEFT, padx=10)
        self.label_combobox_select.after(2000, self.label_combobox_select.destroy)
#according to choosing the table, it determines if they can be updated
    def save_update_reservation(self):
        if self.label_table_name["text"] == "[Not Selected]":
            self.change_warnText_reservation("First Select a Table", "red")

        elif len(self.entry_customer_number.get()) == 0 or len(self.entry_customer_name.get()) == 0:
            self.change_warnText_reservation("Incomplete Info", "red")
        else:
            try:
                self.number_customer = int(self.entry_customer_number.get())
            except:
                self.change_warnText_reservation("Phone Num. Can Be Digits Only", "red")
                return
            Restaurant_obj[self.selected_res].dict_table_object[self.label_table_name["text"]].update_table_infos("N",
                                                                                                                  self.entry_customer_name.get(),
                                                                                                                  self.entry_customer_number.get(),
                                                                                                                  "red")
            Restaurant_obj[self.selected_res].update_reservation_table(self.label_table_name["text"], "add")
            self.change_warnText_reservation("Saved", "green")
            update_database()
#deleting reservations
    def delete_reservation(self):
        if self.label_table_name["text"] == "[Not Selected]":
            self.change_warnText_reservation("First Select a Table", "red")

        else:
            if self.label_table_name["text"] in Restaurant_obj[self.selected_res].reservation_info:
                Restaurant_obj[self.selected_res].dict_table_object[self.label_table_name["text"]].update_table_infos(
                    "Y", "", "", "green")
                Restaurant_obj[self.selected_res].update_reservation_table(self.label_table_name["text"], "del")
                self.entry_customer_number.delete(0, END)
                self.entry_customer_name.delete(0, END)
                self.change_warnText_reservation("Rezervation Deleted", "red")
                update_database()
            else:
                self.change_warnText_reservation("Table is not Reserved", "red")
#creating a new restaurant
    def create_restaurant(self):
        if len(self.entry_res_name.get()) == 0 or len(self.entry_num_table.get()) == 0:
            self.change_warnText_restaurant("Entries Cannot Be Empty", "red")
        else:
            try:
                num_table = int(self.entry_num_table.get())
                if not (6 <= num_table <= 24):
                    self.change_warnText_restaurant("Num. Of Tables May Be Between 6 and 24.", "red")
                else:
                    Restaurant_obj[self.entry_res_name.get()] = Restaurant(self.entry_res_name.get(), num_table, {})
                    self.box_res["values"] = [res for res in Restaurant_obj.keys()]
                    self.change_warnText_restaurant("Restaurant Created", "green")
                    self.entry_res_name.delete(0, END)
                    self.entry_num_table.delete(0, END)
                    update_database()
            except:
                self.change_warnText_restaurant("Numbers for Tables Can Be Digits Only", "red")
#deleting restaurant
    def delete_restaurant(self):
        self.button_del_res.pack_forget()
        self.button_del_res_sure.pack(side=LEFT)

    def sure_delete_restaurant(self):
        if self.box_res.get() == "Not Selected":
            self.button_del_res_sure.pack_forget()
            self.button_del_res.pack(side=LEFT)
            self.change_warnText_del_restaurant("Select a Restaurant", "red")
        else:
            self.button_del_res_sure.pack_forget()
            self.button_del_res.pack(side=LEFT)
            del Restaurant_obj[self.box_res.get()]
            self.box_res["values"] = [res for res in Restaurant_obj.keys()]
            self.box_res.set("Not Selected")
            self.change_warnText_del_restaurant("Deleted", "red")
            update_database()
            for frame in self.frame_tables.winfo_children():
                for table in frame.winfo_children():
                    table.destroy()
            self.label_table_name["text"] = "[Not Selected]"
            self.entry_customer_number.delete(0, END)
            self.entry_customer_name.delete(0, END)
            self.entry_customer_name["state"] = "disabled"
            self.entry_customer_number["state"] = "disabled"

    # control combobox binds.
    def bind_combobox(self, event):
        self.selected_res = self.box_res.get()
        for frame in self.frame_tables.winfo_children():
            for table in frame.winfo_children():
                table.destroy()
        self.label_table_name["text"] = "[Not Selected]"
        self.entry_customer_name.delete(0, END)
        self.entry_customer_number.delete(0, END)
        self.entry_customer_name.configure(state="disabled")
        self.entry_customer_number.configure(state="disabled")
        Restaurant_obj[self.box_res.get()].create_table_object()  # to fill frame with restaurant's tables.
#calling first attributes of project
    def unitUI(self):
        self.label_title = Label(root, text="Restaurant Reservation System", bg="blue", fg="white",
                                 font=("arial", 20, "italic"))
        self.label_title.pack(pady=5, fill=X)
        self.create_frames()
        self.fill_frames()

#database part
def update_database():
    db = dbm.open("app.db", "n")
    # key = restaurant name, value = [total table number, {rezerved table_num: [customer name, customer number]}]
    for res in Restaurant_obj:
        list_values = [Restaurant_obj[res].table_num, Restaurant_obj[res].reservation_info]
        key = pickle.dumps(res)
        db[key] = pickle.dumps(list_values)
    db.close()

#main function that starts
def main():
    global Restaurant_obj
    global app
    global root
    root = Tk()
    root.title("Restaurant Reservation System")
    root.configure(background="dark gray")
    root.geometry("1300x450")
    app = GUI(root)
    Restaurant_obj = {}
    db = dbm.open("app.db", "c")
    # key = restaurant name, value = [total table number, {rezerved table_num: [customer name, customer number]}]
    if len(db.keys()) != 0:
        for key in db.keys():
            values = pickle.loads(db[key])
            Restaurant_obj[pickle.loads(key)] = Restaurant(key, values[0], values[1])
        app.box_res["values"] = [res for res in Restaurant_obj.keys()]
    db.close()
    root.mainloop()


main()
