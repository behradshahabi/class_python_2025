import json

def save_json(input_dict):
    with open (rf"data\task.json", "a") as f :
        json.dump(input_dict, f)
    print ("your data saved ")


date = input("lotafan tarikh ra vared koni (YYYY-MM-DD) :   ")
tasks = input("lotafan kar hayi ke anjam dadid ra benevisid va anha ra ba virgool joda konid :  ")


my_tasks_dict = {date: tasks.split(","),}
save_json(my_tasks_dict)