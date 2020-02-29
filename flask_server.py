from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.ART_Movie_Platform  # 'dbsparta'라는 이름의 db를 만듭니다.

app = Flask(__name__)


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
def Long_Movie_listing():
    result = list(db.Long_movie_list.find({}, {'_id': 0}))
    # articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result': 'success', 'Long_movie_list': result})


@app.route('/art_user_genre_1', methods=['GET'])
def ART_Movie_listing_genre_1():
    # genre_1_give 로 사용자의 최종 선호 장르_1 대입
    # 일단 임시로, "드라마"로 테스트
    genre_1_movie_infos = list(db.ART_movie_list.find({'genre_1': '<장르1>' + '\n' + '드라마'}, {'_id': 0}))
    print(genre_1_movie_infos)
    for i in genre_1_movie_infos:
        i['poster_url'] = str(i['poster']).split('\n')[1]
    print(genre_1_movie_infos)

    return jsonify({'result': 'success', 'info': genre_1_movie_infos})

@app.route('/art_user_genre_2', methods=['GET'])
def ART_Movie_listing_genre_2():
    # genre_2_give 로 사용자의 최종 선호 장르_2 대입
    # 임시로, "멜로/애정/로맨스"로 테스트
    genre_2_movie_infos = list(db.ART_movie_list.find({'genre_2': '<장르2>' + '\n' + '멜로/애정/로맨스'}, {'_id': 0}))
    print(genre_2_movie_infos)
    for i in genre_2_movie_infos:
        i['poster_url'] = str(i['poster']).split('\n')[1]
    print(genre_2_movie_infos)

    return jsonify({'result': 'success', 'info': genre_2_movie_infos})


# API 역할을 하는 부분
@app.route('/user', methods=['POST'])
def saving():
    email = request.form['email']
    pwd = request.form['pwd']
    data = {
        'email': email,
        'pwd': pwd
    }

    db.userdb.insert_one(data)
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
