import sys
import time
import psutil
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon

class HTMLViewerApp(QMainWindow):
    def __init__(self, html_file_path):
        super().__init__()

        self.setWindowTitle("Jarvis")
        self.setGeometry(50, 50, 1800, 800)

        # Always maximized open karaila
        self.showMaximized()
        self.setStyleSheet("background-color: black; color: white;")
        self.setWindowIcon(QIcon("icon.png"))

        self.initUI(html_file_path)

    def initUI(self, html_file_path):
        # Create a central widget and layout
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # Create a QWebEngineView to display HTML content
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        # Set the central widget
        self.setCentralWidget(central_widget)

        # Load the specified HTML file
        self.load_html_file(html_file_path)

        # Set up a timer to update CPU usage every second
        self.cpu_timer = QTimer(self)
        time.sleep(1)
        self.cpu_timer.timeout.connect(self.update_system_info)  # Corrected method name here
        self.cpu_timer.start(1000)  # Update every 1000 milliseconds (1 second)

    def load_html_file(self, file_path):
        url = QUrl.fromLocalFile(file_path)
        self.web_view.setUrl(url)

    def update_system_info(self):
        cpu_percent = psutil.cpu_percent(interval=0.1)
        ram_percent = psutil.virtual_memory().percent
        processes_count = len(psutil.pids())
        
        cpu_html = f'CPU Usage: {cpu_percent}%'
        ram_html = f'Physical Memory: {ram_percent}%'
        processes_html = f'Processes: {processes_count}'
        
        # Convert special characters to HTML entities
        cpu_html = cpu_html.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        ram_html = ram_html.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        processes_html = processes_html.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    
        # Update CPU usage in HTML
        cpu_js_code = f"document.getElementById('cpu').innerHTML = '{cpu_html}';"
        self.web_view.page().runJavaScript(cpu_js_code)
    
        # Update physical memory usage in HTML
        ram_js_code = f"document.getElementById('ram').innerHTML = '{ram_html}';"
        self.web_view.page().runJavaScript(ram_js_code)
    
        # Update processes count in HTML
        processes_js_code = f"document.getElementById('proc').innerHTML = '{processes_html}';"
        self.web_view.page().runJavaScript(processes_js_code)


if __name__ == '__main__':
    # Specify the new path to the HTML file
    # YASH
    html_file_path = 'D:\\Quarantine\\Projects\\Miniporject-Personal-Assistant\\jarvis.html'
    # VARAD
    # html_file_path = 'C:\\Users\\varad\\OneDrive\\Desktop\\py\\Miniporject-Personal-Assistant-\\jarvis.html'

    app = QApplication(sys.argv)
    viewer = HTMLViewerApp(html_file_path)
    viewer.show()
    sys.exit(app.exec_())
