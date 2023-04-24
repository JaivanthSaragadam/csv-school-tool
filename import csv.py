import csv
def write_into_csv(info_list):
    with open ('student_info.csv','a',new lines ='  ')as csv files:
        writer = csv.writer(csv_file)

        writer.writerow(info_list)
condition=True
while(condition):
    student_info = input("enter student information following format(Name age ocntact_number E-mail.ID:")
    print("entered information:"+student_info)

    #split
    student_info_list =student_info.split('   ')
    print ("entered split up information is:"+ str (student_info_list))

    write_into_csv(student_info_list)
    condition_check = input("enter (yes/no) if u want to enter for another :")
    if condition_check == "yes":
        condition = True
    elif condition_check=="no":
        condition = False
