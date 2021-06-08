import sys, os
from skillshare import Skillshare
from stm import cookie

# or by class ID:
# dl.download_course_by_class_id(189505397)

def main(cookie):
    temp = sys.argv[2]
    if len(temp) != 0:
        cookie = temp
    #trial
    ###
    dl = Skillshare(cookie)
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


def info():
    print(r"""	 
                                                        
HELLO Happy to see you !

                """)


if __name__ == "__main__":
    info()
    main(cookie)
