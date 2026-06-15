import traceback
import os
import sys

class CustomException(Exception):
    def __init__(self, error_message, error_detail=None):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message, error_detail)
    
    @staticmethod
    def get_detailed_error_message(error_message, error_detail=None):
        exc_tb = None
        if error_detail is not None:
            if isinstance(error_detail, Exception):
                exc_tb = error_detail.__traceback__
            elif hasattr(error_detail, 'exc_info'):
                _, _, exc_tb = error_detail.exc_info()
        
        # Fallback to sys.exc_info() if no traceback details are found
        if exc_tb is None:
            _, _, exc_tb = sys.exc_info()
            
        if exc_tb:
            file_name = exc_tb.tb_frame.f_code.co_filename
            line_number = exc_tb.tb_lineno
            return f"Error in {file_name} , line number {line_number} : {error_message}"
        
        return error_message
    
    def __str__(self):
        return self.error_message
