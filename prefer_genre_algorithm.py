# 장편영화를 이용하여, 고객 선호 장르를 파악하는 알고리즘 만들기
from pymongo import MongoClient
import random

client = MongoClient('localhost', 27017)
db = client.Short_Movie_Platform

# all_long_movie 라는 변수에 DB값 담기
all_long_movie = list(db.Long_movie_1.find({}))

# result = list(db.Long_movie_1.find({status : "title"}))
# print(result)
# all_main_genre 라는 변수에 main_genre DB값 담기(이것도 코드가 맞는지 모르겠오)
# all_main_genre = list(db.Long_movie_1.find(['main_genre']))
# all_second_genre 라는 변수에 second_genre DB값 담기
# all_second_genre = list(db.Long_movie_1.find(['second_genre']))

# 성공 print(all_long_movie)
# print(all_main_genre)
# print(all_second_genre)

# 장르마다 점수 값 배정
genre_score = {
    '드라마': 0,
    '판타지': 0,
    '공포': 0,
    '멜로/애정/로맨스': 0,
    '모험': 0,
    '스릴러': 0,
    '느와르': 0,
    '다큐멘터리': 0,
    '코미디': 0,
    '가족': 0,
    '미스터리': 0,
    '전쟁': 0,
    '에니메이션': 0,
    '범죄': 0,
    '뮤지컬': 0,
    'SF': 0,
    '액션': 0
}
for i in range(15):
    a = 1
    while a <= 20:
        # 두개랜덤뽑아서 출력
        comparison_movie = random.sample(all_long_movie, 2)
        comparison_movie_1 = comparison_movie[0]
        comparison_movie_2 = comparison_movie[1]

        comparison_movie_1_main_genre = comparison_movie_1['main_genre']
        comparison_movie_1_second_genre = comparison_movie_1['second_genre']
        comparison_movie_2_main_genre = comparison_movie_2['main_genre']
        comparison_movie_2_second_genre = comparison_movie_2['second_genre']

        if comparison_movie_1['main_genre'] == comparison_movie_2['main_genre']:
            continue
        elif comparison_movie_1['main_genre'] != comparison_movie_2['main_genre']:
            break

    # 장르 겹치는지 확인 -> 성공
    # for key in genre_score:
    #     print(key, end=' ')

    for key in genre_score:
        a = comparison_movie_1_main_genre.split('\n')[1]
        b = comparison_movie_1_second_genre.split('\n')[1]
        #print(key)
        #print(a)
        #print(b)
        if a == key:
            genre_score[key] = genre_score[key] + 2

        if b == key:
            genre_score[key] = genre_score[key] + 1

    print(genre_score)
