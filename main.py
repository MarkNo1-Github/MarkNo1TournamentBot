
from tdbm.bot import Main
from dotenv import load_dotenv
import os
import tdbm


def get_config():
    load_dotenv()
    return dict(token=os.getenv('DEVELOP_TOKEN'))


if __name__ == '__main__':
    mybot = Main(get_config())
    mybot.run()
