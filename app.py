from  flask  import * 
app=Flask(__name__)
import ccpc as cp

@app.route('/get_recommendation')
def recommendation():
    return cp.prints()
if  __name__== "__main__":
     app.run()