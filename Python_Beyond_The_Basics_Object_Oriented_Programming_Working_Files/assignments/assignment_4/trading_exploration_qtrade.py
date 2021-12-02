# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 17:40:16 2021

@author: umave
"""
from questrade_api import Questrade
token = '_VwpZkDjqDza9DzAqgLd2p9CJ5BYrGRa0'
# q = Questrade(refresh_token=token)
q = Questrade(refresh_token = token)
accounts = q.accounts


user_id = accounts['userId']
margin_acc_number = int(accounts['accounts'][0]['number'])
current_margin_positions = q.account_positions(margin_acc_number)['positions']

