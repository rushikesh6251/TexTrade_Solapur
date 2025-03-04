import razorpay

RAZORPAY_KEY_ID = "your_public_key_here"
RAZORPAY_KEY_SECRET = "your_secret_key_here"

client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

try:
    client.payment.all()
    print("✅ Authentication successful! Keys are correct.")
except razorpay.errors.BadRequestError:
    print("❌ Authentication failed! Check your Razorpay keys.")
