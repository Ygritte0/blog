#-*-coding:utf-8-*-
from printing_models import print_models as a
from printing_models import show_completed_models as b

unprinted_designs = ['random','condom']
completed_models = []
a(unprinted_designs,completed_models)
b(completed_models)