# coding:utf-8
# from django.test import TestCase
#
# # Create your tests here.

import os, sys

sys.path.append('./spy_utils')



if __name__ == '__main__':
    from spy_utils.spyder import ViopubSpyderApiManager

    # _test2 = ViopubSpyderApiManager(city_short='hb', vpid='42000210000000373477').get_detail()
    _test = ViopubSpyderApiManager(city_short='sc', vpid='5109002400540126').get_list()

