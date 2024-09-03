# write a program to calculate monthly emi



loan_amount=100000

tenure=10

intrest_rate=5


print(loan_amount)
print(tenure)
print(intrest_rate)


 
intrest_rate=int (intrest_rate)/float(12*100)
emi= loan_amount*intrest_rate*(1+intrest_rate)**tenure/((1+intrest_rate)**tenure-1)
print(emi)

# totalintreastpayable
total_payable_amount=emi*tenure
print(f"monthly emi={emi}")
print(f"total amount= {total_payable_amount}")
total_intrest_payable=total_payable_amount-loan_amount
print(f"")


















