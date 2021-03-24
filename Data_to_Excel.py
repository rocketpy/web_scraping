import xlsxwriter


# pip install XlsxWriter

date = time.strftime("%d%m_%H%M", time.localtime())
writer = pd.ExcelWriter('1_'+date+'.xlsx', engine='xlsxwriter')
print('Current time', date)
