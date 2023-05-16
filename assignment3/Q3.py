# tradingitemid 리스트 입력
def tradingchoropleth(*itemid):    

    import pandas as pd
    import plotly.express as px


# 파일 불러오기
    info = pd.read_csv('info.txt', delimiter = '|')

# info 파일에서 미국 회사 분류하기 및 중복 데이터 지우기
    usa_company = info[info['isocountry3'] == "USA"]
    usa_company.drop_duplicates(subset = 'tradingitemid', inplace = True, ignore_index = True)
    
# usa_company 정리하기
    del usa_company['companyname']
    del usa_company['city']
    del usa_company['isocountry3']
    del usa_company['webpage']
    usa_company.sort_values('state')
    
# usa_company state 이름 state code로 변환하기
    usa_company.loc[usa_company.state == "Alabama", "state"] = "AL"
    usa_company.loc[usa_company.state == "Alaska", "state"] = "AK"
    usa_company.loc[usa_company.state == "American Samoa", "state"] = "AS"
    usa_company.loc[usa_company.state == "Arizona", "state"] = "AZ"
    usa_company.loc[usa_company.state == "Arkansas", "state"] = "AR"
    usa_company.loc[usa_company.state == "California", "state"] = "CA"
    usa_company.loc[usa_company.state == "Colorado", "state"] = "CO"
    usa_company.loc[usa_company.state == "Connecticut", "state"] = "CT"
    usa_company.loc[usa_company.state == "Delaware", "state"] = "DE"
    usa_company.loc[usa_company.state == "District Of Columbia", "state"] = "DC"
    usa_company.loc[usa_company.state == "Florida", "state"] = "FL"
    usa_company.loc[usa_company.state == "Georgia", "state"] = "GA"
    usa_company.loc[usa_company.state == "Guam", "state"] = "GU"
    usa_company.loc[usa_company.state == "Hawaii", "state"] = "HI"
    usa_company.loc[usa_company.state == "Idaho", "state"] = "ID"
    usa_company.loc[usa_company.state == "Illinois", "state"] = "IL"
    usa_company.loc[usa_company.state == "Indiana", "state"] = "IN"
    usa_company.loc[usa_company.state == "Iowa", "state"] = "IA"
    usa_company.loc[usa_company.state == "Kansas", "state"] = "KS"
    usa_company.loc[usa_company.state == "Kentucky", "state"] = "KY"
    usa_company.loc[usa_company.state == "Louisiana", "state"] = "LA"
    usa_company.loc[usa_company.state == "Maine", "state"] = "ME"
    usa_company.loc[usa_company.state == "Maryland", "state"] = "MD"
    usa_company.loc[usa_company.state == "Massachusetts", "state"] = "MA"
    usa_company.loc[usa_company.state == "Michigan", "state"] = "MI"
    usa_company.loc[usa_company.state == "Minnesota", "state"] = "MN"
    usa_company.loc[usa_company.state == "Mississippi", "state"] = "MS"
    usa_company.loc[usa_company.state == "Missouri", "state"] = "MO"
    usa_company.loc[usa_company.state == "Montana", "state"] = "MT"
    usa_company.loc[usa_company.state == "Nebraska", "state"] = "NE"
    usa_company.loc[usa_company.state == "Nevada", "state"] = "NV"
    usa_company.loc[usa_company.state == "New Hampshire", "state"] = "NH"
    usa_company.loc[usa_company.state == "New Jersey", "state"] = "NJ"
    usa_company.loc[usa_company.state == "New Mexico", "state"] = "NM"
    usa_company.loc[usa_company.state == "New York", "state"] = "NY"
    usa_company.loc[usa_company.state == "North Carolina", "state"] = "NC"
    usa_company.loc[usa_company.state == "North Dakota", "state"] = "ND"
    usa_company.loc[usa_company.state == "Northern Mariana Is", "state"] = "MP"
    usa_company.loc[usa_company.state == "Ohio", "state"] = "OH"
    usa_company.loc[usa_company.state == "Oklahoma", "state"] = "OK"
    usa_company.loc[usa_company.state == "Oregon", "state"] = "OR"
    usa_company.loc[usa_company.state == "Pennsylvania", "state"] = "PA"
    usa_company.loc[usa_company.state == "Puerto Rico", "state"] = "PR"
    usa_company.loc[usa_company.state == "Rhode Island", "state"] = "RI"
    usa_company.loc[usa_company.state == "South Carolina", "state"] = "SC"
    usa_company.loc[usa_company.state == "South Dakota", "state"] = "SD"
    usa_company.loc[usa_company.state == "Tennessee", "state"] = "TN"
    usa_company.loc[usa_company.state == "Texas", "state"] = "TX"
    usa_company.loc[usa_company.state == "Utah", "state"] = "UT"
    usa_company.loc[usa_company.state == "Vermont", "state"] = "VT"
    usa_company.loc[usa_company.state == "Virginia", "state"] = "VA"
    usa_company.loc[usa_company.state == "Virgin Islands", "state"] = "VI"
    usa_company.loc[usa_company.state == "Washington", "state"] = "WA"
    usa_company.loc[usa_company.state == "West Virginia", "state"] = "WV"
    usa_company.loc[usa_company.state == "Wisconsin", "state"] = "WI"
    usa_company.loc[usa_company.state == "Wyoming", "state"] = "WY"
    
# 입력된 tradingitemid 리스트에 포함된 부분 추출하기
    states_of_itemid = usa_company[usa_company['tradingitemid'].isin(itemid)]    
  
# 각 tradingitemid가 속한 state의 개수 구하기 (state = 포함된 주, count = 각 주에 속한 회사 개수)
    states_num = states_of_itemid.groupby(states_of_itemid.columns.tolist(),as_index=False).size()
    del states_num['tradingitemid']
    states_num['count'] = states_num.groupby(['state'])['size'].transform('count')
    states_num.drop_duplicates(inplace = True)
    
# 해당하는 회사가 속한 미국의 주를 기준으로 하는 Choropleth map
    fig = px.choropleth(states_num, locations = states_num['state'], locationmode="USA-states", color = states_num['count'], scope="usa")
    
    fig.show()
    fig.write_html("states_including_tradingitemid.html")
    
# 함수 예시 - 해당 함수를 실행하면 Choropleth 파일이 생성된다
tradingchoropleth(2586256, 2588913, 49031561, 2587460, 2587024, 2587303)
    
    
    