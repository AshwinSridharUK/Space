from flask import Flask, request, redirect
import requests
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse



app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', '').lower()

    # Start our TwiML response
    resp = MessagingResponse()


    # Determine the right reply for this message
    if 'ASTOne' in body:

        resp.redirect('ENTERHERE')

        print(resp)

    elif 'ASTWO' in body:
        resp.redirect('ENTERHERE')


        print (resp)

    elif 'ASTThree' in body:
        resp.redirect('ENTERHERE')


        print (resp)

    elif 'ASTFour' in body:
        resp.redirect('ENTERHERE')


        print (resp)
    elif 'AST QZ' in body:
        resp.redirect('ENTERHERE')



    else:
        resp.redirect('ENTERHERE')

        print (resp)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
