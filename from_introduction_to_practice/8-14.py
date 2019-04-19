#-*-coding:utf-8-*-
# 参数前加**，可创造关键字参数
def info_of_car(car_maker,car_model,**car_info):
    car = {}
    car['maker'] = car_maker
    car['model'] = car_model
    for key , value in car_info.items():
        car[key] = value
    return car

print(info_of_car('一汽大众','越野',color='black',tow_packeage=True))