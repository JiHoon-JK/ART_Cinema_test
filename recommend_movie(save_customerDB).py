from pymongo import MongoClient
import random

client = MongoClient('localhost', 27017)
db = client.ART_Movie_Platform

# all_short_movie 라는 변수에 DB값 담기(지금 단편영화 db가 없어서 장편영화 db로 함)
all_short_movie = list(db.ART_movie_list.find({}))
#print(all_short_movie)

# 고객정보 임의 설정
customer_name = "스파르타1"
customer_Id = "sparta1"

#고객선택 장르 임의 설정
customer_genre1 = '스릴러'
customer_genre2 = '코미디'

#사용자 선호장르 단편영화 임시 리스트
temp_main_genre_movie = []
temp_second_genre_movie = []



for k in range(len(all_short_movie)):
        #단편영화 장르 값 입시로 저장해두기
        temp_genre1 = all_short_movie[k].get('genre_1').split('\n')[1]
        temp_genre2 = all_short_movie[k].get('genre_2').split('\n')[1]
        #print(all_short_movie[k].get('genre_1').split('\n')[1])
        #print(all_short_movie[k].get('genre_2').split('\n')[1])
        #만약에 고객 메인 장르와 단편영화의 임시장르가 같으면,
        if customer_genre1 == temp_genre1 or customer_genre1 == temp_genre2 :
            #그 영화들을 하나의 리스트로 모아둔다.
            temp_main_genre_movie.append(all_short_movie[k])
        # 만약에 고객 서브 장르와 단편영화의 임시장르가 같으면,
        if customer_genre2 == temp_genre1 or customer_genre2 == temp_genre2 :
            temp_second_genre_movie.append(all_short_movie[k])
        else:
            continue


#고객데이터
customer_info = {
    'name': customer_name,
    'Id': customer_Id,
    'main_genre': customer_genre1,
    'second_genre': customer_genre2,
}
#Customer 이라는 db에 고객정보들 저장
db.Customer.insert_one(customer_info)


#고객이 선호하는 장르 영화 리스트
print(temp_main_genre_movie)
print(temp_second_genre_movie)
#그 리스트 중에 샘플뽑기/ 첫번째 선호장르 영화3개 두번째 선호장르 영화 3개
print("첫번째 선호하는 장르영화는", customer_genre1)
print(random.sample(temp_main_genre_movie, 3)[0])
print(random.sample(temp_main_genre_movie, 3)[1])
print(random.sample(temp_main_genre_movie, 3)[2])

print("두번째 선호하는 장르영화는", customer_genre2)
print(random.sample(temp_second_genre_movie, 3)[0])
print(random.sample(temp_second_genre_movie, 3)[1])
print(random.sample(temp_second_genre_movie, 3)[2])


