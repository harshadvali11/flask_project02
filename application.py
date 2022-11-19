from flask import Flask,render_template

AI=Flask(__name__)

@AI.route('/first')
def first():
    return render_template('h1.html',name='Ashu',age=2)

@AI.route('/second')
def second():
    return render_template('h2.html')

if __name__=='__main__':
    AI.run(debug=True)