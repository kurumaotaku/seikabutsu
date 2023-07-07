from flask import Flask
from flask import render_template
from flask import request
 
app = Flask(__name__)
 
 #ウォークスルーページ
@app.route('/')
def index():
    return render_template('index.html')

#成果物一覧画面
@app.route('/main')
def Main():
    return render_template('main.html')

#Fizzbuzz
@app.route('/fizzbuzz')
def fizzbazz():
    return render_template('fizzbuzz.html',nyuryokuti = "僕がフィズバズくんだよ")

#fizzbuzz 本体
@app.route('/fizzbuzz_post',methods=['POST'])
def fizzbuzz_post():
    nyuryokuti = request.form['fizzbuzz_input']
    print(nyuryokuti + "が入力されました")

    
    if len(nyuryokuti) < 6:
        try:
            nyuryokuti = int(nyuryokuti)
            
        except ValueError:
            nyuryokuti = "数値入れてね。それ以外はだめ"

        if type(nyuryokuti) == int:
            if nyuryokuti % 15 == 0:
                nyuryokuti = "Fizzbuzzですねえ"

            elif nyuryokuti % 5 == 0:
                nyuryokuti = "Buzzですね"

            elif nyuryokuti % 3 == 0:
                nyuryokuti = "Fizzだよ"

            else:
                nyuryokuti = str(nyuryokuti) + "やねえ。どの倍数でもないね"

    else:
        nyuryokuti = "5ケタ以内にしてよ"

    return render_template('fizzbuzz_post.html',nyuryokuti=nyuryokuti)

#階乗
@app.route('/kaijo',methods=["GET"])
def kaijo():
    nyuryokuti = "僕が階乗くんだよ"
    return render_template('kaijo.html',nyuryokuti = nyuryokuti)

@app.route('/kaijo_post',methods=["POST"])
def kaijo_post():
    nyuryokuti = request.form['kaijo_input']
    try:
        nyuryokuti = int(nyuryokuti)
    
    except ValueError:
        nyuryokuti = "数字入れてね"
    
    if type(nyuryokuti) == int:
        if nyuryokuti >= 30:
            nyuryokuti = "さすがにわからんわ"

        elif nyuryokuti == 0 or nyuryokuti == 1:
            nyuryokuti = "1やんねえ。直観に反するよね"

        elif nyuryokuti <= 0:
            nyuryokuti = "正の整数でたのむ"

        else:
            RUIJO = nyuryokuti

            for i in range(nyuryokuti):
                if nyuryokuti == RUIJO:
                    kekka = RUIJO * (RUIJO - 1)
                    RUIJO = RUIJO - 1

                elif nyuryokuti >= RUIJO and RUIJO != 1:
                    kekka = kekka * (RUIJO - 1)
                    RUIJO = RUIJO - 1

                else:
                    break

            nyuryokuti = kekka

    return render_template("kaijo_post.html",nyuryokuti = nyuryokuti)

if __name__ == '__main__':
    app.run()
