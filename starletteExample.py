from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from starlette.routing import Route, Mount
from starlette.middleware.sessions import SessionMiddleware
from starlette.templating import Jinja2Templates

from motor import motor_asyncio
try:
    from numpy.random import randint
except:
    from random import randint
from moneropos import MoneroPoS

async def homepage(request):  # sourcery skip: move-assign
    xmrAmount = 0.001
    
    if not request.session.get('integratedAddress', None):
        if not request.session.get('xmrAmount', None):
            request.session['xmrAmount'] = xmrAmount
        
        if not request.session.get('paymentId', None):
            paymentIdResults = await generateAndCheckPaymentId(request)
            paymentId = paymentIdResults['paymentId']
            request.session['paymentId'] = paymentId
        
        if not request.session.get('appliedToUser', False):
            request.session['appliedToUser'] = False
        
        genNewPayment = moneroWallet.generateNewPayment(paymentId=paymentId)
        integratedAddress = genNewPayment['address']
        request.session['integratedAddress'] = str(integratedAddress)
        
        insertPayment = await insertPaymentIntoDB(paymentId, integratedAddress, xmrAmount)
        
        print(dir(integratedAddress))
        
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
        }
    )

async def lookForConfirmedPayment(request):
    txLookupResults = moneroWallet.findConfirmedIncomingTransactions(
        paymentId=request.session['paymentId'],
        integratedAddress=request.session['integratedAddress'],
        xmrAmount=request.session['xmrAmount'],
    )
    
    foundAConfirmedTransaction = txLookupResults['foundAConfirmedTransaction']
    transactionSumAmountIsCorrect = txLookupResults['transactionSumAmountIsCorrect']
    
    if foundAConfirmedTransaction:
        mongoPaymentsCollection.update_one(
            {
                'paymentId': request.session['paymentId'],
            },
            {
                '$set': {
                    'foundAConfirmedTransaction': True,
                }
            }
        )
        
    if transactionSumAmountIsCorrect:
        mongoPaymentsCollection.update_one(
            {
                'paymentId': request.session['paymentId'],
            },
            {
                '$set': {
                    'transactionSumAmountIsCorrect': True,
                }
            }
        )
        paymentDoc = await mongoPaymentsCollection.find_one({'paymentId': request.session['paymentId']})
        if not paymentDoc.get('appliedToUser', False):
            # processCompletedPayment(username="admin", paymentId=request.session['paymentId'], xmrAmount=request.session['xmrAmount'])
            mongoPaymentsCollection.update_one(
                {
                    'paymentId': request.session['paymentId'],
                },
                {
                    '$set': {
                        'appliedToUser': True,
                    }
                }
            )
            request.session['appliedToUser'] = True

        
    request.session['foundAConfirmedTransaction'] = foundAConfirmedTransaction
    request.session['transactionSumAmountIsCorrect'] = transactionSumAmountIsCorrect
    

    
    return templates.TemplateResponse(
        "checkForPayments.html",
        {
            "request": request,
        }   
    )

async def generateAndCheckPaymentId(request):
    while True:
        paymentId = randint(111111111, 999999999)
        paymentIdCount = await mongoPaymentsCollection.count_documents({'paymentId': paymentId})

        if paymentIdCount == 0:
            return {'success': True, 'paymentId': paymentId}
        
async def insertPaymentIntoDB(paymentId, integratedAddress, xmrAmount):
    await mongoPaymentsCollection.insert_one(
        {
            'paymentId': paymentId,
            'integratedAddress': str(integratedAddress),
            'xmrAmount': xmrAmount,
            'foundAConfirmedTransaction': False,
            'transactionSumAmountIsCorrect': False,
            'appliedToUser': False,
        }
    )


routes = [
    Route('/', endpoint=homepage, methods=["GET"]),
    Route('/lookForConfirmedPayment', endpoint=lookForConfirmedPayment, methods=["GET"]),
    Mount('/static', StaticFiles(directory='static'), name='static'),
]

app = Starlette(debug=True, routes=routes)
app.add_middleware(
    SessionMiddleware, 
    secret_key="~egjfipewgiejwgoegijij37237237237",
    max_age=3600, 
    session_cookie='moneroTestingApp'
)

templates = Jinja2Templates(directory='templates')
moneroWallet = MoneroPoS()
mongoAsyncClient = motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
mongoPoSDB = mongoAsyncClient['moneroPoS']
mongoPaymentsCollection = mongoPoSDB['payments']