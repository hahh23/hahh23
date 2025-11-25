import tkinter as tk
from tkinter import filedialog, messagebox
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


# ----------------------- محاسبات فاصله -----------------------
def dis(lat1, lon1, lat2, lon2):
    R = 6371  
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    centeral_angle = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * centeral_angle


def compute_triangle(coords):
    (lat1, lon1), (lat2, lon2), (lat3, lon3) = coords

    for lat, lon in coords:
        if not valid_coord(lat, lon):
            messagebox.showerror("خطا",
                "مقادیر وارد شده خارج از محدوده مجاز هستند:\n"
                "عرض باید بین -90 تا +90 و طول بین -180 تا +180 باشد.")
            return None, None


    a = dis(lat1, lon1, lat2, lon2)
    b = dis(lat2, lon2, lat3, lon3)
    c = dis(lat3, lon3, lat1, lon1)

    perimeter = a + b + c
    s = perimeter / 2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    if area < 1e-6:
     messagebox.showwarning("توجه ", "مثلث قابل قبولي تشکيل نميشود")
     return


    return area, perimeter


# ----------------------- خواندن فایل -----------------------
def load_file():
    file_path = filedialog.askopenfilename(
        title="انتخاب فایل مختصات",
        filetypes=[("Text files", "*.txt")]
    )

    if not file_path:
        return

    try:
        coords = []
        with open(file_path, "r") as f:
            for line in f:
                lat, lon = map(float, line.replace(",", " ").split())
                coords.append((lat, lon))

        if len(coords) != 3:
            raise ValueError("فایل باید شامل دقیقاً سه خط باشد.")

        # قرار دادن در ورودی‌ها
        e_lat1.delete(0, tk.END); e_lat1.insert(0, coords[0][0])
        e_lon1.delete(0, tk.END); e_lon1.insert(0, coords[0][1])

        e_lat2.delete(0, tk.END); e_lat2.insert(0, coords[1][0])
        e_lon2.delete(0, tk.END); e_lon2.insert(0, coords[1][1])

        e_lat3.delete(0, tk.END); e_lat3.insert(0, coords[2][0])
        e_lon3.delete(0, tk.END); e_lon3.insert(0, coords[2][1])

        messagebox.showinfo("ok", "فايل ها با موفقيت اضافه شد")

    except Exception as e:
        messagebox.showerror("خطا","فايل بارگذاري شده دچار مشکل است")

# ----------------------- بررسي داده ها -----------------------


def valid_coord(lat, lon):
    return (-90 <= lat <= 90) and (-180 <= lon <= 180)



# ----------------------- محاسبه و رسم -----------------------
def compute_and_plot():
    try:
        coords = [
            (float(e_lat1.get()), float(e_lon1.get())),
            (float(e_lat2.get()), float(e_lon2.get())),
            (float(e_lat3.get()), float(e_lon3.get()))
        ]

        area, perimeter = compute_triangle(coords)

        result_label.config(
            text=f"مساحت مثلث: {area:.3f} km²\n"
                 f"محیط مثلث: {perimeter:.3f} km"
        )

        # رسم مثلث
        fig.clear()
        ax = fig.add_subplot(111)

        lats = [coords[0][0], coords[1][0], coords[2][0], coords[0][0]]
        lons = [coords[0][1], coords[1][1], coords[2][1], coords[0][1]]

        ax.plot(lons, lats, marker='o')
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        ax.set_title("Triangle Visualization")
        ax.grid(True)

        canvas.draw()

    except:
        messagebox.showerror("خطا", "ورودی‌ها را درست وارد کنید!")


# ----------------------- GUI -----------------------
root = tk.Tk()
root.title("محاسبات مثلث کروي")
root.geometry("850x750")

tk.Label(root, text="ورود مختصات يه صورت دستي", font=("b nazanin", 14)).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

# نقطه 1
tk.Label(frame, text="نقطه شماره 1: عرض", font=("b nazanin", 14)).grid(row=0, column=3)
e_lat1 = tk.Entry(frame, width=15); e_lat1.grid(row=0, column=2)

tk.Label(frame, text="طول", font=("b nazanin", 14)).grid(row=0, column=1)
e_lon1 = tk.Entry(frame, width=15); e_lon1.grid(row=0, column=0)

# نقطه 2
tk.Label(frame, text="نقطه شماره 2: عرض", font=("b nazanin", 14)).grid(row=1, column=3)
e_lat2 = tk.Entry(frame, width=15); e_lat2.grid(row=1, column=2)

tk.Label(frame, text="طول", font=("b nazanin", 14)).grid(row=1, column=1)
e_lon2 = tk.Entry(frame, width=15); e_lon2.grid(row=1, column=0)

# نقطه 3
tk.Label(frame, text="نقطه شماره 3: عرض", font=("b nazanin", 14)).grid(row=2, column=3)
e_lat3 = tk.Entry(frame, width=15); e_lat3.grid(row=2, column=2)

tk.Label(frame, text="طول", font=("b nazanin", 14)).grid(row=2, column=1)
e_lon3 = tk.Entry(frame, width=15); e_lon3.grid(row=2, column=0)


# ----------------------- دکمه ها  -----------------------


tk.Button(root, text="بارگزاري به صورت فايل", command=load_file, bg="#aaaaaa",fg="white", font=("b titr", 10)).pack(pady=3)
tk.Button(root, text="محاسبه و نمایش", command=compute_and_plot, bg="#444444",fg="white", font=("b titr", 10)).pack(pady=3)


help_frame = tk.LabelFrame(root, text="راهنمای فرمت فایل ورودی", font=("b nazanin", 12), padx=3, pady=3)
help_frame.pack(pady=5, fill="none")

help_text = (
    "فرمت فايل ها به صورت متني بايد باشد \n"
    "هر نقطه در يک خط باشد و شامل دو مولفه\n"
    "دو مولفه از هم به وسيله ، جدا بشوند\n"
)

tk.Label(
    help_frame, 
    text=help_text, 
    justify="right",
    font=("b nazanin", 10),
    fg="black"
).pack()


result_label = tk.Label(root, text="", font=("b titr", 10))
result_label.pack(pady=5)

fig = plt.Figure(figsize=(6, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()
