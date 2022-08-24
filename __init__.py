#!/urs/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

def shisha_gonyu(value,digit,type_=str,decimal_bool=True):
    """
    ひとつの値だけでなく、配列に関しても四捨五入するための関数
    value : float, int, str, list, numpy.ndarrayのいずれかで指定
    digit : 四捨五入する桁数
    type_ : 出力する際のデータ型 (ex. float, int)
    decimal_bool : 小数点以下の四捨五入か否か。Falseの場合は整数桁に関して四捨五入が行われる。
    """        

    if type(value) in [float,int,str]:
        if decimal_bool:
            one_value = one_decimal(value,digit,type_=type_)
        else:
            one_value = one_integer(value,digit,type_=type_)
        return one_value
    
    else:
        value = np.array(value)
        size = value.size
        shape = value.shape
        raveled_value = value.ravel()
        return_value = []
        for i in range(size):
            if decimal_bool:
                one_value = one_decimal(raveled_value[i],digit,type_=type_)
            else:
                one_value = one_integer(raveled_value[i],digit,type_=type_)
            return_value.append(one_value)
            
        return_value = np.array(return_value,dtype=type_).reshape(shape)
        return return_value

def one_decimal(value,digit,type_=str):
    """
    ひとつの値に関して小数点以下を四捨五入するための関数
    value : float, str, のいずれかで指定
    digit : 四捨五入した結果の小数点以下の桁数　(整数->0, 小数点第一位->1, 小数点第二位->2,...)
    type_ : 出力する際のデータ型 (ex. float, int)
    """        
    if digit==0:
        decimal_value = '0'
    else:
        decimal_value = '1'
        for i in range(digit-1):
            decimal_value = '0'+decimal_value
        decimal_value = '0.'+decimal_value
    decimal_object = Decimal(str(value)).quantize(Decimal(decimal_value),rounding=ROUND_HALF_UP)
    return_value = np.array([decimal_object],dtype=type_)[0]
    return return_value

def one_integer(value,digit,type_=str):
    """
    ひとつの値に関して整数の各位で四捨五入するための関数
    value : float, int, str のいずれかで指定
    digit : 四捨五入する位の数 (1の位->1, 10の位->2, ...)
    type_ : 出力する際のデータ型 (ex. float, int)
    """        
    decimal_value = f'1E{digit}'
    decimal_object = Decimal(str(value)).quantize(Decimal(decimal_value),rounding=ROUND_HALF_UP)
    return_value = int(decimal_object)
    return return_value
