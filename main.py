from twitter_module import *
from discord_module import *
import time
from twit import *
from logger import *


ds_tokens = 'kek', 'lol'
ds_token = "OTQwMjA4NzQ1OTY1ODM4Mzg4.YgED3g.ZYJ3RLlwB3MaS8RK4yiIxhPuS8Y"
twit_tokens = 'Bj9mKtA1LsOAvFe4sJDARGpZT', 'Qx2igZISfiA5adG9H92P3taVEWeErAgydV5PzS8rfEmnge8aIQ', "1348038487509921792-qtzPEKSRoqCRrKVvZZQP7PWAV4seNx", "dZ5nqyoSXchgCU9HuMNqt7jkPdgfY3TpFPKawDJjiH9eQ"
username = 'Tison1337'


if __name__ == '__main__':
    with open('invite.txt', 'r') as f:
        old_inv = f.read()
        logger.info('OLD INV LOADED: '+old_inv)

    while True:
        inv_code = get_inv_code(parse(twit_tokens[0], twit_tokens[1],twit_tokens[2],twit_tokens[3], username))

        if inv_code != old_inv and inv_code != '-1':
            logger.info('NEW CODE')
            # print(retrieve_text(link))
            # inv_code = '5Rn8Ys7M'
            for token in ds_tokens:
                try:
                    logger.info(token)
                    logger.info(accept_invite(token, inv_code))
                except Exception as e:
                    logger.info(e)
            with open('invite.txt', 'w') as f:
                f.flush()
                f.write(inv_code)

        time.sleep(5)