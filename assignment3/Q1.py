import pandas as pd

# 파일 불러오기
close_price = pd.read_csv('close_price.csv')
dividend = pd.read_csv('dividend_adjustment.csv')
info = pd.read_csv('info.txt', delimiter = '|')

# 데이터 타입 변환하기
close_price['pricingdate'] = pd.to_datetime(close_price['pricingdate'])
dividend['fromdate'] = pd.to_datetime(dividend['fromdate'])
dividend['todate'] = pd.to_datetime(dividend['todate'])

# info 파일에서 미국 회사 분류하기 및 중복 데이터 지우기
usa_company = info[info['isocountry3'] == "USA"]
usa_company = usa_company['tradingitemid'].drop_duplicates()

# close price & dividend 파일에서 미국 회사 분류하기
usa_close_price = close_price[close_price['tradingitemid'].isin(usa_company)]
usa_close_price = usa_close_price.reset_index(drop = True)
usa_dividend = dividend[dividend['tradingitemid'].isin(usa_company)]
usa_dividend = usa_dividend.reset_index(drop = True)

# 각 회사의 t-1 시점 및 이에 해당하는 close price 찾아내기
firstdate = usa_close_price.loc[usa_close_price.groupby('tradingitemid')['pricingdate'].idxmin()]
firstdate.rename(columns = {'pricingdate' : 't-1 period', 'priceclose' : 't-1 priceclose'}, inplace = True)

# 각 회사의 t 시점 및 이에 해당하는 close price 찾아내기
lastdate = usa_close_price.loc[usa_close_price.groupby('tradingitemid')['pricingdate'].idxmax()]
lastdate.rename(columns = {'pricingdate' : 't period', 'priceclose' : 't priceclose'}, inplace = True)

# 각 회사의 t-1 시점과 t 시점 하나의 테이블로 정리하기
firstlast_close_price = pd.merge(left = firstdate, right = lastdate, on =['tradingitemid'])

# 위에서 정리한 t-1 시점 및 t 시점 테이블과 dividend 테이블 합치기
temp_price_factor = pd.merge(left = firstlast_close_price, right = usa_dividend, on = ['tradingitemid'], how = 'left')

# 합쳐진 테이블에서 blank 셀들 채워넣기
temp_price_factor[['fromdate']] = temp_price_factor[['fromdate']].fillna(pd.Timestamp('20180101'))
temp_price_factor[['todate']] = temp_price_factor[['todate']].fillna(pd.Timestamp('20201231'))
temp_price_factor[['divadjfactor']] = temp_price_factor[['divadjfactor']].fillna(value=1)

# t-1 시점 날짜에 해당하는 divadjfactor 찾고 정리하기
t1 = temp_price_factor.loc[(temp_price_factor['t-1 period'] >= temp_price_factor['fromdate']), ['tradingitemid', 't-1 period', 'fromdate', 'todate', 't-1 priceclose', 'divadjfactor']]
t1.drop_duplicates(subset = 'tradingitemid', inplace = True)
t1.rename(columns = {'fromdate' : 't-1 fromdate', 'todate' : 't-1 todate', 'divadjfactor' : 't-1 divadjfactor'}, inplace = True)

# t 시점 날짜에 해당하는 divadjfactor 찾고 정리하기
t = temp_price_factor.loc[(temp_price_factor['t period'] <= temp_price_factor['todate']), ['tradingitemid', 't period', 'fromdate', 'todate', 't priceclose', 'divadjfactor']]
t.drop_duplicates(subset = 'tradingitemid', inplace = True)
t.rename(columns = {'fromdate' : 't fromdate', 'todate' : 't todate', 'divadjfactor' : 't divadjfactor'}, inplace = True)

# 위에서 정리한 t-1 시점과 t 시점 테이블 하나로 합치기
closeprice_and_factor = pd.merge(left = t1, right = t, on = ['tradingitemid'])

# 주식의 수익 계산을 위한 processed data 테이블 만들기
processed_data = pd.DataFrame()
processed_data['tradingitemid'] = closeprice_and_factor['tradingitemid']
processed_data['Pt-1'] = closeprice_and_factor['t-1 priceclose'] * closeprice_and_factor['t-1 divadjfactor']
processed_data['Pt'] = closeprice_and_factor['t priceclose'] * closeprice_and_factor['t divadjfactor']
processed_data['Rt'] = (processed_data['Pt'] - processed_data['Pt-1']) / processed_data['Pt-1']

# Processed data 테이블에 state 열 추가하고 정리하기
processed_data = pd.merge(processed_data,info[['tradingitemid','state']],on='tradingitemid', how='left')
processed_data.drop_duplicates(subset = 'tradingitemid', inplace = True)
processed_data.sort_values('state')
processed_data.rename(columns = {'state' : 'USA states'}, inplace = True)

# 각 주에 속한 모든 회사들의 수익의 평균 구하고 테이블로 정리하기
mean_values = processed_data.groupby('USA states').mean()
del mean_values['tradingitemid']
del mean_values['Pt-1']
del mean_values['Pt']
state_average_revenue = mean_values.rename(columns = {'Rt' : 'Average revenue of companies in the state'})

# 해당 테이블 파일로 내보내기
state_average_revenue.to_csv('state_average_revenue.csv')
