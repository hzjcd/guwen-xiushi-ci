import http.server
import socketserver
import qrcode
import socket
import os
import webbrowser
from urllib.parse import urlparse
import sys

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

# 为GitHub Pages链接生成二维码

def generate_github_qrcode(page="wz"):
    """
    为GitHub Pages链接生成二维码
    
    Args:
        page: 页面类型，可选值为'wz'(默认)或'zz'
    """
    print(f"\n正在为GitHub Pages链接生成二维码...")
    
    # 根据参数选择页面
    if page == "zz":
        github_url = "https://hzjcd.github.io/guwen-xiushi-ci/zz.html"
        qr_filename = "github_pages_zz_qrcode.png"
        page_name = "古文辨析练习第二页面"
    else:
        github_url = "https://hzjcd.github.io/guwen-xiushi-ci/wz.html"
        qr_filename = "github_pages_qrcode.png"
        page_name = "古文虚实词练习页面"
    
    print(f"链接地址: {github_url}")
    
    # 生成二维码
    generate_qrcode(github_url, qr_filename)
    
    print(f"\n二维码使用说明:")
    print(f"1. 使用手机或其他设备的相机扫描二维码")
    print(f"2. 扫描后将自动跳转到{page_name}")
    print(f"3. 二维码图片已保存为: {qr_filename}")
    print(f"4. 您可以将此二维码分享给他人，方便访问网页")

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
    
    # 如果有命令行参数，检查是否需要直接生成GitHub Pages二维码
    if len(sys.argv) > 1 and sys.argv[1] == "--github":
        # 检查是否有第二个参数指定页面
        page = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] == "zz" else "wz"
        generate_github_qrcode(page)
    else:
        # 显示菜单供用户选择
        print("=== 二维码生成工具 ===")
        print("1. 生成GitHub Pages链接的二维码 (wz.html)")
        print("2. 生成GitHub Pages链接的二维码 (zz.html)")
        print("3. 启动本地服务器并生成本地链接的二维码")
        
        choice = input("请选择操作 (1/2/3): ")
        
        if choice == "1":
            # 生成GitHub Pages二维码 (wz.html)
            generate_github_qrcode("wz")
        elif choice == "2":
            # 生成GitHub Pages二维码 (zz.html)
            generate_github_qrcode("zz")
        else:
            # 启动本地服务器
            start_server()