import sys


def error_message_detail(error, error_detail: sys):
    _, _, exc_traceback = error_detail.exc_info()
    file_name = exc_traceback.tb_frame.f_code.co_filename
    line_number = exc_traceback.tb_lineno
    error_message = f'An error occured in script {file_name} on line {line_number} \n Message: {str(error)}'
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail)

    def __str__(self):
        return self.error_message
