'''
https://blog.csdn.net/qq894492015/article/details/78772039
#include <stdio.h>
int irn;
//判断是闰年还是平年，闰年返回1，平年返回0
int isRunNian(int *y)
{
    //判断是否为闰年
    if((*y%4==0 && *y%100!=0) || *y%400==0) //如果是闰年
    {
        return (1);
    }else //如果是平年
    {
        return (0);
    }
}
void yesterday(int *y, int *m, int *d)
{
    int day=*d-1;
    int month=*m;
    int newYear=*y;
    if(day==0){
        month=*m-1;
        if(month==0){
            newYear=*y-1; month=12;day=31;
        }else{
            if(month==1 || month==3 || month==5 || month==7 || month==8 || month==10){
                day=31;
            }else if(month==4 || month==6 || month==9 || month==11){
                day=30;
            }else if(month==2){
                irn=isRunNian(y);
                if(irn==1){
                    day=29;
                }else{
                    day=28; 
                }
            }
        }
    }
    printf("昨天是%d年%d月%d日。\n", newYear,month,day);
}
void tomorrow(int *y, int *m, int *d)
{
    int newDay=*d+1;
    int newMonth=*m;
    int newYear=*y;
 
    if(*m==1 || *m==3 || *m==5 || *m==7 || *m==8 || *m==10 || *m==12)
    {
        if(*d==31)
        {
            if(*m==12)
            {
                newYear=*y+1;
                newMonth=1;
                newDay=1;
            }
        }
    }else if(*m==4 || *m==6 || *m==9 || *m==11)
    {
        if(*d==30)
        {
            newDay=1;
            newMonth=*m+1;
        }
    }else if(*m==2)
    {
        irn=isRunNian(y);
        if(irn)
        {
            if(*d==29)
            {
                newDay=1; newMonth=*m+1;
            }
        }else{
            if(*d==28)
            {
                newDay=1; newMonth=*m+1;
            }
        }
    }
    printf("明天是%d年%d月%d日。", newYear,newMonth,newDay);
}
 
 
void main()
{
    int y=0,m=0,d=0;
    int irn;
    printf("请输入年份");scanf("%d",&y);
    while(y<1)
    {   
         printf("请重新输入年份");scanf("%d",&y);
    }
    irn=isRunNian(&y);
    printf("请输入月份"); scanf("%d",&m);
    while(m<1 || m>12)
    {
        printf("请重新输入月份"); scanf("%d",&m);
    }
    printf("请输入日期"); scanf("%d",&d);
    do{
        if(d<1 || d>31)
        {
            printf("请重新输入日期"); scanf("%d",&d);
        }else
        {
            if((m==4 || m==6 || m==9 || m==11) && d==31)
            {
                printf("输入错误，%d月没有%d天，请重新输入日期",m,d); scanf("%d",&d);
            }else if(m==2)
            {
                
                if(irn==0 && d>28)
                {
                    printf("输入错误，%d是平年，%d月没有%d天，请重新输入日期",y,m,d); scanf("%d",&d);
                }else if(irn==1 && d>29)
                {
                    printf("输入错误，%d是闰年，%d月没有%d天，请重新输入日期",y,m,d); scanf("%d",&d);
                }else
                {
                    break;
                }
            }else
            {
                break;
            }
        }
    }while(1);
 
    printf("您输入的是%d年%d月%d日\n", y,m,d);
 
    yesterday(&y,&m,&d);
 
    tomorrow(&y,&m,&d);
 
    putchar('\n');
}
'''

flag = 0
def isRunNian(years):
    if years%400 == 0 or (years%4 == 0 and years%100!=0):
        return True
    else:
        return False
def yesterday(y,m,d):
    day = d-1
    month = m
    newYear = y
    if day == 0:
        month = m -1
        if month == 0:
            newYear = y - 1
            month = 12
            day = 31
        else:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
                day = 31
            elif month == 4 or month == 6 or month == 9 or month == 11:
                day = 30
            elif month == 2:
                flag = isRunNian(y);
                if flag == 1:
                    day = 29
                elif flag == 0:
                    day =28
    print("昨天是{0}年{1}月{2}日".format(newYear,month,day))
 
    
while True:
    y = input("Please input a year integer greater than or equal to 1000 and less than equal 3000:")
    
    
    if y.isdigit() and 1000<=int(y)<=3000:
        m = input("Please input a year integer greater than or equal to 1 and less than equal 12:")
        if m.isdigit() and 1<=int(m)<=12:
            d = input("Please input a year integer greater than or equal to 1 and less than equal 31:")
            if d.isdigit() and 1<=int(d)<=31:
                print("Congratulations!All integers are correct!!")
                break
            else:
                print("Wrong d 1000<=interger<=3000")
                print("Please re-enter from scratch")
        else:
            print("Wrong m 1<=interger<=12")
            print("Please re-enter from scratch")                
    else:
        print("Wrong y 1<=interger<=31")
        print("Please re-enter from scratch")
 
print("您输入的是{0}年{1}月{2}日".format(int(y),int(m),int(d)))
yesterday(int(y),int(m),int(d))