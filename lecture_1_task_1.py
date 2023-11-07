#lecture_1

#Implement decorator function for ping 

from pythonping import ping
import subprocess

def repeat_operation(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat_operation(3)
def alive_site():
    output = subprocess.check_output(["ping","-c","1","-q","8.8.8.8"])
    print(output)

alive_site()



    