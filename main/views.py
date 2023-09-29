from django.shortcuts import render, redirect
from django.contrib import messages
import firebase_admin
from django.http import HttpResponse
from firebase_admin import auth,credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def home(request):
    return HttpResponse("home")

def handle_password_reset(request):
    # Get the oobCode and apiKey from the URL
    oob_code = request.GET.get('oobCode')
    api_key = request.GET.get('apiKey')

    if request.method == "POST":
        # Use Firebase Auth to reset the user's password
        try:
            new_password = request.POST.get("new_password")
            confirm_password = request.POST.get("confirm_password")

            if new_password == confirm_password and is_oob_code_valid(oob_code):
                # Change the user's password
                auth.update_user(oob_code, password=new_password)

                messages.success(request, "Password has been reset successfully.")
            else:
                messages.error(request, "Passwords do not match.")
        except auth.ExpiredIdTokenError:
            messages.error(request, "Password Reset Link expired. Please .")

        except auth.InvalidIdTokenError:
            messages.error(request, "Invalid Link.")
            # return render(request, 'password_reset_invalid.html')

    return render(request, 'password_reset_abli_app.html')

def is_oob_code_valid(oob_code):
    try:
        # Use Firebase Admin SDK to verify the OOB code.
        auth.verify_password_reset_code(oob_code)
        # If verification is successful, the code is valid.
        return True
    except Exception as e:
        message.error(f"Firebase Authentication Error ..... {e}")
        return False