import urllib.request
import json
from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/")
def my_form():
    return render_template('my-form.html')

@app.route('/',methods=['POST', 'GET'])
def my_form_post():
    if request.method=='POST':
        TempHighF1 = request.form.get('TempHighF')
        TempAvgF1 = request.form.get('TempAvgF')
        TempLowF1 = request.form.get('TempLowF')
        DewPointHighF1 = request.form.get('DewPointHighF')
        DewPointAvgF1 = request.form.get('DewPointAvgF')
        DewPointLowF1 = request.form.get('DewPointLowF')
        HumidityHighPercent1 = request.form.get('HumidityHighPercent')
        HumidityAvgPercent1 = request.form.get('HumidityAvgPercent')
        HumidityLowPercent1 = request.form.get('HumidityLowPercent')
        SeaLevelPressureHighInches1 = request.form.get('SeaLevelPressureHighInches')
        SeaLevelPressureAvgInches1 = request.form.get('SeaLevelPressureAvgInches')
        SeaLevelPressureLowInches1 = request.form.get('SeaLevelPressureLowInches')
        VisibilityHighMiles1 = request.form.get('VisibilityHighMiles')
        VisibilityAvgMiles1 = request.form.get('VisibilityAvgMiles')
        VisibilityLowMiles1 = request.form.get('VisibilityLowMiles')
        WindHighMPH1 = request.form.get('WindHighMPH')
        WindAvgMPH1 = request.form.get('WindAvgMPH')
        WindGustMPH1 = request.form.get('WindGustMPH')
        PrecipitationSumInches1 = request.form.get('PrecipitationSumInches')
        Fog1 =request.form.get('Fog')
        Rain1 = request.form.get('Rain')
        Thunderstorms1 = request.form.get('Thunderstorms')
    #return Thunderstorms1
        
        data = {

                "Inputs": {

                        "input1":

                        [

                            {

                                    'TempHighF': TempHighF1,

                                    'TempAvgF': TempAvgF1,

                                    'TempLowF': TempLowF1,

                                    'DewPointHighF': DewPointHighF1,

                                    'DewPointAvgF': DewPointAvgF1,

                                    'DewPointLowF': DewPointLowF1,

                                    'HumidityHighPercent': HumidityHighPercent1,

                                    'HumidityAvgPercent': HumidityAvgPercent1,

                                    'HumidityLowPercent': HumidityLowPercent1,

                                    'SeaLevelPressureHighInches': SeaLevelPressureHighInches1,

                                    'SeaLevelPressureAvgInches': SeaLevelPressureAvgInches1,

                                    'SeaLevelPressureLowInches': SeaLevelPressureLowInches1,

                                    'VisibilityHighMiles': VisibilityHighMiles1,

                                    'VisibilityAvgMiles': VisibilityAvgMiles1,

                                    'VisibilityLowMiles': VisibilityLowMiles1,

                                    'WindHighMPH': WindHighMPH1,

                                    'WindAvgMPH': WindAvgMPH1,

                                    'WindGustMPH': WindGustMPH1,

                                    'PrecipitationSumInches': PrecipitationSumInches1, 

                                    
                            }

                        ],

                },

            "GlobalParameters":  {

            }

        }



        body = str.encode(json.dumps(data))



        url = 'https://ussouthcentral.services.azureml.net/workspaces/9b9b1db4b0154b879b71c0d0363f9bb0/services/103b554c6aa34daea22e183e487f67a0/execute?api-version=2.0&format=swagger'

        api_key = 'G0VlHWmKVeAhmEP8kkYZCR04asSime0hmtm8XERbROWTxcS1j9MPUe6o+rhgXATbj4rPDBE3WbsRGtWDR7Mqtw==' # Replace this with the API key for the web service

        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}



        req = urllib.request.Request(url, body, headers)


   # return body
        try:

            response = urllib.request.urlopen(req)



            result = response.read()
            result1 = result.decode("utf-8")
            resp = json.loads(result1)
	    

            outpt = resp['Results']
            prob = outpt['output1']
            prob1 = prob[0]['Scored Probabilities']
            result= float(prob1)
            
            if result < 0.4:
                return(render_template('redirect.html',result=result,color="#008000"))
            elif result >= 0.4 and result < 0.6:
                return(render_template('redirect.html',result=result,color="#FFFF00"))
            else:
                return(render_template('redirect.html',result=result,color="#FF0000"))
           # print(result)

        except urllib.error.HTTPError as error:

            print("The request failed with status code: " + str(error.code))



         # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure

            print(error.info())

            print(json.loads(error.read().decode("utf8", 'ignore')))
        return result
    else:
        return str(error.code)

if __name__ == "__main__":
    app.run()

