from book_gym import Gym_Book
from config import opts_init


if __name__ == '__main__':
    opts = opts_init()
    gym_book = Gym_Book()
    if opts.mode == 'order':
        gym_book.seckill()
    else:
        gym_book.order_info()
