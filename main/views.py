from django.shortcuts import render, redirect
from django.contrib import messages
import firebase_admin
from firebase_admin import auth

def handle_password_reset(request, oob_code):
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
        