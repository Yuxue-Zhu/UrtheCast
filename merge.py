Original_List = ['one', 'two', 'three']
Add_List = ['one', 'two', 'five', 'six']
Delete_List = ['two', 'five']
#Result_List = ['three', 'six', 'one'] 

def merge(l1,l2):
   
    ans = list(set(l1) | set(l2))
    for i in range(len(ans)-1):
        for j in range(i+1,len(ans)):
            if len(ans[j-1])<len(ans[j]):# in decent lenth order
                temp=ans[j]
                ans[j]=ans[j-1]
                ans[j-1]=temp
            elif len(ans[j-1])==len(ans[j]) and ans[j-1]<ans[j]: # if tie, reverse alphabetical
                temp=ans[j]
                ans[j]=ans[j-1]
                ans[j-1]=temp
    return ans
def main():
    for i in Delete_List:
        try: 
            
            Original_List.remove(i)
        except:
            pass
        try: 
            
            Add_List.remove(i)
        except:
            continue
    
    print(merge(Original_List,Add_List))


if __name__ == "__main__":
    main()