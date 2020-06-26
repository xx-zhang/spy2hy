# coding:utf-8
# from django.test import TestCase
#
# # Create your tests here.

import os, sys

sys.path.append('./spy_utils')


if __name__ == '__main__':
    from spy_utils.spyder import ViopubSpyderApiManager
    _test = ViopubSpyderApiManager(city_short='bj', vpid='11000210000000478873').get_detail()
    print(_test)