import os
import sys
from src.mlops_project_setup.logger import logging

def get_error_details(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error Occured in python Script name [{0}] line number [{1}] error message[{2}]".format(filename,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message,error_details:sys):
        super().__init__(error_message)
        self.error_details = get_error_details(error_message,error_details)
    def __str__(self):
        return self.error_message