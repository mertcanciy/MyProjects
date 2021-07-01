from tkinter import *
import re
from bs4 import BeautifulSoup
import requests
import random


class Course:
    def __init__(self, course_code):
        self.course_code = course_code
        # insert to listbox with correct form.
        self.course_days_and_hours = []  # list of tuples(day, hour interval)
        # to access cell to change easily.
        self.hours_cell_location = {}  # {"Monday":[(9.0,11.0)]}

    # insert to listbox with correct form.
    def __str__(self):
        # convert days and hours to text.
        list_text_day_hour = [" ".join(x) for x in self.course_days_and_hours]
        text_day_hour = " ".join(list_text_day_hour)

        return "%s %s" % (self.course_code, text_day_hour)

    # save to data structures with correct form.
    def add_days_and_hours(self, day_info, hour_info):
        # split days and hours to combine course hour and day.
        course_days = re.split("[\s]+", day_info)
        course_hours = re.split("[\s]+", hour_info)

        # row has 2 day but just one hour interval.
        if len(course_days) > len(course_hours):
            course_hours.append(course_hours[-1])

        # row has 2 hour intervals but 1 days.
        elif len(course_hours) > len(course_days):
            course_days.append(course_days[-1])

        self.course_days_and_hours.append(course_days)
        self.course_days_and_hours.append(course_hours)

        # convert time interval to cell location to access easily.
        for i in range(len(course_hours)):
            # time format to float
            (start, end) = course_hours[i].replace(":", ".").split("-")
            # some courses have different times in a day.
            self.hours_cell_location.setdefault(course_days[i], [])
            self.hours_cell_location[course_days[i]].append((float(start), float(end)))


class Cell:
    def __init__(self, name, color, column_name, size):
        self.name = name
        self.color = color
        self.column_name = column_name
        self.label_widget = None
        self.size = size

    def create_cell(self, frame, pack_side, padx_amount, pady_amount):
        self.label_widget = Label(frame, text=self.name, bg=self.color, width=self.size, font=("arial", 7, "bold"))
        self.label_widget.pack(side=pack_side, padx=padx_amount, pady=pady_amount)

    # control process
    def change_color(self, color):
        self.label_widget.config(bg=color)

    # turn back when change selected item on listbox.
    def get_old_color(self):
        self.label_widget.config(bg=self.color)

    # when added.
    def change_name_and_color(self, color, name):
        self.color = color
        self.name = name
        self.label_widget.config(bg=color, text=name)

    # when deleted.
    def clear_cell(self):
        self.color ="green"
        self.name = ""
        self.label_widget.config(bg=self.color, text=self.name)



class GUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.dict_cell_object = {}
        self.unitUI()

    def create_frames(self):
        # main frames
        self.frame_first = Frame(root)
        self.frame_first.pack(side=TOP, fill=X, padx=50, pady=5)

        self.frame_second = Frame(root, relief=GROOVE, bd=2)
        self.frame_second.pack(side=TOP, fill=X, padx=20)

        self.frame_third = Frame(root)
        self.frame_third.pack(side=TOP, fill=BOTH)

        # children frames of second frames
        self.frame_listbox_course = Frame(self.frame_second)
        self.frame_buttons = Frame(self.frame_second)
        self.frame_listbox_selected = Frame(self.frame_second)
        self.frame_filter = Frame(self.frame_listbox_course)
        self.frame_listbox = Frame(self.frame_listbox_course)
        self.frame_listbox_course.pack(side=LEFT, pady=10)
        self.frame_buttons.pack(side=LEFT, padx=20)
        self.frame_listbox_selected.pack(side=LEFT, pady=10)
        self.frame_filter.pack(padx=50)
        self.frame_listbox.pack(padx=10)

        # children frames of third frames.
        self.frame_table = Frame(self.frame_third)
        self.frame_info = Frame(self.frame_third)
        self.frame_days = Frame(self.frame_table, background="sky blue")
        self.frame_hours_rows= Frame(self.frame_table)
        self.frame_hours = Frame(self.frame_hours_rows, background="sky blue")
        self.frame_rows = Frame(self.frame_hours_rows)
        self.list_row_frames = [Frame(self.frame_rows) for i in range(8)]
        self.frame_table.pack(side=LEFT, fill=BOTH)
        self.frame_info.pack(side=LEFT, fill=BOTH)
        self.frame_days.pack(side=TOP, fill=X)
        self.frame_hours_rows.pack(side=TOP, fill=BOTH)
        self.frame_hours.pack(side=LEFT, fill=Y)
        self.frame_rows.pack(side=LEFT)
        for frame in self.list_row_frames:
            frame.pack(side=LEFT, fill=Y)


    def fill_first_frame(self):
        self.label_url = Label(self.frame_first, text="Course Offerings Url:", font=("arial", 10, "bold")).pack(side=LEFT, padx=10)
        self.entry_url = Entry(self.frame_first, width=85)
        self.entry_url.insert(END, "https://www.sehir.edu.tr/tr/duyurular/2019_2020_akademik_yili_bahar_donemi_ders_programi")
        self.entry_url.pack(side=LEFT)
        self.button_fetch = Button(self.frame_first, text="Fetch Courses", bg="white", fg="black", relief=RIDGE,font=("Arial", 10, "bold"), command=manage_app.fetch_website)
        self.button_fetch.pack(side=LEFT, padx=5)

    def fill_second_frame(self):
        self.label_filter = Label(self.frame_filter, text="Filter:", font=("Arial", 10, "bold")).pack(side=LEFT)
        self.entry_filter = Entry(self.frame_filter, width=20)
        self.entry_filter.pack()
        self.entry_filter.bind("<Key>", manage_app.update_listbox)
        scrollbar = Scrollbar(self.frame_listbox)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox_all = Listbox(self.frame_listbox, width=55, height=4, selectmode=SINGLE, highlightbackground="black")
        self.listbox_all.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox_all.yview)
        self.listbox_all.bind("<<ListboxSelect>>", manage_app.paint_cells)
        self.listbox_all.pack()
        self.button_add = Button(self.frame_buttons, text="Add", bg="white", fg="black", relief=RIDGE, font=("Arial", 10, "bold"), command=manage_app.add_course)
        self.button_add.pack(pady=10)
        self.button_remove = Button(self.frame_buttons, text="Remove", bg="white", fg="black", relief=RIDGE, font=("Arial", 10, "bold"), command=manage_app.remove_course)
        self.button_remove.pack()
        self.label_selected = Label(self.frame_listbox_selected, text="Selected Courses", font=("Arial", 10, "bold")).pack()
        scrollbar2 = Scrollbar(self.frame_listbox_selected)
        scrollbar2.pack(side=RIGHT, fill=Y)
        self.listbox_selected = Listbox(self.frame_listbox_selected,selectmode=MULTIPLE, width=55, height=4, highlightbackground="black")
        self.listbox_selected.config(yscrollcommand=scrollbar2.set)
        scrollbar2.config(command=self.listbox_selected.yview)
        self.listbox_selected.pack()
        self.listbox_selected.bind("<<ListboxSelect>>", manage_app.get_previous_state)

    def fill_third_frame(self):
        title_table = ["hours", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        index_frame = -1  # to put course rows to correct frame
        for title in title_table:
            if title == "hours":
                # create header of hour
                Cell(title, "black", title, 12).create_cell(self.frame_days, LEFT, 0, 0)
                # create cells of hours.
                i = 9
                while i != 22:
                    hour = "%d:00-%d:30" % (i, i)
                    hour2 = "%d:30-%d:00" % (i, i + 1)
                    Cell(hour, "sky blue", title, 12).create_cell(self.frame_hours, TOP, 1, 1)
                    Cell(hour2, "sky blue", title, 12).create_cell(self.frame_hours, TOP, 1, 1)
                    i += 1
            else:
                # create header of days
                Cell(title, "sky blue", title, 14).create_cell(self.frame_days, LEFT, 1, 1)
                # create cells
                i = 9
                while i != 22:
                    # create cell object by key for day's hours.
                    # examples--> 90 is key for 9:00, 95 for 9:30
                    self.dict_cell_object.setdefault(title, {})
                    cell1 = Cell("", "green", title, 14)
                    self.dict_cell_object[title][i*10] = cell1
                    cell1.create_cell(self.list_row_frames[index_frame], TOP, 1, 1)
                    cell1.label_widget.config(font=("arial", 7, "bold"))
                    cell2 = Cell("", "green", title, 14)
                    self.dict_cell_object[title][i*10 + 5] = cell2
                    cell2.create_cell(self.list_row_frames[index_frame], TOP, 1, 1)
                    cell2.label_widget.config(font=("arial", 7, "bold"))
                    i += 1
            index_frame += 1


    def unitUI(self):
        self.title = Label(root, text="SEHIR COURSE PLANNER", fg="sky blue", bg="black", font=("Arial", 15, "bold")).pack(fill=X)
        self.create_frames()
        self.fill_first_frame()
        self.fill_second_frame()
        self.fill_third_frame()


class Management:
    def __init__(self):
        self.course_objects = {}  # all courses
        self.control_cells = []  # control yellow or red for selected course on listbox.
        self.added_course_row = {}  # to save cells of courses we added to help control process.
        self.color_options = ['dodger blue', 'pale turquoise', 'dark turquoise', 'medium turquoise',
'turquoise', 'cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'LemonChiffon4', 'cornsilk2', 'cornsilk4' , 'honeydew2', 'dark orchid', 'dark violet' ,
'blue violet', 'purple']

    def fetch_website(self):
        try:
            if app.entry_url.get() != "https://www.sehir.edu.tr/tr/duyurular/2019_2020_akademik_yili_bahar_donemi_ders_programi":
                return
            url = requests.get("https://www.sehir.edu.tr/tr/duyurular/2019_2020_akademik_yili_bahar_donemi_ders_programi")
            soup = BeautifulSoup(url.content, "html.parser")
            all_rows = soup.find("table", class_="MsoTableGrid").find_all("tr")[1:]
            for row in all_rows:
                # row doesn't day and time.
                if len(row.find_all("td")[2].text) == 1:
                    continue

                # just get course code, days, hours.
                needed_informations = [row.find_all("td")[x].text for x in [0, 2, 3]]

                # create course object.
                course_object = Course(needed_informations[0])
                course_object.add_days_and_hours(needed_informations[1], needed_informations[2])

                # to get easily rows course hours from listboxes.
                self.course_objects[course_object.__str__()] = course_object

                # insert them to listbox.
                app.listbox_all.insert(END, course_object.__str__())
        except:
            pass

    # control selecting process on all courses listbox.
    def paint_cells(self, event):
        try:
            # infos selected course's cells.
            index = int(app.listbox_all.curselection()[0])
            key = app.listbox_all.get(index)
            # get previous state all of them we selected before.
            for cell in self.control_cells:
                cell.get_old_color()
            self.control_cells.clear()  # delete old selected rows.
            self.clashes = False  # control clashing process.
            # to get cells of selected course's hours.
            self.selected_course = self.course_objects[key]
            self.selected_course_cells = []
            self.unempty_cells = [cell for cells in self.added_course_row.values() for cell in cells]
            for day in self.selected_course.hours_cell_location:
                for hours in self.selected_course.hours_cell_location[day]:
                    # color for cells which are between time intervals.
                    for i in range(int(hours[0]*10), int(hours[1]*10), 5):  # cell's keys format: for 22:00 = 22.0
                        # find cell object by key.
                        if i % 5 != 0:
                            # convert hours like 18:30 so here 183 to 185.(same cell represents both 183 and 185)
                            remainder = i % 5
                            cell = app.dict_cell_object[day][i+(5-remainder)]
                        else:
                            cell = app.dict_cell_object[day][i]
                        self.selected_course_cells.append(cell)

            # control cell before painting.
            clashing_list = self.control_clashing(self.selected_course_cells)
            if len(clashing_list) != 0:
                self.clashes = True
                for cell in clashing_list:
                    cell.change_color("red")
                    self.control_cells.append(cell)
            else:
                for cell in self.selected_course_cells:
                    cell.change_color("yellow")
                    self.control_cells.append(cell)
        except:
            pass

    def control_clashing(self, selected_course_cells):
        clash_cells = []
        for cell in selected_course_cells:
            if cell in self.unempty_cells:
                clash_cells.append(cell)
        return clash_cells

    def add_course(self):
        try:
            # if it's crashes.
            if self.clashes:
                label_info = Label(app.frame_info, text="Could not be added", bg="red")
                label_info.pack(side=TOP)
                label_info.after(2000, label_info.destroy)
                return
            # adding process.
            random_color = self.color_options[random.randint(0, len(self.color_options) - 1)]
            for cell in self.control_cells:
                self.added_course_row.setdefault(self.selected_course, [])
                cell.change_name_and_color(random_color, self.selected_course.course_code)
                self.added_course_row[self.selected_course].append(cell)
            # delete color to be unique.
            self.color_options.remove(random_color)
            # add course to selected courses
            app.listbox_selected.insert(END, self.selected_course)

        except:
            pass

    # if selected item on listbox_selected.
    def get_previous_state(self, event):
        try:
            # get real cell color were selected before.
            for cell in self.control_cells:
                cell.get_old_color()
            self.control_cells.clear()  # delete old selected rows.
        except:
            pass

    def remove_course(self):
        try:
            update_index = 0  # when item was deleted
            for i in app.listbox_selected.curselection():
                # get selected course
                key = app.listbox_selected.get(i - update_index)
                selected_course = self.course_objects[key]
                # to add color to color_option.
                cell_color = self.added_course_row[selected_course][0].color
                # clear cells.
                for cell in self.added_course_row[selected_course]:
                    cell.clear_cell()
                # add color to color options.
                self.color_options.append(cell_color)
                app.listbox_selected.delete(i - update_index)
                del self.added_course_row[selected_course]
                update_index += 1  # if indexes of others items decreased.

        except:
            pass

    # filtering process.
    def update_listbox(self, event):
        try:
            app.listbox_all.delete(0, "end")
            w = event.widget
            text = w.get().upper()
            for course in self.course_objects.values():
                if text in course.course_code:
                    app.listbox_all.insert(END, course)
        except:
            pass


root = Tk()
root.title('SEHIR COURSE PLANNER')
manage_app = Management()
app = GUI(root)
root.mainloop()






