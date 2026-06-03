import argparse
# I need to command that python CLI_Data_Paraor.py employees.csv
# python CLI_Data_Paraor.py employees.csv --min-salary 100000

def main():
   r = argparse.ArgumentParser(
      description="A native Python CLI tool to parse and filter employee data."
   )

   r.add_argument(
      "filepath",
      help="the path to the CSV file i want to parse"
   )
   r.add_argument(
      "--min-salary",
      type = int,
      default =0,
      help="Filter out employees making less than this amount (default:0)"
   )

   args = r.parse_args()

   print(f"Target file: {args.filepath}")
   print(f"Minimum salary filter: {args.min_salary}")

   f = open(args.filepath).read()
   lines = f.splitlines()
   del f

   headers = lines[0].split(',')
   

   parsed_data =[]
  

   for line in lines[1:]:
      if not line.strip():
         continue
      raw_data = tuple(line.split(','))
      data = (raw_data[0],raw_data[1],raw_data[2],int(raw_data[3]))
      parsed_data.append(data)
      

   
   # new_list = []
   # for row in parsed_data[0:]:
   #    if(row[3] >= args.min_salary):
   #       new_list.append(row)
   new_list = [row for row in parsed_data if row[3] >= args.min_salary]
   # departments = set()
   # for row in new_list[0:]:
   #    departments.add(row[2])
   departments = {row[2] for row in new_list} # this is use of comprehension
      
   d={}
   for row in new_list[0:]:
      for department in departments:
        if(department == row[2]):
           x= row[0]
           d[x] = department
   for department in departments:
      print(f"[{department}]")
      for employee,dept in d.items():
         if dept == department:
            for row in new_list:
               if row[0] == employee:
                  print(f" - {row[0]} (Age: {row[1]}, Salary: ${row[3]})")
      print()
      
             
  
         

      
      
      



if __name__ == "__main__":
   main()
