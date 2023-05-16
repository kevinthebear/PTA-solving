# 팀 이름 입력
def teamname(team_abbreviation):

    import pandas as pd
    pd.options.mode.chained_assignment = None

# 파일 불러오기
    games = pd.read_csv('games.csv')

# 데이터 타입 변환 및 날짜 적용하기
    games['GAME_DATE'] = pd.to_datetime(games['GAME_DATE'])
    games = games[games['GAME_DATE'] >= '2010-01-01']

# 입력 받은 팀의 원정경기
    homegame = games[games['MATCHUP'].str.contains('@', na=False)]
    gamewithtarget =  homegame[homegame['MATCHUP'].str.contains(str(team_abbreviation) + ' @', na=False)]

# 원정경기 상대팀 구하기
    gamewithtarget
    gamewithtarget['TARGET_TEAM'] = gamewithtarget['MATCHUP'].str.slice(start=-3)

# 입력 받은 팀이 진 경우 구하기
    gamewithtarget = gamewithtarget[gamewithtarget['WL'] == 'L']

# 입력 받은 팀 상대로 가장 많이 우승한 팀 (최악의 상대팀)
    worstopponent = gamewithtarget['TARGET_TEAM'].value_counts()[:1].index.tolist()

# 최악의 팀을 상대로 평균 득점 PTS 구하기
    worstopponentgames = gamewithtarget[gamewithtarget['TARGET_TEAM'].isin(worstopponent)]
    worstopponent_and_avgpts = worstopponentgames.groupby('TARGET_TEAM')['PTS'].mean()
    print('\nThe following is the worst opponent team, and the PTS value against this team.\n')
    print(worstopponent_and_avgpts)
    
# 함수 예시 - 해당 함수를 실행하면 최악의 팀과 그 팀을 상대로 한 평균 득점이 나온다.
teamname('ATL')
