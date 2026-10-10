import os
from http.server import BaseHTTPRequestHandler, HTTPServer

import mysql.connector
from mysql.connector import Error


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "mysql"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "appuser"),
        password=os.environ["DB_PASSWORD"],
        database=os.getenv("DB_NAME", "appdb"),
        connection_timeout=5,
    )


class AppHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Application is running")
            return

        if self.path == "/":
            try:
                connection = get_db_connection()
                cursor = connection.cursor()

                cursor.execute("SELECT VERSION()")
                db_version = cursor.fetchone()[0]

                cursor.close()
                connection.close()

                response = f"Python app connected to MySQL! Version: {db_version}"
                status = 200

            except Error:
                response = "Database connection failed"
                status = 503

            self.send_response(status)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(response.encode("utf-8"))
            return

        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"Not Found")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), AppHandler)
    print("Application listening on port 8080", flush=True)
    server.serve_forever()
