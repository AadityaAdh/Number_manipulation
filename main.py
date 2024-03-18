class num_manipulation:
    def __init__(self,value):
        self.value=value

    def calclen(self):
        value=self.value
        i=10
        count=2
        while(True):
            if(value/i<10):
                break
            i=i*10
            count +=1
        return(count)

    def bitwise(self):
        my_len=self.calclen()
        value=self.value

        element=value
        x=1


        while(True):
            some=element/(10**(my_len-x))
            first=int(some)
            print(first)
            element=element%(10**(my_len-x))
            x +=1

            if(element<=0):
                break

    def nomanipulation(self,bit,rep_value):
        my_len = self.calclen()
        value = self.value

        element = value
        x = 1
        counter=0
        my_int_value=''

        while (True):
            some = element / (10 ** (my_len - x))
            first = int(some)

            counter += 1

            if (counter==int(bit)):
                first=int(rep_value)

            my_int_value=my_int_value+str(first)



            element = element % (10 ** (my_len - x))
            x += 1

            if (element <= 0):
                return my_int_value
                break











val=input("Enter your value\n")
val=int(val)
number1=num_manipulation(val)
while(True):
    print("1.Bit wise values \n")
    print("2.No manipulation \n")
    print("3.Length of my value \n")
    print("4.Exit \n")

    choice=input("Input your choice \n")
    choice=int(choice)

    match choice:
        case 1:

            number1.bitwise()
        case 2:
            print("your original number is \n {}\n".format(number1.value))
            bitt=input("enter the position where you want replacement \n")
            rep_valuee=input("enter the value with which you want to replace \n")
            print(number1.nomanipulation(bitt,rep_valuee))
        case 3:
            print(number1.calclen())

        case 4:
            break

