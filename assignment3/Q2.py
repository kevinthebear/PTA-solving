# tradingitemid 입력
def graphid(itemid):
    
    import pandas as pd
    import plotly.express as px
    
# 파일 불러오기
    close_price = pd.read_csv('close_price.csv')
    dividend = pd.read_csv('dividend_adjustment.csv')

# 데이터 타입 변환하기
    close_price['pricingdate'] = pd.to_datetime(close_price['pricingdate'])
    dividend['fromdate'] = pd.to_datetime(dividend['fromdate'])
    dividend['todate'] = pd.to_datetime(dividend['todate'])

# close price & dividend 파일 합치기
    temp_price_factor = pd.merge(close_price, dividend, on='tradingitemid', how='left')
    temp_price_factor[['fromdate']] = temp_price_factor[['fromdate']].fillna(pd.Timestamp('20180101'))
    temp_price_factor[['todate']] = temp_price_factor[['todate']].fillna(pd.Timestamp('20201231'))
    temp_price_factor[['divadjfactor']] = temp_price_factor[['divadjfactor']].fillna(value=1)

# close price & dividend 합친 후 날짜 맞추고 중복 값 제거하기
    mask = ((temp_price_factor['fromdate'] <= temp_price_factor['pricingdate']) 
            & (temp_price_factor['pricingdate'] <= temp_price_factor['todate'])) 
    price_factor = temp_price_factor.loc[mask]
    price_factor = price_factor.drop_duplicates(subset=['tradingitemid', 'pricingdate'])

# 날짜마다 tradingitemid의 수정가격을 보여주는 테이블
    processed_data = pd.DataFrame()
    processed_data['tradingitemid'] = price_factor['tradingitemid']
    processed_data['pricingdate'] = price_factor['pricingdate']
    processed_data['adjustedprice'] = price_factor['priceclose'] * price_factor['divadjfactor']

# tradingitemid의 수정가격의 동적 그래프를 생성하는 함수
    graph_data = processed_data.loc[processed_data['tradingitemid'] == itemid]

    fig = px.line(graph_data, x='pricingdate', y='adjustedprice', title= str(itemid) + ' Portfolio Value')

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
                ])
            )
        )
    
    fig.update_layout(xaxis_title='Date', yaxis_title='Value ($)')
    
    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=True,
            linecolor='black',
            linewidth=1.5,
            tickfont=dict(
                family='Arial',
                size=14,
                color='black',
                ),
            gridcolor='#F5F5F5',
            
            ),
        yaxis=dict(
            showgrid=True,
            showline=True,
            linecolor='black',
            linewidth=1.5,
            showticklabels=True,
            tickfont=dict(
                family='Arial',
                size=14,
                color='black',
                ),
            gridcolor='#F5F5F5',
            ),
        autosize=True,
        margin=dict(
            autoexpand=True,
            l=100,
            r=20,
            t=110,
            ),
        showlegend=True,
        plot_bgcolor='white'
        )
    
    fig.show()
    fig.write_html(str(itemid) + "portfoliovalue.html")

# 함수 예시 - 해당 함수를 실행하면 동적 그래프 파일이 생성된다
graphid(2590254)