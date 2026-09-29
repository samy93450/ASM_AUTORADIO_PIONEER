import os, sys, threading, socket
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

APP_NAME='ASM Autoradio Pioneer'
PORT=18761

def app_dir():
    return Path(getattr(sys, '_MEIPASS', Path(__file__).resolve().parent))

def user_data_dir():
    base=Path(os.environ.get('LOCALAPPDATA', Path.home()))
    p=base/'ASM Technologies'/'ASM Autoradio Pioneer'
    p.mkdir(parents=True, exist_ok=True)
    return p

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args): pass
    def end_headers(self):
        self.send_header('Cache-Control','no-cache, no-store, must-revalidate')
        self.send_header('Pragma','no-cache')
        self.send_header('Expires','0')
        super().end_headers()

def free_port(preferred):
    for p in [preferred,0]:
        s=socket.socket();
        try:
            s.bind(('127.0.0.1',p)); return s.getsockname()[1]
        except OSError: pass
        finally: s.close()

def main():
    root=app_dir(); os.chdir(root)
    port=free_port(PORT)
    server=ThreadingHTTPServer(('127.0.0.1',port), QuietHandler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    url=f'http://127.0.0.1:{port}/index.html'
    try:
        import webview
        win=webview.create_window(APP_NAME,url,width=1480,height=940,min_size=(1100,720),resizable=True,background_color='#05080b')
        webview.start(private_mode=False, storage_path=str(user_data_dir()), debug=False)
    finally:
        server.shutdown()

if __name__=='__main__': main()
