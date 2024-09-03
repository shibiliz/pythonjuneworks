employee={"name":"shibili","dept":"r&d","salary":"56666","combo_offer":"5777","extra_work days":2}
for k,v in employee.items():

    print(k,v)

# print employee netpay

if "extra_working_days" in employee:

    net_pay=employee.get("salary")+employee.get("combo_offer")*employee.get("extra_working_days")
    print(net_pay)

else:

    net_pay=employee.get("salary")
    print(net_pay)
