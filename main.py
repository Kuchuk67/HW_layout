
# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

# Для начала определим настройки запуска
hostName = "localhost" # Адрес для доступа по сети
serverPort = 8080 # Порт для доступа по сети

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        #print(self.path)
        get_ = self.path.split('/')
        get_ = (get_[-1])
        if get_ == 'style.css':
            with open("style.css", 'r', encoding='utf-8') as f:
                html_contacts = f.read()
            self.send_response(200)  # Отправка кода ответа
            self.send_header("Content-type", "text/css")  # Отправка типа данных, который будет передаваться
            self.end_headers()  # Завершение формирования заголовков ответа
            # self.wfile.write(html_contacts.encode())
            self.wfile.write(bytes(html_contacts, "utf-8"))  # Тело ответа
        elif get_ == 'user.avif':
            with open("img/user.avif", 'rb') as f:
                html_contacts = f.read()
            self.send_response(200)  # Отправка кода ответа
            self.send_header("Content-type", "image/jpg")  # Отправка типа данных, который будет передаваться
            self.end_headers()  # Завершение формирования заголовков ответа
            self.wfile.write(html_contacts)  # Тело ответа
        else:
            with open("static/contact.html", 'r', encoding='utf-8') as f:
                html_contacts = f.read()
            self.send_response(200) # Отправка кода ответа
            self.send_header("Content-type", "text/html") # Отправка типа данных, который будет передаваться
            self.end_headers() # Завершение формирования заголовков ответа
            #self.wfile.write(html_contacts.encode())
            self.wfile.write(bytes(html_contacts, "utf-8")) # Тело ответа

if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрах в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")