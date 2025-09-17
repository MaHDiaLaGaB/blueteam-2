
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="cyberspace.log",
    filemode="w"
)

logging.debug("this is debug log")
logging.info("this is info log")
logging.warning("this is warning log")
logging.error("this is error log")


def sum_even_nums(nums: list):
    logging.info("the function started")
    even = []
    logging.debug(f"the even list: {even}")
    for num in nums:
        logging.info(f"the number is: {num}")
        if num % 2 == 0:
            logging.info(f"this is even number {num}")
            even.append(num)
    logging.info(f"the sum of even is: {sum(even)}")
    return sum(even)

my_list = [x for x in range(1, 30)]
sum_even_nums(my_list)