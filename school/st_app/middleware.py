import time


def log_middleware(get_response):
    def middleware(request):
        start = time.time()
        response = get_response(request)
        execution_time = round(time.time() - start, 3)
        with open("logs.txt", "a") as file:
            text = f"Метод запроса: {request.method}, путь: {request.path}, время выполнения: {execution_time} сек.\n"
            file.write(text)
        return response

    return middleware
