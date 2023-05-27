from flask import Flask
FAI=Flask(__name__)
@FAI.route('/fp1')
def fp1():
    return "This is first project in flask"

if __name__=='__main__':
    FAI.run(debug=True)  
    