from flask import Flask, Markup, render_template, request
app = Flask(__name__)

@app.route('/',methods=['GET']) #url패턴
def main():
    return render_template('gugu.html')

@app.route('/gugu_result',methods=['POST'])
def gugu_result():
    dan = int(request.form['dan'])
    result=''
    for i in range(1,10):
        result += f'{dan}x{i}={dan*i}<br>'
    # html 태그를 인식하게 하는 함수
    result = Markup(result)
    return render_template('gugu_result.html',result=result)

if __name__ == '__main__':
    # 현재파일 ==>
    # __변수__  시스템변수
    # threaded를 True로 설정하면 신경망 모형을 불러오는 코드에서 에러가 발생하므로 False로 설정
    app.run(port=8000, threaded=False) #멀티스레스x