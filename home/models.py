import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.db import models


class QRCode(models.Model):
    BANK_CHOICES = [
        ('sberbank', 'Сбербанк'),
    ]

    bank = models.CharField(
        max_length=20, choices=BANK_CHOICES, default='sberbank'
    )
    recipient_name = models.CharField(
        max_length=255, help_text="Имя получателя (например, Иванов Иван Иванович)"
    )
    phone = models.CharField(
        max_length=15, help_text="Номер телефона получателя в формате +7XXXXXXXXXX"
    )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Введите сумму оплаты"
    )
    comment = models.CharField(
        max_length=255, blank=True, null=True, help_text="Комментарий для платежа"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    qr_code = models.ImageField(
        upload_to='qr_codes/', null=True, blank=True
    )

    def __str__(self):
        return f"{self.bank} - {self.recipient_name} - {self.amount} руб"

    def generate_qr_code(self):
        # Формируем данные в формате СБП
        data = (
            f"000201" 
            f"010211"  
            f"2607{self.phone}"  
            f"520483"  
            f"5802RU" 
            f"530{len(str(self.amount)):02}{float(self.amount):.2f}" 
            f"7001{self.recipient_name}"  
            f"6304"  
        )

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        qr_file = BytesIO()
        img.save(qr_file, format='PNG')
        qr_file.seek(0)
        self.qr_code.save(
            f"{self.id}_qr.png", ContentFile(qr_file.read()), save=False
        )
        self.save()