from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.ART_Movie_Platform  # 'dbsparta'라는 이름의 db를 만듭니다.

app = Flask(__name__)

all_long_movie = list(db.Long_movie_list.find({}))

# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('main.html')


@app.route('/page2')
def page2():
    return render_template('page2.html')


@app.route('/page3')
def page3():
    return render_template('page3.html')


@app.route('/user', methods=['GET'])
def listing():
    result = list(db.Long_movie_list.find({}, {'_id': 0}))
    # articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result': 'success', 'Long_movie_list': result})


@app.route('/main', methods=['GET'])
def listing2():
    result = list(db.ART_movie_list.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'ART_movie_list': result})


# API 역할을 하는 부분
@app.route('/user', methods=['POST'])
def saving():
    email = request.form['email']
    pwd = request.form['pwd']
    genre_1 = request.form['genre_1']
    genre_2 = request.form['genre_2']

    data = {
        'email': email,
        'pwd': pwd,
        'genre_1': genre_1,
        'genre_2': genre_2
    }

    db.userdb.insert_one(data)
    return jsonify({'result': 'success'})


# @app.route('/user2', methods=['GET'])
# def listing3():
#     # 모든 document 찾기 & _id 값은 출력에서 제외하기
#     result = list(db.customer_genre.find({}, {'_id': 0}))
#     # genres라는 키 값으로 영화정보 내려주기
#     return jsonify({'result': 'success', 'genres': result})



@app.route('/user2', methods=['POST'])
def genre_cnt():
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
    choice_title = request.form['m_title_give']
    print("test")
    print(choice_title)

    for i in range(len(all_long_movie)):
        if choice_title == all_long_movie[i].get('title').split('\n')[1]:
            selected_main_genre = all_long_movie[i].get('main_genre').split('\n')[1]
            selected_second_genre = all_long_movie[i].get('second_genre').split('\n')[1]
            for key in genre_score:
                if selected_main_genre == key:
                    genre_score[key] = genre_score[key] + 2

                if selected_second_genre == key:
                    genre_score[key] = genre_score[key] + 1

    print(genre_score)

    # 결과 값 도출
    result = sorted(genre_score.items(), key=lambda x: x[1], reverse=True)
    #print(result)
    customer_main_genre = result[0][0]
    customer_second_genre = result[1][0]
    print("첫번째 선호하는 장르는", customer_main_genre)
    print("두번째 선호하는 장르는", customer_second_genre)

    genre_data = {
        'main_genre': customer_main_genre,
        'second_genre': customer_second_genre
    }
    db.customer_genre.insert_one(genre_data)
    # db.customer_genre.update_one(genre_data)

    return jsonify({'result': 'success'})




@app.route('/userupdate', methods=['POST'])
def update():
    genre_1 = request.form['genre_1']
    genre_2 = request.form['genre_2']

    db.userdb.update_one({'genre_1': ''}, {'$set': {'genre_1': genre_1}})
    db.userdb.update_one({'genre_2': ''}, {'$set': {'genre_2': genre_2}})

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)