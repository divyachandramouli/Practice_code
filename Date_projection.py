#Date_projection.py
'''
Date Projection
Complete the which_date() function below which returns the day that follows a specified time period after an initial date. Time periods can be specified in two different ways: as a number of days like "1 day" or "30 days", or as a number of weeks like "2 weeks" or "12 weeks".


	'''
from datetime import datetime as dt
from datetime import timedelta 
def which_date(start_date,time):
    """
    This function takes as input a string depicting a date in YYYY/mm/dd
    format and a string stating a time period in the form of "X day(s)" or
    "Y week(s)". Output should be a string in form YYYY/mm/dd with the date
    that is X days or Y weeks after the initial date.
    """
    d=dt.strptime(start_date,"%Y/%m/%d")
    diff=time.split(" ")
    
    if ((diff[1]=="day") or (diff[1]=="day(s)") or (diff[1]=='days')):
    	n=int(diff[0])
    elif ((diff[1]=='week') or (diff[1]=='weeks') or (diff[1]=='week(s)')):
    	n=int(diff[0])*7
    else:
    	return "Invalid way of specifying"

    mod_date= d + timedelta(days=n)
    end_date=dt.strftime(mod_date,"%Y/%m/%d")
    print (end_date)
    return (end_date)



def test():
    """
    Here are a few tests to check if your code is working correctly! This
    function will be run when the Test Run button is selected. Additional
    tests that are not part of this function will also be run when the Submit
    Answer button is selected.
    """
    assert which_date('2016/02/10','35 days') == '2016/03/16'
    assert which_date('2016/12/21','3 weeks') == '2017/01/11'
    assert which_date('2015/01/17','1 week') == '2015/01/24'
    print("All tests completed.")


if __name__ == "__main__":
    test()
    












