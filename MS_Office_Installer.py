import customtkinter
from PIL import Image
import xml.etree.ElementTree as Xml

pages = {}
width = 400
height = 500
selected = []


class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.wm_overrideredirect(True)
        self.geometry(self.Center_Window_To_Display(width, height))
        self._set_appearance_mode("Light")
        self.title("MS Office")

        self.mainFrame = customtkinter.CTkFrame(self, fg_color="white", border_width=1, border_color="orange",
                                                corner_radius=0)
        self.mainFrame.pack(padx=3, pady=3, fill="both", expand=True)

        self.current_page = None

        for P in (Download, SelectApplication):
            page = P(self.mainFrame, self)
            pages[P.__name__] = page

        self.show_frame("SelectApplication")

    def show_frame(self, page_name):
        if self.current_page is not None:
            self.current_page.pack_forget()
        page = pages[page_name]
        page.pack(side="top", padx=1, pady=1, fill="both", expand=True)
        page.tkraise()

        self.current_page = page

    def Center_Window_To_Display(self, _width: int, _height: int):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (_width / 2))
        y = int((screen_height / 2) - (_height / 2))
        return f"{_width}x{_height}+{x}+{y}"

    def start_drag(self, event):
        self._drag_data = {'x': event.x, 'y': event.y}

    def on_drag(self, event):
        x = self.winfo_x() + event.x - self._drag_data['x']
        y = self.winfo_y() + event.y - self._drag_data['y']
        self.geometry(f"+{x}+{y}")

    def stop_drag(self):
        self._drag_data = None

    def minimize_window(self):
        self.withdraw()


class Download(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(fg_color="red", corner_radius=0)
        self.btn = customtkinter.CTkButton(self, text="Download", width=100, height=30)
        self.btn.pack(side="top", expand=True)
        self.btn.bind("<Button-1>", lambda event: self.CLic())

    def CLic(self):
        self.controller.show_frame("SelectApplication")
        x = self.controller.winfo_x()
        y = self.controller.winfo_y()
        _height = self.controller.winfo_height()
        self.controller.geometry(f"400x500+{x}+{(y+100) - 250}")


class SelectApplication(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(fg_color="transparent", corner_radius=0)

        self.icons = {
            "Logo": Image.open("Image_Resources/logo.png"),
            "Close": Image.open("Image_Resources/close.png"),
            "Access": Image.open("Image_Resources/access.png"),
            "Lync": Image.open("Image_Resources/skype.png"),
            "OneNote": Image.open("Image_Resources/onenote.png"),
            "PowerPoint": Image.open("Image_Resources/powerpoint.png"),
            "Word": Image.open("Image_Resources/word.png"),
            "Excel": Image.open("Image_Resources/excel.png"),
            "OneDrive": Image.open("Image_Resources/onedrive.png"),
            "Outlook": Image.open("Image_Resources/outlook.png"),
            "Publisher": Image.open("Image_Resources/publisher.png")
        }

        self._drag_data = None
        self.config_path = "Configuration-x64.xml"
        self.temp_file = "temp.xml"

        # Setup for each frame
        self.headerFrame = customtkinter.CTkFrame(self, fg_color="transparent", height=26, corner_radius=0)
        self.headerFrame.pack(side="top", fill="both")
        self.headerFrame.bind("<ButtonPress-1>", controller.start_drag)
        self.headerFrame.bind("<B1-Motion>", controller.on_drag)
        self.headerFrame.bind("<ButtonRelease-1>", controller.stop_drag)
        self.headerFrame.bind("<Double-Button-1>", controller.minimize_window)
        self.titleFrame = customtkinter.CTkFrame(self, fg_color="transparent", height=20, corner_radius=0)
        self.titleFrame.pack(side="top", fill="both")
        self.bodyFrame = customtkinter.CTkFrame(self, fg_color="transparent", corner_radius=0)
        self.bodyFrame.pack(side="top", fill="both", expand=True)
        self.body1Frame = customtkinter.CTkFrame(self, fg_color="transparent", corner_radius=0)
        self.body1Frame.pack(side="top", fill="both")
        self.footerFrame = customtkinter.CTkFrame(self, fg_color="transparent", height=26, corner_radius=0)
        self.footerFrame.pack(side="top", fill="both")

        # Object inside title frame
        self.exitLabel = customtkinter.CTkLabel(self.titleFrame, text="", width=0, height=0,
                                                image=self.icon("Close", 0.02))
        self.exitLabel.pack(side="right", padx=24, anchor="n")
        self.exitLabel.bind("<Button-1>", lambda event: exit())
        self.titleLabel = customtkinter.CTkLabel(self.titleFrame, text="", width=0, height=0,
                                                 image=self.icon("Logo", 0.65))
        self.titleLabel.pack(side="left", padx=26)

        # Object inside body frame
        self.appFrame = customtkinter.CTkFrame(self.bodyFrame, fg_color="transparent", height=26, border_width=0,
                                               corner_radius=0)
        self.appFrame.pack(side="top", pady=(50, 0))
        self.AccessBtn = customtkinter.CTkButton(self.appFrame, width=70, height=70)
        self.AccessBtn.pack(side="left", padx=2, pady=2)
        self.SkypeBtn = customtkinter.CTkButton(self.appFrame, width=70, height=70)
        self.SkypeBtn.pack(side="left", padx=2, pady=2)
        self.OneNoteBtn = customtkinter.CTkButton(self.appFrame, width=70, height=70)
        self.OneNoteBtn.pack(side="left", padx=2, pady=2)

        self.appFrame1 = customtkinter.CTkFrame(self.bodyFrame, fg_color="transparent", height=26, border_width=0,
                                                corner_radius=70)
        self.appFrame1.pack(side="top")
        self.PowerPointBtn = customtkinter.CTkButton(self.appFrame1, width=70, height=70)
        self.PowerPointBtn.pack(side="left", padx=2, pady=2)
        self.WordBtn = customtkinter.CTkButton(self.appFrame1, width=70, height=70)
        self.WordBtn.pack(side="left", padx=2, pady=2)
        self.ExcelBtn = customtkinter.CTkButton(self.appFrame1, width=70, height=70)
        self.ExcelBtn.pack(side="left", padx=2, pady=2)
        self.OneDriveBtn = customtkinter.CTkButton(self.appFrame1, width=70, height=70)
        self.OneDriveBtn.pack(side="left", padx=2, pady=2)

        self.appFrame2 = customtkinter.CTkFrame(self.bodyFrame, fg_color="transparent", height=26, border_width=0,
                                                corner_radius=0)
        self.appFrame2.pack(side="top")
        self.OutlookBtn = customtkinter.CTkButton(self.appFrame2, width=70, height=70)
        self.OutlookBtn.pack(side="left", padx=2, pady=2)
        self.PublisherBtn = customtkinter.CTkButton(self.appFrame2, width=70, height=70)
        self.PublisherBtn.pack(side="left", padx=2, pady=2)

        self.AccessBtn.bindtags(["Access"])
        self.SkypeBtn.bindtags(["Lync"])
        self.OneNoteBtn.bindtags(["OneNote"])
        self.PowerPointBtn.bindtags(["PowerPoint"])
        self.WordBtn.bindtags(["Word"])
        self.ExcelBtn.bindtags(["Excel"])
        self.OneDriveBtn.bindtags(["OneDrive"])
        self.OutlookBtn.bindtags(["Outlook"])
        self.PublisherBtn.bindtags(["Publisher"])

        self.apps_button = [
            self.AccessBtn,
            self.SkypeBtn,
            self.OneNoteBtn,
            self.PowerPointBtn,
            self.WordBtn,
            self.ExcelBtn,
            self.OneDriveBtn,
            self.OutlookBtn,
            self.PublisherBtn
        ]

        for button in self.apps_button:
            button.configure(text="", image=self.icon(button.bindtags()[0], 0.05), fg_color="transparent",
                             corner_radius=0, hover=False)
            button.bind("<Button-1>", lambda event, btn=button: self.Click(btn))
            button.bind("<Enter>", lambda event, btn=button: self.Enter(btn))
            button.bind("<Leave>", lambda event, btn=button: self.Leave(btn))

        # Object inside body1 frame
        self.installBtn = customtkinter.CTkButton(self.body1Frame, text="Install", width=100, height=30,
                                                  hover_color="#d9d9d9", fg_color="transparent",
                                                  text_color="gray", corner_radius=0, border_width=1,
                                                  border_color="gray", state="disabled", command=self.Install,
                                                  font=customtkinter.CTkFont(family="Segoe UI", size=14, weight="bold"))
        self.installBtn.pack(pady=26)

    def icon(self, icon_name: str, scale_factor: float):
        global width, height
        icon_image = self.icons[icon_name]
        width, height = icon_image.size
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)
        return customtkinter.CTkImage(icon_image, size=(new_width, new_height))

    def Enter(self, button):
        name = button.bindtags()[0]
        button.configure(image=self.icon(name, 0.058))

    def Leave(self, button):
        name = button.bindtags()[0]
        if button.cget("border_width") == 0:
            button.configure(image=self.icon(name, 0.05))

    def Click(self, button):
        self.controller.show_frame("Download")
        x = self.controller.winfo_x()
        y = self.controller.winfo_y()
        _height = self.controller.winfo_height()
        self.controller.geometry(f"400x150+{x}+{y + (_height/2 - 100)}")
        name = button.bindtags()[0]
        if button.cget("border_width") == 0:
            button.configure(border_width=1, border_color="orange")
            selected.append(name)
        else:
            button.configure(border_width=0)
            selected.remove(name)

        if len(selected) > 0:
            self.installBtn.configure(state="normal")
        else:
            self.installBtn.configure(state="disabled")

    def Install(self):
        tree = Xml.parse(self.config_path)
        root1 = tree.getroot()

        for id_list in selected:
            for product in root1.findall(".//Product"):
                for exclude_app in product.findall(".//ExcludeApp"):
                    if exclude_app.attrib.get("ID") == id_list:
                        product.remove(exclude_app)

        tree.write(self.temp_file)


if __name__ == "__main__":
    Main().mainloop()
