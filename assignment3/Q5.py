# 학교 이름 입력
def schoolname(schoolname):
    
    import pandas as pd
    
# 파일 불러오기
    player_info = pd.read_csv('player_info.csv')

# 해당 학교를 다니는 NBA 선수
    player_school = player_info[player_info['school'] == schoolname]

# 활동하는 선수들
    active_players = player_school[player_school['rosterstatus'] == 'Active']

# 활동하지 않는 선수들
    inactive_players = player_school[player_school['rosterstatus'] == 'Inactive']

# 활동하는 선수들의 평균 경력
    print("\n활동하는 선수들의 평균 경력:", active_players['season_exp'].describe()['mean'])
    
# 활동하지 않는 선수들의 평균 경력
    print("활동하는 않는 선수들의 평균 경력:", inactive_players['season_exp'].describe()['mean'])
          
# 함수 예시
schoolname('UCLA')