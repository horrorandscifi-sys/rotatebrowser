import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PyQt6.QtWebEngineWidgets import QWebEngineView

class RotateBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RotateBrowser")
        self.resize(1024, 768)

        # Список разрешенных доменов
        self.allowed_sites = [
            "google.com", "github.com", "youtube.com", "yandex.ru", "ya.ru",
            "aliexpress.com", "aliexpress.ru", "rutracker.org", "nnmclub.to",
            "ridero.ru", "kufar.by", "rutor.info", "rutor.is"
        ]

        # Инициализация интерфейса
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        
        # Обработка изменения URL (блокировка)
        self.browser.urlChanged.connect(self.check_url)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        layout = QVBoxLayout()
        layout.addWidget(self.url_bar)
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

    def check_url(self, q):
        host = q.host().lower()
        # Проверяем, есть ли хост в списке разрешенных
        is_allowed = any(site in host for site in self.allowed_sites)
        
        if not is_allowed and host != "":
            self.browser.setHtml(f"<h1>Доступ запрещен</h1><p>Сайт {host} не входит в белый список RotateBrowser.</p>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RotateBrowser()
    window.show()
    sys.exit(app.exec())
