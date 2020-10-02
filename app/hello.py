from flask import Flask,render_template,request,url_for
import requests
app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
def hello():
    if request.method=='POST':
        cs=request.form['a']
        geo=request.form['r2']
        gen=request.form['r1']
        age=request.form['b']
        tenure=request.form['c']
        balance=request.form['d']
        np=request.form['e']
        hc=request.form['r3']
        im=request.form['r4']
        es=request.form['f']
        try:
            cs=int(cs)
            geo=int(geo)
            gen=int(gen)
            age=int(age)
            tenure=int(tenure)
            balance=float(balance)
            np=int(np)
            hc=int(hc)
            im=int(im)
            es=float(es)
        except:
            return render_template('data.html',err_msg='Enter Valid Data')
        url = "https://qxk1s4orj6.execute-api.us-east-1.amazonaws.com/telecom/"
        payload = " {\"data\":\"" + str(cs) + ',' + str(geo) + ',' + str(gen) + ',' + str(age) + ',' + str(tenure) + ',' + str(balance) + ',' + str(np) +','+str(hc)+ ','+str(im)+',' + str(es) + "\"" + "}"

        headers = {
            'X-Amz-Content-Sha256': 'beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3',
            'X-Amz-Date': '20200930T095337Z',
            'Authorization': 'AWS4-HMAC-SHA256 Credential=ASIA4KDESJFDUSSQKJSG/20200930/us-east-1/execute-api/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=b81935cc533d5efb8db465da9c12f4a3ed76ca80089dfc3edebdb39df4fe5f7c',
            'Content-Type': 'text/plain'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response=response.text.encode('utf8')
        response=str(response)
        print(response)
        result=response[3]
        print(result)
        if result=='N':
            return render_template('data.html',result=str(0))
        else:
            return render_template('data.html',result=str(1))
    else:
        return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True)
