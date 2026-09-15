from http.server import HTTPServer, BaseHTTPRequestHandler 
# 파이썬 기본 라이브러리인 http.server에서 웹 서버 생성용 'HTTPServer' 클래스와 
# HTTP 요청 처리용 'BaseHTTPRequestHandler' 클래스를 불러옵니다.

import json
# 파이썬 객체(dict 등)를 JSON 문자열로 변환하거나 그 반대로 변환하기 위한 json 모듈을 불러옵니다.

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
# BaseHTTPRequestHandler를 상속받아, 요청이 들어왔을 때 어떻게 처리할지 정의하는 커스텀 클래스를 선언합니다.

    # GET 요청 처리
    def do_GET(self):
    # 클라이언트가 GET 방식으로 요청을 보냈을 때 자동으로 호출되는 메서드입니다.

        self.send_response(200)
        # 클라이언트에게 성공 상태 코드인 '200 OK' 응답 헤더를 보냅니다.

        self.send_header('Content-type', 'application/json')
        # 응답 데이터의 형식이 'JSON' 데이터임을 알리는 헤더를 추가합니다.

        self.end_headers()
        # HTTP 헤더 작성이 끝났음을 알리고 헤더 전송을 완료합니다.

        response = {"message": "Hello! GET 요청을 성공적으로 받았습니다."}
        # 클라이언트에게 응답으로 전달할 데이터를 파이썬 딕셔너리 형태로 작성합니다.

        self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
        # json.dumps(): 딕셔너리를 JSON 문자열로 변환합니다.
        # .encode('utf-8'): 문자열을 네트워크 전송이 가능한 바이트(byte) 형태로 변환합니다.
        # self.wfile.write(): 응답 쓰기 스트림에 데이터를 실어 클라이언트로 전송합니다.


def run_server(port=8000):
# 지정한 포트 번호로 서버를 설정하고 실행하는 함수를 정의합니다. (기본값: 8000)

    server_address = ('', port)
    # 서버가 대기할 IP 주소와 포트를 튜플로 설정합니다. ''는 모든 네트워크 인터페이스(localhost 포함)에서의 접속을 허용함을 의미합니다.

    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    # 설정한 주소/포트와 요청 처리 클래스(SimpleHTTPRequestHandler)를 결합하여 HTTP 서버 객체를 생성합니다.

    print(f"서버가 http://localhost:{port} 에서 실행 중입니다...")
    # 서버가 정상적으로 시작되었음을 콘솔에 출력합니다.

    httpd.serve_forever()
    # 서버를 무한 루프로 동작시켜 클라이언트의 요청을 계속해서 대기하고 처리합니다.


if __name__ == '__main__':
# 이 파일이 외부에서 import되지 않고 직접 실행되었을 때만 아래 코드를 실행하도록 보호합니다.

    run_server()
    # run_server 함수를 호출하여 실제 서버를 가동합니다.