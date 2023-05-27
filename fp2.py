from flask import Flask

FAI=Flask(__name__)

@FAI.route('/fp2')
def fp2():
    return 'This is project2 in flask'

if __name__=='__main__':
    FAI.run(debug=True)