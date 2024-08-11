def users(username,city):
    
    if type(username ) is not str:
        raise TypeError("username str tipinde olmalıdır")
    if type(city) is not str:
        raise TypeError("city str tipinde olmalıdır")
    

try:
    users("yusuf","eskişehir")
except Exception as e :
    print(e)        
