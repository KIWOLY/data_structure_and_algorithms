def find_first_occurrence(my_list, num):
    if num not in my_list:
        return None
    for i in range(len(my_list)):
        if my_list[i]==num:
            return i
if __name__=="__main__":       
   my_list=[5,7,9,3,1,10,8,6,4,2,0]
   num=int(input("enter a number: "))
   print(find_first_occurrence(my_list, num))
 
