class FourDigitYearConverter:

    regex = '[0-9]{4}'

    def to_python(self,value):
        return int(value)

    def to_url(self, value):
        return f'{value:4d}'
    
    # value: is for slicing value
    #4 for width or digit or index 4
    #d for integer