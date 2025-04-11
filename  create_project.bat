@echo off
:: Agar foydalanuvchi PowerShell ichida ishga tushirsa, avtomatik cmd.exe ga o‘tkazish

echo === Django loyihasini yaratish boshlanmoqda ===

:: Virtual muhit yaratish
python -m venv venv
call venv\Scripts\activate

:: Kerakli kutubxonalarni o'rnatish
pip install --upgrade pip
pip install django djangorestframework markdown django-filter

:: Django loyihasini yaratish
django-admin startproject root .
django-admin startapp blog

:: Kerakli kutubxonalarni `requirements.txt` ga yozish
pip freeze > requirements.txt\

README.md

echo === Loyihangiz muvaffaqiyatli yaratildi! ===
pause
