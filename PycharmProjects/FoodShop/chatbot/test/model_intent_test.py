from chatbot.Preprocess2 import Preprocess2
from chatbot.IntentModel import IntentModel

p = Preprocess2(word2index_dic='c:/Users/user/PycharmProjects/FoodShop/chatbot/data/chatbot_dict.bin',
                userdic='c:/Users/user/PycharmProjects/FoodShop/chatbot/data/user_dic.tsv')
intent = IntentModel(model_name='c:/Users/user/PycharmProjects/FoodShop/chatbot/train/intent_model.keras', proprocess=p)

items=['오늘 탕수육 주문 가능한가요?','여행 가고 싶어요.',
       '다음주 일요일로 변경가능한가요?','안녕하세요']

for item in items:
    predict = intent.predict_class(item)
    predict_label = intent.labels[predict]
    print(item)
    print("의도 예측 클래스 : ", predict)
    print("의도 예측 레이블 : ", predict_label)