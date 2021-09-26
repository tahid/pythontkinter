import tkinter as tk

import tksheet

top = tk.Tk()

sheet = tksheet.Sheet(top)

sheet.pack( fill="both" , expand=1)

sheet.set_sheet_data([[f"{ri+cj}" for cj in range(4)] for ri in range(5)])

# table enable choices listed below:

sheet.enable_bindings(("single_select",

                       "row_select",

                       "column_width_resize",

                       "arrowkeys",

                       "right_click_popup_menu",

                       "rc_select",

                       "rc_insert_row",

                       "rc_delete_row",

                       "copy",

                       "cut",

                       "paste",

                       "delete",

                       "undo",

                       "edit_cell"))

top.mainloop()