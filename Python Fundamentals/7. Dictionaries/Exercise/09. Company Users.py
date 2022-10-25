company_info = input().split(" -> ")

company_info_dict = {}

while not company_info[0] == "End":

    if company_info[0] not in company_info_dict:
        company_info_dict[company_info[0]] = []
    if company_info[1] not in company_info_dict[company_info[0]]:
        company_info_dict[company_info[0]].append(company_info[1])

    company_info = input().split(" -> ")

sorted_cmpny_inf = sorted(company_info_dict.items(), key=lambda by_name: by_name[0])

for tup in sorted_cmpny_inf:
    company_name, employee_id = tup
    print(company_name)
    for employee in employee_id:
        print(f"-- {employee}")

