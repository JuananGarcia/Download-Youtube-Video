from pytube import YouTube
from pytube.cli import on_progress
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tkinter.font import Font

def main():
    def common_download(url, get_stream, filename_extension):
        try:
            video = YouTube(url=url, on_progress_callback=on_progress)
            stream = get_stream(video)
            dir = filedialog.askdirectory()
            if dir:
                info_message.config(text="Descargando.....")
                filename = f"{video.title}.{filename_extension}" if filename_extension else None
                stream.download(output_path=dir, filename=filename)
                info_message.config(text="Descarga completada!")
                input_url.delete(0, END)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def download_video():
        url = input_url.get()
        common_download(url, lambda video: video.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution(), None)

    def download_song():
        url = input_url.get()
        common_download(url, lambda video: video.streams.get_audio_only(), "mp3")

    root = Tk()
    root.title("YouDownloader")
    root.geometry("600x200")
    root.resizable(FALSE, FALSE)

    input_frame = Frame(root)
    input_frame.pack(pady=30)

    url_label = Label(input_frame, text="URL del video:", font=Font(size=12))
    url_label.pack(side="left", padx=7)

    input_url = ttk.Entry(input_frame, width=45)
    input_url.pack(side="left")

    buttons_frame = Frame(root)
    buttons_frame.pack(pady=10)

    download_audio_btn = tk.Button(buttons_frame, text="Descargar audio", command=download_song)
    download_audio_btn.pack(side="left", padx=20)

    download_video_btn = tk.Button(buttons_frame, text="Descargar video", command=download_video)
    download_video_btn.pack(side="left", padx=20)

    info_message = Label(root, text="")
    info_message.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
