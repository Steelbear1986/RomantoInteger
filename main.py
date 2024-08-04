class Solution:
    def romanToInt(self, s: str) -> int:
        dict= {900:'CM',400:'CD',90:'XC',40:'XL',4:'IV',9:'IX',1000:'M',500:'D',100:'C',50:'L',10:'X',5:'V',1:'I'}
        c=0
        for key, value  in   dict.items():
            while value in s :
                  s=s.replace(f'{value}','',1)
                  c+=key
        return c