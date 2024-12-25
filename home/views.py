from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
from io import BytesIO
import base64

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode()
    return img_base64

def qr_code_view(request):
    qr_code_base64 = None
    error_message = None

    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone'] 
            amount = form.cleaned_data['amount'] 
            recipient_name = form.cleaned_data['recipient_name']
            try:
                data = (
                    f"https://www.sberbank.com/sms/pbpn?"
                    f"requisiteNumber={phone}"  
                    f"&amount={float(amount):.2f}"  
                    f"&comment={recipient_name}"  
                )

                qr_code_base64 = generate_qr_code(data)

            except Exception as e:
                error_message = f"Ошибка при генерации QR-кода: {str(e)}"
    else:
        form = QRCodeForm()

    return render(request, 'qr_form.html', {
        'form': form,
        'qr_code_base64': qr_code_base64,
        'error_message': error_message
    })