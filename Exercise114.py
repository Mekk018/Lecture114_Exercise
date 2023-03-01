from forex_python.bitcoin import BtcConverter
import datetime
import matplotlib.pyplot as plt

print("โปรแกรมภาพรวมตลาดบิตคอยน์ภายใน 1 ปี")
print("-"*25)
print("EXAMPLE: Input start date")
print("Ex:Input year: 2016")
start_date_year = int(input("Input year: "))
print("Ex:Input month: 5")
start_date_month = int(input("Input month: "))
print("Ex:Input day: 19")
start_date_day = int(input("Input day: "))
print("-"*25)

b = BtcConverter()
start_date = datetime.date(start_date_year, start_date_month, start_date_day)
end_date = datetime.date(start_date_year+1, start_date_month, start_date_day)
result_price_list = b.get_previous_price_list("THB", start_date, end_date)

date_result = result_price_list.keys()
rate_result = result_price_list.values()

plt.figure("โปรแกรมภาพรวมตลาดบิตคอยน์")
plt.title("BTC CHART CHANGE (THB)")
plt.plot(date_result, rate_result)
plt.xlabel("DATE")
plt.ylabel("BTC / THB RATE")
plt.show()