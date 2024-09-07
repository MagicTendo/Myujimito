from customtkinter import CTk, set_appearance_mode, CTkImage, CTkLabel, CTkEntry, CTkButton, YES, END
from tkinter import Menu, messagebox
from pystray import MenuItem, Icon
from pywinstyles import apply_style, set_opacity
from PIL import Image
from threading import Thread
from os import _exit

import languages
import resource_manager
import settings
import volume

VERSION = "2.0.0"

global volume_input


class Myujimito(CTk):
    def __init__(self):
        super().__init__()

        volume_threshold = resource_manager.dataframe["volume_threshold"].values[0]
        user_language = languages.get_user_language()
        user_boot_up = resource_manager.dataframe["boot_up"].values[0]

        def change_volume_threshold():
            """
            Update the new volume threshold inserted by the user in the config.csv
            """
            if volume_input.get().isnumeric():
                get_threshold = int(volume_input.get())

                if get_threshold > 100:
                    get_threshold = 100
                elif get_threshold < 0:
                    get_threshold = 0

                resource_manager.dataframe.at[resource_manager.dataframe.index[0], "volume_threshold"] = get_threshold
                resource_manager.dataframe.to_csv(resource_manager.get_config(), sep=";", index=False)

                volume_input.delete(0, END)

                new_volume_threshold = resource_manager.dataframe["volume_threshold"].values[0]

                label_current_threshold.configure(text=languages.texts[user_language]["new_threshold"]
                                                  .replace("{threshold}", str(new_volume_threshold)))

        self.title(languages.texts[user_language]["myujimito"])
        self.iconbitmap(resource_manager.get_resource("icon.ico"))
        self.geometry("700x500")
        self.resizable(False, False)
        self.config(background="#ffc532")
        set_appearance_mode("light")
        apply_style(self, "mica")

        background_image_resource = Image.open(resource_manager.get_resource("background.png"))
        background_image = CTkImage(background_image_resource, size=(700, 700))

        background_label = CTkLabel(self, text="", image=background_image)
        background_label.place(relwidth=1, relheight=1)

        label_title = CTkLabel(master=self, text=f"{languages.texts[user_language]["myujimito"]} {VERSION}",
                               font=("Courier", 50, "bold"), text_color="#ffffff", bg_color="#ffc532")
        label_title.pack(expand=YES)
        set_opacity(label_title.winfo_id(), color="#ffc532")

        label_subtitle = CTkLabel(master=self, text=languages.texts[user_language]["subtitle"],
                                  font=("Lexend", 25, "bold"), text_color="#ffffff", bg_color="#ffc532")
        label_subtitle.pack(expand=YES)
        set_opacity(label_subtitle.winfo_id(), color="#ffc532")

        label_current_threshold = CTkLabel(master=self,
                                           text=languages.texts[user_language]["current_threshold"]
                                           .replace("{threshold}", str(volume_threshold)),
                                           font=("Lexend", 25, "bold"), text_color="#ffffff", bg_color="#ffc532")
        label_current_threshold.pack(expand=YES)
        set_opacity(label_current_threshold.winfo_id(), color="#ffc532")

        global volume_input
        volume_input = CTkEntry(master=self, width=150, height=40, font=("Comic Sans MS", 30, "bold"),
                                placeholder_text_color="#ffffff", fg_color="#99750c", text_color="#ffffff",
                                bg_color="#ffc532", border_color="#99750c", border_width=10, corner_radius=10,
                                justify="center")
        volume_input.insert(0, volume_threshold)
        volume_input.pack(expand=YES)
        set_opacity(volume_input.winfo_id(), color="#ffc532")

        submit_button = CTkButton(master=self, text=languages.texts[user_language]["set"],
                                  font=("Lexend", 35, "bold"), fg_color="#faffa5", bg_color="#ffc532",
                                  text_color="#99750c", border_color="#faffa5", border_width=10, corner_radius=10,
                                  hover_color="#eaf089", command=change_volume_threshold)
        submit_button.pack(expand=YES)
        set_opacity(submit_button.winfo_id(), color="#ffc532")

        if user_boot_up:
            user_boot_up_icon = "✅"
        else:
            user_boot_up_icon = "❎"

        menu_bar = Menu(self.master)

        languages_menu = Menu(menu_bar, tearoff=0)
        languages_menu.add_command(label="English",
                                   command=lambda: [settings.change_language("en"), self.reload_application()])
        languages_menu.add_command(label="Español",
                                   command=lambda: [settings.change_language("es"), self.reload_application()])
        languages_menu.add_command(label="Français",
                                   command=lambda: [settings.change_language("fr"), self.reload_application()])
        languages_menu.add_command(label="Yunayunopi",
                                   command=lambda: [settings.change_language("yu"), self.reload_application()])
        languages_menu.add_command(label="日本語",
                                   command=lambda: [settings.change_language("jp"), self.reload_application()])

        settings_menu = Menu(menu_bar, tearoff=0)
        settings_menu.add_command(label=languages.texts[user_language]["set_volume_limit"],
                                  command=change_volume_threshold)
        settings_menu.add_command(label=languages.texts[user_language]["run_in_background"],
                                  command=self.run_in_background)
        settings_menu.add_cascade(label=languages.texts[user_language]["change_language"], menu=languages_menu)
        settings_menu.add_command(label=f"{languages.texts[user_language]["open_at_boot_up"]} {user_boot_up_icon}",
                                  command=lambda: [settings.set_boot_up_config(), self.reload_application()])
        settings_menu.add_command(label=languages.texts[user_language]["close"], command=self.close_window)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label=languages.texts[user_language]["server_support"],
                              command=settings.open_server_support)
        help_menu.add_command(label=languages.texts[user_language]["help"], command=settings.open_website)

        menu_bar.add_cascade(label=languages.texts[user_language]["settings"], menu=settings_menu)
        menu_bar.add_cascade(label="?", menu=help_menu)

        self.config(menu=menu_bar)

        try:
            self.protocol("WM_DELETE_WINDOW", self.close_window)
            self.bind("<FocusOut>", self.run_in_background)
        except:
            os._exit(0)

    def run_in_background(self, event=None):
        """
        Launch the check_volume() processus in background to check if the volume threshold is respected
        :param event: the element that launched this function
        """
        run_background = Thread(target=volume.check_volume)
        run_background.start()
        self.hide_window()

    def reload_application(self):
        """
        Refresh the whole application, mainly to update either the language or the boot up icon from activated or not
        """
        Myujimito.destroy(self)

        new_myujimito = Myujimito()
        new_myujimito.mainloop()

    def hide_window(self):
        """
        Hide the application to allow to run in background, and create a systray icon
        """
        self.withdraw()

        image = Image.open(resource_manager.get_resource("icon.ico"))
        menu = [MenuItem(languages.texts[languages.get_user_language()]["show"], self.show_window),
                MenuItem(languages.texts[languages.get_user_language()]["close"], self.close_window_from_icon)]

        icon = Icon("name", image, languages.texts[languages.get_user_language()]["myujimito"], menu)
        Thread(target=icon.run(), daemon=True).start()

    def show_window(self, icon):
        """
        Show back the application and remove the systray icon
        :param icon: the application systray's icon
        """
        volume.run_volume_check = False

        icon.stop()
        self.after(0, self.deiconify)
        self.lift()
        self.focus_force()

        new_volume_threshold = resource_manager.dataframe["volume_threshold"].values[0]
        volume_input.delete(0, END)
        volume_input.insert(0, new_volume_threshold)

    def close_window(self):
        """
        Close and force the application to stop
        """
        self.unbind("<FocusOut>")

        if messagebox.askokcancel(languages.texts[languages.get_user_language()]["close"],
                                  languages.texts[languages.get_user_language()]["close_message"]):
            self.destroy()
            _exit(0)
        else:
            self.bind("<FocusOut>", self.run_in_background)

    def close_window_from_icon(self, icon):
        """
        Close, remove the systray icon and force the application to stop
        :param icon: the application systray's icon
        """
        icon.stop()
        self.quit()
        self.destroy()
        _exit(0)


if __name__ == "__main__":
    myujimito = Myujimito()
    myujimito.mainloop()
