from django.shortcuts import render, redirect
from django.contrib import messages
import firebase_admin
from django.http import HtppResponse
from firebase_admin import auth

"""def handle_password_reset(request, oob_code):
    try:
        # Verify the oob_code (out-of-band code)
        auth.check_password_reset_code(oob_code)

        if request.method == "POST":
            new_password = request.POST.get("new_password")
            confirm_password = request.POST.get("confirm_password")

            if new_password == confirm_password:
                # Change the user's password
                auth.update_user(oob_code, password=new_password)

                messages.success(
                    request, "Password has been reset successfully."
                )
            else:
                messages.error(request, "Passwords do not match.")

        return render(request, "password_reset_abli_app.html")
    except auth.ExpiredOobCodeError:
        messages.error(request, "Password reset link has expired.")
        
    except Exception as e:
        messages.error(request, f"Error: {str(e)}")
        
"""
def home(request):
	return HttpResponse("home")


def handle_reset_verify(request):
    # Get the oobCode and apiKey from the URL
    oob_code = request.GET.get('oobCode')
    api_key = request.GET.get('apiKey')

    # Initialize Firebase Admin SDK
    firebase_admin.initialize_app(options={
        "apiKey": api_key,
    })

    # Verify the password reset action
    try:
        # Use Firebase Auth to reset the user's password
        auth.confirm_oob_code(oob_code)
        
        if request.method == "POST":
	        new_password = request.POST.get("new_password")
	        confirm_password = request.POST.get("confirm_password")
        
        if new_password == confirm_password:
        # Change the user's password
	        auth.update_user(oob_code, password=new_password)
        
	        messages.success(
	        request, "Password has been reset successfully."
	        )
        else:
	        messages.error(request, "Passwords do not match.")
        # Password reset is successful
	        
    except auth.ExpiredOobCodeError:
        # Oob code is expired
        messages.error(request, "Passwords Reset Link expired. Please .")
        #return render(request, 'password_reset_expired.html')
    except auth.OobCodeInvalidError:
        # Oob code is invalid
        messages.error(request, "Invalid Link.")
        #return render(request, 'password_reset_invalid.html')