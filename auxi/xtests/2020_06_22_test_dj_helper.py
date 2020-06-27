# coding:utf-8
import os
import sys
import django


def django_setup():
    DjangoModulePath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.append(DjangoModulePath)
    os.chdir(DjangoModulePath)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
    django.setup()


if __name__ == '__main__':
    pass


