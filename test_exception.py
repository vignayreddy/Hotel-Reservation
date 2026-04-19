from src.custom_exception import CustomException
from src.logger import get_logger
import sys 


logger = get_logger(__name__)
def divide_number(a,b):
    try:
        result = a/b 
        logger.info("Dividing two numbers")
    except Exception as e:
        logger.error("Dividing by zero error occured")
        raise CustomException("Custom Error zero",sys)

if __name__=="__main__":
    try:
        logger.info("starting main program")
        divide_number(10,0)
    except CustomException as e:
        logger.error(str(e))
