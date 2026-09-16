import socket

def start_http_server(host='', port=8000):
    # 사용할 주소 체계와 통신방식을 인자로 넣는다.
    # AF_INET은 IPv4를 SOCK_STREAM은 TCP를 사용한다는 것.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 옵션을 변경하는 함수이다.
    # 매개변수로 어디에 있는 옵션을 바꿀 건지, 어떤 옵션을 바꿀 건지, 옵션에 어떤 값을 줄 건지 를 설정한다.
    # SOL_SOCKET: 소켓 설정을 변경, SO_REUSEADDR: 소켓 설정 중 주소 재사용 옵션, 1: 해당 옵션을 킴
    # 이 함수를 사용한 이유는 서버를 키고 껐을 때 사용했던 주소가와 포트가 잔여 처리를 위해 TIME_WAIT 상태로 잠겨 있게됨.
    # 이를 무시하고 바로 주소와 포트번호를 이용함.
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 주소와 포트에 소켓을 장착
    server_socket.bind((host, port))
    # 소켓 실행. 외부의 요청을 들을 수 있는 상태로 만듬. 함수안의 숫자는 대기열의 개수. 한번에 5명까지 대기할 수 있고 그 이상의 요청은 거절함.
    server_socket.listen(5)
    print(f"서버 실행 중: http://localhost:{port}")

    while True:
        # accept(): 블로킹 함수로 accept() 함수가 실행되면 요청이 들어올 때 까지 멈추고 동작하지 않음.
        # 이후 요청이 들어오면 accept()가 동작해서 클라이언트를 1:1로 전담할 소켓을 생성하고 클라이언트의 주소와 함께 반환함.
        # 이렇게 만드는 이유는 server_socket이 요청까지 처리하면 그 시간 동안 클라이언트의 다른 요청을 받고 처리할 수 없어서 요청을 받는
        # 소켓과 요청을 처리하는 소켓을 구분함.
        # 주의할 점은 client_socket은 요청을 보낸 클라이언트 쪽의 소켓이 아니라 그 소켓과 통신하기 위해 새로 만든 전용 소켓임.
        # server_socket은 요청 감지, 연결 신호만 감지하고, 실제 클라이언트와 소통하는건 client_socket이 전담함.
        # server_socket은 클라이언트의 정보를 모름
        client_socket, client_address = server_socket.accept()
        # recv(): 요청 정보를 앍는 함수.
        request_data = client_socket.recv(1024).decode('utf-8')
        
        if not request_data:
            # 요청 데이터가 없다면 소켓을 닫음. 닫지 않으면 계속 점유하게됨.
            client_socket.close()
            continue

        # 1. 요청 데이터를 줄(line) 단위로 분리
        lines = request_data.split('\r\n')
        
        # 2. 첫 번째 줄(Start Line) 추출 (예: "GET / HTTP/1.1")
        first_line = lines[0]
        
        # 3. 공백 기준으로 단어 나누기 -> ['GET', '/', 'HTTP/1.1']
        method = first_line.split(' ')[0]
        path = first_line.split(' ')[1]

        # 4. HTTP 메서드에 따른 조건문 처리
        if method == 'GET':
            body = f'{{"message": "GET 요청 수신완료 (경로: {path})"}}'
        elif method == 'POST':
            # POST 데이터(Body)는 헤더와 빈 줄(\r\n\r\n)로 구분된 맨 마지막 요소에 위치
            post_body = request_data.split('\r\n\r\n')[1]
            body = f'{{"message": "POST 요청 수신완료", "received": "{post_body}"}}'
        else:
            body = '{"message": "지원하지 않는 메서드입니다."}'

        # 응답 전송
        body_bytes = body.encode('utf-8')
        # 튜플이 아니라 하나의 긴 문자열이됨.
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: application/json; charset=utf-8\r\n"
            f"Content-Length: {len(body_bytes)}\r\n"
            "Connection: close\r\n"
            "\r\n"
        )
        # 클라이언트에게 응답을 보냄.
        client_socket.sendall(response.encode('utf-8') + body_bytes)
        client_socket.close()

if __name__ == '__main__':
    start_http_server()