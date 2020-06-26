# coding:utf-8
# https://stackoverflow.com/questions/4685217/parse-raw-http-headers/

from email.parser import BytesParser
from http.server import BaseHTTPRequestHandler
from io import BytesIO


class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, request_text):
        self.rfile = BytesIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message


# t = HTTPRequest(request_text=request_text)

class ParseReqHeader():
    @staticmethod
    def get_request_text_by_file(file_path):
        with open(file_path, 'rb') as f:
            try:
                return f.read()
            finally:
                f.close()

    @staticmethod
    def parse0(request_text, file_path=None):
        return {k: v.strip() for k, v in [line.split(":", 1)
                                          for line in request_text.decode().splitlines() if ":" in line]}

    @staticmethod
    def parse1(request_text=None, file_path=None):
        # TODO: 如果提供了file_path, 优先filepath
        if file_path:
            request_text = ParseReqHeader().get_request_text_by_file(file_path)

        request_line, headers_alone = request_text.split(b'\r\n', 1)
        headers = BytesParser().parsebytes(headers_alone)
        return {k: v for k, v in headers.items()}


def parse_request_by_filepath(file_path):
    return ParseReqHeader().parse1(file_path=file_path)


def parse_request_by_text(request_text):
    return ParseReqHeader().parse1(request_text=request_text)


if __name__ == "__main__":
    _ = ParseReqHeader().parse1(file_path='c://test.txt')
    print(_)

