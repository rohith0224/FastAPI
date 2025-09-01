import uvicorn
from fastapi import FastAPI
from BaseModel import Banknote
import pickle
import pandas as pd

model=pickle.load(open("model.pkl",'rb'))


app=FastAPI()
@app.get("/")
def index():
    return {"message":"Hello, World"}

@app.post("/predict")
def predict_banknote(data:Banknote):
    data=data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
    
    input_data=pd.DataFrame([[variance,skewness,curtosis,entropy]],columns=['variance','skewness','curtosis','entropy'])
    
    prediction=model.predict(input_data)[0]
    
    if(prediction==0):
        return {"message":"The banknote is Authentic"}
    else:
        return {"message":"The banknote is Not Authentic"}
    
if __name__=="__main__":
    uvicorn.run(app,host='127.0.0.1',port=8000)
    