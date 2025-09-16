# Kutubxona Boshqaruv Tizimi - Library App

Bu loyiha Python dasturlash tilida yozilgan kutubxona boshqaruv tizimi (CLI ilova)dir. Ilova orqali kitoblarni qo'shish, ko'rish, o'chirish, yangilash va qidirish mumkin.

## Xususiyatlar

- 📚 **Kitob qo'shish** - Yangi kitoblar qo'shish
- 👀 **Kitoblarni ko'rish** - Barcha kitoblarni jadval formatida ko'rsatish
- 🗑️ **Kitobni o'chirish** - Tanlangan kitobni o'chirish
- ✏️ **Kitobni yangilash** - Kitob nomi va muallifini o'zgartirish
- ✅ **Status o'zgartirish** - Kitobning o'qilgan/o'qilmagan holatini belgilash
- 🔍 **Qidirish** - Nom, muallif yoki yil bo'yicha kitoblarni qidirish
- 🔽 **Filterlash** - O'qilgan yoki o'qilmagan kitoblarni ajratib ko'rsatish

## Talablar

- **Python 3.8** yoki undan yuqori versiya
- **Rich kutubxonasi** (ixtiyoriy - jadvallarni chiroyli ko'rsatish uchun)

### Rich kutubxonasini o'rnatish

```bash
pip install rich
```

> **Eslatma**: Agar `rich` kutubxonasi o'rnatilmagan bo'lsa, ilova oddiy `print()` funksiyasidan foydalanadi.

## O'rnatish va ishga tushirish

1. **Loyihani yuklab oling**:
   ```bash
   git clone [repository-url]
   cd library-app
   ```

2. **Kerakli kutubxonalarni o'rnating**:
   ```bash
   pip install rich
   ```

3. **Ilovani ishga tushiring**:
   ```bash
   python app.py
   ```

## Fayl tuzilmasi

```
library-app/
├── README.md    # Loyiha haqida ma'lumot
├── app.py       # Asosiy dastur kodi
```

## Foydalanish

Dastur ishga tushgandan so'ng sizga quyidagi menyu ko'rsatiladi:

```
=== KUTUBXONA BOSHQARUV TIZIMI ===
1. Kitob qo'shish
2. Kitoblarni ko'rish
3. Kitobni o'chirish
4. Kitobni yangilash
5. Kitob statusini o'zgartirish
6. Kitoblarni qidirish
7. Kitoblarni filterlash
0. Chiqish
```

### Kitob ma'lumotlari

Har bir kitob quyidagi ma'lumotlarni o'z ichiga oladi:
- **Nomi** (title) - Kitobning nomi
- **Muallifi** (author) - Kitob muallifi
- **Yili** (year) - Nashr yili
- **Holati** (status) - O'qilgan (✓) yoki o'qilmagan (✗)

## Funksiyalar haqida batafsil

### 1. Kitob qo'shish
- Foydalanuvchidan kitob nomi, muallif va nashr yilini so'raydi
- Ma'lumotlarni tekshiradi (bo'sh bo'lmasligi kerak)
- Yangi kitobni kutubxonaga qo'shadi (dastlab "o'qilmagan" holatida)

### 2. Kitoblarni ko'rish
- Barcha kitoblarni jadval ko'rinishida chiqaradi
- Har bir kitob uchun tartib raqami, nomi, muallifi, yili va holatini ko'rsatadi
- Agar kutubxona bo'sh bo'lsa, tegishli xabar beradi

### 3. Kitobni o'chirish
- Avval barcha kitoblar ro'yxatini ko'rsatadi
- Foydalanuvchi o'chirmoqchi bo'lgan kitobning raqamini kiradi
- Tanlangan kitobni o'chiradi

### 4. Kitobni yangilash
- Mavjud kitobning nomini va muallifini o'zgartirish imkonini beradi
- Foydalanuvchi yangi ma'lumotlarni kiritadi
- O'zgarishlar saqlanadi

### 5. Status o'zgartirish
- Kitobning "o'qilgan" yoki "o'qilmagan" holatini almashtiradi
- Bir marta bosish bilan holatni o'zgartiradi

### 6. Qidirish
- Kitob nomi, muallif yoki nashr yili bo'yicha qidirish
- Qisman mos kelgan natijalarni ham ko'rsatadi
- Topilgan kitoblar jadval formatida chiqariladi

### 7. Filterlash
- Faqat o'qilgan kitoblarni ko'rsatish
- Faqat o'qilmagan kitoblarni ko'rsatish

## Xatoliklardan himoyalanish

Dastur quyidagi holatlarda xatoliklarni to'g'ri boshqaradi:
- Noto'g'ri raqam kiritilganda
- Bo'sh qiymatlar kiritilganda
- Mavjud bo'lmagan indeks tanlanganda
- Noto'g'ri menyu tanlovlari

## Texnik ma'lumotlar

- **Dasturlash tili**: Python 3.8+
- **Tashqi kutubxonalar**: Rich (ixtiyoriy)
- **Ma'lumotlar saqlash**: Xotirada (list strukturasi)
- **Interfeys**: Command Line Interface (CLI)

## Kelajakdagi rivojlanish rejalari

- [ ] Ma'lumotlarni faylga saqlash (JSON/CSV)
- [ ] Kitob kategoriyalari qo'shish
- [ ] Kitob reytingi tizimi
- [ ] Web interfeysi yaratish
- [ ] Ma'lumotlar bazasi bilan integratsiya

## Muallif

Ushbu loyiha o'quv maqsadlarida yaratilgan.

## Litsenziya

Ushbu loyiha ochiq kodli hisoblanadi va Najot Ta'lim o'quv maqsadlarida erkin foydalanish mumkin.
