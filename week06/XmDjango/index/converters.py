
class IntConverter:
    regex = '[0-9]+' #匹配正则

    def to_python(self,value):  #在url中获取，转给python 通过此功能 接收
        return int(value)

    def to_url(self,value): # 传回url
        return str(value)    
class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self,value):
        return int(value)
        
    def to_url(self,value):
        return '%04d' % value 