import http.server
import socketserver
import qrcode
import socket
import os
import webbrowser
from urllib.parse import urlparse

# 获取本地IP地址
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # 连接到一个公共IP（不会实际发送数据）
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
    finally:
        s.close()
    return local_ip

# 生成二维码
def generate_qrcode(url, filename='qrcode.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"二维码已保存为: {filename}")
    
    # 自动打开二维码图片
    webbrowser.open(filename)

# 启动HTTP服务器
def start_server(port=8000):
    handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", port), handler) as httpd:
        local_ip = get_local_ip()
        url = f"http://{local_ip}:{port}/wz.html"
        
        print(f"服务器已启动，访问地址: {url}")
        print("按 Ctrl+C 停止服务器")
        
        # 生成二维码
        generate_qrcode(url)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n服务器已停止")

if __name__ == "__main__":
    # 检查是否安装了qrcode库
    try:
        import qrcode
    except ImportError:
        print("正在安装qrcode库...")
        os.system("pip install qrcode[pil]")
        import qrcode
    
    # 切换到当前目录
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # 启动服务器
    start_server()